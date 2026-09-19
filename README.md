# Le livre Maker Junior

Le support écrit des ateliers maker : fabrication, électronique et programmation. Écrit en Markdown, publié en site statique avec [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Organisation

| Dossier | Contenu |
|---|---|
| `docs/` | Le livre publié — pages élèves, fiches de référence, carnet de bord, médias |
| `animation/` | Les fiches d'animation et de projet. **Hors du site publié**, lisibles seulement ici |
| `animation/gabarits/` | Les gabarits La Plateforme — la forme d'export, vierge |
| `.github/workflows/` | La publication automatique |

Les pages de séance décrivent le déroulé ; les fiches de `docs/fiches/` sont la référence transverse à laquelle les séances renvoient.

## Deux usages

Le dépôt produit deux choses à partir du même travail.

**Le livre**, dans `docs/`, écrit pour les jeunes : tutoiement, texte court, l'image d'abord.

**Les fiches La Plateforme**, dans `animation/`, écrites pour toi, ta hiérarchie et tes partenaires : fiche communication, synthèse de projet, et une fiche de conduite par séance. Elles suivent les gabarits LP pour pouvoir être exportées en Google Doc à la même forme que celles des collègues — **les titres de section ne se renomment pas**. Ce qui n'entre dans aucun champ va en « Notes de préparation », après le trait horizontal, et sera ignoré à l'export.

C'est ce qui permet d'écrire dans `animation/` ce qui n'a rien à faire sous les yeux d'un jeune : budget, ressources humaines, objectifs en langage Bloom, planning prévisionnel, bilan honnête d'un atelier qui s'est mal passé.

Les deux sorties ne sont pas indépendantes : `animation/<projet>/communication.md` est la source du titre, de l'accroche et de la promesse du parcours, et la page `docs/projets/<projet>/index.md` en est une réécriture pour le jeune. Si l'une change, vérifier l'autre.

Contrôler qu'une fiche est toujours exportable :

```bash
norm() { grep '^## ' "$1" | sed -E 's/ \(.*//; s/ — .*//'; }
diff <(norm animation/gabarits/seance.md) <(norm animation/rover/s01.md)
```

## Écrire

**Les pages élèves sont courtes** : l'image d'abord, environ 800 mots affichés pour une séance de 1 h 45. La [séance 1 du rover](docs/projets/rover/seances/s01-base-motrice.md) est l'exemple ; la méthode complète est dans la skill `.claude/skills/nouvelle-seance-maker-junior/`.

```bash
python3 .claude/skills/nouvelle-seance-maker-junior/mots-affiches.py docs/projets/rover/seances/s01-base-motrice.md
```

Les fichiers sont du Markdown ordinaire, lisibles tels quels sur GitHub. Quelques conventions :

**Les encadrés** utilisent la syntaxe d'alerte GitHub, transformée en encadré coloré sur le site :

```markdown
> [!CAUTION] Titre de l'encadré
> Le texte de l'avertissement.
```

`[!CAUTION]` pour la sécurité, `[!NOTE]` pour un concept, `[!TIP]` pour une vérification, `[!IMPORTANT]` pour un point de contrôle.

**Les médias manquants** sont marqués par un emplacement réservé, qui s'affiche en pointillés sur le site :

```markdown
<span class="todo-media">[photo : ce qu'il faut photographier]</span>
```

Cherche `todo-media` dans le dépôt pour lister ce qu'il reste à prendre en photo.

**Les vidéos** s'insèrent en HTML, avec un piège : MkDocs réécrit les chemins relatifs des images en syntaxe Markdown, mais pas ceux d'une balise `<video>`. Comme chaque page est publiée dans son propre dossier, il faut **un `../` de plus** que pour une image voisine.

```html
<video controls playsinline preload="metadata" src="../../../../assets/rover-s01/video.mp4"></video>
```

## Aperçu local

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

Le site est sur <http://127.0.0.1:8000> et se recharge à chaque enregistrement.

## Publier

Un `git push` sur `main` suffit : le workflow reconstruit le site et le met en ligne.

La première fois seulement, dans **Settings → Pages**, régler **Source** sur *GitHub Actions*.

## Médias

Les images sont converties avant d'entrer dans le dépôt.

```bash
# Photo : JPEG 2000 px, métadonnées EXIF retirées (elles contiennent la position GPS)
magick photo.HEIC -auto-orient -strip -resize '2000x2000>' -quality 85 sortie.jpg

# Capture d'écran Retina : moitié de la résolution
magick capture.png -strip -resize '1638x>' sortie.png

# Vidéo : H.264 720p, sans piste audio
ffmpeg -i video.MOV -vf scale=-2:720 -c:v libx264 -crf 24 -preset slow \
       -an -movflags +faststart sortie.mp4
```
