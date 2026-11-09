"""Hook MkDocs : les liens vers un autre site, ou vers un outil du livre, s'ouvrent dans un nouvel onglet.

Le livre se lit en écran partagé pendant l'atelier : un lien externe (MakeCode,
Tinkercad, une documentation) ne doit pas remplacer la page de la séance. Les outils
du livre (page relais, tableau de bord) non plus. Un outil est un dossier de docs/
qui contient un index.html écrit à la main plutôt qu'une page Markdown.
"""
import os
import re

LIEN = re.compile(r'<a (?![^>]*\btarget=)([^>]*\bhref="([^"]*)"[^>]*)>')
outils = set()


def on_files(files, config):
    outils.clear()
    for f in files:
        if f.src_uri.endswith("index.html") and not f.is_documentation_page():
            outils.add(os.path.dirname(f.src_uri))
    return files


def on_page_content(html, page, config, files):
    site = (config.get("site_url") or "").rstrip("/")

    def vers_outil(href):
        chemin = href.split("#")[0].rstrip("/")
        if chemin.endswith("index.html"):
            chemin = chemin[: -len("index.html")].rstrip("/")
        return any(chemin == o or chemin.endswith("/" + o) for o in outils)

    def ouvrir(m):
        attributs, href = m.group(1), m.group(2)
        externe = href.startswith(("http://", "https://")) and not (site and href.startswith(site))
        if externe or vers_outil(href):
            return f'<a {attributs} target="_blank" rel="noopener">'
        return m.group(0)

    return LIEN.sub(ouvrir, html)
