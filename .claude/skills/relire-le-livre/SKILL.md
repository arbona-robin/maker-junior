---
name: relire-le-livre
description: Relire l'ensemble du livre Maker Junior après une série de modifications, et signaler les incohérences entre pages de séance, fiches de référence, fiches d'animation, cahier des charges et feuilles imprimées. À utiliser quand l'utilisateur dit « relis les fiches », « vérifie la cohérence », « fais une passe sur le livre », ou après un redécoupage de séances. Signale et propose ; ne corrige qu'après accord.
version: 1.0.0
---

# Relire le livre

Après un redécoupage ou une série de modifications, le livre se contredit : une valeur changée à un endroit et pas à l'autre, un bloc utilisé avant d'être présenté, une fiche générale qui parle du rover. Cette skill fait une passe complète et **rend un rapport**. Elle ne corrige rien sans accord.

## 1. Les contrôles mécaniques

```bash
python3 .claude/skills/relire-le-livre/verifier.py
.venv/bin/mkdocs build --strict
```

Le script signale ce qui se voit sans comprendre le texte : style banni, code propre au rover dans une fiche générale, bloc DF-Driver avant l'installation de l'extension, titres qui divergent entre le menu, la page du projet, la page et la fiche d'animation, sections du gabarit, médias inutilisés. La construction stricte signale les liens et ancres morts.

## 2. La relecture

Lire **en entier** chaque fichier concerné, pas des extraits : les incohérences d'ordre ne se voient qu'à la lecture suivie. Lire aussi **le sens** de chaque phrase, pas seulement sa place : un paragraphe bien rangé peut dire quelque chose de faux. Dans l'ordre :

1. **Les fiches de référence** (`docs/fiches/`), une par une.
2. **Les pages de séance** du projet touché, dans l'ordre du parcours.
3. **Les fiches d'animation** de ces séances, et `projet.md`.
4. **Le cahier des charges**, sa feuille d'équipe (`outils/feuilles/`), la page du projet.

Pour chaque fichier, se poser ces questions :

| Question | Exemple de défaut |
|---|---|
| **Chaque paragraphe dit-il une seule chose, et juste ?** Relire phrase par phrase : une comparaison doit être exacte, un renvoi doit mener au même sujet, deux notions voisines ne se mélangent pas dans un paragraphe. | L'I2C comparé au groupe radio, alors que la radio diffuse à tous ; la phrase sur l'extension collée au paragraphe sur l'I2C. |
| **Chaque bloc et chaque notion servent-ils ?** Un bloc qui ne change rien au résultat se retire, même s'il est « plus propre ». Vérifier dans la doc ou le code source plutôt que supposer. | `limiter` entre 0 et 255 alors que le bloc `Motor` plafonne déjà seul. |
| **L'ordre se suit-il ?** Chaque outil est présenté avant d'être utilisé, chaque section s'appuie sur les précédentes. | Un exemple avec des blocs DF-Driver avant la section qui installe l'extension. |
| **La fiche est-elle générale ?** Une fiche de `docs/fiches/` sert plusieurs projets : concepts, exemples neutres. Le code propre à un projet est dans la séance. | `vM1`, la table, la bande 83 dans la fiche MakeCode. |
| **Chaque chose est-elle dite à un seul endroit ?** La séance renvoie à la fiche, la fiche ne recopie pas la séance. | Le même pas à pas dans la fiche et dans la page. |
| **Les valeurs concordent-elles ?** Cahier des charges, feuille d'équipe, pages, fiches d'animation. | 3 h d'impression ici, 4 h là ; 25 × 25 × 20 cm partout ? |
| **Les renvois disent-ils vrai ?** « En séance 4… », « la S9 », « comme en S2 » : la séance citée fait-elle encore ça ? | Après un redécoupage, « la table, en S9 » alors qu'elle est en S8. |
| **Les noms de blocs sont-ils ceux de l'écran ?** Les vérifier sur les images rendues (`docs/assets/blocks/`), pas de mémoire. | « temps écoulé (ms) » au lieu de « temps d'exécution (ms) ». |
| **La page suit-elle le format de sa séance ?** S1 à S5 guidées ; S6 à S9 et S11 : encadré « Nouveau concept » sous le titre, puis le travail de l'équipe. Voir la skill `nouvelle-seance-maker-junior`, §6. | Un concept détaillé dans la page au lieu de la fiche. |

## 3. Le rapport

Un tableau par gravité, **le plus gênant pour un jeune en premier** :

| Fichier | Problème | Correction proposée |
|---|---|---|
| `docs/fiches/carte-dfr0548.md:82` | La section « Le servomoteur » utilise un bloc DF-Driver avant la section qui installe l'extension | Déplacer la section après « Les blocs » |

- Une ligne par problème, avec `fichier:ligne`.
- La correction proposée est concrète : quoi déplacer, quoi réécrire, quelle valeur retenir.
- Quand deux valeurs se contredisent et qu'on ne sait pas laquelle est la bonne, **le demander** plutôt que choisir.

Puis s'arrêter et demander quelles corrections appliquer. Après correction : relancer `verifier.py` et la construction, et regarder les images de blocs redessinées.
