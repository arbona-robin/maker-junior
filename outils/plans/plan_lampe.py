"""Plan de découpe du support de la lampe (Objets connectés, séance 1), à l'échelle 1, sur un A4.

    python3 outils/plans/plan_lampe.py

Écrit docs/assets/plans/lampe-support-v5.svg, puis le PDF (A4 paysage, à imprimer à 100 %)
et le PNG de la page, avec Inkscape. Contraintes : le dessus de 40 mm porte les bandes de cuivre,
les deux montants sont égaux, la base contient le boîtier 4 × AA (65 mm au moins), le rabat fait
20 mm au moins, et le tout tient en 285 mm sur un A4. Les cotes sont en millimètres : changer SECTIONS
ou LARGEUR suffit à refaire le plan.

Même code graphique que le plan du châssis du rover : trait plein noir, on découpe ;
pointillé, on plie ; cotes en rouge, étiquettes grises ; longueur totale en violet.
"""

import subprocess
from pathlib import Path

LARGEUR = 70  # la bande de carton, en mm : le micro:bit (52 mm) et ses pistes
# (longueur en mm, nom affiché dans la section)
SECTIONS = [(80, "montant"), (40, "bandes de cuivre"), (80, "montant"), (65, "base"), (20, "rabat")]
PAGE = (297, 210)  # A4 paysage : la bande tient en 285 mm, marges comprises
MARGE_X, HAUT = 6, 80  # le plan est centré verticalement autour de HAUT

RACINE = Path(__file__).resolve().parent.parent.parent
SORTIE = RACINE / "docs/assets/plans/lampe-support-v5"
INKSCAPE = "/Applications/Inkscape.app/Contents/MacOS/inkscape"

ROUGE, GRIS, VIOLET = "#ff4d4d", "#6e6e6e", "#8f8fc2"


def etiquette(x, y, texte, fond=GRIS, taille=4.2):
    largeur = len(texte) * taille * 0.56 + 2
    return (f'<rect x="{x - largeur / 2:.2f}" y="{y - taille * 0.85:.2f}" width="{largeur:.2f}" '
            f'height="{taille * 1.15:.2f}" fill="{fond}"/>'
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{taille}" fill="#fff" text-anchor="middle" '
            f'font-family="Helvetica, Arial, sans-serif">{texte}</text>')


def cote_h(x1, x2, y, texte, couleur=ROUGE, fond=GRIS):
    """Cote horizontale : la ligne, deux petits traits aux bouts, l'étiquette au milieu."""
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{couleur}" stroke-width="0.25"/>'
            f'<line x1="{x1}" y1="{y - 1.5}" x2="{x1}" y2="{y + 1.5}" stroke="{couleur}" stroke-width="0.25"/>'
            f'<line x1="{x2}" y1="{y - 1.5}" x2="{x2}" y2="{y + 1.5}" stroke="{couleur}" stroke-width="0.25"/>'
            + etiquette((x1 + x2) / 2, y - 1.5, texte, fond))


CUIVRE = "#e08a4f"
PISTE = 6  # largeur du ruban de cuivre, en mm
DEPASSE = 6  # la piste dépasse l'anneau du micro:bit de ce côté, pour que la rondelle et l'écrou portent sur le cuivre


def circuit(x0, y0):
    """Le circuit, vu de la face intérieure (celle du plan imprimé).

    Le micro:bit est sur le premier montant, côté extérieur, anneaux vers le bas de la lampe.
    Ses vis traversent le carton : les pistes partent de leurs pastilles, côté intérieur.
    Les deux bandes tactiles sont sur le dessus, côté extérieur : une vis relie chacune à sa piste.
    """
    m = []
    # Le micro:bit, en pointillé : sa place, côté extérieur. Anneaux à 28 mm du bas, au-dessus du rabat.
    bx, bw, bl = x0 + 24, 52, 42
    by = y0 + (LARGEUR - bw) / 2
    m.append(f'<rect x="{bx}" y="{by}" width="{bl}" height="{bw}" fill="none" stroke="#555" '
             f'stroke-width="0.3" stroke-dasharray="0.8,0.8"/>'
             f'<text x="{bx + bl / 2 + 6}" y="{by + bw / 2}" font-size="3.4" fill="#555" text-anchor="middle" '
             f'font-family="Helvetica, Arial, sans-serif" transform="rotate(-90 {bx + bl / 2 + 6} {by + bw / 2})">'
             f'micro:bit, côté extérieur</text>')
    # Les anneaux, vus de l'intérieur : l'ordre est inversé par rapport à la face avant.
    anneaux = {"GND": 4.4, "3V": 15.2, "2": 26, "1": 36.8, "0": 47.6}
    def y_de(nom):
        return by + anneaux[nom]
    ax = bx + 4
    for nom, dy in anneaux.items():
        m.append(f'<circle cx="{ax}" cy="{by + dy}" r="2" fill="none" stroke="#555" stroke-width="0.3"/>'
                 f'<text x="{ax - DEPASSE - 1}" y="{by + dy + 1.2}" font-size="2.6" fill="#555" text-anchor="end" '
                 f'font-family="Helvetica, Arial, sans-serif">{nom}</text>')
    def piste(xa, xb, y, nom):
        # Le nom et la longueur à couper sont écrits sur la piste, entre les deux vis.
        return (f'<rect x="{xa:.2f}" y="{y - PISTE / 2:.2f}" width="{xb - xa:.2f}" height="{PISTE}" '
                f'fill="{CUIVRE}" fill-opacity="0.5"/>'
                f'<text x="{xa + DEPASSE + 4:.2f}" y="{y + 1.2:.2f}" font-size="2.8" fill="#7a3d12" '
                f'font-family="Helvetica, Arial, sans-serif">{nom} · {xb - xa:.0f} mm</text>')
    def vis(x, y):
        return (f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.6" fill="#fff" stroke="#000" stroke-width="0.35"/>'
                f'<line x1="{x - 1:.2f}" y1="{y:.2f}" x2="{x + 1:.2f}" y2="{y:.2f}" stroke="#000" stroke-width="0.3"/>'
                f'<line x1="{x:.2f}" y1="{y - 1:.2f}" x2="{x:.2f}" y2="{y + 1:.2f}" stroke="#000" stroke-width="0.3"/>')
    dessus = x0 + 80
    bande_p2, bande_gnd = dessus + 9, dessus + 25  # les bandes tactiles, côté extérieur
    fin = x0 + 80 + 40 + 80  # le bas du second montant
    # Les pistes, côté intérieur.
    m.append(piste(ax - DEPASSE, bande_p2 + 3, y_de("2"), "P2"))
    m.append(piste(ax - DEPASSE, bande_gnd + 3, y_de("GND"), "GND"))
    # Les bandes tactiles du dessus, côté extérieur : en contour.
    for bxb, nom in ((bande_p2, "bouton"), (bande_gnd, "masse")):
        m.append(f'<rect x="{bxb - PISTE / 2}" y="{y0 + 4}" width="{PISTE}" height="{LARGEUR - 8}" fill="none" '
                 f'stroke="{CUIVRE}" stroke-width="0.5" stroke-dasharray="1.2,0.8"/>'
                 f'<text x="{bxb}" y="{y0 + 3}" font-size="2.6" fill="#7a3d12" text-anchor="middle" '
                 f'font-family="Helvetica, Arial, sans-serif">{nom}</text>'
                 f'<text x="{bxb + 1}" y="{y0 + 44}" font-size="2.6" fill="#7a3d12" text-anchor="middle" '
                 f'font-family="Helvetica, Arial, sans-serif" transform="rotate(-90 {bxb + 1} {y0 + 44})">'
                 f'{LARGEUR - 8:.0f} mm</text>')
    # Leur place, depuis le pli : sous le plan, deux cotes.
    for k, bxb in enumerate((bande_p2, bande_gnd)):
        m.append(cote_h(dessus, bxb - PISTE / 2, y0 + LARGEUR + 15 + 7 * k, f"{bxb - PISTE / 2 - dessus:.0f} mm",
                        CUIVRE, "#b5652f"))
    # Les vis : trois dans les anneaux du micro:bit, une par bande tactile, et les bornes en bas du second montant.
    for nom in ("2", "1", "GND"):  # la vis de l'anneau 1 tient le micro:bit, et l'écrou reçoit la pince DI
        m.append(vis(ax, y_de(nom)))
    m.append(vis(bande_p2, y_de("2")))
    m.append(vis(bande_gnd, y_de("GND")))
    return m


def plan():
    longueur = sum(l for l, _ in SECTIONS)
    x0 = (PAGE[0] - longueur) / 2
    y0 = HAUT - LARGEUR / 2
    morceaux = []
    # Le contour : on découpe.
    morceaux.append(f'<rect x="{x0}" y="{y0}" width="{longueur}" height="{LARGEUR}" '
                    f'fill="none" stroke="#000" stroke-width="0.35"/>')
    # Les plis, les cotes de chaque section, les noms.
    x = x0
    for i, (l, nom) in enumerate(SECTIONS):
        morceaux.append(cote_h(x, x + l, y0 - 6, f"{l} mm"))
        if nom:
            morceaux.append(f'<text x="{x + l / 2}" y="{y0 + LARGEUR + 7}" font-size="3.8" fill="#333" '
                            f'text-anchor="middle" font-family="Helvetica, Arial, sans-serif">{nom}</text>')
        x += l
        if i < len(SECTIONS) - 1:
            morceaux.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0 + LARGEUR}" stroke="#000" '
                            f'stroke-width="0.3" stroke-dasharray="1.6,1.2"/>')
    morceaux += circuit(x0, y0)
    # La longueur totale, et la largeur de la bande.
    morceaux.append(cote_h(x0, x0 + longueur, y0 - 16, f"{longueur} mm", VIOLET, VIOLET))
    xl = x0 + 80 + 40 + 80 + 12  # la marge est trop étroite : la cote de largeur se place dans la base, vide
    morceaux.append(f'<line x1="{xl}" y1="{y0}" x2="{xl}" y2="{y0 + LARGEUR}" stroke="{ROUGE}" stroke-width="0.25"/>'
                    f'<line x1="{xl - 1.5}" y1="{y0}" x2="{xl + 1.5}" y2="{y0}" stroke="{ROUGE}" stroke-width="0.25"/>'
                    f'<line x1="{xl - 1.5}" y1="{y0 + LARGEUR}" x2="{xl + 1.5}" y2="{y0 + LARGEUR}" stroke="{ROUGE}" stroke-width="0.25"/>'
                    + etiquette(xl + 9, y0 + LARGEUR / 2 + 1.5, f"{LARGEUR} mm"))
    # La légende et le contrôle d'échelle.
    ylg = y0 + LARGEUR + 34
    morceaux.append(
        f'<line x1="{x0}" y1="{ylg}" x2="{x0 + 12}" y2="{ylg}" stroke="#000" stroke-width="0.35"/>'
        f'<text x="{x0 + 15}" y="{ylg + 1.3}" font-size="3.8" font-family="Helvetica, Arial, sans-serif">on découpe</text>'
        f'<line x1="{x0 + 50}" y1="{ylg}" x2="{x0 + 62}" y2="{ylg}" stroke="#000" stroke-width="0.3" stroke-dasharray="1.6,1.2"/>'
        f'<text x="{x0 + 65}" y="{ylg + 1.3}" font-size="3.8" font-family="Helvetica, Arial, sans-serif">on plie</text>'
        f'<text x="{x0}" y="{ylg + 9}" font-size="3.8" font-family="Helvetica, Arial, sans-serif">'
        f'Le rabat passe sous la première section, collé ou scotché. Le plan se colle sur la face intérieure : '
        f'les pistes de cuivre aussi.</text>'
        f'<text x="{x0}" y="{ylg + 15}" font-size="3.8" font-family="Helvetica, Arial, sans-serif">'
        f'Séance 1 : percer à la punaise, depuis l\'intérieur, les vis des deux bandes, puis coller les bandes '
        f'sur la face extérieure, sur les trous.</text>'
        f'<text x="{x0}" y="{ylg + 21}" font-size="3.8" font-family="Helvetica, Arial, sans-serif">'
        f'Séance 2 : coller les pistes, agrandir chaque trou à la punaise, visser.</text>'
        f'<text x="{x0}" y="{ylg + 27}" font-size="3.8" font-family="Helvetica, Arial, sans-serif">'
        f'Sur l\'écrou 1 : la pince DI de la matrice. Sur l\'écrou GND : la pince G, et le − du pack sous la rondelle. '
        f'Le + du pack : la pince V.</text>'
        f'<text x="{x0}" y="{ylg + 33}" font-size="3.8" font-family="Helvetica, Arial, sans-serif">'
        f'Imprimer en A4 paysage, à 100 % : vérifier à la règle que la bande fait {LARGEUR} mm de large.</text>'
        f'<text x="{PAGE[0] - MARGE_X}" y="{ylg + 33}" font-size="3.4" fill="#777" text-anchor="end" '
        f'font-family="Helvetica, Arial, sans-serif">Support de la lampe · v5 · échelle 1</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PAGE[0]}mm" height="{PAGE[1]}mm" '
            f'viewBox="0 0 {PAGE[0]} {PAGE[1]}"><rect width="100%" height="100%" fill="#fff"/>'
            + "".join(morceaux) + "</svg>\n")


if __name__ == "__main__":
    svg = SORTIE.with_suffix(".svg")
    svg.write_text(plan(), encoding="utf-8")
    subprocess.run([INKSCAPE, str(svg), "--export-type=pdf", f"--export-filename={SORTIE.with_suffix('.pdf')}"],
                   check=True, capture_output=True)
    subprocess.run([INKSCAPE, str(svg), "--export-type=png", "--export-dpi=150",
                    f"--export-filename={SORTIE.with_suffix('.png')}"], check=True, capture_output=True)
    # Pour le site, l'image se recadre sur le plan : la page A3 est presque vide autour.
    png = SORTIE.with_suffix(".png")
    subprocess.run(["magick", str(png), "-trim", "+repage", "-bordercolor", "white", "-border", "20", str(png)], check=True)
    print("écrit", svg.relative_to(RACINE), "+ .pdf + .png")
