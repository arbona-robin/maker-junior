---
name: integrer-les-retours
description: Relever les modifications et les commentaires faits dans le Google Doc d'un projet (fiches d'animation exportées), les regrouper par famille, proposer un traitement pour chacune, puis les intégrer dans le dépôt et renvoyer le Doc. À utiliser quand l'utilisateur dit « j'ai commenté le Doc », « regarde mes retours », « intègre les commentaires », « qu'est-ce qui a changé dans le Doc », ou avant tout push vers le Doc.
version: 1.0.0
---

# Intégrer les retours du Google Doc

Le dépôt est la source, le Google Doc en est l'export (voir `animation/README.md`). Mais c'est dans le Doc qu'on relit : on y corrige à la main et on y commente. Cette skill ramène ces retours dans le dépôt, sans en perdre, et sans les appliquer mot pour mot quand ils signalent un problème plus large.

## 1. Relever

```bash
.venv/bin/python outils/sync_gdoc.py diff <projet>
```

La sortie a trois parties :

1. **Modifié dans le Doc depuis le dernier push** : les retouches faites à la main dans le Doc. Le prochain push les effacerait. Elles viennent de l'instantané `animation/.gdoc/<projet>.json`.
2. **Différences entre le Doc et le dépôt** : ce que le push écrirait. Une retouche du Doc y apparaît aussi, en sens inverse : ne pas la compter deux fois.
3. **Commentaires ouverts** : l'identifiant entre crochets, l'auteur, le passage cité, le texte.

Relire ensuite, dans le dépôt, chaque fiche concernée autour du passage : un commentaire porte souvent sur plus que la phrase citée.

## 2. Regrouper par famille

Un même retour peut toucher plusieurs endroits. Avant de proposer quoi que ce soit, regrouper :

| Famille | Exemple | Traitement habituel |
|---|---|---|
| **Coquille, orthographe, typographie** | « 6ème » pour « 6e », une faute d'accord | Corriger, puis **chercher la même faute partout** (`grep`) : dans toutes les fiches du projet, et dans `docs/` si elle y est aussi |
| **Retouche de formulation** | Une phrase réécrite dans le Doc | La reporter dans la fiche. L'ajuster seulement si elle enfreint une règle du dépôt (style, vocabulaire), et le dire |
| **Clarté pour un lecteur extérieur** | « Est-ce parlant pour quelqu'un qui ne connaît pas le projet ? » | Réécrire sans jargon interne (« la table », « A1 », « S10 »). Vérifier les autres fiches destinées à la hiérarchie : le même jargon y est souvent |
| **Fait devenu faux** | « Le découpage du châssis est maintenant en S2 » | Corriger la phrase, puis **chercher toutes les affirmations qui dépendent du même fait** : fiches d'animation, `projet.md`, `communication.md`, pages élèves, page du projet |
| **Remarque de fond** | Un choix pédagogique contesté, une séance à redécouper | Ne pas l'appliquer seul : proposer une option, avec ses conséquences sur les autres séances, et attendre l'accord |
| **Question** | « Pourquoi ce temps ? » | Répondre dans le rapport. Ne modifier une fiche que si la réponse révèle un défaut |

Quand un même retour revient à plusieurs endroits, ou qu'un commentaire et une retouche disent la même chose, c'est **une seule famille**, traitée une fois, partout.

## 3. Proposer

Un rapport, puis s'arrêter :

| # | Famille | Où (Doc et dépôt) | Ce qui est demandé | Traitement proposé |
|---|---|---|---|---|
| 1 | Retouche de formulation | projet · Description | « à partir de la 6ème séance » | Reporter, en « 6e » |
| 2 | Clarté | projet · Description | « la table » n'est pas parlant | « une table équipée d'une caméra » ; même mot dans communication.md : oui ou non |

- Donner le texte proposé en entier quand il remplace une phrase : l'utilisateur valide un texte, pas une intention.
- Signaler ce qui s'étend au-delà du passage commenté (autres fiches, pages élèves).
- Quand deux options se valent, recommander l'une des deux.
- Les retouches du Doc qu'on ne garde pas se disent aussi : le push va les effacer.

## 4. Intégrer

Après l'accord :

1. Modifier **les fiches du dépôt**, jamais le Doc. Si la modification touche la promesse du parcours, `communication.md` est la source et `docs/projets/<projet>/index.md` sa dérivation : mettre les deux à jour.
2. Appliquer les règles habituelles : gabarit intact (`animation/gabarits/`), style du dépôt (pas de tiret cadratin, pas de formule à effet).
3. Vérifier :
   ```bash
   .venv/bin/python outils/sync_gdoc.py diff <projet>        # la retouche du Doc est-elle reportée ?
   python3 .claude/skills/relire-le-livre/verifier.py         # si docs/ a été touché
   .venv/bin/mkdocs build --strict
   ```
4. **Répondre aux commentaires, avant de pousser.** Le push réécrit les sections modifiées : un commentaire accroché à leur texte en serait détaché. Pour chaque commentaire, une réponse courte qui dit ce qui a été fait, et la clôture s'il est traité :
   ```bash
   .venv/bin/python outils/sync_gdoc.py repondre <projet> <ID> "Reformulé : « … »." --resoudre
   ```
   Un commentaire non traité (remarque de fond en attente, question) reçoit une réponse, sans `--resoudre`.
5. Pousser. `--force` n'est permis qu'une fois **chaque** retouche du Doc reportée ou explicitement abandonnée :
   ```bash
   .venv/bin/python outils/sync_gdoc.py push <projet> --force
   ```
   Le push met l'instantané à jour. Le commiter avec les fiches.

## 5. Rendre compte

En deux lignes : ce qui est intégré, les commentaires résolus, et le Doc à jour. Puis ceux qui restent ouverts, et pourquoi.
