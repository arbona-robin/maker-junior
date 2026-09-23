# Le livre Maker Junior — règles du dépôt

Site MkDocs Material. `docs/` est publié, `animation/` ne l'est pas.

## Deux sorties, deux destinataires

| | `docs/` | `animation/` |
|---|---|---|
| Qui lit | Les jeunes | Toi, la hiérarchie, les partenaires |
| Publié | Sur le site | Non — GitHub seulement |
| Registre | Tutoiement, notice IKEA, ~800 mots par séance | Opératoire, chiffré, honnête |
| Format | Libre | Gabarit La Plateforme, sections figées |

**Budget, ressources humaines, objectifs en langage Bloom, planning prévisionnel, bilan d'atelier : dans `animation/`, jamais dans `docs/`.**

La circulation va dans un seul sens. `animation/<projet>/communication.md` est la **source** du titre, de l'accroche et de la promesse du parcours ; `docs/projets/<projet>/index.md` en est une **dérivation**, réécrite pour le jeune. Si l'une change, vérifier l'autre.

## Les fiches d'animation s'exportent

Elles suivent les gabarits de `animation/gabarits/`, parce qu'elles doivent partir en Google Doc à la même forme que celles des collègues. **Les titres de section ne se renomment pas, ne se réordonnent pas, ne se suppriment pas.** Une section vide porte « — ». Ce qui n'entre dans aucun champ va en « Notes de préparation », après le trait horizontal.

Contrôle :

```bash
norm() { grep '^## ' "$1" | sed -E 's/^## Activité [0-9]+.*/## Activité/; s/ \(.*//; s/ — .*//' | uniq; }
diff <(norm animation/gabarits/seance.md) <(norm animation/rover/s01.md)
```

## Vocabulaire

On parle de **« projet »**, jamais de « trimestre ». Dans le texte comme dans les chemins.

## Écrire une séance

La méthode complète est dans la skill `.claude/skills/nouvelle-seance-maker-junior/`, à charger avant de commencer. Ses références LP (`references/redaction-lp.md`, `modalites.md`, `bloom.md`) se chargent au moment de rédiger, pas avant.

## Vérifier

```bash
.venv/bin/mkdocs build --strict     # échoue sur tout lien mort
python3 .claude/skills/nouvelle-seance-maker-junior/mots-affiches.py <page>
```

## Rendre compte

**Quand le travail s'est passé comme prévu, le dire en deux lignes.** Fait, vérifié, et la question ouverte s'il y en a une. Rien d'autre.

Le détail ne se déroule que s'il change quelque chose pour le lecteur :

- un écart constaté entre ce qui était demandé et ce qui a été trouvé
- un arbitrage pris tout seul, sur lequel il peut être en désaccord
- un chiffre, une valeur ou un nom qui modifie ce qu'il va faire ensuite

Le reste — la liste des contrôles passés, le détail de ce qui a été relu, la justification d'un choix évident — n'apporte rien et noie ce qui compte. Une question en attente se met **en dernier, sur sa propre ligne**, pour qu'elle ne se perde pas dans un compte rendu.

## Commits

**Sans trailer d'attribution** — ni `Co-Authored-By`, ni mention d'outil. C'est une règle du dépôt.
