# Rover — Fiche Synthèse de Projet

Gabarit : [`animation/gabarits/projet.md`](../gabarits/projet.md) · Fiche communication : [`communication.md`](communication.md)

> Le planning des 12 séances est prévisionnel : chaque séance passée corrige la suivante.

## Titre du projet

Rover d'exploration

## Objectif général

Concevoir, fabriquer et piloter un rover télécommandé, du châssis en carton à la programmation radio, puis relever en équipe une série de missions définies par un cahier des charges.

## Livrable du parcours

Deux rovers. Celui que chaque jeune fabrique, câble et programme seul pendant les quatre premières séances. Puis celui que son équipe de deux ou trois conçoit à partir d'un cahier des charges, confronté à ce cahier des charges en revue de conception puis engagé dans les épreuves. Chaque équipe présente son rover sur une page web publiée : c'est ce que chaque jeune garde du projet.

## Objectifs pédagogiques

- Être capable de réaliser une pièce conforme à un plan coté, en carton découpé comme en impression 3D
- Être capable de câbler une carte d'extension et ses moteurs sans erreur de polarité, contrôle de traction validé
- Être capable de programmer en MakeCode un déplacement commandé par radio, sans aide
- Être capable de diagnostiquer une panne en isolant le code, le câblage et l'alimentation
- Être capable de concevoir en équipe un rover répondant à un cahier des charges, et de justifier ses choix devant le groupe

## Description du projet

Le parcours se déroule en deux temps. Pendant les quatre premières séances, chaque jeune construit seul un rover télécommandé complet : châssis en carton découpé sur plan, motorisation, électronique, programme et pilotage par radio avec un second micro:bit. Personne ne passe à la suite sans avoir fait rouler le sien. On remet ensuite aux jeunes un cahier des charges et ils se regroupent par deux ou trois pour concevoir un nouveau rover, conçu pour accomplir des missions précises, avec du carton et des pièces qu'ils modélisent et impriment en 3D. Ils apprennent la lecture de plan et les gestes de découpe, la modélisation et l'impression 3D, le câblage et la polarité, la programmation par blocs, la liaison radio, la commande d'un servomoteur, le dialogue avec la table selon un protocole imposé, une méthode de dépannage qui sépare le code du montage, le travail à plusieurs sur un objet commun, et la présentation de leur rover sur une page web. La démarche est celle de l'atelier : on fabrique dès la première séance, on teste, on corrige, on documente au carnet de bord. À partir de la séance 5, chaque notion nouvelle tient en 30 minutes au plus, et le reste de la séance appartient à l'équipe, pour appliquer la notion au rover ou poursuivre sa conception. Le travail devient collectif à partir de la séance 5, au milieu de la phase 2. Le parcours se termine par une revue de conception, où chaque équipe vérifie si son rover répond au cahier des charges, puis par les épreuves.

## Prérequis

Indispensable : aucun. Le parcours est conçu pour des débutants complets, en fabrication comme en programmation.

Utile : avoir déjà manipulé un ordinateur, ou déjà ouvert un éditeur de code par blocs (Scratch, MakeCode).

## Ressources humaines

1 animateur numérique, maîtrisant MakeCode et le micro:bit.

Un second adulte est utile à toutes les séances, vu le matériel en jeu (outils de découpe, imprimante, accus, table). Il est indispensable dès qu'on découpe : en S2, et à chaque séance de S5 à S11, puisque le carton y reste libre.

## Matériel

**Par jeune**

- 2 micro:bit v2 (un embarqué, un en télécommande)
- 1 carte d'extension DFRobot DFR0548
- 1 kit châssis : 2 moteurs TT + roues, élastiques
- Carton, papier quadrillé 5 × 5 mm réel
- 1 boîtier d'accus NiMH
- 1 bac nominatif

**Commun**

- Trois postes de découpe, chacun avec un outil de découpe (scalpel), une règle métallique à rebord et un tapis de découpe, et des crayons
- Ruban adhésif
- Imprimante 3D et filament
- Un chargeur d'accus
- Boîtes en carton de test, une par poste au minimum
- Poste de démonstration : moteur et bloc d'accus, multimètre
- Matériaux de récupération (bouchons, pots, pailles, chutes…), en bac commun
- Plan incliné à 10°, échantillons imprimés (40 × 40 × 56 mm), AprilTag 36h11 imprimés et découpés (un par équipe, numéros 1 à 20)
- Servomoteurs, deux au plus par équipe
- En phase 2, l'électronique des rovers individuels est remise en commun. Les rovers sont photographiés puis démontés à la clôture de la S5, et chaque équipe prend dans ce stock ce que le cahier des charges autorise.
- La table et son pont radio (protocoles A1 et B1), avec une Kinect ou une webcam

## Ressources numériques

- MakeCode (makecode.microbit.org), gratuit et sans inscription, avec l'extension DF-Driver à ajouter par URL
- Tinkercad en mode classe (comptes créés par l'animateur, sans adresse personnelle des jeunes)
- Slicer de l'imprimante sur le poste de l'animateur
- Kiri:Moto (grid.space/kiri), slicer dans le navigateur, sans compte : les jeunes y estiment la durée de leurs pièces
- 1 ordinateur par jeune
- Le livre en ligne, ouvert en écran partagé pendant l'atelier
- Plans de découpe imprimés (`docs/assets/plans/`)
- Carnet de bord numérique (éditeur de texte)
- Gabarit de la page web de présentation du rover (S11) : [`docs/assets/gabarit-page-rover.zip`](../../docs/assets/gabarit-page-rover.zip)
- Les tags des rovers, 1 à 20, un par page : [`docs/assets/tags/tags-rover-01-20.pdf`](../../docs/assets/tags/tags-rover-01-20.pdf) : carré noir de 90 mm, marge blanche de 11,2 mm, cadre de découpe, à imprimer à 100 %

## Budget

Pour 12 jeunes. Prix indicatifs TTC.

| Poste                                                                                                                                                                                                                                                                                                                                                                  | Qté   | Prix unitaire | Total   | Statut     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------- | ------- | ---------- |
| **Électronique**                                                                                                                                                                                                                                                                                                                                                       |       |               |         |            |
| micro:bit v2                                                                                                                                                                                                                                                                                                                                                           | 24    | 20 €          | 480 €   | Possédé    |
| Carte DFRobot DFR0548                                                                                                                                                                                                                                                                                                                                                  | 12    | 12 €          | 144 €   | Possédé    |
| Moteur TT et sa roue                                                                                                                                                                                                                                                                                                                                                   | 24    | 4 €           | 96 €    | Possédé    |
| Boîtier 4 × AA                                                                                                                                                                                                                                                                                                                                                         | 12    | 2 €           | 24 €    | Possédé    |
| Accus NiMH AA                                                                                                                                                                                                                                                                                                                                                          | 48    | 3 €           | 144 €   | Possédé    |
| Câble USB                                                                                                                                                                                                                                                                                                                                                              | 12    | 3 €           | 36 €    | Possédé    |
| Servomoteur                                                                                                                                                                                                                                                                                                                                                            | 12    | 3 €           | 36 €    | Possédé    |
| *Sous-total électronique*                                                                                                                                                                                                                                                                                                                                              |       |               | *960 €* |            |
| **Équipement commun**                                                                                                                                                                                                                                                                                                                                                  |       |               |         |            |
| Chargeur d'accus                                                                                                                                                                                                                                                                                                                                                       | 1     | 35 €          | 35 €    | Possédé    |
| Multimètre                                                                                                                                                                                                                                                                                                                                                             | 1     | 20 €          | 20 €    | Possédé    |
| Outil de découpe                                                                                                                                                                                                                                                                                                                                                       | 3     | 8 €           | 24 €    | Possédé    |
| Règle métallique à rebord                                                                                                                                                                                                                                                                                                                                              | 3     | 10 €          | 30 €    | Possédé    |
| Tapis de découpe A3                                                                                                                                                                                                                                                                                                                                                    | 3     | 12 €          | 36 €    | Possédé    |
| Imprimante 3D                                                                                                                                                                                                                                                                                                                                                          | 1     |               |         | Possédé    |
| Ordinateurs                                                                                                                                                                                                                                                                                                                                                            | 12    |               |         | Possédé    |
| La table, son pont radio et sa caméra                                                                                                                                                                                                                                                                                                                                  | 1     |               |         | Possédé    |
| **Découpe numérique (investissement proposé, une des deux)**                                                                                                                                                                                                                                                                                                           |       |               |         |            |
| Option A : Cricut Maker 5                                                                                                                                                                                                                                                                                                                                              | 1     | 500 €         | 500 €   | Proposé    |
| Option B : découpe laser xTool S1 40 W classe 1, [pack tout-en-un](https://www.a4.fr/pack-tout-en-un-decoupeuse-graveuse-laser-40-w-xtool-s1-classe-1.html) avec extracteur de fumée (2 680 €) et [kit de sécurité incendie](https://www.a4.fr/kit-de-securite-incendie-pour-machines-xtool-s1-et-m1-ultra.html) avec détection de flamme et extinction au CO₂ (163 €) | 1     | 2 843 €       | 2 843 € | Proposé    |
| **Par parcours**                                                                                                                                                                                                                                                                                                                                                       |       |               |         |            |
| Consommables, forfait : élastiques, carton, papier quadrillé, ruban adhésif, colle, impression des tags et des plans, une bobine de filament                                                                                                                                                                                                                           | 1     | 100 €         | 100 €   | À racheter |
| Casse : 15 % de l'électronique                                                                                                                                                                                                                                                                                                                                         | 1     | 144 €         | 144 €   | À racheter |
| Option A : tapis de coupe adhésifs, lame pour matériaux épais, carton gris en feuilles                                                                                                                                                                                                                                                                                 | 1     | 120 €         | 120 €   | À racheter |
| Option B : filtres de l'extracteur de fumée                                                                                                                                                                                                                                                                                                                            | 1 jeu | 120 €         | 120 €   | À racheter |

Un parcours coûte environ 364 €, soit 30 € par jeune : 100 € de consommables, 144 € de casse et 120 € de consommables propres à la machine de découpe. Le reste du matériel se réutilise d'un parcours à l'autre.

Le matériel déjà possédé vaut 1 105 €, sans compter l'imprimante 3D, les ordinateurs et la table. L'atelier a trois postes de découpe manuelle, pour limiter le nombre de lames utilisées en même temps.

**Investissement proposé : une découpe laser, pour 2 843 € avec le kit incendie.** Une Cricut, à 500 €, serait une solution plus limitée.

L'atelier dispose déjà d'une imprimante 3D, qui fabrique des pièces en volume. La découpe laser fabrique des pièces à plat (châssis, plaques, supports, gabarits) et elle grave. Avec l'électronique et la programmation déjà enseignées, l'atelier couvrirait toute la chaîne d'un fablab : concevoir à l'ordinateur, fabriquer, assembler, programmer.

Dans le parcours Rover, le châssis serait dessiné puis découpé par la machine, comme les pièces imprimées en S6. Le temps passé au cutter irait à la conception, et les jeunes manipuleraient moins de lames. La machine proposée est de classe 1 : elle est fermée, elle filtre les fumées, et le kit incendie détecte les flammes et les éteint automatiquement.

Elle servirait aussi aux autres ateliers créatifs de La Plateforme, pour des maquettes, de la signalétique ou des objets en bois gravés que les jeunes emportent.

À l'usage, les deux machines coûtent la même chose, 120 € de consommables par parcours. La découpe laser utilise en plus le carton de récupération, et elle est la seule des deux à travailler le bois et à graver.

|                   | Option A : Cricut                                  | Option B : découpe laser                                                                         |
| ----------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Carton            | Carton gris en feuilles, acheté au format du tapis | Tout carton plat, récupération comprise                                                          |
| Bois              | Non                                                | Découpe et gravure                                                                               |
| Sécurité          | Lame dans la machine, pas de fumée                 | Fumées et risque d'inflammation du carton : filtration et kit incendie, surveillance d'un adulte |
| Coût par parcours | Tapis, lame et carton gris à racheter              | Filtres à remplacer                                                                              |

## Séance 1 — Phase 1 — Découverte & prise en main

**Titre :** Fais tourner tes moteurs

**Notions :** câblage et polarité · chaîne de programmation · notion d'extension et de bibliothèque · commande de moteur · séparer une panne de code d'une panne de montage

**Livrable intermédiaire :** électronique câblée et validée, programme faisant tourner les deux moteurs, moteur `M1` marqué, carnet de bord renseigné

## Séance 2 — Phase 1 — Découverte & prise en main

**Titre :** Fabrique ton rover et fais-le rouler droit

**Notions :** lecture de plan coté et traçage · rainage, pliage et découpe du carton · réglage du sens de rotation · fonction et réutilisation du code · diagnostic mécanique avant correction logicielle · vitesse minimale de démarrage · dérive et compensation · reproductibilité d'une mesure

**Livrable intermédiaire :** rover monté qui roule droit sur 1,50 m, fonction `avancer`, réglages notés au carnet

## Séance 3 — Phase 1 — Découverte & prise en main

**Titre :** Ta plaque, et les mouvements de ton rover

**Notions :** modélisation 3D et contrainte de conception · impression additive, couches, slicer · direction différentielle · programme de vérification : tout appeler, dans un ordre connu

**Livrable intermédiaire :** plaque personnelle exportée en `.STL`, cinq fonctions de mouvement appelées par un programme de vérification. Le défi du retour au garage est en « va plus loin ».

## Séance 4 — Phase 2 — Exploration & création

**Titre :** Pilote ton rover à distance

**Notions :** capteur embarqué et mesure brute · seuil de décision · variable · `si` / `sinon si` / `sinon` · protocole : canal partagé et vocabulaire partagé · bande de fréquence, et ce qui la distingue du groupe · protocole imposé et standardisation · message clé-valeur · troncature silencieuse au-delà de 8 caractères · comparaison de chaînes · gestionnaire d'événement `quand une donnée est reçue` · débit d'émission et saturation du récepteur · témoin visuel comme instrument de débogage · réemploi des cinq fonctions de la S3

**Livrable intermédiaire :** rover individuel terminé et piloté par radio, seuils et protocole consignés au carnet, plaque montée. Fin du temps individuel.

## Séance 5 — Phase 2 — Exploration & création

**Titre :** Formez votre équipe et concevez le rover de mission

**Notions :** lecture d'un cahier des charges · répartition des rôles dans une équipe · prototypage carton · relevé et tracé d'un plan à partir d'une idée

**Livrable intermédiaire :** équipes de 2 ou 3 constituées, plan tracé et premier prototype carton du rover de mission, support de tag en carton compris

## Séance 6 — Phase 2 — Exploration & création

**Titre :** Dessinez les pièces de votre rover

**Notions :** CAO par esquisse : révolution, extrusion, esquisse libre · pièces partagées : trouver, réemployer, modifier, citer l'auteur · durée d'impression estimée dans Kiri:Moto · choix du procédé : impression, carton, récupération

**Livrable intermédiaire :** pièces de l'équipe dessinées et parties à l'impression, ou fabriquées en carton ou en récupération

## Séance 7 — Phase 2 — Exploration & création

**Titre :** Faites bouger une pièce avec un servomoteur

**Notions :** servomoteur : un angle, pas une vitesse · branchement sur les broches `S7` et `S8` de la DFR0548 · commande d'un actionneur par bouton, puis depuis la télécommande

**Livrable intermédiaire :** deux servomoteurs commandés par le programme, montés sur le rover si l'équipe en a l'usage

## Séance 8 — Phase 2 — Exploration & création

**Titre :** Faites piloter votre rover par la table

**Notions :** protocole imposé A1 · bande et groupe · la valeur reçue devient une vitesse · variable lue par tout le programme · gestionnaire radio qui ne bloque pas · arrêt sur silence · changement de mode et son témoin à l'écran

**Livrable intermédiaire :** rover conforme à A1, piloté par la table comme par sa télécommande

## Séance 9 — Phase 2 — Exploration & création

**Titre :** Guidez votre rover vers une cible

**Notions :** recevoir une mesure et non un ordre · décision à bord · condition sur un signe et un seuil · mode manuel et mode autonome

**Livrable intermédiaire :** rover qui réagit à `cap` et `dist`, testé avec un micro:bit émetteur

## Séance 10 — Phase 3 — Finalisation & valorisation

**Titre :** Votre rover face au cahier des charges

**Notions :** revue de conception · écart entre l'attendu et l'obtenu · vérification par un tiers · priorisation des corrections

**Livrable intermédiaire :** cahier des charges coché, écarts relevés et corrections engagées

## Séance 11 — Phase 3 — Finalisation & valorisation

**Titre :** Présentez votre rover sur une page web

**Notions :** page web à partir d'un gabarit HTML · balise, titre, paragraphe, image · variable CSS · justifier un choix de conception

**Livrable intermédiaire :** page de présentation du rover remplie, avec trois choix de conception justifiés

## Séance 12 — Phase 3 — Finalisation & valorisation

**Titre :** Vos rovers en épreuve

**Notions :** démonstration · bilan de projet

**Livrable intermédiaire :** épreuves courues, bilan collectif


