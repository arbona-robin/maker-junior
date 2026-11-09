"""Le capuchon du bouton de tir (Jeu d'arcade, séance 4), un bouton d'arcade en dôme.

    /Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd outils/plans/capuchon_bouton.py

Écrit docs/assets/arcade-s04/capuchon-52mm.stl : le fichier donné aux jeunes, volontairement trop
grand (52 mm). En séance, ils l'importent dans Tinkercad, le mesurent et le ramènent à 40 mm, le
diamètre prévu par le plan du bouton, avant de le personnaliser. Cotes en millimètres.
"""
import os
import FreeCAD as App
import Mesh
import Part

RACINE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else "outils/plans", "..", ".."))
SORTIE = os.path.join(RACINE, "docs", "assets", "arcade-s04", "capuchon-52mm.stl")

DIAMETRE = 52      # trop grand exprès : 40 mm une fois à l'échelle
COLLERETTE = 3.0   # épaisseur du disque de base, dessous plat pour le collage
RAPPORT = 0.85     # rayon du dôme / rayon de la collerette


def capuchon(diametre):
    r = diametre / 2
    rd = r * RAPPORT
    hd = rd * 0.5
    base = Part.makeCylinder(r, COLLERETTE)
    m = App.Matrix()
    m.scale(1, 1, hd / rd)
    dome = Part.makeSphere(rd).transformGeometry(m)
    dome = dome.common(Part.makeBox(4 * r, 4 * r, 2 * hd, App.Vector(-2 * r, -2 * r, 0)))
    dome.translate(App.Vector(0, 0, COLLERETTE))
    return base.fuse(dome).removeSplitter()


Mesh.Mesh(capuchon(DIAMETRE).tessellate(0.05)).write(SORTIE)
print("écrit", SORTIE)
