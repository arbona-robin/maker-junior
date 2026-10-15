# Objets connectés — Le pont et le tableau de bord

Le pont est un micro:bit branché en USB à l'ordinateur de l'animateur. Il écoute la bande `40` et recopie chaque message radio sur le port série. Le tableau de bord, une page web, lit ce port série et affiche chaque micro:bit et ses mesures.

Le tableau de bord : [`docs/tableau-de-bord/index.html`](../../docs/tableau-de-bord/index.html), publié sur le site. Il s'ouvre dans Chrome ou Edge, les seuls navigateurs qui lisent le port série.

## Le programme du pont

Le code, la mise en route et le dépannage sont dans la fiche élève [Installer le pont et le tableau de bord](../../docs/fiches/pont-et-tableau-de-bord.md), publiée pour qu'un jeune puisse refaire l'expérience chez lui. Elle est la seule source du code : une modification du pont se fait là.

## Le contrat entre le pont et la page

| Sens | Une ligne par message | Exemple |
|---|---|---|
| Pont → page | `numéro de série,clé,valeur,signal` | `-1934561230,temp,21,-62` |
| Page → pont | `clé,valeur` | `interA,1` |

Le numéro de série vaut `0` quand l'émetteur n'a pas `radio régler le numéro de série de transmission` : la page affiche alors une carte d'alerte « Sans numéro de série ».

## Ce que fait la page

- Une carte par micro:bit, ajoutée à son premier message. Le nom se change en cliquant dessus, et reste mémorisé dans le navigateur.
- Une mesure par clé, affichée selon le début de la clé : la table est dans le [catalogue](../../docs/projets/objets-connectes/catalogue.md#la-langue-commune), et dans `AFFICHAGES` en tête du script de la page.
- Hors ligne après 30 secondes sans message : la carte pâlit et passe en fin de grille.
- Un interrupteur basculé passe aussitôt dans l'état demandé, grisé, « envoyé… ». Au message suivant de la carte, il prend l'état réel : celui demandé si l'ordre est passé, l'ancien sinon. Sans réponse après 12 secondes, il l'écrit.
- Une ligne abîmée en route (champ manquant, clé trop longue, deux lignes collées) est notée « Ligne illisible » dans le journal, sans créer de carte. La première ligne après la connexion est jetée : elle a pu commencer avant.
- La force du signal en barres et en dBm, utile pour tester la portée en séance 9.
- Le journal de tous les messages, avec un filtre par micro:bit et une pause.
- **Projection** masque le journal et agrandit les cartes.
- **Mode démo** fait apparaître six faux micro:bit, sans pont. L'adresse `…/tableau-de-bord/?demo` le lance directement.
- Un bandeau « Pont débranché » quand on retire le câble : l'affichage se fige, les objets continuent.

## Avant la séance 5

1. Programmer le pont selon la fiche, fermer l'onglet MakeCode, ouvrir le tableau de bord, **Connecter le pont**.
2. Allumer un micro:bit de test qui émet `temp` toutes les 5 secondes, numéro de série compris : sa carte doit apparaître.
3. Basculer un interrupteur `inter` en mode démo, puis avec une lampe qui l'écoute, un papier sur l'écran de son micro:bit : elle s'allume et s'éteint.
