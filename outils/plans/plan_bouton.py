"""Plan de découpe du bouton de tir (Jeu d'arcade, séance 4), à l'échelle 1, quatre par A4.

    python3 outils/plans/plan_bouton.py

Écrit docs/assets/plans/bouton-de-tir-v1.svg, puis le PDF (A4 portrait, à imprimer à 100 %)
et le PNG de la page, avec Inkscape.

Le bouton est une seule pièce de carton, pliée en deux faces. Deux plis rapprochés forment une
charnière, qui écarte les faces au repos et les ramène après l'appui. Une bande de ruban de cuivre
sur chaque face, côté intérieur (celui du plan imprimé) : une fois plié, elles se font face et se
chevauchent sous le capuchon. Chaque bande sort par un bord opposé, où mord la pince crocodile,
et s'arrête loin de l'autre bord, pour que la pince ne touche jamais les deux bandes.

Même code graphique que les plans de la lampe et du châssis : trait plein noir, on découpe ;
pointillé, on plie ; cotes en rouge, étiquettes grises ; cuivre en orange.
"""

import subprocess
from pathlib import Path

LARGEUR = 55      # largeur de la pièce, en mm
FACE = 42         # hauteur d'une face : le capuchon de 40 mm y tient
CHARNIERE = 5     # écart entre les deux plis
PISTE = 6         # largeur du ruban de cuivre
RETRAIT = 15      # chaque bande s'arrête à 15 mm du bord opposé à sa pince
CAPUCHON = 40     # diamètre du capuchon

HAUTEUR = 2 * FACE + CHARNIERE
PAGE = (210, 297)  # A4 portrait

RACINE = Path(__file__).resolve().parent.parent.parent
SORTIE = RACINE / "docs/assets/plans/bouton-de-tir-v1"
INKSCAPE = "/Applications/Inkscape.app/Contents/MacOS/inkscape"

ROUGE, GRIS, CUIVRE, BRUN = "#ff4d4d", "#6e6e6e", "#e08a4f", "#7a3d12"
POLICE = 'font-family="Helvetica, Arial, sans-serif"'


def etiquette(x, y, texte, fond=GRIS, taille=3.6):
    largeur = len(texte) * taille * 0.56 + 2
    return (f'<rect x="{x - largeur / 2:.2f}" y="{y - taille * 0.85:.2f}" width="{largeur:.2f}" '
            f'height="{taille * 1.15:.2f}" fill="{fond}"/>'
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{taille}" fill="#fff" text-anchor="middle" {POLICE}>{texte}</text>')


def cote_h(x1, x2, y, texte):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{ROUGE}" stroke-width="0.25"/>'
            f'<line x1="{x1}" y1="{y - 1.5}" x2="{x1}" y2="{y + 1.5}" stroke="{ROUGE}" stroke-width="0.25"/>'
            f'<line x1="{x2}" y1="{y - 1.5}" x2="{x2}" y2="{y + 1.5}" stroke="{ROUGE}" stroke-width="0.25"/>'
            + etiquette((x1 + x2) / 2, y - 1.5, texte))


def cote_v(x, y1, y2, texte):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{ROUGE}" stroke-width="0.25"/>'
            f'<line x1="{x - 1.5}" y1="{y1}" x2="{x + 1.5}" y2="{y1}" stroke="{ROUGE}" stroke-width="0.25"/>'
            f'<line x1="{x - 1.5}" y1="{y2}" x2="{x + 1.5}" y2="{y2}" stroke="{ROUGE}" stroke-width="0.25"/>'
            + etiquette(x - 7, (y1 + y2) / 2 + 1.2, texte))


def piece(x0, y0, cotes):
    m = []
    # Le contour : on découpe.
    m.append(f'<rect x="{x0}" y="{y0}" width="{LARGEUR}" height="{HAUTEUR}" fill="none" stroke="#000" stroke-width="0.35"/>')
    # Les deux plis de la charnière.
    for y in (y0 + FACE, y0 + FACE + CHARNIERE):
        m.append(f'<line x1="{x0}" y1="{y}" x2="{x0 + LARGEUR}" y2="{y}" stroke="#000" stroke-width="0.3" stroke-dasharray="1.6,1.2"/>')
    # Les bandes de cuivre, côté imprimé. Celle du haut sort à droite, celle du bas à gauche.
    ya = y0 + FACE / 2
    yb = y0 + FACE + CHARNIERE + FACE / 2
    for xa, xb, y, pince in ((x0 + RETRAIT, x0 + LARGEUR, ya, "droite"), (x0, x0 + LARGEUR - RETRAIT, yb, "gauche")):
        m.append(f'<rect x="{xa}" y="{y - PISTE / 2}" width="{xb - xa}" height="{PISTE}" fill="{CUIVRE}" fill-opacity="0.55"/>'
                 f'<text x="{(xa + xb) / 2}" y="{y + 1.1}" font-size="2.6" fill="{BRUN}" text-anchor="middle" {POLICE}>'
                 f'cuivre · {xb - xa:.0f} mm</text>')
        xp = x0 + LARGEUR + 2.5 if pince == "droite" else x0 - 2.5
        m.append(f'<text x="{xp}" y="{y + 1}" font-size="2.6" fill="{BRUN}" text-anchor="{"start" if pince == "droite" else "end"}" {POLICE}>pince</text>')
    # La place du capuchon, de l'autre côté, au-dessus du chevauchement des bandes.
    cx = x0 + (RETRAIT + LARGEUR - RETRAIT) / 2
    m.append(f'<circle cx="{cx}" cy="{ya}" r="{CAPUCHON / 2}" fill="none" stroke="#555" stroke-width="0.3" stroke-dasharray="0.8,0.8"/>'
             f'<text x="{cx}" y="{ya - CAPUCHON / 2 + 4.5}" font-size="2.5" fill="#555" text-anchor="middle" {POLICE}>capuchon, de l\'autre côté</text>')
    m.append(f'<text x="{x0 + LARGEUR / 2}" y="{y0 + FACE + CHARNIERE / 2 + 0.9}" font-size="2.4" fill="#555" text-anchor="middle" {POLICE}>charnière</text>')
    if cotes:
        m.append(cote_h(x0, x0 + LARGEUR, y0 - 5, f"{LARGEUR} mm"))
        m.append(cote_v(x0 - 12, y0, y0 + FACE, f"{FACE} mm"))
        m.append(cote_v(x0 - 12, y0 + FACE, y0 + FACE + CHARNIERE, f"{CHARNIERE}"))
        m.append(cote_v(x0 - 12, y0 + FACE + CHARNIERE, y0 + HAUTEUR, f"{FACE} mm"))
    return m


def plan():
    morceaux = []
    xs = (40, 125)
    ys = (28, 140)
    for i, y in enumerate(ys):
        for j, x in enumerate(xs):
            morceaux += piece(x, y, cotes=(i == 0 and j == 0))
    yl = 250
    lignes = [
        "Découpe le contour, plie aux deux pointillés : la face du bas vient sous la face du haut, côté imprimé dedans.",
        "Colle le ruban de cuivre côté imprimé, sur les deux bandes orange : elles se retrouvent face à face, sans se toucher.",
        "Deux élastiques tiennent le bouton fermé. Le capuchon se colle de l'autre côté, sur le cercle.",
        "Une pince mord le cuivre à droite, l'autre à gauche, jamais du côté où le cuivre s'arrête avant le bord.",
    ]
    morceaux.append(f'<line x1="22" y1="{yl - 9}" x2="34" y2="{yl - 9}" stroke="#000" stroke-width="0.35"/>'
                    f'<text x="37" y="{yl - 7.7}" font-size="3.6" {POLICE}>on découpe</text>'
                    f'<line x1="72" y1="{yl - 9}" x2="84" y2="{yl - 9}" stroke="#000" stroke-width="0.3" stroke-dasharray="1.6,1.2"/>'
                    f'<text x="87" y="{yl - 7.7}" font-size="3.6" {POLICE}>on plie</text>')
    for k, t in enumerate(lignes):
        morceaux.append(f'<text x="22" y="{yl + 6 * k}" font-size="3.3" {POLICE}>{t}</text>')
    morceaux.append(f'<text x="22" y="{yl + 30}" font-size="3.3" {POLICE}>Imprimer en A4 portrait, à 100 % : '
                    f'vérifier à la règle que la pièce fait {LARGEUR} mm de large.</text>'
                    f'<text x="{PAGE[0] - 12}" y="{PAGE[1] - 8}" font-size="3" fill="#777" text-anchor="end" {POLICE}>'
                    f'Bouton de tir · v1 · échelle 1</text>')
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
    png = SORTIE.with_suffix(".png")
    subprocess.run(["magick", str(png), "-trim", "+repage", "-bordercolor", "white", "-border", "20", str(png)], check=True)
    print("écrit", svg.relative_to(RACINE), "+ .pdf + .png")
