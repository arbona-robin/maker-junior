# Jeu d'arcade — Fiche Synthèse de Projet

Gabarit : [`animation/gabarits/projet.md`](../gabarits/projet.md) · Fiche communication : [`communication.md`](communication.md) · Notes : [`notes-de-preparation.md`](notes-de-preparation.md)

> Le planning des 12 séances est prévisionnel : chaque séance passée corrige la suivante. La séance 10 est ajustable : c'est elle qu'on retire si le projet n'en compte que 11.

## Titre du projet

Jeu d'arcade et ses commandes

## Objectif général

Créer un jeu vidéo d'arcade et fabriquer les commandes physiques pour y jouer, d'abord en suivant un modèle commun, puis en inventant son propre jeu.

## Livrable du parcours

Deux jeux. Le jeu de tir que chaque jeune programme et dessine pendant les cinq premières séances, joué avec un micro:bit au poignet et un bouton de tir en carton dont il a dessiné et emporte le capuchon imprimé. Puis le jeu qu'il invente, seul ou en équipe, avec les commandes fabriquées pour lui : tapis, pads, planche, punching-ball. Chaque jeu a son lien de partage, jouable au clavier chez soi, et les jeux d'équipe sont joués par d'autres en dernière séance.

## Objectifs pédagogiques

- Être capable de programmer en blocs un jeu d'arcade complet (sprites, collisions, score, vies, fin de partie) en suivant un tutoriel, puis de le modifier sans aide
- Être capable de réaliser un interrupteur en carton et aluminium et de le faire lire par une broche du micro:bit, contact vérifié à l'appui et au relâchement
- Être capable de modéliser une pièce qui respecte un plan coté, le capuchon s'emboîtant sur le bouton sans reprise
- Être capable d'expliquer le dialogue entre la manette et le jeu (mots envoyés, réactions reçues) et de l'adapter à une manette de son invention
- Être capable de concevoir un jeu et ses commandes, de le faire tester par d'autres joueurs et de justifier les modifications apportées après le test

## Description du projet

Pendant les cinq premières séances, chaque jeune construit le même jeu de tir dans MakeCode Arcade, dont il dessine les personnages et le décor en pixel art, puis la manette pour y jouer : un micro:bit porté au poignet, que l'on incline pour se déplacer, et un bouton de tir en carton surmonté d'un capuchon modélisé dans Tinkercad. La manette parle au jeu par la liaison série, à travers une page relais, et réagit à ce qui s'y passe : elle sonne et affiche les vies. Ensuite, seul ou en équipe, chacun choisit une famille de jeux (plateforme, course, rythme, réflexes, sport) et invente les commandes qui vont avec, en carton, en récupération ou en impression 3D. Ils apprennent la programmation par blocs et la logique d'un jeu, le pixel art, le circuit fermé et la lecture d'une broche, l'accéléromètre comme commande, la modélisation sur plan coté, le dialogue entre deux programmes selon un protocole, et le test par d'autres joueurs. Chaque notion est présentée dans les dix premières minutes, puis chacun avance à son rythme dans un tutoriel MakeCode : les tutoriels portent la consigne pas à pas, l'animateur circule. Le parcours se termine par une salle d'arcade où les jeux sont joués par d'autres.

## Prérequis

Indispensable : aucun. Le parcours est accessible à des débutants complets.

Utile : avoir suivi le projet Rover ou Objets connectés. MakeCode, le micro:bit et Tinkercad y ont été vus, et le parcours y fait référence sans en dépendre.

## Ressources humaines

1 animateur numérique, maîtrisant MakeCode Arcade, MakeCode micro:bit et Tinkercad.

## Matériel

**Par jeune**

- 1 micro:bit v2 et son bracelet
- 1 câble micro-USB de 2 m, pour jouer le micro:bit au poignet
- Le bouton de tir : carton, papier aluminium, 2 pinces crocodile
- Le capuchon imprimé du bouton, que le jeune emporte
- 1 ordinateur, le même à chaque séance : la progression des tutoriels est enregistrée dans son navigateur

**Commun**

- Trois postes de découpe, chacun avec un outil de découpe, une règle métallique à rebord et un tapis de découpe
- Le plan coté du bouton de tir et du capuchon, imprimé
- Colle, ruban adhésif, papier aluminium
- Imprimante 3D et filament
- Pour les manettes d'équipe : cartes DFR0548 (9 broches, pour les jeux de rythme), pinces crocodile, matériaux de récupération en bac commun
- Casques, pour la séance musique

## Ressources numériques

- MakeCode Arcade (arcade.makecode.com), gratuit et sans inscription
- La skillmap du jeu de tir : trois activités enchaînées (S1, S2, S3), le jeu de chaque séance repris à la suivante. Dépôt [arbona-robin/tutoriels-arcade](https://github.com/arbona-robin/tutoriels-arcade)
- Les tutoriels des familles de jeux (plateforme, course, rythme et réflexes), dans le même dépôt
- L'extension Arcade « Manette », apportée par le dépôt dans chaque tutoriel
- MakeCode micro:bit (makecode.microbit.org) et le tutoriel de la manette (S3)
- La page relais, dans Chrome ou Edge, seuls navigateurs qui lisent la liaison série
- Tinkercad en mode classe (comptes créés par l'animateur, sans adresse personnelle des jeunes)
- Slicer de l'imprimante sur le poste de l'animateur
- Le livre en ligne, ouvert en écran partagé pendant l'atelier

## Budget

Pour 12 jeunes. Prix indicatifs TTC. Le matériel « Possédé » reprend les prix unitaires de la fiche Rover.

| Poste | Qté | Prix unitaire | Total | Statut |
| --- | --- | --- | --- | --- |
| **Électronique** | | | | |
| micro:bit v2 | 12 | 20 € | 240 € | Possédé |
| Bracelet micro:bit | 12 | | | Possédé |
| Câble micro-USB 2 m | 12 | 4 € | 48 € | À acheter |
| Pinces crocodile | 1 | | | Possédé |
| Carte DFRobot DFR0548, magasin du projet | 12 | 12 € | 144 € | Possédé |
| *Sous-total électronique* | | | *432 €* | |
| **Équipement commun** | | | | |
| Outil de découpe | 3 | 8 € | 24 € | Possédé |
| Règle métallique à rebord | 3 | 10 € | 30 € | Possédé |
| Tapis de découpe A3 | 3 | 12 € | 36 € | Possédé |
| Imprimante 3D | 1 | | | Possédé |
| Ordinateurs | 12 | | | Possédé |
| Casques | 12 | | | Possédé |
| **Par parcours** | | | | |
| Filament PLA : capuchons et pièces des manettes d'équipe | 1 | 15 € | 15 € | À racheter |
| Carton, papier aluminium, colle, ruban adhésif | 1 | 30 € | 30 € | À racheter |
| Découpe : lames de rechange | 1 | 10 € | 10 € | À racheter |
| Casse : 15 % des micro:bit et câbles manipulés, 288 € | 1 | 43 € | 43 € | À racheter |

Un parcours coûte environ 98 €, soit 8 € par jeune : 55 € de consommables et 43 € de casse.

Le premier parcours demande 48 € d'achats, les câbles micro-USB de 2 m.

## Séance 1 — Phase 1 — Découverte & prise en main

**Titre :** Ton premier jeu de tir

**Notions :** sprite et pixel art : vaisseau, ennemis, projectile, avec un vrai temps de dessin · déplacement au clavier · projectile · ennemis qui apparaissent au hasard · collision entre deux sortes de sprites · skillmap, activité 1

**Livrable intermédiaire :** vaisseau qui tire sur des ennemis, jouable au clavier, lien de partage copié en fin de séance

## Séance 2 — Phase 1 — Découverte & prise en main

**Titre :** Finis ton jeu : décor, score, vies

**Notions :** pixel art du décor, avec un vrai temps de dessin · score et vies · écran de démarrage · fin de partie · décor qui défile · difficulté qui augmente avec le score · skillmap, activité 2

**Livrable intermédiaire :** jeu complet et rejouable au clavier

## Séance 3 — Phase 1 — Découverte & prise en main

**Titre :** Ta manette micro:bit

**Notions :** liaison série · protocole d'un mot par ligne · page relais · boutons A et B · réactions de la manette (`bip`, `bien`, `mal`, vies affichées) · fermer MakeCode avant de jouer · tutoriel micro:bit de la manette, skillmap activité 3

**Livrable intermédiaire :** jeu joué avec le micro:bit en main, qui sonne et affiche les vies

## Séance 4 — Phase 1 — Découverte & prise en main

**Titre :** Dessine ton bouton de tir

**Notions :** modélisation 3D dans Tinkercad à partir d'un plan coté commun · contrainte de conception : le capuchon appuie sur le contact et tient dessus · personnalisation : emblème, initiale · impression additive et slicer

**Livrable intermédiaire :** capuchon exporté en `.STL`, nommé selon la convention, imprimé par l'animateur avant S5

## Séance 5 — Phase 1 — Découverte & prise en main

**Titre :** Ta manette : le bracelet et le bouton de tir

**Notions :** découpe au plan coté · circuit fermé · interrupteur carton et aluminium : deux cartons garnis d'aluminium, un écarteur en carton percé au centre, le capuchon collé au-dessus du trou · broche en entrée avec résistance de tirage · micro:bit au poignet · rotation de l'avant-bras pour haut et bas · zone morte

**Livrable intermédiaire :** bouton monté avec son capuchon, jeu joué au bracelet et au bouton. Fin du temps individuel.

## Séance 6 — Phase 2 — Exploration & création

**Titre :** Choisissez votre jeu

**Notions :** cahier des charges · seul ou en équipe · familles de jeux : plateforme, course, rythme, réflexes, sport · couple jeu et commandes · 3 contacts au plus sans carte d'extension, 9 avec la DFR0548 · rôles · croquis

**Livrable intermédiaire :** équipes formées, jeu et commandes choisis, croquis, tutoriel de la famille de jeux lancé

## Séance 7 — Phase 2 — Exploration & création

**Titre :** Le cœur de votre jeu

**Notions :** les notions du tutoriel choisi : gravité et saut, plan des tuiles, caméra, score au temps de survie, signal en cadence · pixel art des personnages et des tuiles

**Livrable intermédiaire :** prototype jouable au clavier

## Séance 8 — Phase 2 — Exploration & création

**Titre :** Fabriquez vos commandes

**Notions :** un contact par broche · l'accéléromètre dans l'objet : inclinaison ou force du geste · une ou deux pièces imprimées si les commandes en ont besoin

**Livrable intermédiaire :** commandes fabriquées et câblées, qui envoient leurs mots

## Séance 9 — Phase 2 — Exploration & création

**Titre :** Le boss, ou les niveaux

**Notions :** état du jeu et phases · compteur propre à un sprite · nouvelle sorte de sprite

**Livrable intermédiaire :** jeu avec une progression : boss, niveaux ou vagues

## Séance 10 — Phase 3 — Finalisation & valorisation

**Titre :** Soignez votre jeu : musique et pixel art

**Notions :** éditeur de musique d'Arcade, musique de fond · effets sonores joués par la manette · retouche des sprites, des tuiles et du décor

**Livrable intermédiaire :** jeu avec sa musique et ses images finies. Séance ajustable, retirée si le projet compte 11 séances.

## Séance 11 — Phase 3 — Finalisation & valorisation

**Titre :** Faites jouer les autres

**Notions :** test par une autre équipe · noter ce qui bloque · régler la difficulté et les réactions de la manette

**Livrable intermédiaire :** jeu corrigé après un test croisé

## Séance 12 — Phase 3 — Finalisation & valorisation

**Titre :** La salle d'arcade

**Notions :** installer une borne : jeu, commandes, page relais · expliquer son jeu à un joueur qui le découvre

**Livrable intermédiaire :** bornes installées, jeux joués par d'autres jeunes ou les familles, chaque jeu avec son lien de partage
