# Rover — Fiche Synthèse de Projet

Gabarit : [`animation/gabarits/projet.md`](../gabarits/projet.md) · Fiche communication : [`communication.md`](communication.md)

> **Le planning des 12 séances est prévisionnel.** Le parcours se déroule pour la première fois ; chaque séance écrite corrige la suivante. Les séances marquées *à définir* attendent d'être arbitrées.

## Titre du projet

Rover d'exploration

## Objectif général

Concevoir, fabriquer et piloter un rover télécommandé, du châssis en carton à la programmation radio, puis relever en équipe une série de missions définies par un cahier des charges.

## Livrable du parcours

Deux rovers. Celui que chaque jeune fabrique, câble et programme seul pendant les quatre premières séances. Puis celui que son équipe de deux ou trois conçoit à partir d'un cahier des charges, homologué et capable d'accomplir les missions.

## Objectifs pédagogiques

- Être capable de réaliser une pièce conforme à un plan coté, en carton découpé comme en impression 3D
- Être capable de câbler une carte d'extension et ses moteurs sans erreur de polarité, contrôle de traction validé
- Être capable de programmer en MakeCode un déplacement commandé par radio, sans aide
- Être capable de diagnostiquer une panne en isolant le code, le câblage et l'alimentation
- Être capable de concevoir en équipe un rover répondant à un cahier des charges, et de justifier ses choix devant le groupe

## Description du projet

Le parcours se déroule en deux temps. Pendant les quatre premières séances, chaque jeune construit seul un rover télécommandé complet : châssis en carton découpé sur plan, motorisation, électronique, programme et pilotage par radio avec un second micro:bit. Personne ne passe à la suite sans avoir fait rouler le sien. On remet ensuite aux jeunes un cahier des charges et ils se regroupent par deux ou trois pour concevoir un nouveau rover, taillé pour accomplir des missions précises — avec le carton, et avec des pièces qu'ils modélisent et impriment en 3D. Ils apprennent la lecture de plan et les gestes de découpe, la modélisation et l'impression 3D, le câblage et la polarité, la programmation par blocs, la liaison radio, une méthode de dépannage qui sépare le code du montage, et le travail à plusieurs sur un objet commun. La démarche est celle de l'atelier : on fabrique dès la première séance, on teste, on corrige, on documente au carnet de bord. Le parcours se termine par l'homologation des rovers et l'épreuve des missions.

## Prérequis

**Indispensable** : aucun. Le parcours est conçu pour des débutants complets, en fabrication comme en programmation.

**Utile** : avoir déjà manipulé un ordinateur, ou déjà ouvert un éditeur de code par blocs (Scratch, MakeCode).

## Ressources humaines

1 animateur numérique, maîtrisant MakeCode et le micro:bit.

**+ 1 second adulte sur les séances comportant de la découpe au cutter** (S1, S5, et toute séance de prototypage). Douze cutters en service simultané avec un seul adulte est le point de tension du parcours. Sur la S1, le renfort est nécessaire à partir de la 55ᵉ minute, pas dès l'ouverture.

## Matériel

**Par jeune**

- 2 micro:bit v2 (un embarqué, un en télécommande)
- 1 carte d'extension DFRobot DFR0548
- 1 kit châssis : 2 moteurs TT + roues, élastiques
- Carton, papier quadrillé 5 × 5 mm réel
- 1 boîtier d'accus NiMH
- 1 bac nominatif

**Commun**

- Cutters, règles métalliques à rebord, tapis de découpe, crayons
- Ruban adhésif
- Imprimante 3D et filament
- Station de charge
- Boîtes en carton de test — une par poste au minimum
- Cales pour faire tourner les roues à vide
- Poste de démonstration : moteur + pinces croco + bloc d'accus, LED + résistance, multimètre

## Ressources numériques

- MakeCode (makecode.microbit.org), gratuit, sans inscription — extension DF-Driver à ajouter par URL
- Tinkercad en mode classe (comptes créés par l'animateur, sans adresse personnelle des jeunes)
- Bambu Studio, le trancheur de l'imprimante
- 1 ordinateur par jeune
- Le livre en ligne, ouvert en écran partagé pendant l'atelier
- Plans de découpe imprimés (`docs/assets/plans/`)
- Carnet de bord numérique

## Budget

À affiner une fois les 12 séances écrites. Les postes sont connus — micro:bit et cartes DFR0548 (réutilisables d'un parcours à l'autre), moteurs et roues (réutilisables), accus et station de charge (réutilisables), carton, papier quadrillé et filament 3D (consommables) — mais le volume de consommables dépend du nombre de prototypes par équipe en phase 2, qui n'est pas encore arbitré.

## Séance 1 — Phase 1 — Découverte & prise en main

**Titre :** Fabrique et monte la base motrice
**Notions :** lecture de plan coté et traçage · rainage, pliage et découpe du carton · chaîne de programmation · notion d'extension et de bibliothèque · commande de moteur
**Livrable intermédiaire :** base du rover assemblée, programme faisant tourner les deux moteurs, carnet de bord renseigné

→ [Fiche d'animation](s01.md) · [Page élève](../../docs/projets/rover/seances/s01-base-motrice.md)

## Séance 2 — Phase 1 — Découverte & prise en main

**Titre :** Ton rover obéit
**Notions :** direction différentielle · fonction et réutilisation du code · diagnostic mécanique avant correction logicielle · vitesse minimale de démarrage · dérive et compensation · événement bouton et boucle `répéter` · boucle ouverte · reproductibilité d'une mesure
**Livrable intermédiaire :** rover terminé qui roule droit sur 1,50 m, cinq fonctions de mouvement, défi du retour au garage tenté et mesuré

*La séance s'ouvre sur la fin de la S1 : 7 jeunes sur 9 n'avaient pas terminé.*

→ [Fiche d'animation](s02.md) · [Page élève](../../docs/projets/rover/seances/s02-ton-rover-obeit.md)

## Séance 3 — Phase 1 — Découverte & prise en main

**Titre :** Ton identité, et le problème de la télécommande
**Notions :** modélisation 3D et contrainte de conception · impression additive, couches, slicer · capteur embarqué et mesure brute · seuil de décision · variable · `si` / `sinon si` / `sinon`
**Livrable intermédiaire :** plaque personnelle exportée en `.STL`, programme d'affichage directionnel sur la seconde carte, seuils notés

→ [Fiche d'animation](s03.md) · [Page élève](../../docs/projets/rover/seances/s03-identite-et-telecommande.md)

## Séance 4 — Phase 2 — Exploration & création

**Titre :** Pilote ton rover à distance
**Notions :** protocole — canal partagé et vocabulaire partagé · bande de fréquence, et ce qui la distingue du groupe · protocole imposé et standardisation · message clé-valeur · troncature silencieuse au-delà de 8 caractères · comparaison de chaînes · gestionnaire d'événement `quand une donnée est reçue` · débit d'émission et saturation du récepteur · témoin visuel comme instrument de débogage · réemploi des cinq fonctions de la S2 et des seuils de la S3
**Livrable intermédiaire :** rover individuel terminé et piloté par radio, protocole consigné au carnet, plaque montée — **fin du temps individuel**

*La séance s'ouvre sur la remise des plaques imprimées et leur pose sur les rovers, en cinq minutes de lancement — pas en activité. La clôture est le pivot du parcours : annonce du travail en équipe et des missions, sans les chiffres.*

→ [Fiche d'animation](s04.md) · [Page élève](../../docs/projets/rover/seances/s04-pilote-a-distance.md)

## Séance 5 — Phase 2 — Exploration & création

**Titre :** Formez votre équipe et concevez le rover de mission
**Notions :** lecture d'un cahier des charges · répartition des rôles dans une équipe · prototypage carton · relevé et tracé d'un plan à partir d'une idée
**Livrable intermédiaire :** équipes de 2–3 constituées, plan tracé et premier prototype carton du rover de mission

*C'est le pivot du parcours : le cahier des charges est remis ici, et le travail devient collectif. C'est aussi ici que le relevé de plan au quadrillage trouve sa place — le traçage n'est plus un détour, c'est le sujet.*

**Le cahier des charges, remis en séance 5.** Les obstacles et les échantillons sont **présentés physiquement** ce jour-là : un cahier des charges qu'on peut prendre en main se conçoit mieux qu'un cahier des charges lu.

Il tient en deux listes, et les deux sont indépendantes. La première dit **ce que le rover doit savoir faire** — c'est ce qui sera vérifié à l'homologation, rover par rover, sans chronomètre ni adversaire. La seconde dit **ce qu'on leur fera courir** en S12 — c'est la compétition, et elle suppose l'homologation acquise.

**Liste 1 — Caractéristiques techniques (vérifiées à l'homologation, S11)**

1. **Pilotage à distance** par un ou plusieurs opérateurs
2. **Pente** : monter un plan incliné de 5 cm de haut sur 30 cm de long, soit environ **9,5°**
3. **Obstacle ponctuel** : franchir une barre de 1 × 1 cm de section, plus large que le rover
4. **Échantillon métallique** : saisir et transporter une pièce fine, quelques millimètres de haut
5. **Échantillon non métallique** : saisir et transporter un objet de 4 × 4 × 10 cm
6. **Slalom** : évoluer entre des obstacles sans les toucher

**Liste 2 — Épreuves (courues en S12)**

1. **Le parcours**, chronométré — un rover à la fois, le meilleur temps gagne
2. **Le capture the flag**, avec l'échantillon non métallique — les équipes ensemble sur le terrain, la première à ramener l'objet à sa base gagne
3. **L'échantillon métallique**, épreuve individuelle — ramener la pièce à la base
4. **La pente maximale** — plan à angle réglable, on monte par paliers jusqu'au décrochage, le rover qui tient l'angle le plus raide gagne
5. **Le transport fragile** — ramener un échantillon posé sur un plateau non fixé au rover, sans le faire tomber

La pente apparaît dans les deux listes, et c'est volontaire : **9,5° est le plancher** que tout rover doit franchir pour être homologué, la pente maximale est **le défi au-dessus du plancher**. Un rover homologué de justesse court quand même l'épreuve, il la perd. Prévoir un plan incliné à angle réglable et un rapporteur — un plan fixe ne permet que le plancher.

Chaque point de la liste 1 est une contrainte de conception. Chaque ligne de la liste 2 est un jeu. Un rover peut être homologué et perdre toutes les épreuves : c'est voulu, et ça se dit aux équipes dès la S5.

**Le transport fragile est là pour équilibrer les autres.** Le parcours, le capture the flag et la pente récompensent tous la vitesse ou la force ; celui-ci récompense la maîtrise. Sans lui, toutes les équipes optimisent la même chose et les rovers se ressemblent. Reste à fixer quel échantillon il emploie — le 4 × 4 × 10 ou une pièce dédiée — et la hauteur du plateau.

**Cinq épreuves en 1 h 45, c'est serré.** Soit on en court une ou deux en fin de S11, soit on les taille courtes : un passage par équipe, pas de repêchage.

## Séance 6 — Phase 2 — Exploration & création

**Titre :** *à définir*
**Notions :** *à définir*
**Livrable intermédiaire :** *à définir*

## Séance 7 — Phase 2 — Exploration & création

**Titre :** *à définir*
**Notions :** *à définir*
**Livrable intermédiaire :** *à définir*

## Séance 8 — Phase 2 — Exploration & création

**Titre :** *à définir*
**Notions :** *à définir*
**Livrable intermédiaire :** *à définir*

## Séance 9 — Phase 2 — Exploration & création

**Titre :** *à définir*
**Notions :** *à définir*
**Livrable intermédiaire :** *à définir*

## Séance 10 — Phase 3 — Finalisation & valorisation

**Titre :** *à définir*
**Notions :** *à définir*
**Livrable intermédiaire :** *à définir*

## Séance 11 — Phase 3 — Finalisation & valorisation

**Titre :** Faites homologuer le rover de votre équipe
**Notions :** conformité au cahier des charges · essais et réglages · répétition des missions
**Livrable intermédiaire :** rover d'équipe homologué, missions répétées au moins une fois en conditions

## Séance 12 — Phase 3 — Finalisation & valorisation

**Titre :** Vos rovers en mission
**Notions :** démonstration · bilan de projet
**Livrable intermédiaire :** missions accomplies, bilan collectif

*La forme de la valorisation finale — les Jeux, un public, un jury — n'est pas confirmée. Voir les notes.*

---

## Notes de préparation

**Ce qui reste à arbitrer.**

- **Cinq séances sur douze** (S6, S7, S8, S9, S10) n'ont pas encore de contenu. Les ancrages connus sont la radio en S4, la bascule en équipe et le prototypage en S5, l'homologation puis les missions en fin de parcours.
- **L'impression 3D est introduite en S3** (plaque d'identité), avec Tinkercad et Bambu Studio. Reste à décider où elle **revient** en phase 2, quand les équipes dessineront les pièces de leur mécanisme : c'est là qu'elle portera vraiment le projet.
- **La valorisation finale n'est pas confirmée.** Les Jeux, un public, un jury : rien n'est acté. La fiche communication ne promet donc pas d'événement public. À reprendre ici et dans la com dès que c'est tranché.
- **Ce que chaque jeune emporte** n'est pas décidé : le rover final appartient à une équipe de deux ou trois. Voir la note de [`communication.md`](communication.md).

**Pistes à arbitrer.** Rien ci-dessous n'est décidé, à prendre ou à laisser ligne par ligne. Les deux propositions qui étaient de vraies épreuves ont été tranchées : la pente maximale et le transport fragile sont en liste 2, l'échange d'échantillon entre équipes est écarté.

*Ce ne sont pas des épreuves : trois façons de rendre plus exigeant ce qui est déjà prévu.*

1. **La garde au sol est annoncée comme une cote, dès la S5** : « il faut 10 mm libres sous le châssis ». Sinon le pack d'accus finit sous le rover sans que personne y pense, et le défaut se découvre à l'homologation, trop tard pour reconcevoir. Le rover des photos a déjà ce défaut.
2. **L'échantillon de 4 × 4 × 10 est posé debout.** Couché, il se pousse jusqu'à la base sans rien saisir. Debout, il faut le prendre ou le faire basculer : deux familles de solutions, aucune évidente.
3. **Le slalom se court en marche arrière**, ou avec l'opérateur dos au parcours et un coéquipier qui le guide à la voix. C'est ce qui donne du poids à « pilotable par un ou plusieurs opérateurs » : sans ça, la ligne se coche sans avoir rien coûté.

*Une remarque, qui n'est pas une épreuve.* « Métallique » appelle l'aimant, et l'aimant pose tout de suite la bonne question : un aimant fixe oblige à repousser l'objet jusqu'à la base en marche arrière, un aimant sur bras mobile permet de le lâcher. Le second demande une pièce imprimée — c'est le premier endroit du parcours où l'impression 3D sert un mécanisme et plus la décoration. Ne rien trancher à leur place : la contrainte suffit à faire naître les deux solutions.

**Le découpage LP et le rythme réel ne coïncident pas.** Les phases LP sont 1–3 / 4–9 / 10–12 ; le parcours bascule de l'individuel au collectif entre la S4 et la S5. Ce n'est pas un problème — la S4 clôt le rover individuel à l'intérieur de la phase 2 — mais il faut le savoir en lisant le planning.

**Bloom.** Les cinq objectifs couvrent quatre niveaux : *Appliquer* (réaliser, câbler, programmer) sur la phase 1, *Analyser* (diagnostiquer) sur la phase 2, *Créer* et *Évaluer* (concevoir en équipe et justifier) sur les phases 2 et 3. La progression attendue par le guide LP est respectée.

**Sur la durée.** 12 × 1 h 45 dont plusieurs séances chargées (S1 déjà mesurée : 2 jeunes sur 9 ont terminé). Prévoir que la phase 2 absorbe du retard, et garder les variantes − comme soupape plutôt que de rogner sur la rétrospective.
