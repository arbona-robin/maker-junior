"""Schéma de la séance 4 Objets connectés : le porte-clés pixel en silhouette, en relief sur plaque, et le piège.

python3 outils/plans/schema_porte_cles.py > docs/assets/objets-connectes-s04/25-silhouette-relief-piege.svg
"""
P = 5  # mm par pixel
FACE = ["..XXXX..", ".XXXXXX.", "XX.XX.XX", "XX.XX.XX", "XXXXXXXX", "X.XXXX.X", "XX....XX", ".XXXXXX."]
HAUT, BAS = "#eca54f", "#f3bd70"   # pixel haut, pixel bas : deux tons proches, le dessin se lit d'un bloc
s = []


def T(x, y, t, sz=2.8, c="#555", w="normal", a="middle"):
    s.append(f'<text x="{x}" y="{y}" font-size="{sz}" fill="{c}" font-weight="{w}" text-anchor="{a}">{t}</text>')


def couleur(r, c):
    return HAUT if (r + c) % 2 == 0 else BAS


def pixels(ox, oy, grille):
    for r, rang in enumerate(grille):
        for c, ch in enumerate(rang):
            if ch == "X":
                s.append(f'<rect x="{ox + c * P}" y="{oy + r * P}" width="{P}" height="{P}" fill="{couleur(r, c)}" stroke="#333" stroke-width="0.25"/>')


def profil(ox, sol, plaque, haut, bas):
    """Vue de côté de la rangée 3 du visage : la plaque éventuelle, puis les pixels en damier."""
    dessus = sol - plaque
    if plaque:
        s.append(f'<rect x="{ox}" y="{dessus}" width="40" height="{plaque}" fill="#e6e1d6" stroke="#333" stroke-width="0.3"/>')
    r = 3
    for c, ch in enumerate(FACE[r]):
        if ch == "X":
            h = haut if (r + c) % 2 == 0 else bas
            s.append(f'<rect x="{ox + c * P}" y="{dessus - h}" width="{P}" height="{h}" fill="{couleur(r, c)}" stroke="#333" stroke-width="0.25"/>')


s.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 124" width="200mm" height="124mm" font-family="Helvetica, Arial, sans-serif">')
s.append('<title>Le porte-clés pixel : en silhouette, en relief sur une plaque, et le piège du contact par un coin</title>')
s.append('<rect width="200" height="124" fill="#fff"/>')

# 1. En silhouette
ox, oy = 12, 30
T(32, 10, "1. En silhouette", 3.6, "#000", "bold"); T(32, 15, "vu de dessus")
s.append(f'<rect x="{ox + 15}" y="{oy - 10}" width="10" height="10" fill="{HAUT}" stroke="#333" stroke-width="0.25"/>')
s.append(f'<circle cx="{ox + 20}" cy="{oy - 5}" r="1.5" fill="#fff" stroke="#333" stroke-width="0.3"/>')
pixels(ox, oy, FACE)
T(ox + 28, oy - 6, "patte 10 × 10 × 2 mm,", 2.6, "#555", "normal", "start"); T(ox + 28, oy - 2.5, "trou de 3 mm", 2.6, "#555", "normal", "start")
T(ox + 20, oy + 45, "seuls les pixels existent :"); T(ox + 20, oy + 48.5, "les yeux et la bouche sont des trous")
T(32, 88, "vu de côté"); profil(ox, 98, 0, 4, 3); T(ox + 20, 103, "pixels de 4 et 3 mm, en damier")

# 2. En relief sur une plaque
ox, oy = 82, 30
T(102, 10, "2. En relief sur une plaque", 3.6, "#000", "bold"); T(102, 15, "en alternative, vu de dessus")
s.append(f'<rect x="{ox}" y="{oy}" width="40" height="40" fill="#e6e1d6" stroke="#333" stroke-width="0.4"/>')
s.append(f'<circle cx="{ox + 3}" cy="{oy + 3}" r="1.5" fill="#fff" stroke="#333" stroke-width="0.3"/>')
pixels(ox, oy, FACE)
T(ox + 20, oy + 45, "plaque 40 × 40 mm, trou dans un coin :"); T(ox + 20, oy + 48.5, "les pixels peuvent être séparés")
T(102, 88, "vu de côté"); profil(ox, 98, 1, 3, 2); T(ox + 20, 103, "plaque 1 mm + pixels de 3 et 2 mm")

# Le piège
ox = 152
T(172, 10, "Le piège", 3.6, "#000", "bold"); T(172, 15, "pour la silhouette")
pixels(ox, 24, ["X...", "XX..", "..XX", "...X"])
s.append(f'<circle cx="{ox + 10}" cy="34" r="2.6" fill="none" stroke="#c62828" stroke-width="0.7"/>')
T(ox + 24, 30, "Non", 2.8, "#c62828", "bold", "start"); T(ox + 24, 34, "touche par un", 2.6, "#555", "normal", "start"); T(ox + 24, 37.5, "coin : casse", 2.6, "#555", "normal", "start")
pixels(ox, 56, ["X...", "XX..", ".XXX", "...X"])
s.append(f'<rect x="{ox + 5}" y="66" width="5" height="5" fill="none" stroke="#2e7d32" stroke-width="0.7"/>')
T(ox + 24, 62, "Oui", 2.8, "#2e7d32", "bold", "start"); T(ox + 24, 66, "un pixel de plus :", 2.6, "#555", "normal", "start")
T(ox + 24, 69.5, "ils se touchent", 2.6, "#555", "normal", "start"); T(ox + 24, 73, "par un côté", 2.6, "#555", "normal", "start")

# Légende
s.append(f'<rect x="10" y="110" width="5" height="5" fill="{HAUT}" stroke="#333" stroke-width="0.25"/>'); T(17, 114, "pixel haut", 2.8, "#333", "normal", "start")
s.append(f'<rect x="40" y="110" width="5" height="5" fill="{BAS}" stroke="#333" stroke-width="0.25"/>'); T(47, 114, "pixel bas", 2.8, "#333", "normal", "start")
T(190, 114, "Un pixel = une Boîte de 5 × 5 mm, sur la grille d'accrochage de 5 mm. 4 mm au plus hors tout.", 2.8, "#333", "normal", "end")
s.append("</svg>")
print("\n".join(s))
