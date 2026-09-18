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

- Cutters, règles métalliques, tapis de découpe, crayons
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
**Livrable intermédiaire :** rover terminé qui roule droit sur 2 mètres, cinq fonctions de mouvement, défi du retour au garage tenté et mesuré

*La séance s'ouvre sur la fin de la S1 : 7 jeunes sur 9 n'avaient pas terminé.*

→ [Fiche d'animation](s02.md) · [Page élève](../../docs/projets/rover/seances/s02-ton-rover-obeit.md)

## Séance 3 — Phase 1 — Découverte & prise en main

**Titre :** Ton identité, et le problème de la télécommande
**Notions :** modélisation 3D et contrainte de conception · impression additive, couches, slicer · capteur embarqué et mesure brute · seuil de décision · variable · `si` / `sinon si` / `sinon`
**Livrable intermédiaire :** plaque personnelle exportée en `.STL`, programme d'affichage directionnel sur la seconde carte, seuils notés

→ [Fiche d'animation](s03.md) · [Page élève](../../docs/projets/rover/seances/s03-identite-et-telecommande.md)

## Séance 4 — Phase 2 — Exploration & création

**Titre :** Pilote ton rover à distance
**Notions :** liaison radio entre deux micro:bit · groupe radio et canal · émetteur et récepteur · réemploi des seuils d'inclinaison de la S3 et des cinq fonctions de la S2

*La séance s'ouvre sur la distribution des plaques imprimées, et leur pose sur les rovers. Les photos d'impression sont déjà dans `docs/assets/rover-s04/`.*
**Livrable intermédiaire :** rover individuel terminé et piloté par radio — **fin du temps individuel**

## Séance 5 — Phase 2 — Exploration & création

**Titre :** Formez votre équipe et concevez le rover de mission
**Notions :** lecture d'un cahier des charges · répartition des rôles dans une équipe · prototypage carton · relevé et tracé d'un plan à partir d'une idée
**Livrable intermédiaire :** équipes de 2–3 constituées, plan tracé et premier prototype carton du rover de mission

*C'est le pivot du parcours : le cahier des charges est remis ici, et le travail devient collectif. C'est aussi ici que le relevé de plan au quadrillage trouve sa place — le traçage n'est plus un détour, c'est le sujet.*

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

**Le découpage LP et le rythme réel ne coïncident pas.** Les phases LP sont 1–3 / 4–9 / 10–12 ; le parcours bascule de l'individuel au collectif entre la S4 et la S5. Ce n'est pas un problème — la S4 clôt le rover individuel à l'intérieur de la phase 2 — mais il faut le savoir en lisant le planning.

**Bloom.** Les cinq objectifs couvrent quatre niveaux : *Appliquer* (réaliser, câbler, programmer) sur la phase 1, *Analyser* (diagnostiquer) sur la phase 2, *Créer* et *Évaluer* (concevoir en équipe et justifier) sur les phases 2 et 3. La progression attendue par le guide LP est respectée.

**Sur la durée.** 12 × 1 h 45 dont plusieurs séances chargées (S1 déjà mesurée : 2 jeunes sur 9 ont terminé). Prévoir que la phase 2 absorbe du retard, et garder les variantes − comme soupape plutôt que de rogner sur la rétrospective.
