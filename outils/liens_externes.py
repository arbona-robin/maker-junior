"""Hook MkDocs : les liens vers un autre site s'ouvrent dans un nouvel onglet.

Le livre se lit en écran partagé pendant l'atelier : un lien externe (MakeCode,
Tinkercad, une documentation) ne doit pas remplacer la page de la séance.
"""
import re

LIEN = re.compile(r'<a (?![^>]*\btarget=)([^>]*\bhref="https?://[^"]*"[^>]*)>')


def on_page_content(html, page, config, files):
    site = (config.get("site_url") or "").rstrip("/")

    def ouvrir(m):
        attributs = m.group(1)
        if site and f'href="{site}' in attributs:
            return m.group(0)
        return f'<a {attributs} target="_blank" rel="noopener">'

    return LIEN.sub(ouvrir, html)
