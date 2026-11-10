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
| Effets sonores sur la manette | La manette joue les effets (tir, impact, vie perdue). Le jeu garde sa musique de fond : l'extension, qui coupe aujourd'hui tout le son, est à modifier |
| Mots courts | Les tampons série du micro:bit font 20 octets par défaut |

## Le découpage

12 séances, dont une ajustable (S10) : c'est elle qu'on retire si le projet n'en compte que 11. Le jeu de tir sert de base commune (publié : https://arcade.makecode.com/_6XEcLbKsE53d). La manette commune est le micro:bit porté au poignet dans le bracelet du kit, avec un bouton de tir en carton. Le bouton est une seule pièce de carton pliée, deux bandes de ruban de cuivre face à face, une charnière qui fait ressort, une encoche par face où la pince mord le bout d'une seule bande (plan : `outils/plans/plan_bouton.py`). Son capuchon part d'un modèle fourni trop grand (`outils/plans/capuchon_bouton.py`, FreeCAD), que chaque jeune met à l'échelle et personnalise dans Tinkercad : pas de pièce imprimée lourde par jeune.

### Phase 1 : chacun construit le même jeu et la même manette

| Séance | Titre | Notions | Livrable |
|---|---|---|---|
| S1 | Ton premier jeu de tir | pixel art : vaisseau, ennemis, projectile, avec un vrai temps de dessin · déplacement au clavier · projectile · ennemis au hasard · collision entre deux sortes de sprites | vaisseau qui tire sur des ennemis, jouable au clavier |
| S2 | Finis ton jeu : décor, score, vies | écran de démarrage · score et vies · fin de partie · décor en sprites qui défilent derrière le héros (profondeur `z`, fantôme), sans extension · pixel art du décor, avec un temps de dessin à part · ennemis qui accélèrent en « va plus loin » | jeu complet et rejouable au clavier |
| S3 | Ta manette micro:bit | liaison série · protocole d'un mot par ligne · page relais · boutons A et B · réactions de la manette · fermer MakeCode avant de jouer | jeu joué avec le micro:bit en main, qui sonne et affiche les vies |
| S4 | Dessine ton bouton de tir | importer une pièce qui existe : capuchon de bouton d'arcade fourni à 52 mm, ramené à 40 mm par le calcul de l'échelle · couper avec une forme en Perçage · personnalisation · bouton en carton d'après un plan · test de continuité au multimètre | capuchon exporté en `.STL`, imprimé avant S5 ; bouton en carton qui fait contact |
| S5 | Ta manette : le bracelet et le bouton de tir | capuchon tenu par les élastiques · bouton entre P1 et GND, lu comme une broche pressée, condition « ou » · micro:bit au poignet, axe et seuils mesurés de nouveau · zone morte | jeu joué au bracelet et au bouton. Fin du temps individuel |

### Phase 2 : en équipe, un jeu et sa manette

L'animateur montre un concept quelques minutes en début de séance, le reste du temps appartient à l'équipe.

| Séance | Titre | Concept | Livrable |
|---|---|---|---|
| S6 | Choisissez votre jeu | cahier des charges · seul ou en équipe · couple jeu et manette · 3 contacts au plus sans carte d'extension · rôles · croquis | équipes formées, jeu et manette choisis, croquis, tutoriel du type de jeu lancé |
| S7 | Le cœur de votre jeu | les notions du tutoriel choisi : gravité, plan des tuiles, caméra, score au temps de survie, cadence · pixel art des personnages et des tuiles | prototype jouable au clavier |
| S8 | Fabriquez votre manette | un contact par broche · l'accéléromètre dans l'objet · une ou deux pièces imprimées si la manette en a besoin | manette fabriquée et câblée, qui envoie ses mots |
| S9 | Le boss, ou les niveaux | état du jeu et phases · compteur propre à un sprite · nouvelle sorte de sprite | jeu avec une progression : boss, niveaux ou vagues |
| S10 | Soignez votre jeu : musique et pixel art (ajustable) | éditeur de musique d'Arcade, musique de fond · retouche des sprites, des tuiles et du décor | jeu avec sa musique et ses images finies |
| S11 | Faites jouer les autres | test par une autre équipe · régler la difficulté et les réactions de la manette | jeu corrigé après un test croisé |

### Phase 3 : valorisation

| Séance | Titre | Livrable |
|---|---|---|
| S12 | La salle d'arcade | bornes installées, jeux joués par d'autres jeunes ou les familles, avec leur lien de partage |

Points à vérifier au premier essai du bracelet : le câble USB part du poignet (longueur, débranchement sur un geste brusque), et les fils du bouton peuvent sauter des pinces crocodile quand le bras bouge.

## Les familles de jeux du projet (S6)

| Famille | Pour le jeune | Jeux | Manette | Ce qui est nouveau par rapport au jeu de tir |
|---|---|---|---|---|
| Plateforme | jeu de plateforme | sauter, ramasser, éviter | bracelet + bouton | gravité et saut, plan des tuiles, caméra |
| Course et évitement | jeu de course | voiture, skate, obstacles | planche d'équilibre, skate, volant, accéléromètre | presque rien : c'est le jeu de tir sans le tir. Le score au temps de survie est nouveau |
| Rythme | jeu de rythme | danse, batterie, piano | contacts en carton : tapis, pads, touches | un signal qui descend en cadence vers une ligne, une fenêtre de temps, plusieurs contacts |
| Réaction | jeu de réflexes | tape-taupe | boutons en carton | un signal qui apparaît au hasard, un compte à rebours |
| Geste | jeu de sport | boxe, skee-ball, pêche, tennis | l'objet frappé, lancé ou secoué, micro:bit dedans | la force du mouvement, à doser : la manette envoie 2 ou 3 niveaux (`doux`, `moyen`, `fort`) |

Rythme et réflexes partagent une mécanique (un signal, appuyer au bon moment) et un tutoriel : le tape-taupe d'abord, puis le signal qui descend. Danse, batterie et piano ne diffèrent que par l'habillage. Le sport reprend la même mécanique, seule la manette change : au skee-ball, un lancer trop doux reste court, un lancer trop fort sort de la piste.

### Les contacts

Sans carte d'extension, seules P0, P1 et P2 sont faciles d'accès : 3 contacts. La DFR0548 donne accès à 9 broches (P0, P1, P2, P8, P12 à P16), mais demande sa propre alimentation (3,5 à 5,5 V) : bonne pour un piano ou une batterie sur la table, pas pour un bracelet. Les boutons A, B et le logo du micro:bit s'ajoutent si le micro:bit est fixé sur la manette. Un interrupteur sur P0 demande `pins.setAudioPinEnabled(false)`.

Le plafond réel est l'extension : la page relais transmet les 7 boutons de la console Arcade (gauche, droite, haut, bas, A, B, menu), soit 6 touches utiles. Six notes suffisent pour un piano en gamme pentatonique (do, ré, mi, sol, la, do aigu), où rien ne sonne faux.

Évolutions de l'extension, gardées pour le tutoriel rythme. D'abord la musique : le jeu garde sa musique de fond et seuls les effets passent à la manette, au lieu de couper tout le son du jeu dès que la manette se connecte. Ensuite un bloc « quand la manette envoie [mot] », pour des mots libres (`t1` à `t9`, `coup`, `doux`, `fort`). C'est le principe des messages radio du Rover. Trois points à régler : l'extension annonce à la page relais les mots qu'elle écoute (les autres déclenchent toujours l'alerte des lettres perdues), le bloc se déclenche une fois par appui et pas à chaque mot répété, et les boutons de la phase commune restent inchangés.

## Les tutoriels

### En séance : la notion, puis le tutoriel

Chaque notion est présentée en dix minutes, puis chacun avance à son rythme dans un tutoriel MakeCode, l'animateur circule. Les tutoriels portent la consigne pas à pas : l'animateur, très sollicité, gagne du temps pour aider, et les jeunes gagnent en autonomie. Chaque tutoriel reste court, 10 à 12 étapes : refaire un long tutoriel lasse vite.

Le jeu de tir est une skillmap (parcours de tutoriels enchaînés, Arcade seulement) de trois activités, une par séance : S1 le vaisseau, les ennemis et le tir ; S2 le décor, le score et les vies ; S3 les blocs Manette. Le code et les dessins passent d'une activité à la suivante (`allowcodecarryover`, actif par défaut). Adresse : `arcade.makecode.com/--skillmap#github:arbona-robin/tutoriels-arcade/<fichier>`.

La progression est enregistrée dans le navigateur. Chaque jeune garde le même poste d'une séance à l'autre. Si un travail est perdu malgré tout :

- chaque activité de la skillmap démarre aussi sans le travail précédent, à partir du code de référence de la séance : le jeune perd ses dessins, pas la séance ;
- en fin de séance, chacun copie le lien de partage de son jeu, ou l'exporte : on le rouvre et on continue.

La manette micro:bit (S3) se programme dans MakeCode micro:bit, où les skillmaps n'existent pas : un tutoriel séparé, dans le dépôt [arbona-robin/tutoriels-microbit](https://github.com/arbona-robin/tutoriels-microbit). L'éditeur micro:bit affiche un bandeau « Contenu non approuvé » sur tout tutoriel venu d'un dépôt GitHub hors de la liste de Microsoft : sans conséquence. Le même dépôt pourra porter des tutoriels pour les premières séances du Rover et de la lampe pixel.

### Les tutoriels du dépôt

Hébergés sur GitHub, en français, ouverts par un lien. Le dépôt apporte aussi les blocs Manette à chaque tutoriel. Chacun part du jeu de tir et n'ajoute que ce qui manque.

| Tutoriel | Lien | État |
|---|---|---|
| Plateforme (13 étapes) | https://arcade.makecode.com/?lang=fr#tutorial:https://github.com/arbona-robin/tutoriels-arcade/plateforme | Testé. Le jeu final avec manette : https://arcade.makecode.com/_dm7fipEA3PX7 |
| Course et évitement | — | À écrire, court : centré sur le score au temps de survie |
| Rythme et réflexes | — | À écrire : le tape-taupe d'abord, puis le signal qui descend vers la ligne. Sert aussi au jeu de sport |

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
- Une manette plus lente que le jeu prend du retard : chaque son joué « jusqu'à la fin », chaque icône (600 ms) ou texte affiché bloque sa boucle d'écoute, pendant que le jeu continue d'envoyer (un `bip` par tir, un `bien` par ennemi). Les mots s'empilent, les réactions arrivent en rafale ; si la réserve déborde, des mots collés défilent en lettres pendant plusieurs secondes de silence. La console de la page relais (F12, préfixe `[relais]`) donne les mots par seconde dans chaque sens.
- Dès qu'un dépôt a un tag, MakeCode charge le dernier tag, pas le dernier commit : chaque publication de tutoriel demande un nouveau tag (`v0.2.0`, `v0.3.0`…) avec la même version dans `pxt.json`. MakeCode garde en plus la liste des tags en cache plusieurs heures : un tutoriel ou une skillmap poussés le jour même peuvent afficher « Aucun contenu chargé ». Pour vider ce cache tout de suite, ouvrir `https://www.makecode.com/api/gh/arbona-robin/tutoriels-arcade/refs?nocache=1` (la liste des versions), et `https://www.makecode.com/api/ghtutorial/arbona-robin/tutoriels-arcade/<tutoriel>?noCache=1` pour un tutoriel. Publier quand même les tutoriels la veille de la séance, pour les vérifier en ligne.
- Certains blocs restent en anglais dans l'éditeur Arcade en français : « camera suit sprite », « location », « Player ».
- Pour figer la version de MakeCode pendant le parcours : les adresses versionnées (`arcade.makecode.com/v3/`), ou une copie hébergée (`pxt staticpkg`).

## À trancher ou à faire

- Le temps d'impression des capuchons pour tout le groupe, à lire au slicer.
- Un câble micro-USB de 2 m par poste, pour le micro:bit au poignet.
- La skillmap du jeu de tir (trois activités) et le tutoriel micro:bit de la manette.
- Les tutoriels course et évitement, rythme et réflexes.
- L'extension : musique du jeu conservée, et bloc « quand la manette envoie [mot] » avec la page relais, au moment du tutoriel rythme.
- Une fiche de référence par notion : gravité et saut, plan des tuiles, caméra, interrupteur maison.
- La page relais en ligne (site ou GitHub Pages), à la préparation des séances.
- Un test automatique de la chaîne avant chaque séance, dans `outils/`.
