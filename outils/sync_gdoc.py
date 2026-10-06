"""Synchronise les fiches d'animation du dépôt avec le Google Doc du projet.

    .venv/bin/python outils/sync_gdoc.py diff rover [s01]   # compare, lecture seule
    .venv/bin/python outils/sync_gdoc.py push rover [s01]   # écrit le dépôt dans le Doc
    .venv/bin/python outils/sync_gdoc.py copie rover        # copie de test, privée

Option --doc ID : travailler sur un autre Doc que celui de animation/export.yml
(une copie de test, par exemple). Option --force : pousser même si le Doc a été
modifié depuis le dernier push.

Le Doc contient une fiche par tableau à deux colonnes : le titre de section à
gauche, le contenu à droite, une ligne par section `##` de la fiche du dépôt.
La trame des tableaux est fixe. Seuls varient le nombre de lignes « Activité N »
d'une séance, le nombre de lignes « Séance N » de la synthèse et le nombre de
tableaux de séance : un tableau de séance absent du dépôt est supprimé au push
complet. Le contenu vient toujours du dépôt.

Identifiants OAuth : ~/.config/maker-junior/credentials.json (hors dépôt).
"""

import difflib
import json
import os
import re
import sys
from pathlib import Path

import yaml
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

RACINE = Path(__file__).resolve().parent.parent
ANIMATION = RACINE / "animation"
GITHUB = "https://github.com/arbona-robin/maker-junior/blob/main/"
SITE = re.search(r"^site_url:\s*(\S+)", (RACINE / "mkdocs.yml").read_text(), re.M).group(1).rstrip("/") + "/"
IMAGE = r"`(docs/[^`]+\.(?:jpe?g|png|gif|webp))`"
IMAGES = {}  # id d'objet du Doc → URL source, tenu à jour à chaque lecture
CONFIG = Path.home() / ".config" / "maker-junior"
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.file",
]
VARIABLE = re.compile(r"^Activité \d+$|^Séance \d+ — ")
TAILLE = {"magnitude": 10, "unit": "PT"}
BLANC = {"color": {"rgbColor": {"red": 1, "green": 1, "blue": 1}}}
TRAIT = {"color": {"color": {"rgbColor": {"red": 0.8, "green": 0.8, "blue": 0.8}}},
         "width": {"magnitude": 0.75, "unit": "PT"}, "dashStyle": "SOLID"}


def connexion():
    jeton = CONFIG / "token.json"
    creds = None
    if jeton.exists() and set(SCOPES) <= set(json.loads(jeton.read_text()).get("scopes", [])):
        creds = Credentials.from_authorized_user_file(str(jeton))
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    elif not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(str(CONFIG / "credentials.json"), SCOPES)
        creds = flow.run_local_server(port=0)
    jeton.write_text(creds.to_json())
    jeton.chmod(0o600)
    return build("docs", "v1", credentials=creds), build("drive", "v3", credentials=creds)


def u16(texte):
    """Longueur en unités UTF-16, l'unité des index de l'API Docs."""
    return len(texte.encode("utf-16-le")) // 2


# --- Markdown du dépôt → paragraphes ----------------------------------------
# Un bloc est {"runs": [(texte, style)]} pour un paragraphe,
# ou {"table": [[runs, …], …]} pour un tableau Markdown.

def lien(url, dossier):
    """Lien absolu : le site pour ce qui est dans docs/, GitHub pour le reste."""
    if re.match(r"https?://", url):
        return url
    chemin = os.path.relpath(os.path.normpath(dossier / url.split("#")[0]), RACINE)
    if not chemin.startswith("docs/"):
        return GITHUB + chemin
    chemin = chemin.removeprefix("docs/")
    if chemin.endswith(".md"):
        chemin = re.sub(r"(^|/)index$", r"\1", chemin.removesuffix(".md"))
        chemin = chemin + "/" if chemin and not chemin.endswith("/") else chemin
    return SITE + chemin


def url_image(chemin):
    return SITE + chemin.removeprefix("docs/")


def en_ligne(texte, dossier, style=None):
    style = style or {}
    motif = re.compile(
        r"\*\*(.+?)\*\*|(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])|`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)"
    )
    runs, pos = [], 0
    for m in motif.finditer(texte):
        if m.start() > pos:
            runs.append((texte[pos:m.start()], style))
        if m.group(1) is not None:
            runs += en_ligne(m.group(1), dossier, {**style, "bold": True})
        elif m.group(2) is not None:
            runs += en_ligne(m.group(2), dossier, {**style, "italic": True})
        elif m.group(3) is not None:
            runs.append((m.group(3), style))
        else:
            runs += en_ligne(m.group(4), dossier, {**style, "link": {"url": lien(m.group(5), dossier)}})
        pos = m.end()
    if pos < len(texte):
        runs.append((texte[pos:], style))
    return runs


def rendre(md, dossier):
    blocs, courant, table = [], None, []

    def fermer():
        nonlocal courant
        if courant is not None:
            texte = re.sub(r"\s+", " ", courant).strip()
            images = re.findall(IMAGE, texte)
            texte = re.sub(r"\s*\*?\((?:disponible\s*:\s*)?" + IMAGE + r"\)\*?|\s*" + IMAGE, "", texte)
            runs = en_ligne(texte, dossier)
            if texte.startswith("**Modalité"):
                runs = [(t, {k: v for k, v in s.items() if k != "bold"} | {"italic": True}) for t, s in runs]
            blocs.append({"runs": runs})
            blocs.extend({"image": url_image(i)} for i in images)
        courant = None

    def fermer_table():
        if table:
            rangs = [[c.strip() for c in l.strip().strip("|").split("|")] for l in table]
            rangs = [r for r in rangs if not all(re.fullmatch(r":?-+:?", c) for c in r)]
            blocs.append({"table": [[en_ligne(c, dossier) for c in r] for r in rangs]})
            table.clear()

    for ligne in md.splitlines():
        if ligne.startswith("|"):
            fermer()
            table.append(ligne)
            continue
        fermer_table()
        ligne = re.sub(r"^> ?", "", ligne)
        item = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", ligne)
        if not ligne.strip():
            fermer()
        elif item:
            fermer()
            retrait = "    " if len(item.group(1)) >= 2 else ""
            puce = "• " if item.group(2) in "-*" else item.group(2) + " "
            courant = retrait + puce + item.group(3)
        elif ligne.startswith("#"):
            fermer()
            courant = "**" + ligne.lstrip("# ") + "**"
            fermer()
        else:
            courant = (courant + " " if courant is not None else "") + ligne
    fermer()
    fermer_table()
    return blocs or [{"runs": [("—", {})]}]


def texte_runs(runs):
    return "".join(t for t, _ in runs)


def lignes_blocs(blocs):
    sortie = []
    for b in blocs:
        if "table" in b:
            sortie += [" | ".join(texte_runs(c) for c in r) for r in b["table"]]
        elif "image" in b:
            sortie.append(f"[image {b['image']}]")
        else:
            sortie.append(texte_runs(b["runs"]))
    return sortie


# --- Fiches du dépôt --------------------------------------------------------

def fiche_du_depot(chemin):
    """Liste des (titre de ligne, blocs) dans l'ordre du Doc."""
    texte = re.sub(r"<!--.*?-->", "", chemin.read_text(), flags=re.S)
    titre = texte.splitlines()[0]
    sections = []
    for bloc in re.split(r"^## ", texte, flags=re.M)[1:]:
        titre_section, _, corps = bloc.partition("\n")
        if titre_section.startswith("Notes de préparation"):
            break
        corps = re.sub(r"^---$", "", corps, flags=re.M)
        m = re.match(r"(Activité \d+.*?) — (.*)", titre_section)
        if m:
            titre_section, corps = m.group(1), f"**{m.group(2)}**\n\n{corps}"
        sections.append((titre_section, rendre(corps.strip(), chemin.parent)))
    m = re.search(r"Séance (\d+) · (.*)", titre)
    if m:
        sections.insert(0, (f"Séance {int(m.group(1))}", rendre(m.group(2), chemin.parent)))
    return sections


def noms_fiches(projet):
    return ["communication", "projet"] + sorted(p.stem for p in (ANIMATION / projet).glob("s[0-9][0-9].md"))


# --- Lecture du Doc ---------------------------------------------------------

def texte_paragraphe(para):
    morceaux = []
    for e in para["elements"]:
        if "inlineObjectElement" in e:
            morceaux.append(f"[image {IMAGES.get(e['inlineObjectElement']['inlineObjectId'], '?')}]")
        else:
            morceaux.append(e.get("textRun", {}).get("content", ""))
    return "".join(morceaux).rstrip("\n")


def memoriser_images(doc):
    IMAGES.clear()
    for k, o in doc["tabs"][0]["documentTab"].get("inlineObjects", {}).items():
        props = o["inlineObjectProperties"]["embeddedObject"].get("imageProperties", {})
        IMAGES[k] = props.get("sourceUri", "?")


def lignes_cellule(cellule):
    sortie = []
    for el in cellule.get("content", []):
        if "paragraph" in el:
            sortie.append(("• " if "bullet" in el["paragraph"] else "") + texte_paragraphe(el["paragraph"]))
        elif "table" in el:
            for r in el["table"]["tableRows"]:
                sortie.append(" | ".join("\n".join(lignes_cellule(c)) for c in r["tableCells"]))
    # insertTable laisse un paragraphe vide avant chaque tableau imbriqué
    return [l for l in sortie if l]


def fiche_du_titre(titre):
    if "Fiche Communication" in titre:
        return "communication"
    if "Synthèse de Projet" in titre:
        return "projet"
    m = re.search(r"· Séance (\d+)", titre)
    return f"s{int(m.group(1)):02d}" if m else None


def corps(doc):
    return doc["tabs"][0]["documentTab"]["body"]["content"]


def tables_du_doc(doc):
    """{fiche: élément table} pour les tableaux de premier niveau du premier onglet."""
    tables = {}
    for el in corps(doc):
        if "table" in el:
            fiche = fiche_du_titre("\n".join(lignes_cellule(el["table"]["tableRows"][0]["tableCells"][0])))
            if fiche:
                tables[fiche] = el
    return tables


def rangs(el):
    return el["table"]["tableRows"]


def cle(titre):
    return re.sub(r" \(.*?\)", "", titre).strip()


# --- Comparaison ------------------------------------------------------------

def unites(lignes):
    """Découpe un contenu en unités comparables, sans le formatage."""
    texte = "\n".join(lignes)
    if texte.strip() in ("", "—"):
        return []
    texte = texte.replace("’", "'").replace(" ", " ").replace(" ", " ")
    texte = re.sub(r"Description :", "", texte)
    morceaux = re.split(r"\n|•| · | - |(?<=[.!?;])\s+|\s\(\d+\)\s", texte)
    sortie = []
    for m in morceaux:
        m = re.sub(r"^\s*(?:[-•◦]|\d+\.|\(\d+\))\s*", "", m)
        m = re.sub(r"\s+", " ", m).strip(" .;")
        if m:
            sortie.append(m)
    return sortie


def comparer(doc, depot):
    doc_par_cle = {cle(t): (t, c) for t, c in doc}
    depot_par_cle = {cle(t): (t, c) for t, c in depot}
    ordre = [cle(t) for t, _ in depot] + [cle(t) for t, _ in doc if cle(t) not in depot_par_cle]
    rapport, compte = [], {"identique": 0, "différent": 0, "vide dans le Doc": 0, "absent": 0}
    for k in ordre:
        if k not in doc_par_cle or k not in depot_par_cle:
            compte["absent"] += 1
            rapport.append(f"  {k} : absent {'du Doc' if k not in doc_par_cle else 'du dépôt'}")
            continue
        (t_doc, c_doc), (t_depot, c_depot) = doc_par_cle[k], depot_par_cle[k]
        u_doc, u_depot = unites(c_doc), unites(lignes_blocs(c_depot))
        titre_change = t_doc != t_depot
        if u_doc == u_depot and not titre_change:
            compte["identique"] += 1
            continue
        if not u_doc and u_depot:
            compte["vide dans le Doc"] += 1
            rapport.append(f"  {k} : vide dans le Doc")
            continue
        compte["différent"] += 1
        rapport.append(f"  {k}")
        if titre_change:
            rapport.append(f"      titre  Doc « {t_doc} » · dépôt « {t_depot} »")
        for ligne in difflib.ndiff(u_doc, u_depot):
            if ligne[0] in "-+":
                rapport.append(f"    {'Doc  ' if ligne[0] == '-' else 'dépôt'} {ligne[2:]}")
    return ", ".join(f"{v} {k}" for k, v in compte.items() if v), rapport


def commentaires(drive, doc_id):
    sortie, page = [], None
    while True:
        r = drive.comments().list(
            fileId=doc_id, pageToken=page, includeDeleted=False,
            fields="nextPageToken,comments(content,resolved,author/displayName,quotedFileContent/value,replies(content,author/displayName))",
        ).execute()
        sortie += [c for c in r.get("comments", []) if not c.get("resolved")]
        page = r.get("nextPageToken")
        if not page:
            return sortie


def diff(docs, drive, doc_id, projet, filtre):
    doc = docs.documents().get(documentId=doc_id, includeTabsContent=True).execute()
    memoriser_images(doc)
    tables = tables_du_doc(doc)
    print(f"{doc['title']} · révision {doc['revisionId'][:12]}\n")
    for nom in noms_fiches(projet):
        if filtre and nom != filtre:
            continue
        if nom not in tables:
            print(f"{nom} : pas de tableau dans le Doc\n")
            continue
        du_doc = [("\n".join(lignes_cellule(r["tableCells"][0])), lignes_cellule(r["tableCells"][1]))
                  for r in rangs(tables[nom])[1:]]
        resume, rapport = comparer(du_doc, fiche_du_depot(ANIMATION / projet / f"{nom}.md"))
        print(f"{nom} : {resume}")
        print("\n".join(rapport) + ("\n" if rapport else ""))
    ouverts = commentaires(drive, doc_id)
    print(f"Commentaires ouverts : {len(ouverts)}")
    for c in ouverts:
        cite = c.get("quotedFileContent", {}).get("value", "")
        print(f"  {c['author']['displayName']} sur « {cite[:60]} » : {c['content']}")
        for rep in c.get("replies", []):
            print(f"      ↳ {rep['author']['displayName']} : {rep['content']}")


# --- Écriture ---------------------------------------------------------------

class Doc:
    def __init__(self, docs, doc_id):
        self.docs, self.id = docs, doc_id
        self.relire()

    def relire(self):
        self.doc = self.docs.documents().get(documentId=self.id, includeTabsContent=True).execute()
        memoriser_images(self.doc)

    def ecrire(self, requetes):
        if requetes:
            self.docs.documents().batchUpdate(documentId=self.id, body={
                "requests": requetes,
                "writeControl": {"requiredRevisionId": self.doc["revisionId"]},
            }).execute()
        self.relire()


def style_texte(debut, fin, style, champs):
    return {"updateTextStyle": {"range": {"startIndex": debut, "endIndex": fin},
                                "textStyle": style, "fields": champs}}


def remplir(cellule, blocs, base, marqueurs):
    """Requêtes qui remplacent le contenu d'une cellule. Les tableaux sont posés
    à la place d'un marqueur, dans un second temps."""
    debut = cellule["content"][0]["startIndex"]
    fin = cellule["content"][-1]["endIndex"] - 1
    paragraphes = []
    for b in blocs:
        if "table" in b:
            marque = f"⟦T{len(marqueurs)}⟧"
            marqueurs[marque] = b
            paragraphes.append([(marque, {})])
        elif "image" in b:
            marque = f"⟦I{len(marqueurs)}⟧"
            marqueurs[marque] = b
            paragraphes.append([(marque, {})])
        else:
            paragraphes.append(b["runs"])
    texte = "\n".join(texte_runs(p) for p in paragraphes)
    requetes = []
    if fin > debut:
        requetes.append({"deleteContentRange": {"range": {"startIndex": debut, "endIndex": fin}}})
    if not texte:
        return requetes
    requetes.append({"insertText": {"location": {"index": debut}, "text": texte}})
    requetes.append(style_texte(debut, debut + u16(texte), base, "bold,italic,fontSize,link,foregroundColor"))
    pos = debut
    for p in paragraphes:
        for t, s in p:
            if s:
                requetes.append(style_texte(pos, pos + u16(t), s, ",".join(s)))
            pos += u16(t)
        pos += 1
    return requetes


def a_jour(cellule, blocs):
    return lignes_cellule(cellule) == lignes_blocs(blocs)


def creer_table(doc, nb_rangs, modele):
    """Ajoute en fin de Doc un tableau vide, à la trame du tableau modèle."""
    doc.ecrire([{"insertText": {"endOfSegmentLocation": {}, "text": "\n"}},
                {"insertTable": {"rows": nb_rangs, "columns": 2, "endOfSegmentLocation": {}}}])
    nouveau = [el for el in corps(doc.doc) if "table" in el][-1]
    debut = {"index": nouveau["startIndex"]}
    cellules = rangs(modele)

    def style(cellule, rang, col, nb_rangs_zone, nb_cols):
        s = {k: v for k, v in cellule["tableCellStyle"].items() if k not in ("rowSpan", "columnSpan")}
        return {"updateTableCellStyle": {
            "tableRange": {"tableCellLocation": {"tableStartLocation": debut, "rowIndex": rang, "columnIndex": col},
                           "rowSpan": nb_rangs_zone, "columnSpan": nb_cols},
            "tableCellStyle": s, "fields": ",".join(s)}}

    colonnes = modele["table"]["tableStyle"]["tableColumnProperties"]
    doc.ecrire([
        *[{"updateTableColumnProperties": {"tableStartLocation": debut, "columnIndices": [i],
                                           "tableColumnProperties": c, "fields": "widthType,width"}}
          for i, c in enumerate(colonnes)],
        {"mergeTableCells": {"tableRange": {"tableCellLocation": {"tableStartLocation": debut, "rowIndex": 0,
                                                                  "columnIndex": 0}, "rowSpan": 1, "columnSpan": 2}}},
        style(cellules[0]["tableCells"][0], 0, 0, 1, 2),
        style(cellules[1]["tableCells"][0], 1, 0, nb_rangs - 1, 1),
        style(cellules[1]["tableCells"][1], 1, 1, nb_rangs - 1, 1),
    ])


def ajuster_rangs(doc, nom, voulus):
    """Ajoute ou retire les lignes variables pour suivre le dépôt. La trame fixe
    doit être identique, sinon on s'arrête."""
    el = tables_du_doc(doc.doc)[nom]
    presents = [cle("\n".join(lignes_cellule(r["tableCells"][0]))) for r in rangs(el)[1:]]
    fixes = lambda cles: [k for k in cles if not VARIABLE.match(k)]
    if fixes(presents) != fixes(voulus):
        sys.exit(f"{nom} : la trame du Doc ne correspond pas à la fiche du dépôt.\n"
                 f"  Doc   {fixes(presents)}\n  dépôt {fixes(voulus)}")
    for i in reversed(range(len(presents))):
        if VARIABLE.match(presents[i]) and presents[i] not in voulus:
            doc.ecrire([{"deleteTableRow": {"tableCellLocation": {
                "tableStartLocation": {"index": el["startIndex"]}, "rowIndex": i + 1, "columnIndex": 0}}}])
            el = tables_du_doc(doc.doc)[nom]
            del presents[i]
    for i, k in enumerate(voulus):
        if k not in presents:
            doc.ecrire([{"insertTableRow": {"tableCellLocation": {
                "tableStartLocation": {"index": el["startIndex"]}, "rowIndex": i, "columnIndex": 0},
                "insertBelow": True}}])
            el = tables_du_doc(doc.doc)[nom]
            presents.insert(i, k)


def poser(doc, marqueurs):
    """Remplace chaque marqueur par son image ou son tableau imbriqué."""
    def position(marque):
        para = next(p for p in paragraphes_du_doc(corps(doc.doc)) if texte_paragraphe(p["paragraph"]) == marque)
        return para["startIndex"]

    for marque, bloc in marqueurs.items():
        if "table" not in bloc:
            continue
        p = position(marque)
        effacer = {"deleteContentRange": {"range": {"startIndex": p, "endIndex": p + u16(marque)}}}
        lignes = bloc["table"]
        doc.ecrire([effacer, {"insertTable": {"rows": len(lignes), "columns": len(lignes[0]), "location": {"index": p}}}])
        table = next(el for el in tables_imbriquees(corps(doc.doc)) if p <= el["startIndex"] <= p + 2)
        requetes = [{"updateTableColumnProperties": {
            "tableStartLocation": {"index": table["startIndex"]}, "columnIndices": [i],
            "tableColumnProperties": {"widthType": "FIXED_WIDTH", "width": {"magnitude": l, "unit": "PT"}},
            "fields": "widthType,width"}} for i, l in enumerate(largeurs(lignes))]
        requetes.append({"updateTableCellStyle": {
            "tableStartLocation": {"index": table["startIndex"]},
            "tableCellStyle": {f"border{c}": TRAIT for c in ("Left", "Right", "Top", "Bottom")},
            "fields": "borderLeft,borderRight,borderTop,borderBottom"}})
        petit = {"fontSize": {"magnitude": 9, "unit": "PT"}}
        for r in reversed(range(len(lignes))):
            for c in reversed(range(len(lignes[0]))):
                cellule = rangs(table)[r]["tableCells"][c]
                base = petit | ({"bold": True} if r == 0 else {})
                requetes += remplir(cellule, [{"runs": lignes[r][c]}], base, {})
        doc.ecrire(requetes)

    # Les images en dernier et d'un seul coup : Google crée une révision en
    # arrière-plan après chaque image, qui ferait échouer l'écriture suivante.
    images = sorted(((position(m), m, b["image"]) for m, b in marqueurs.items() if "image" in b), reverse=True)
    doc.ecrire([r for p, m, url in images for r in (
        {"deleteContentRange": {"range": {"startIndex": p, "endIndex": p + u16(m)}}},
        {"insertInlineImage": {"uri": url, "location": {"index": p},
                               "objectSize": {"height": {"magnitude": 150, "unit": "PT"}}}},
    )])


def largeurs(lignes, total=310, souple=30):
    """Largeur des colonnes d'un tableau imbriqué, en points. Les colonnes courtes
    prennent ce qu'il leur faut, les longues se partagent le reste."""
    longueurs = [max(len(texte_runs(r[i])) for r in lignes) for i in range(len(lignes[0]))]
    besoin = [n * 5 + 14 for n in longueurs]
    souples = [i for i, n in enumerate(longueurs) if n > souple]
    if not souples:
        return [round(total * b / sum(besoin), 1) for b in besoin]
    reste = total - sum(b for i, b in enumerate(besoin) if i not in souples)
    return [round(reste / len(souples), 1) if i in souples else b for i, b in enumerate(besoin)]


def paragraphes_du_doc(contenu):
    for el in contenu:
        if "paragraph" in el:
            yield el
        elif "table" in el:
            for r in el["table"]["tableRows"]:
                for c in r["tableCells"]:
                    yield from paragraphes_du_doc(c["content"])


def tables_imbriquees(contenu, profondeur=0):
    for el in contenu:
        if "table" in el:
            if profondeur:
                yield el
            for r in el["table"]["tableRows"]:
                for c in r["tableCells"]:
                    yield from tables_imbriquees(c["content"], profondeur + 1)


def etat(doc_id, revision=None):
    fichier = CONFIG / "revisions.json"
    revisions = json.loads(fichier.read_text()) if fichier.exists() else {}
    if revision is None:
        return revisions.get(doc_id)
    revisions[doc_id] = revision
    fichier.write_text(json.dumps(revisions, indent=1))


def push(docs, doc_id, projet, filtre, force):
    doc = Doc(docs, doc_id)
    connue = etat(doc_id)
    if connue and connue != doc.doc["revisionId"] and not force:
        sys.exit("Le Doc a été modifié depuis le dernier push. Lancer diff, reporter dans le dépôt "
                 "ce qui doit l'être, puis push --force.")

    marqueurs, bilan = {}, []
    if not filtre:
        for nom in sorted(set(tables_du_doc(doc.doc)) - set(noms_fiches(projet)), reverse=True):
            el = tables_du_doc(doc.doc)[nom]
            doc.ecrire([{"deleteContentRange": {"range": {
                "startIndex": el["startIndex"], "endIndex": el["endIndex"]}}}])
            bilan.append(f"{nom} : supprimée, absente du dépôt")

    tables = tables_du_doc(doc.doc)
    seances = sorted(n for n in tables if n.startswith("s"))
    modele = tables[seances[0]]
    prefixe = "\n".join(lignes_cellule(rangs(modele)[0]["tableCells"][0])).split(" · ")[0]

    for nom in noms_fiches(projet):
        if filtre and nom != filtre:
            continue
        fiche = fiche_du_depot(ANIMATION / projet / f"{nom}.md")
        voulus = [cle(t) for t, _ in fiche]
        cree = nom not in tables_du_doc(doc.doc)
        if cree:
            if not nom.startswith("s"):
                sys.exit(f"{nom} : pas de tableau dans le Doc.")
            creer_table(doc, len(fiche) + 1, tables_du_doc(doc.doc)[seances[0]])
            entete = [{"runs": [(f"{prefixe} · Séance {int(nom[1:])}", {})]}]
        else:
            ajuster_rangs(doc, nom, voulus)
            entete = None

        el = [e for e in corps(doc.doc) if "table" in e][-1] if cree else tables_du_doc(doc.doc)[nom]
        requetes, modifies = [], 0
        for i in reversed(range(len(fiche))):
            titre, blocs = fiche[i]
            valeur, etiquette = rangs(el)[i + 1]["tableCells"][1], rangs(el)[i + 1]["tableCells"][0]
            if not a_jour(valeur, blocs):
                requetes += remplir(valeur, blocs, {"fontSize": TAILLE, "bold": False, "italic": False}, marqueurs)
                modifies += 1
            libelle = [{"runs": [(titre, {})]}]
            if not a_jour(etiquette, libelle):
                requetes += remplir(etiquette, libelle, {"fontSize": TAILLE, "bold": True}, {})
        if entete:
            requetes += remplir(rangs(el)[0]["tableCells"][0], entete,
                                {"fontSize": {"magnitude": 10.5, "unit": "PT"}, "bold": True,
                                 "foregroundColor": BLANC}, {})
        doc.ecrire(requetes)
        bilan.append(f"{nom} : {'créée, ' if cree else ''}{modifies} section(s) écrite(s)")

    poser(doc, marqueurs)
    etat(doc_id, doc.doc["revisionId"])
    print("\n".join(bilan))


if __name__ == "__main__":
    args, autre_doc, force = sys.argv[1:], None, False
    if "--force" in args:
        args.remove("--force")
        force = True
    if "--doc" in args:
        i = args.index("--doc")
        autre_doc = args[i + 1]
        del args[i:i + 2]
    if len(args) < 2 or args[0] not in ("diff", "push", "copie"):
        sys.exit(__doc__)
    commande, projet = args[0], args[1]
    filtre = args[2] if len(args) > 2 else None
    doc_id = autre_doc or yaml.safe_load((ANIMATION / "export.yml").read_text())[projet]["doc"]
    docs, drive = connexion()
    if commande == "copie":
        copie = drive.files().copy(fileId=doc_id, body={"name": "TEST sync, à supprimer"}).execute()
        print(copie["id"])
    elif commande == "diff":
        diff(docs, drive, doc_id, projet, filtre)
    else:
        push(docs, doc_id, projet, filtre, force)
