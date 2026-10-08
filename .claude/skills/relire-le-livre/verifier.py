#!/usr/bin/env python3
"""Contrôles mécaniques du livre : ce qu'un script voit sans comprendre le texte.

    python3 .claude/skills/relire-le-livre/verifier.py

Chaque ligne du rapport donne le fichier, la ligne et le problème. Rien n'est corrigé.
La relecture qui demande de comprendre (ordre, doublons, sens) se fait ensuite à la main,
selon SKILL.md.
"""
import glob
import os
import re
import sys

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(RACINE)

PAGES = sorted(glob.glob("docs/projets/*/seances/*.md"))
FICHES = sorted(f for f in glob.glob("docs/fiches/*.md") if not f.endswith("index.md"))
ANIMATION = sorted(glob.glob("animation/*/s*.md"))
TOUT = sorted(glob.glob("docs/**/*.md", recursive=True)) + sorted(glob.glob("animation/**/*.md", recursive=True))

rapport = []


def signaler(categorie, fichier, ligne, message):
    rapport.append((categorie, fichier, ligne, message))


def lignes(fichier):
    with open(fichier, encoding="utf-8") as f:
        return f.read().split("\n")


def hors_code(fichier):
    """Les lignes hors blocs de code, avec leur numéro."""
    dans_code = False
    for n, ligne in enumerate(lignes(fichier), 1):
        if ligne.strip().startswith("```"):
            dans_code = not dans_code
            continue
        if not dans_code:
            yield n, ligne


# 1. Style : ce que le dépôt a banni.
INTERDITS = [
    (r"—", "tiret cadratin", TOUT),
    (r"[Cc]arnet de bord|\bau carnet\b|dans (ton|le|votre) carnet", "le carnet de bord n'existe plus", PAGES + FICHES + ANIMATION),
    (r"^## Avant de partir", "section « Avant de partir » supprimée du livre", PAGES),
    (r"^## Ce que (tu dois|vous devez) avoir", "checklist de fin supprimée du livre", PAGES),
    (r"\btrimestre\b", "on dit « projet »", TOUT),
    (r"temps écoulé \(ms\)", "le bloc s'appelle « temps d’exécution (ms) »", TOUT),
    (r"quand une chaîne est reçue", "le bloc s'appelle « quand une donnée est reçue par radio »", TOUT),
    (r"ne mesure pas", "consigne retirée : « compte les carreaux » suffit", PAGES + FICHES),
]
for motif, message, fichiers in INTERDITS:
    for f in fichiers:
        if f.startswith("animation/gabarits") and motif == "—":
            continue
        for n, ligne in hors_code(f):
            # Le tiret des titres (« Séance 4 — … », « Activité 1 (20 min) — … ») est une convention de structure.
            if motif == "—" and (ligne.startswith("#") or ligne.strip() in ("—", "- —") or re.search(r"Séance \d+ —", ligne)):
                continue
            if re.search(motif, ligne):
                signaler("style", f, n, message)

# 2. Fiches générales : pas de code propre à un projet.
PROPRE_AU_ROVER = r"\bvM1\b|\bvM2\b|bande `?83`?|\barlab\b|setGroup\(10\)"
for f in FICHES:
    for n, ligne in enumerate(lignes(f), 1):
        if re.search(PROPRE_AU_ROVER, ligne):
            signaler("fiche générale", f, n, "code ou valeur propre au rover : sa place est dans la séance")

# 3. Ordre : un bloc DF-Driver utilisé avant l'installation de l'extension, dans la même fiche.
for f in FICHES + PAGES:
    texte = lignes(f)
    installation = next((n for n, l in enumerate(texte, 1) if re.search(r"pxt-motor|Ajoute l'extension|### L'installer", l)), None)
    premier_usage = next((n for n, l in enumerate(texte, 1) if re.search(r"motor\.(MotorRun|servo|motorStopAll)", l)), None)
    if installation and premier_usage and premier_usage < installation:
        signaler("ordre", f, premier_usage, f"bloc DF-Driver utilisé avant l'installation de l'extension (ligne {installation})")

# 4. Titres de séance : le menu, la page du projet et le H1 de la page disent la même chose.
nav = open("mkdocs.yml", encoding="utf-8").read()
for f in PAGES:
    h1 = lignes(f)[0].lstrip("# ").strip()
    chemin = f.replace("docs/", "")
    m = re.search(r'"([^"]+)":\s*' + re.escape(chemin), nav)
    if not m:
        signaler("titres", f, 1, "page absente du menu")
    elif m.group(1) != h1:
        signaler("titres", f, 1, f"menu « {m.group(1)} » ≠ titre « {h1} »")
    index = os.path.join(os.path.dirname(os.path.dirname(f)), "index.md")
    if os.path.exists(index):
        nom = os.path.basename(f)
        mi = re.search(r"\[([^\]]+)\]\(seances/" + re.escape(nom) + r"\)", open(index, encoding="utf-8").read())
        if not mi:
            signaler("titres", index, 1, f"{nom} absente de la page du projet")
        elif mi.group(1) != h1:
            signaler("titres", index, 1, f"« {mi.group(1)} » ≠ titre de la page « {h1} »")
for f in ANIMATION:
    if "gabarits" in f:
        continue
    titre = lignes(f)[0]
    m = re.search(r"Page élève\*\* \[`([^`]+)`\]", "\n".join(lignes(f)[:4]))
    if m and not os.path.exists(m.group(1)):
        signaler("titres", f, 3, f"page élève introuvable : {m.group(1)}")
    elif m:
        h1 = lignes(m.group(1))[0]
        t_page = re.sub(r"^# Séance \d+ — ", "", h1).strip()
        t_fiche = re.sub(r"^# .*? — Séance \d+ · ", "", titre).strip()
        if t_page != t_fiche:
            signaler("titres", f, 1, f"fiche « {t_fiche} » ≠ page « {t_page} »")

# 5. Gabarit : chaque fiche d'animation a les sections du gabarit, dans l'ordre.
def sections(fichier):
    vues = []
    for l in lignes(fichier):
        if l.startswith("## "):
            s = re.sub(r"^## Activité \d+.*", "## Activité", l)
            s = re.sub(r" \(.*", "", s)
            s = re.sub(r" — .*", "", s)
            if not vues or vues[-1] != s:
                vues.append(s)
    return vues
GABARIT = sections("animation/gabarits/seance.md")
for f in ANIMATION:
    if "gabarits" in f:
        continue
    if sections(f) != GABARIT:
        signaler("gabarit", f, 1, "sections différentes du gabarit (diff avec animation/gabarits/seance.md)")

# 6. Médias : présents sur le disque, et utilisés.
cites = set()
for f in TOUT:
    for m in re.finditer(r"assets/([^)\s\"']+)", open(f, encoding="utf-8").read()):
        cites.add(m.group(1))
for f in glob.glob("docs/assets/*-s[0-9][0-9]/*") + glob.glob("docs/assets/rover-cahier-des-charges/*"):
    rel = f.replace("docs/assets/", "")
    if rel not in cites:
        signaler("médias", f, 0, "fichier que plus aucune page n'utilise")

# Rapport
if not rapport:
    print("Aucun problème mécanique.")
    sys.exit(0)
for categorie in dict.fromkeys(c for c, *_ in rapport):
    print(f"\n## {categorie}")
    for c, f, n, msg in rapport:
        if c == categorie:
            print(f"- {f}:{n} : {msg}")
sys.exit(1)
