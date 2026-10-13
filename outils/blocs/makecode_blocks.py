"""Hook MkDocs : remplace chaque bloc ```blocks par l'image PNG déjà dessinée.

L'image se nomme d'après le contenu du code (voir cle_bloc). Elle est produite
une fois par outils/blocs/dessiner-blocs.js et commitée dans docs/assets/blocks/.
Si l'image n'existe pas encore, le bloc est laissé tel quel : le script
docs/assets/js/makecode-blocks.js le dessine alors à l'ouverture de la page.
"""
import hashlib
import os
import re
import struct

LANGUE = "fr"
EXTENSION = "motor=github:DFRobot/pxt-motor"
MATRICE = "neopixel-extended=github:arbona-robin/pxt-neopixel-matrix-extension#v2.1.3"


def extension(code: str) -> str:
    """L'extension à charger : celle de la matrice si le code l'utilise, DF-Driver sinon."""
    return MATRICE if "neopixelExtended" in code else EXTENSION
DOSSIER = "assets/blocks"
BLOC = re.compile(r"^```blocks\n(.*?)\n```[ \t]*$", re.M | re.S)


def cle_bloc(code: str) -> str:
    """Même calcul que dans dessiner-blocs.js."""
    texte = f"{LANGUE}|{extension(code)}|{code.strip()}"
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:12]


def on_page_markdown(markdown, page, config, files):
    docs = config["docs_dir"]
    dossier_page = os.path.dirname(page.file.src_path)

    def remplacer(m):
        code = m.group(1)
        nom = f"{cle_bloc(code)}.png"
        fichier = os.path.join(docs, DOSSIER, nom)
        if not os.path.exists(fichier):
            return m.group(0)
        with open(fichier, "rb") as f:
            largeur = struct.unpack(">I", f.read(24)[16:20])[0] // 2  # PNG à double résolution
        src = os.path.relpath(f"{DOSSIER}/{nom}", dossier_page or ".").replace(os.sep, "/")
        # Image Markdown (et non <img>) : MkDocs réécrit son chemin selon l'URL de la page.
        alt = "Programme MakeCode : " + " ".join(code.split())
        alt = alt.replace("\\", "").replace("[", "(").replace("]", ")")
        return (
            '<figure class="screenshot makecode-rendu" markdown>\n'
            f'![{alt}]({src}){{ width="{largeur}" }}\n'
            "</figure>"
        )

    return BLOC.sub(remplacer, markdown)
