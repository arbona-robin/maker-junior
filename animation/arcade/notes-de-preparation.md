# Jeu d'arcade : notes de préparation

Troisième projet de l'année, en préparation. Rien n'est encore publié dans `docs/`. Le code, la page relais et les tutoriels sont dans le dépôt [arbona-robin/tutoriels-arcade](https://github.com/arbona-robin/tutoriels-arcade).

## L'idée

Un jeu MakeCode Arcade, joué avec une manette micro:bit que les jeunes programment et fabriquent. Comme les autres projets : 5 à 6 séances où tout le monde construit la même chose, puis un projet seul ou en groupe. Code, fabrication numérique et électronique dans chaque partie.

Un collègue anime un parcours jeu vidéo sous Unity et Unreal Engine. La différence doit se voir dès la première séance : ici, le jeu sort de l'écran. Le micro:bit n'est pas seulement une manette tenue en main, il est mis en situation dans un objet fabriqué, et c'est l'objet qui joue.

## Les choix techniques

| Choix | Raison |
|---|---|
| Pas de Bluetooth | Jugé trop risqué en atelier (appairage, interférences entre postes) |
| Micro:bit en USB, page relais WebSerial | MakeCode Arcade ne lit pas la liaison série. La page lit le micro:bit et transmet au simulateur du jeu. Chrome ou Edge seulement |
| Extension Arcade « Manette » | La manette appuie sur les boutons du clavier : le jeu se construit et se teste au clavier, la manette se branche après, sans toucher au jeu |
| Vocabulaire générique du jeu vers la manette | `bip`, `bien`, `mal`, `alerte`, `gagne`, `perdu`, et un chiffre de 0 à 9. Le jeu dit ce qui se passe, chaque manette choisit sa réaction : le code de la première partie resservira dans le projet |
| Sons seulement sur la manette | Le jeu se tait dès que la manette envoie son premier message |
| Mots courts | Les tampons série du micro:bit font 20 octets par défaut |

## Les séances communes

Le jeu de tir (publié : https://arcade.makecode.com/_6XEcLbKsE53d) : un vaisseau, des ennemis, le score et les vies, un écran de démarrage, un décor dessiné qui défile. A tire, B active un bouclier (piste « aller plus loin »). La manette fait bip au tir, réagit aux ennemis détruits et aux chocs, affiche les vies.

Ce que les 5 à 6 séances doivent contenir, en plus du jeu :

- fabriquer un interrupteur en carton (aluminium, carton, pinces) branché sur P0, P1 ou P2 ;
- programmer la télécommande : le micro:bit envoie ses mots, reçoit les réactions ;
- mettre le micro:bit en situation avec l'accéléromètre : fixé sur une planche d'équilibre, un volant, une raquette, un sac de frappe ;
- peut-être Tinkercad et l'impression 3D, comme sur les autres parcours : capuchons de boutons, coque de manette, support qui fixe le micro:bit sur l'objet.

Le boss du jeu de tir peut faire le lien vers le projet : il introduit un état du jeu (phases), un compteur propre à un sprite, une nouvelle sorte de sprite.

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

- L'ordre des séances communes : où placer l'interrupteur en carton, l'accéléromètre en situation et l'impression 3D.
- Tinkercad ou non dans ce parcours.
- Les tutoriels course d'obstacles, danse, tape-taupe.
- Une fiche de référence par notion : gravité et saut, plan des tuiles, caméra, interrupteur maison.
- La page relais sur le site, ou sur GitHub Pages, plutôt qu'en local.
- Un test automatique de la chaîne avant chaque séance, dans `outils/`.
