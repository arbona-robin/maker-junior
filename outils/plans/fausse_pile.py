"""Fausse pile AA pour le pack de la matrice (Objets connectés, séance 2).

    /Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd outils/plans/fausse_pile.py

Écrit docs/assets/objets-connectes-s02/fausse-pile-aa.stl. La pile prend la place d'un accu
dans le boîtier 4 × AA : la matrice n'est plus alimentée que par trois accus, et son seuil de
lecture descend assez pour le signal du micro:bit. Une bande de ruban de cuivre 6 mm, d'un seul
tenant, court dans la rainure : d'un bout, le long du flanc, jusqu'à l'autre bout. La rainure
la garde à sa place et à fleur.
"""

from pathlib import Path

import Part
from FreeCAD import Vector

DIAMETRE, LONGUEUR = 14.0, 49.5  # le corps : une pile AA fait 14,5 × 50,5 mm, téton compris
TETON, HAUTEUR_TETON = 5.5, 1.2  # le téton du +, que certains boîtiers exigent pour faire contact
RAINURE, PROFONDEUR = 6.6, 0.3  # pour le ruban de 6 mm

SORTIE = Path(__file__).resolve().parent.parent.parent / "docs/assets/objets-connectes-s02/fausse-pile-aa.stl"

r = DIAMETRE / 2
pile = Part.makeCylinder(r, LONGUEUR)
# La rainure du flanc, sur toute la longueur.
pile = pile.cut(Part.makeBox(PROFONDEUR + 1, RAINURE, LONGUEUR, Vector(r - PROFONDEUR, -RAINURE / 2, 0)))
# Les rainures des deux bouts, du flanc jusqu'au-delà du centre : le cuivre y fait le contact.
for z in (0, LONGUEUR - PROFONDEUR):
    pile = pile.cut(Part.makeBox(r + 1, RAINURE, PROFONDEUR, Vector(-2, -RAINURE / 2, z)))
# Le téton, au centre d'un bout : le cuivre passe dessus. Sans lui, la lamelle du + ne touchait pas le ruban.
# Il part du fond de la rainure, pour faire corps avec la pile.
pile = pile.fuse(Part.makeCylinder(TETON / 2, HAUTEUR_TETON + PROFONDEUR, Vector(0, 0, LONGUEUR - PROFONDEUR)))
pile.exportStl(str(SORTIE))
print("écrit", SORTIE)
