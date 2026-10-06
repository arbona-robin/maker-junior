# Fiches d'animation

Les fiches de conduite de séance et les fiches de projet, au format attendu par La Plateforme Jeunesse.

Ce dossier est hors du site publié. Il vit dans le dépôt, se lit sur GitHub, mais n'apparaît ni dans le menu du livre ni dans sa recherche. Les élèves ne tombent pas dessus, ce qui permet d'y écrire ce qui ne les concerne pas : budget, ressources humaines, objectifs en langage Bloom, planning prévisionnel.

## Le format

Les fiches suivent les gabarits LP. **Les titres de section ne se renomment pas, ne se réordonnent pas, ne se suppriment pas** : c'est ce qui permettra d'exporter vers un Google Doc de la même forme que celui des collègues, sans reprise manuelle. Dans les fiches séance et projet, ce qui n'entre dans aucun champ n'y figure pas : la fiche reste courte et lisible. La fiche communication garde une section « Notes de préparation », après le trait horizontal, ignorée à l'export.

| Gabarit | Pour quoi |
|---|---|
| [`gabarits/communication.md`](gabarits/communication.md) | La fiche de présentation du parcours, pour le recrutement et les familles |
| [`gabarits/projet.md`](gabarits/projet.md) | La synthèse de projet, pour la hiérarchie et les partenaires |
| [`gabarits/seance.md`](gabarits/seance.md) | La fiche de conduite d'une séance |

Les conseils de rédaction champ par champ, la liste des modalités pédagogiques et les verbes de Bloom sont dans les références de la skill `nouvelle-seance-maker-junior`.

## Rover

- [Fiche communication](rover/communication.md)
- [Fiche synthèse de projet](rover/projet.md) : planning prévisionnel des 12 séances et budget
- [Séance 1 — Fais tourner tes moteurs](rover/s01.md)
- [Séance 2 — Fabrique ton rover et fais-le rouler droit](rover/s02.md)
- [Séance 3 — Ta plaque, et les mouvements de ton rover](rover/s03.md)
- [Séance 4 — Pilote ton rover à distance](rover/s04.md)
- [Séance 5 — Formez votre équipe et concevez le rover de mission](rover/s05.md)
- [Séance 6 — Dessinez les pièces de votre rover](rover/s06.md)
- [Séance 7 — Faites bouger une pièce avec un servomoteur](rover/s07.md)
- [Séance 8 — Faites piloter votre rover par la table](rover/s08.md)
- [Séance 9 — Guidez votre rover vers une cible](rover/s09.md)
- [Séance 10 — Votre rover face au cahier des charges](rover/s10.md)
- [Séance 11 — Présentez votre rover sur une page web](rover/s11.md)
- [Séance 12 — Vos rovers en épreuve](rover/s12.md)

## Objets connectés

- [Fiche communication](objets-connectes/communication.md)
- [Fiche synthèse de projet](objets-connectes/projet.md) : planning prévisionnel des 10 séances et budget
- [Séance 1 — Fabrique ta lampe et allume-la](objets-connectes/s01.md)
- [Séance 2 — Compose la lumière de ta lampe](objets-connectes/s02.md)
- [Séance 3 — Fais-la s'allumer quand il fait nuit](objets-connectes/s03.md)
- [Séance 4 — Dessine l'emblème de ta lampe](objets-connectes/s04.md)
- [Séance 5 — Fais parler les lampes entre elles](objets-connectes/s05.md)
- [Séance 6 — Choisissez votre produit](objets-connectes/s06.md)
- [Séance 7 — Construisez la structure de votre produit](objets-connectes/s07.md)
- [Séance 8 — Faites fonctionner votre produit et montrez ses données](objets-connectes/s08.md)
- [Séance 9 — Testez et installez votre produit](objets-connectes/s09.md)
- [Séance 10 — Présentez vos objets connectés](objets-connectes/s10.md)
- [Le pont et le tableau de bord](objets-connectes/pont.md)

Une fiche de séance est créée avant l'atelier, complétée après : les sections « Bilan » et « Adaptations pour la prochaine fois » se remplissent une fois la séance passée, et nourrissent la fiche suivante.

## Export vers le Google Doc

Le dépôt est la source, le Google Doc de chaque projet en est l'export. Leurs identifiants sont dans [`export.yml`](export.yml). Les commandes prennent le nom du projet : `rover`, `objets-connectes`.

```bash
.venv/bin/pip install -r outils/requirements.txt          # une fois
.venv/bin/python outils/sync_gdoc.py diff rover [s01]     # ce qui diffère, et les commentaires ouverts
.venv/bin/python outils/sync_gdoc.py push rover [s01]     # écrit le dépôt dans le Doc
```

Le push refuse d'écrire si le Doc a été modifié depuis le précédent : lancer `diff`, reporter dans la fiche ce qui doit l'être, puis `push --force`. Il faut les identifiants OAuth dans `~/.config/maker-junior/credentials.json`.
