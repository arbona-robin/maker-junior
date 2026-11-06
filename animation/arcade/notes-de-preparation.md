# Jeu d'arcade : notes de préparation

Troisième projet de l'année, en préparation. Rien n'est encore publié dans `docs/`. Le code, la page relais et les tutoriels sont dans le dépôt [arbona-robin/tutoriels-arcade](https://github.com/arbona-robin/tutoriels-arcade).

## L'idée

Un jeu MakeCode Arcade, joué avec une manette micro:bit que les jeunes programment et fabriquent. Comme les autres projets : des séances où tout le monde construit la même chose, puis un projet en équipe. Code, fabrication numérique et électronique dans chaque partie.

Un collègue anime un parcours jeu vidéo sous Unity et Unreal Engine. La différence doit se voir dès la première séance : ici, le jeu sort de l'écran. On joue avec un geste et un bouton qu'on a fabriqué, puis, en équipe, avec une manette inventée pour son jeu.

## Les choix techniques

| Choix | Raison |
|---|---|
| Pas de Bluetooth | Jugé trop risqué en atelier (appairage, interférences entre postes) |
| Micro:bit en USB, page relais WebSerial | MakeCode Arcade ne lit pas la liaison série. La page lit le micro:bit et transmet au simulateur du jeu. Chrome ou Edge seulement |
| Extension Arcade « Manette » | La manette appuie sur les boutons du clavier : le jeu se construit et se teste au clavier, la manette se branche après, sans toucher au jeu |
| Vocabulaire générique du jeu vers la manette | `bip`, `bien`, `mal`, `alerte`, `gagne`, `perdu`, et un chiffre de 0 à 9. Le jeu dit ce qui se passe, chaque manette choisit sa réaction : le code de la première partie resservira dans le projet |
| Sons seulement sur la manette | Le jeu se tait dès que la manette envoie son premier message |
| Mots courts | Les tampons série du micro:bit font 20 octets par défaut |

## Le découpage

11 séances. Le jeu de tir sert de base commune (publié : https://arcade.makecode.com/_6XEcLbKsE53d). La manette commune est le micro:bit porté au poignet dans le bracelet du kit, avec un bouton de tir en carton. Pas de pièce imprimée lourde par jeune : seul un petit capuchon de bouton, quelques minutes d'impression chacun.

### Phase 1 : chacun construit le même jeu et la même manette

| Séance | Titre | Notions | Livrable |
|---|---|---|---|
| S1 | Ton premier jeu de tir | sprite dessiné · déplacement au clavier · projectile · ennemis au hasard · collision entre deux sortes de sprites | vaisseau qui tire sur des ennemis, jouable au clavier |
| S2 | Finis ton jeu : décor, score, vies | score et vies · écran de démarrage · fin de partie · décor dessiné qui défile · difficulté qui augmente avec le score | jeu complet et rejouable au clavier |
| S3 | Ta manette micro:bit | liaison série · protocole d'un mot par ligne · page relais · boutons A et B · réactions de la manette · fermer MakeCode avant de jouer | jeu joué avec le micro:bit en main, qui sonne et affiche les vies |
| S4 | Dessine ton bouton de tir | modélisation 3D dans Tinkercad à partir d'un plan coté commun · contrainte de conception : le capuchon appuie sur le contact et tient dessus · personnalisation · impression additive et slicer | capuchon exporté en `.STL`, imprimé par l'animateur avant S5 |
| S5 | Ta manette : le bracelet et le bouton de tir | découpe au plan coté · circuit fermé · interrupteur carton et aluminium · broche en entrée avec résistance de tirage · micro:bit au poignet · rotation de l'avant-bras pour haut et bas · zone morte | bouton monté avec son capuchon, jeu joué au bracelet et au bouton. Fin du temps individuel |

### Phase 2 : en équipe, un jeu et sa manette

L'animateur montre un concept quelques minutes en début de séance, le reste du temps appartient à l'équipe.

| Séance | Titre | Concept | Livrable |
|---|---|---|---|
| S6 | Choisissez votre jeu | cahier des charges · couple jeu et manette · 3 contacts au plus sans carte d'extension · rôles · croquis | équipes formées, jeu et manette choisis, croquis, tutoriel du type de jeu lancé |
| S7 | Le cœur de votre jeu | gravité, plan des tuiles, caméra, ou les notions du tutoriel choisi | prototype jouable au clavier |
| S8 | Fabriquez votre manette | un contact par broche · l'accéléromètre dans l'objet · une ou deux pièces imprimées si la manette en a besoin | manette fabriquée et câblée, qui envoie ses mots |
| S9 | Le boss, ou les niveaux | état du jeu et phases · compteur propre à un sprite · nouvelle sorte de sprite | jeu avec une progression : boss, niveaux ou vagues |
| S10 | Faites jouer les autres | test par une autre équipe · régler la difficulté et les réactions de la manette | jeu corrigé après un test croisé |

### Phase 3 : valorisation

| Séance | Titre | Livrable |
|---|---|---|
| S11 | La salle d'arcade | bornes installées, jeux joués par d'autres jeunes ou les familles, avec leur lien de partage |

Points à vérifier au premier essai du bracelet : le câble USB part du poignet (longueur, débranchement sur un geste brusque), et les fils du bouton peuvent sauter des pinces crocodile quand le bras bouge.

## Après : jeux et manettes physiques

Pistes de jeux, toutes faisables avec les notions du jeu de tir, chacune avec sa manette :

| Jeu | Manette |
|---|---|
| Danse (flèches qui tombent, sprite personnalisé) | Tapis à contacts au sol |
| Batterie, piano | Pads ou touches en carton |
| Course d'obstacles | Planche d'équilibre ou skate, accéléromètre |
| Tape-taupe | Boutons maison |
| Course d'athlétisme | Pédales ou frappe alternée |
| Skee-ball, boxe, pêche, funambule | Accéléromètre dans l'objet |

Sans carte d'extension, seules P0, P1 et P2 sont faciles d'accès : 3 contacts au plus. La carte DFR0548 peut servir de carte d'extension. Un interrupteur sur P0 demande `pins.setAudioPinEnabled(false)`.

Il manque des notions pour un jeu de plateforme ou d'aventure : gravité et saut, plan des tuiles, caméra. D'où les tutoriels, un par type de jeu, qui partent du jeu de tir et n'ajoutent que ce qui manque.

## Les tutoriels

Hébergés sur GitHub, en français, ouverts par un lien. Le dépôt apporte aussi les blocs Manette à chaque tutoriel.

| Tutoriel | Lien | État |
|---|---|---|
| Jeu de plateforme (13 étapes) | https://arcade.makecode.com/?lang=fr#tutorial:https://github.com/arbona-robin/tutoriels-arcade/plateforme | Testé. Le jeu final avec manette : https://arcade.makecode.com/_dm7fipEA3PX7 |
| Course d'obstacles, danse, tape-taupe | — | À écrire |

Le tutoriel plateforme : niveau déjà dessiné, l'élève dessine lui-même les murs des plateformes. Héros, gravité, caméra, saut, pièces, lave, drapeau, puis la manette. Une partie filmée en GIF ouvre le tutoriel.

## Les manettes publiées

| Programme | Lien |
|---|---|
| Boucle de lecture (à tester en premier) | https://makecode.microbit.org/_Tb5WrvHCc2Dq |
| Événement « quand une donnée est reçue » | https://makecode.microbit.org/_9KwAkm9hUAi3 |

Inclinaison pour les directions, A et B, le logo pour le menu.

## Pièges constatés

- Un onglet MakeCode resté connecté au micro:bit vole des caractères sur la liaison série : mots tronqués, manette qui répond mal. La page relais affiche une alerte. Consigne à prévoir dans les séances : fermer MakeCode avant de connecter la manette.
- Le micro:bit qui défile un long texte pendant qu'il reçoit fait déborder son tampon : la manette se fige, une LED allumée au centre.
- Après une modification sur GitHub, MakeCode garde l'ancienne version du tutoriel en cache. Seule une version créée depuis MakeCode, avec un compte GitHub, vide ce cache.
- Certains blocs restent en anglais dans l'éditeur Arcade en français : « camera suit sprite », « location », « Player ».
- Pour figer la version de MakeCode pendant le parcours : les adresses versionnées (`arcade.makecode.com/v3/`), ou une copie hébergée (`pxt staticpkg`).

## À trancher ou à faire

- Le plan coté commun du bouton de tir, et le temps d'impression des capuchons pour tout le groupe.
- Les tutoriels course d'obstacles, danse, tape-taupe.
- Une fiche de référence par notion : gravité et saut, plan des tuiles, caméra, interrupteur maison.
- La page relais sur le site, ou sur GitHub Pages, plutôt qu'en local.
- Un test automatique de la chaîne avant chaque séance, dans `outils/`.
