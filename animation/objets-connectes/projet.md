# Objets connectés — Fiche Synthèse de Projet

Gabarit : [`animation/gabarits/projet.md`](../gabarits/projet.md) · Fiche communication : [`communication.md`](communication.md)

> Le planning des 10 séances est prévisionnel : chaque séance passée corrige la suivante.

## Titre du projet

Objets connectés

## Objectif général

Fabriquer un objet connecté personnel qui mesure, décide et communique, puis concevoir en équipe un objet connecté, l'installer et le faire fonctionner dans ses conditions réelles.

## Livrable du parcours

Une lampe d'ambiance par jeune : un support en carton personnalisé, un circuit en ruban de cuivre, une matrice de LED RGB dont il a composé la lumière, un capteur qui l'allume à la tombée du jour, un emblème qu'il a dessiné et fait imprimer, et une liaison radio avec les lampes des autres. Puis un produit par équipe de deux ou trois, installé et visible sur le tableau de bord commun. Chaque équipe présente son produit et ses lampes sur une page web publiée : c'est ce que chaque jeune garde du parcours.

## Objectifs pédagogiques

- Être capable de réaliser un circuit électrique fermé puis de le faire commander par un micro:bit, entrée et sortie identifiées, sans erreur de polarité
- Être capable de programmer un objet qui allume sa lumière seul à partir d'un seuil choisi d'après des mesures relevées, et qui ne réagit qu'au changement d'état
- Être capable de concevoir une pièce imprimée en 3D qui respecte des contraintes de dimension et s'imprime sans défaut, puis une pièce qui porte un composant existant
- Être capable de comparer une organisation radio centralisée et une organisation distribuée, en expliquant ce qui arrive quand un objet tombe en panne
- Être capable de concevoir en équipe un objet connecté, de le tester dans ses conditions réelles et de justifier ses choix techniques devant un public non spécialiste

## Description du projet

Pendant les cinq premières séances, chaque jeune construit la même lampe d'ambiance, qu'il personnalise : couleurs, animation, emblème. En la construisant, il traverse toute la chaîne d'un objet connecté : un circuit électrique, de la lumière adressable, un capteur et un seuil, une pièce conçue en 3D, la radio. Les équipes de deux ou trois conçoivent ensuite un produit, choisi dans un catalogue ajusté à l'inventaire ou inventé par l'équipe, à taille réelle quand c'est possible. Tous les produits parlent le même protocole radio. Un pont USB recopie ce trafic vers un tableau de bord web, qui reconnaît chaque micro:bit et choisit l'affichage de chaque mesure d'après sa clé ; il supervise le système sans le commander : débranché, les objets continuent de fonctionner. Ils apprennent le circuit électrique et sa commande par une broche, la mesure et le seuil, l'état mémorisé, la conception d'une pièce pour une fonction, le message diffusé et le message adressé, l'alimentation d'un objet qui doit durer, le test des cas limites, et la présentation d'un choix technique sur une page web. Une notion par séance, présentée dans les dix premières minutes, pour que chacun avance ensuite à son rythme. Le rythme ne suit pas le découpage 3/6/3 : la phase 1 compte cinq séances, parce que la lampe est le socle technique de tout le chantier ; la phase 2 en compte trois, et la phase 3 deux, l'épreuve et l'installation étant réunies en séance 9.

## Prérequis

Indispensable : aucun. Le parcours est accessible à des débutants complets.

Utile : avoir suivi le projet Rover. La radio, les capteurs, MakeCode et Tinkercad y ont été vus, et le parcours y fait référence sans en dépendre.

## Ressources humaines

1 animateur numérique, maîtrisant MakeCode, le micro:bit, Tinkercad et un peu de soudure (préparation des matrices).

## Matériel

**Par jeune**

- 1 micro:bit v2, alimenté par un boîtier 2 × AAA (de préférence) ou par l'USB
- 1 matrice RGB 8 × 8 WS2812
- 1 boîtier 4 × AA d'accus NiMH, pour la matrice
- 1 support de lampe en carton pré-découpé
- Ruban de cuivre, 1 LED 5 mm
- 3 câbles à pinces crocodile
- 1 bac nominatif

**Commun**

- Bornes de connexion à levier
- Câbles Dupont, fil souple multibrin
- Trois postes de découpe : outil de découpe, règle métallique à rebord, tapis
- Pied à coulisse, règles
- Imprimante 3D, filament PLA
- Papier calque, colle, ruban adhésif
- Chargeur d'accus, multimètre
- Pour le chantier : capteurs selon l'inventaire, servomoteurs, moteurs TT, cartes DFR0548, breadboards, adaptateurs secteur USB 5 V
- 1 micro:bit pour le pont USB

## Ressources numériques

- MakeCode (makecode.microbit.org), gratuit et sans inscription, avec l'extension `neopixel` ajoutée depuis la fenêtre Extensions
- Chrome ou Edge, pour Afficher données et pour le pont USB
- Tinkercad en mode classe (comptes créés par l'animateur, sans adresse personnelle des jeunes)
- Slicer de l'imprimante sur le poste de l'animateur
- Le [tableau de bord](../../docs/tableau-de-bord/index.html), une page web qui se configure d'après les clés reçues, et le programme du pont : voir [`pont.md`](pont.md)
- 1 ordinateur par jeune
- Le livre en ligne, ouvert en écran partagé pendant l'atelier
- Carnet de bord numérique
- Gabarit de la page web de présentation (S10), commun à tous les parcours : [`docs/assets/gabarit-page.zip`](../../docs/assets/gabarit-page.zip), un éditeur de texte et un navigateur

## Budget

Pour 12 jeunes. Prix indicatifs TTC. Le matériel « Possédé » reprend les prix unitaires de la fiche Rover.

| Poste | Qté | Prix unitaire | Total | Statut |
| --- | --- | --- | --- | --- |
| **Électronique** | | | | |
| micro:bit v2 (12 lampes, pont) | 13 | 20 € | 260 € | Possédé |
| Boîtier 4 × AA | 12 | 2 € | 24 € | Possédé |
| Accus NiMH AA | 48 | 3 € | 144 € | Possédé |
| Câble USB | 12 | 3 € | 36 € | Possédé |
| Carte DFRobot DFR0548, magasin du chantier | 12 | 12 € | 144 € | Possédé |
| Moteur TT, magasin du chantier | 24 | 4 € | 96 € | Possédé |
| Servomoteur, magasin du chantier | 12 | 3 € | 36 € | Possédé |
| LED 5 mm, résistances, pinces crocodile, câbles Dupont, breadboards, barrettes | 1 | | | Possédé |
| Boîtier 2 × AAA avec connecteur micro:bit | 12 | 2 € | 24 € | Proposé |
| Accus NiMH AAA | 24 | 2 € | 48 € | Proposé |
| Matrice RGB 8 × 8 WS2812, lots de 3 | 4 | 10 € | 40 € | À acheter |
| Bornes de connexion à levier, boîte de 50 | 1 | 19 € | 19 € | À acheter |
| Ruban de cuivre adhésif conducteur, 10 mm × 20 m | 1 | 10 € | 10 € | À acheter |
| Matrice RGB, lot de 3 de rechange | 1 | 10 € | 10 € | Proposé |
| Adaptateur secteur USB 5 V, produits installés près d'une prise | 6 | 5 € | 30 € | Proposé |
| Capteurs du chantier, selon l'inventaire | | | | Selon le catalogue |
| *Sous-total électronique* | | | *921 €* | |
| **Équipement commun** | | | | |
| Chargeur d'accus | 1 | 35 € | 35 € | Possédé |
| Multimètre | 1 | 20 € | 20 € | Possédé |
| Outil de découpe | 3 | 8 € | 24 € | Possédé |
| Règle métallique à rebord | 3 | 10 € | 30 € | Possédé |
| Tapis de découpe A3 | 3 | 12 € | 36 € | Possédé |
| Pied à coulisse | 1 | 15 € | 15 € | Proposé |
| Fer à souder et étain, pour la préparation des matrices | 1 | 30 € | 30 € | Proposé |
| Imprimante 3D | 1 | | | Possédé |
| Ordinateurs | 12 | | | Possédé |
| **Par parcours** | | | | |
| Filament PLA : emblèmes et pièces du chantier | 2 | 25 € | 50 € | À racheter |
| Découpe : lames de rechange | 1 | 10 € | 10 € | À racheter |
| Carton, colle, papier calque, ruban adhésif, élastiques | 1 | 40 € | 40 € | À racheter |
| Casse : 15 % de l'électronique des lampes | 1 | 78 € | 78 € | À racheter |

Un parcours coûte environ 178 €, soit 15 € par jeune : 100 € de consommables d'impression, de découpe et de fabrication, et 78 € de casse. La casse est calculée sur ce que les jeunes manipulent toute l'année (micro:bit, matrices, boîtiers et accus des lampes, soit 520 €).

Le premier parcours demande 69 € d'achats : matrices, bornes et ruban de cuivre. Les matrices se réutilisent, les lampes restant à l'atelier. S'y ajoutent 40 € proposés (rechange, adaptateurs secteur), les capteurs du chantier après inventaire, et 72 € de boîtiers et d'accus AAA si le stock n'en a pas.

## Séance 1 — Phase 1 — Découverte & prise en main

**Titre :** Fabrique ta lampe et allume-la

**Notions :** circuit fermé · polarité de la LED · le micro:bit comme source d'énergie · sortie numérique · entrée analogique · seuil

**Livrable intermédiaire :** lampe montée, LED allumée puis clignotante par programme, bandes de cuivre utilisées comme bouton qui affiche une icône au toucher

## Séance 2 — Phase 1 — Découverte & prise en main

**Titre :** Compose la lumière de ta lampe

**Notions :** alimentation séparée et masse commune · adressage d'un élément dans un ensemble · index en deux dimensions · couleur en trois nombres · luminosité bridée

**Livrable intermédiaire :** matrice câblée et fixée sur la lampe, une couleur choisie et une animation

## Séance 3 — Phase 1 — Découverte & prise en main

**Titre :** Fais-la s'allumer quand il fait nuit

**Notions :** mesure brute · Afficher données · seuil · variable d'état · ne réagir qu'au changement

**Livrable intermédiaire :** lampe qui s'allume seule sous le seuil et s'éteint au-dessus, seuil noté au carnet

## Séance 4 — Phase 1 — Découverte & prise en main

**Titre :** Dessine l'emblème de ta lampe

**Notions :** modélisation 3D · contrainte de conception · relief et creux · îlots détachés · impression additive et slicer

**Livrable intermédiaire :** emblème exporté en `.STL`, nommé selon la convention, imprimé par l'animateur avant la séance 5

## Séance 5 — Phase 1 — Découverte & prise en main

**Titre :** Fais parler les lampes entre elles

**Notions :** une bande pour tous · message diffusé et message adressé · organisation centralisée et distribuée · ce qui arrive quand un élément tombe en panne

**Livrable intermédiaire :** lampe qui mesure, décide, agit, émet et reçoit ; vague réussie avec le chef, puis en relais au moins en groupe

## Séance 6 — Phase 2 — Exploration & création

**Titre :** Choisissez votre produit

**Notions :** servomoteur et moteur à courant continu · choisir un composant pour une fonction · cahier des charges · contraintes d'implantation

**Livrable intermédiaire :** équipe formée, cahier des charges en cinq lignes validé, croquis, matériel réservé au magasin

## Séance 7 — Phase 2 — Exploration & création

**Titre :** Construisez la structure de votre produit

**Notions :** CAO fonctionnelle · mesure de l'existant et jeu · orientation d'impression selon les efforts · support de capteur et fixation

**Livrable intermédiaire :** structure montée à blanc, pièces 3D envoyées à l'impression ; plus aucune impression après cette séance

## Séance 8 — Phase 2 — Exploration & création

**Titre :** Faites fonctionner votre produit et montrez ses données

**Notions :** schéma de câblage · alimentation d'un objet qui dure · sobriété d'émission · protocole commun · chemin de la donnée · système et supervision

**Livrable intermédiaire :** produit fonctionnel en version brute, qui émet sur le protocole commun et apparaît en ligne sur le tableau de bord

## Séance 9 — Phase 3 — Finalisation & valorisation

**Titre :** Testez et installez votre produit

**Notions :** cas limites · test d'endurance · portée radio réelle · implantation · scénario de démonstration et plan B

**Livrable intermédiaire :** produit installé à son emplacement, stable sans intervention, photographié ; présentation d'une minute répétée, entretien réparti

## Séance 10 — Phase 3 — Finalisation & valorisation

**Titre :** Présentez vos objets connectés

**Notions :** page web à partir d'un gabarit HTML · balise, titre, paragraphe, image · variable CSS · présenter et argumenter un choix technique · bilan de projet

**Livrable intermédiaire :** page de présentation de l'objet remplie, avec un choix justifié et les lampes de l'équipe ; démonstration menée
