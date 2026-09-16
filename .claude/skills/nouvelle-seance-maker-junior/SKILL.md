---
name: nouvelle-seance-maker-junior
description: Rédiger une nouvelle séance du livre des ateliers Maker Junior (dépôt maker-junior) — page élève, fiche d'animation, carnet de bord, fiches de référence et médias. À utiliser quand l'utilisateur dit "nouvelle séance", "créer la séance N", "prépare la S4", "rédige la page de la séance", ou fournit des photos et captures d'un montage de test à intégrer dans une séance. Couvre les questions à poser, l'arbitrage entre page de séance et fiche de référence, la conversion des médias et la vérification du site.
version: 1.2.0
---

# Rédiger une séance du livre Maker Junior

Le livre est le support écrit des ateliers. Une séance s'y publie **avant** l'atelier, et reste en ligne après.

## Deux règles qui ne se discutent pas

**On parle de « projet », jamais de « trimestre ».** Dans le texte comme dans les chemins.

**On n'écrit rien au-delà de la séance qu'on prépare.** Le parcours se déroule en beta : décrire les séances suivantes, leurs phases ou leurs contenus produit des pages à refaire. Dans les index, une séance non écrite apparaît sans description. Pas de « la prochaine fois, tu feras… » en fin de page.

## 1. Lire l'état du dépôt avant de poser la moindre question

```bash
ls docs/projets/*/seances/          # séances déjà écrites
ls docs/fiches/                     # fiches de référence existantes
ls docs/assets/                     # médias déjà en place
ls animation/*/                     # fiches d'animation
```

Puis lire **la séance précédente** du même projet en entier. Elle donne la structure, la façon de nommer les blocs, les renvois vers les fiches. La **S1 du rover** sert de référence pour la longueur : elle a été raccourcie après l'atelier (voir §6).

Lire aussi la **fiche d'animation** de la séance précédente (`animation/<projet>/sNN.md`) : ses sections « Bilan après séance » et « Adaptations pour la prochaine fois » contiennent souvent ce qu'il faut corriger maintenant.

## 2. Les questions à poser

Poser tout en un seul message, en liste numérotée compacte. Ne pas utiliser AskUserQuestion pour ça — c'est du contenu libre, pas un choix entre options. Réserver AskUserQuestion aux vrais arbitrages (deux montages possibles, deux ordres de déroulé).

Marquer ce qu'on a déjà déduit du dépôt ou des médias fournis, pour que l'utilisateur ne retape pas ce qui est connu.

### Identité

1. Numéro et titre de la séance, formulé côté jeune (« Fais rouler ton rover », pas « Étude de la boucle ouverte »)
2. Ce que le jeune repart avec, en une phrase
3. Durée, si elle change de l'habituelle
4. **Ce qui reste à finir de la séance précédente** : combien de jeunes, et jusqu'où ils sont allés. Le bilan de la fiche d'animation le dit souvent déjà

### Contenu

5. **Le déroulé, dans l'ordre réel de l'atelier** — c'est la réponse la plus importante. Une ligne par étape suffit ; les détails se demandent après.
6. **Les notions nouvelles** introduites dans la séance. Ce sont elles qui décident des encadrés et des fiches (voir §3).
7. **Les exercices posés aux jeunes** : l'énoncé, et où chercher les blocs ou les pièces. La solution se déplie après, jamais avant.
8. **Les dangers spécifiques** à cette séance. Les règles générales (cutter, moteurs) sont déjà dans les fiches ; ne demander que ce qui est nouveau.
9. Ce qui a **changé depuis la séance précédente** dans le montage, le code ou le matériel.

### Ressources

10. Photos et vidéos du montage de test — préciser dans quel ordre elles ont été prises si ce n'est pas l'ordre des noms de fichiers.
11. Captures d'écran (MakeCode, logiciel de CAO…).
12. Plans, gabarits, fichiers à imprimer.
13. Matériel, par jeune et en commun.

### Animation

14. Minutage des phases.
15. Variante + et variante −.
16. Points de vigilance.
17. Besoin en adultes, si différent de l'habituel.

### Ce qu'on ne demande pas

Les valeurs numériques visibles sur les captures (vitesse, durée, angle). On les **lit sur les images** et on les annonce à l'utilisateur, en signalant tout écart avec ce qu'il a écrit. Texte et images doivent raconter la même chose ; si l'utilisateur veut d'autres valeurs, il faudra refaire les captures.

## 3. Page de séance ou fiche de référence

C'est l'arbitrage structurant, à faire pour **chaque notion** de la question 6.

> La page de séance est le **déroulé** : ce qu'on fait, dans l'ordre, en pas courts.
> La fiche est la **référence** : ce qu'on relit hors séance, trois semaines plus tard.

Pour chaque notion, dans cet ordre :

**a. Une fiche la couvre-t-elle déjà ?**

```bash
ls docs/fiches/
grep -ril "<mot-clé de la notion>" docs/fiches/
```

Si oui → la séance y **renvoie** (`→ [Titre](../../../fiches/xxx.md)`) au lieu de répéter. Vérifier au passage si la fiche a besoin d'être complétée par ce qu'apporte la séance : c'est fréquent, et c'est ce qui fait qu'une fiche reste utile.

**b. Sinon, la notion est-elle transverse ?** Une notion mérite une fiche si elle sera consultée hors de cette séance, ou si une séance ultérieure s'appuiera dessus. Un geste d'atelier, un branchement, un outil logiciel : oui. Un détail propre à un montage : non.

**c. Sinon** → elle reste dans la séance, en encadré `[!NOTE]`.

Les consignes de sécurité font exception : elles sont **en toutes lettres dans la séance, au moment du geste**, et la fiche en donne la version longue. Jamais un simple lien.

## 4. Les fichiers à créer ou mettre à jour

| Fichier | Quoi |
|---|---|
| `docs/projets/<projet>/seances/sNN-<slug>.md` | La page de séance. **Créer** |
| `docs/projets/<projet>/seances/index.md` | Ajouter la ligne, avec sa description. **Mettre à jour** |
| `mkdocs.yml` | Ajouter l'entrée dans `nav`. **Mettre à jour** |
| `docs/carnet-de-bord/<projet>-sNN.md` | Le carnet de la séance. **Créer** |
| `docs/carnet-de-bord/index.md` | Ajouter le lien. **Mettre à jour** |
| `animation/<projet>/sNN.md` | La fiche d'animation, hors site. **Créer** |
| `animation/README.md` | Ajouter le lien. **Mettre à jour** |
| `docs/fiches/<nouvelle>.md` + `docs/fiches/index.md` + `mkdocs.yml` | Seulement si §3 l'a décidé |
| `docs/fiches/<existante>.md` | Compléter si la séance apporte du nouveau |

Oublier `mkdocs.yml` fait échouer la construction en `--strict`. Oublier les index laisse une page inatteignable.

## 5. Les médias

Dossier : `docs/assets/<projet>-sNN/`. Numérotation : **01-19 pour les photos** dans l'ordre du déroulé, **20-39 pour les captures**, `video-<sujet>.mp4` pour les vidéos. Nommer par le sujet, jamais par le numéro d'origine de l'appareil.

**Toujours regarder chaque image avant de la nommer.** Convertir en aperçu réduit dans `/tmp`, lire, puis décider. Il arrive que des fichiers sans rapport se soient glissés dans le lot : les signaler plutôt que les intégrer.

```bash
# Photo : JPEG 2000 px, EXIF retiré (les photos d'iPhone contiennent la position GPS)
magick photo.HEIC -auto-orient -strip -resize '2000x2000>' -quality 85 sortie.jpg

# Capture Retina : moitié de résolution, le texte reste net
magick capture.png -strip -resize '1638x>' sortie.png

# Vidéo : H.264 720p, sans audio (bruit d'atelier, voix)
ffmpeg -i video.MOV -vf scale=-2:720 -c:v libx264 -crf 24 -preset slow \
       -an -movflags +faststart sortie.mp4
```

Les originaux sont supprimés après vérification. **Confirmer avec l'utilisateur avant de supprimer** — c'est irréversible.

Attention : en zsh, les tableaux commencent à l'indice 1. Une boucle de renommage indexée à 0 décale tout silencieusement. Préférer un mapping explicite, un appel par fichier.

### Médias manquants

Ce qui n'a pas encore été photographié prend un emplacement réservé, visible sur le site et lisible sur GitHub :

```markdown
<span class="todo-media">[photo : ce qu'il faudra photographier]</span>
```

## 6. Écrire la page

### Court, sans répétition, droit au but

**La direction, c'est la notice IKEA.** L'image montre ; le texte ne dit que ce que l'image ne peut pas dire : un nom de bloc, une valeur, une consigne de sécurité.

**L'objectif chiffré : environ 800 mots affichés pour une séance de 1 h 45.** La S1 du rover en fait 758, un tiers de sa première version (voir §7 pour la mesure).

Pourquoi : quand il y a trop de texte, les jeunes ne lisent pas. La masse paraît insurmontable et la page n'est plus ouverte. C'était le bilan de la première S1 du rover : notice peu utilisée. Tout y était nouveau, le livre compris, et l'autonomie viendra avec les séances. Mais la page était de toute façon beaucoup trop verbeuse.

La page se lit **pendant l'atelier, en écran partagé** : le livre d'un côté, MakeCode ou le montage de l'autre.

**La S1 du rover est l'exemple** : longueur, pas, encadrés, légendes. Sa première version (commit `8fa3561`, 2 436 mots affichés) montre ce qu'on a coupé pour y arriver :

```bash
git show 8fa3561:docs/projets/rover/seances/s01-base-motrice.md
```

| Défaut | Première version | Version actuelle |
|---|---|---|
| La même consigne répétée | La boîte de test : encadré §1, encadré §8, texte §10. « Écran vers l'extérieur » : texte, puis légende | Un seul encadré boîte de test, en §8, au premier allumage. « Écran vers l'extérieur » une fois |
| La légende qui redit le texte | Texte : « écran vers l'extérieur, boutons A et B accessibles » ; légende : idem | 3 légendes sur la page, là où l'image seule ne suffit pas |
| La phrase d'amorce | « Ton programme sait parler à l'écran, mais il ne connaît pas encore les moteurs. Il lui manque le vocabulaire. » | « **Extensions** → colle cette adresse → clique sur « motor ». » |
| Le commentaire sur l'importance | « Prends-le au sérieux. » · « C'est le raisonnement le plus utile de la séance » · « Ce réflexe va te servir pendant les onze séances » | Rien |
| Le pourquoi en trois paragraphes | Encadré « Ce qu'une broche peut donner… », trois paragraphes | Deux lignes, puis → la fiche DFR0548 |
| Deux voies détaillées | « Solution 1 — imprime » et « Solution 2 — recopie », chacune avec sa sous-section | Imprimer par défaut ; « Pas d'imprimante ? Recopie le plan » replié ; le détail dans la fiche carton |
| Ce que l'image montre déjà | Les cotes du plan recopiées en texte sous le plan | « Trait plein : tu découpes. Pointillé : tu plies. » |

**Les règles :**

- **L'image d'abord.** Si la photo ou la capture montre le geste, le texte tient en une ligne, ou disparaît.
- **Un pas sans image se signale** : demander la photo à l'utilisateur plutôt que la remplacer par du texte.
- **La page se suit en ne lisant que les titres et les images.** Si ce n'est pas le cas, ce sont les titres ou les images qu'il faut revoir, pas le texte qu'il faut allonger.
- **Un pas = une action, à l'impératif.** Une ou deux phrases. Pas de transition entre les pas.
- **Une consigne se dit une fois.** Si elle est déjà dans un encadré, le texte n'y revient pas.
- **Les encadrés sont courts aussi.** `[!NOTE]` : deux lignes. `[!CAUTION]` : une ligne par règle, sans justification ; la justification est dans la fiche.
- **Au doute, renvoyer à la fiche** plutôt qu'expliquer dans la séance.
- **Relire en coupant.** Pour chaque phrase : si je l'enlève, le jeune fait-il le pas moins bien ? Sinon, l'enlever.

**L'écran partagé** a deux conséquences : une capture se recadre sur ce qu'il faut voir, et on évite ce qui devient illisible en demi-largeur (tableau large, rangée de trois photos quand une suffit).

**Une séance précédente non terminée** (question 4) : la page s'ouvre sur un pas « Termine la séance N » qui renvoie aux sections concernées de l'ancienne page. On ne recopie rien.

### La mise en forme

**Les encadrés** s'écrivent en syntaxe d'alerte GitHub, rendue nativement sur github.com et convertie en encadré coloré sur le site :

```markdown
> [!CAUTION] Titre de l'encadré
> Le texte.
```

| Type | Usage | Rendu |
|---|---|---|
| `[!CAUTION]` | Sécurité, à lire avant le geste | orange, triangle |
| `[!NOTE]` | Le concept, le pourquoi | bleu |
| `[!TIP]` | Vérification, test rapide | vert |
| `[!IMPORTANT]` | Point de contrôle animateur | vert également sur le site, violet sur GitHub |

**Les solutions d'exercice** se replient, pour que le jeune cherche d'abord :

```markdown
<details markdown>
<summary>La solution</summary>

…

</details>
```

**Les images** en syntaxe Markdown, dans une `<figure markdown>` avec légende. Deux ou trois photos du même geste vont dans un `<div class="photo-row" markdown>`. Les captures d'écran portent `class="screenshot"` sur la figure, pour disposer de plus de largeur.

**Les vidéos** en HTML, avec **un `../` de plus** que pour une image voisine : MkDocs réécrit les chemins relatifs des images en Markdown, mais pas ceux d'une balise `<video>`, et chaque page est publiée dans son propre dossier.

```html
<video controls playsinline preload="metadata" src="../../../../assets/rover-sNN/video.mp4"></video>
```

**Le nom des blocs** se recopie tel qu'il est à l'écran. L'éditeur MakeCode est en français (`au démarrage`, `toujours`, `pause (ms)`, `Télécharger`), l'extension DF-Driver ne l'est pas (`Motor M1 dir CW speed 100`). Ne jamais traduire ce que le jeune va chercher des yeux dans la palette.

Fin de page : la checklist « Ce que tu dois avoir à la fin », le rituel de rangement, le lien vers le carnet de bord. Rien sur la séance suivante.

## 7. Vérifier

```bash
.venv/bin/mkdocs build --strict
```

`--strict` échoue sur tout lien mort — c'est le garde-fou principal.

Mesurer le texte **affiché** de la page élève — sans balises, chemins ni textes alternatifs, que `wc -w` compterait :

```bash
python3 .claude/skills/nouvelle-seance-maker-junior/mots-affiches.py docs/projets/<projet>/seances/sNN-*.md
```

Au-delà d'environ 800 mots pour 1 h 45 (S1 du rover : 758), relire §6 et couper avant de livrer. Annoncer le chiffre à l'utilisateur. Vérifier ensuite que les médias résolvent réellement, ce que la construction ne teste pas :

```bash
python3 - <<'PY'
import re, os, glob
bad = []
for page in glob.glob('site/**/*.html', recursive=True):
    base = os.path.dirname(page)
    for src in re.findall(r'(?:<img|<video)[^>]*?src="([^"]+)"', open(page).read()):
        if not src.startswith(('http', 'data:')) and not os.path.exists(
                os.path.normpath(os.path.join(base, src))):
            bad.append((page, src))
print(*bad, sep="\n") if bad else print("médias : OK")
PY
```

Puis, à l'œil, sur `.venv/bin/mkdocs serve` :

- la nouvelle séance apparaît dans le menu et dans le sommaire des séances
- les encadrés sont colorés, pas des citations brutes
- les solutions se déplient
- les vidéos se lisent
- rien de `animation/` n'a fuité dans le site ni dans la recherche

Enfin : commit **sans trailer d'attribution**, puis `git push`. Le workflow republie le site seul.
