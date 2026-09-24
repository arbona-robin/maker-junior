# Rover — Fiche Synthèse de Projet

Gabarit : [`animation/gabarits/projet.md`](../gabarits/projet.md) · Fiche communication : [`communication.md`](communication.md)

> **Le planning des 12 séances est prévisionnel** : chaque séance passée corrige la suivante.

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

Le parcours se déroule en deux temps. Pendant les quatre premières séances, chaque jeune construit seul un rover télécommandé complet : châssis en carton découpé sur plan, motorisation, électronique, programme et pilotage par radio avec un second micro:bit. Personne ne passe à la suite sans avoir fait rouler le sien. On remet ensuite aux jeunes un cahier des charges et ils se regroupent par deux ou trois pour concevoir un nouveau rover, taillé pour accomplir des missions précises — avec le carton, et avec des pièces qu'ils modélisent et impriment en 3D. Ils apprennent la lecture de plan et les gestes de découpe, la modélisation et l'impression 3D, le câblage et la polarité, la programmation par blocs, la liaison radio, la commande d'un servomoteur, le dialogue avec la table selon un protocole imposé, une méthode de dépannage qui sépare le code du montage, le travail à plusieurs sur un objet commun, et la présentation de leur rover sur une page web. La démarche est celle de l'atelier : on fabrique dès la première séance, on teste, on corrige, on documente au carnet de bord. Le parcours se termine par une revue de conception, où chaque équipe vérifie si son rover répond au cahier des charges, puis par les épreuves.

## Prérequis

**Indispensable** : aucun. Le parcours est conçu pour des débutants complets, en fabrication comme en programmation.

**Utile** : avoir déjà manipulé un ordinateur, ou déjà ouvert un éditeur de code par blocs (Scratch, MakeCode).

## Ressources humaines

1 animateur numérique, maîtrisant MakeCode et le micro:bit.

**+ 1 second adulte, utile à toutes les séances** vu le matériel en jeu (outils de découpe, imprimante, accus, table), **et indispensable dès qu'on découpe** : S2, et chaque séance de S5 à S11, puisque le carton y reste libre. Douze outils de découpe en service simultané avec un seul adulte est le point de tension du parcours. Sur la S2, le renfort est nécessaire de la 10ᵉ à la 55ᵉ minute.

## Matériel

**Par jeune**

- 2 micro:bit v2 (un embarqué, un en télécommande)
- 1 carte d'extension DFRobot DFR0548
- 1 kit châssis : 2 moteurs TT + roues, élastiques
- Carton, papier quadrillé 5 × 5 mm réel
- 1 boîtier d'accus NiMH
- 1 bac nominatif

**Commun**

- Outils de découpe (scalpels), règles métalliques à rebord, tapis de découpe, crayons
- Ruban adhésif
- Imprimante 3D et filament
- Station de charge
- Boîtes en carton de test — une par poste au minimum
- Cales pour faire tourner les roues à vide
- Poste de démonstration : moteur + pinces croco + bloc d'accus, LED + résistance, multimètre
- Matériaux de récupération (bouchons, pots, pailles, chutes…), en bac commun
- Plan incliné à 10°, échantillons imprimés (40 × 40 × 56 mm), AprilTag 36h11 imprimés et découpés (un par équipe, numéros 1 à 20)
- Servomoteurs — deux au plus par équipe
- **En phase 2, l'électronique des rovers individuels est remise en commun** — photo puis démontage à la clôture de la S5 — et chaque équipe y prend ce que le cahier des charges autorise
- La table et son pont radio (protocoles A1 et B1)

## Ressources numériques

- MakeCode (makecode.microbit.org), gratuit, sans inscription — extension DF-Driver à ajouter par URL
- Tinkercad en mode classe (comptes créés par l'animateur, sans adresse personnelle des jeunes)
- Bambu Studio, le trancheur de l'imprimante, sur le poste de l'animateur
- Kiri:Moto (grid.space/kiri), slicer dans le navigateur, sans compte : les jeunes y estiment la durée de leurs pièces
- 1 ordinateur par jeune
- Le livre en ligne, ouvert en écran partagé pendant l'atelier
- Plans de découpe imprimés (`docs/assets/plans/`)
- Carnet de bord numérique
- Gabarit de la page de présentation du rover (S11) : [`docs/assets/gabarit-page-rover.zip`](../../docs/assets/gabarit-page-rover.zip)
- Les tags des rovers, 1 à 20, un par page : [`docs/assets/tags/tags-rover-01-20.pdf`](../../docs/assets/tags/tags-rover-01-20.pdf) — carré noir de 90 mm, marge blanche de 11,2 mm, cadre de découpe ; imprimer à 100 %

## Budget

À affiner. Les postes sont connus — micro:bit et cartes DFR0548 (réutilisables d'un parcours à l'autre), moteurs et roues (réutilisables), accus et station de charge (réutilisables), carton, papier quadrillé et filament 3D (consommables) — mais le volume de consommables dépend du nombre de prototypes par équipe en phase 2, qui n'est pas encore arbitré.

## Séance 1 — Phase 1 — Découverte & prise en main

**Titre :** Fais tourner tes moteurs
**Notions :** câblage et polarité · chaîne de programmation · notion d'extension et de bibliothèque · commande de moteur · séparer une panne de code d'une panne de montage
**Livrable intermédiaire :** électronique câblée et validée, programme faisant tourner les deux moteurs, moteur `M1` marqué, carnet de bord renseigné

→ [Fiche d'animation](s01.md) · [Page élève](../../docs/projets/rover/seances/s01-fais-tourner-tes-moteurs.md)

## Séance 2 — Phase 1 — Découverte & prise en main

**Titre :** Fabrique ton rover et fais-le rouler droit
**Notions :** lecture de plan coté et traçage · rainage, pliage et découpe du carton · réglage du sens de rotation · fonction et réutilisation du code · diagnostic mécanique avant correction logicielle · vitesse minimale de démarrage · dérive et compensation · reproductibilité d'une mesure
**Livrable intermédiaire :** rover monté qui roule droit sur 1,50 m, fonction `avancer`, réglages notés au carnet

→ [Fiche d'animation](s02.md) · [Page élève](../../docs/projets/rover/seances/s02-fabrique-ton-rover.md)

## Séance 3 — Phase 1 — Découverte & prise en main

**Titre :** Ta plaque, et les mouvements de ton rover
**Notions :** modélisation 3D et contrainte de conception · impression additive, couches, slicer · direction différentielle · programme de vérification : tout appeler, dans un ordre connu
**Livrable intermédiaire :** plaque personnelle exportée en `.STL`, cinq fonctions de mouvement appelées par un programme de vérification — le défi du retour au garage est en « va plus loin »

*La CAO ouvre la séance, pour être sûr qu'elle soit finie et que les plaques partent à l'impression avant la S4.*

→ [Fiche d'animation](s03.md) · [Page élève](../../docs/projets/rover/seances/s03-ta-plaque-et-tes-mouvements.md)

## Séance 4 — Phase 2 — Exploration & création

**Titre :** Pilote ton rover à distance
**Notions :** capteur embarqué et mesure brute · seuil de décision · variable · `si` / `sinon si` / `sinon` · protocole — canal partagé et vocabulaire partagé · bande de fréquence, et ce qui la distingue du groupe · protocole imposé et standardisation · message clé-valeur · troncature silencieuse au-delà de 8 caractères · comparaison de chaînes · gestionnaire d'événement `quand une donnée est reçue` · débit d'émission et saturation du récepteur · témoin visuel comme instrument de débogage · réemploi des cinq fonctions de la S3
**Livrable intermédiaire :** rover individuel terminé et piloté par radio, seuils et protocole consignés au carnet, plaque montée — **fin du temps individuel**

*La séance s'ouvre sur la remise des plaques imprimées et leur pose sur les rovers, en cinq minutes de lancement — pas en activité. C'est la séance la plus chargée du parcours : télécommande, protocole et récepteur.*

→ [Fiche d'animation](s04.md) · [Page élève](../../docs/projets/rover/seances/s04-pilote-a-distance.md)

## Séance 5 — Phase 2 — Exploration & création

**Titre :** Formez votre équipe et concevez le rover de mission
**Notions :** lecture d'un cahier des charges · répartition des rôles dans une équipe · prototypage carton · relevé et tracé d'un plan à partir d'une idée
**Livrable intermédiaire :** équipes de 2–3 constituées, plan tracé et premier prototype carton du rover de mission, support de tag en carton compris

*C'est le pivot du parcours : le cahier des charges est remis ici, et le travail devient collectif. C'est aussi ici que le relevé de plan au quadrillage trouve sa place — le traçage n'est plus un détour, c'est le sujet.*

**Le cahier des charges, remis en séance 5.** Le plan incliné, l'échantillon et un tag sont **présentés physiquement** ce jour-là : un cahier des charges qu'on peut prendre en main se conçoit mieux qu'un cahier des charges lu.

Il tient en deux listes indépendantes. La première dit **ce que le rover doit être** : des caractéristiques que l'équipe confronte à son rover en revue de conception, sans chronomètre ni adversaire. La revue guide, elle ne disqualifie pas : elle dit à l'équipe ce qui manque et ce qu'il reste à reprendre. La seconde dit **ce qu'on lui fera courir** en S12 ; tous les rovers y participent.

**Liste 1 — Caractéristiques, passées en revue de conception (S10)**

1. **Pente** : monter un plan incliné à **10°**, soit environ 5,2 cm de haut sur 30 cm de long
2. **Échantillon** : déplacer sur **50 cm** l'échantillon — une pièce imprimée de 40 × 40 × 56 mm, deux disques reliés par un cône — **posé debout, sans le renverser**. Le pousser, le saisir, le soulever : au choix de l'équipe
3. **Support de tag** : porter à plat, visible du dessus, un AprilTag 36h11 : 90 mm de noir, marge blanche de 11,2 mm comprise dans ce qui doit rester visible
4. **Encombrement** : tenir dans **25 × 25 × 20 cm** (longueur, largeur, hauteur) — de quoi loger quatre roues, ou deux roues et une pince
5. **Électronique**, prise dans le stock commun : au plus 1 carte DFR0548, 2 micro:bit (le rover et sa télécommande), 4 moteurs et 2 servomoteurs
6. **Impression 3D** : au plus **3 h d'impression par équipe** sur l'ensemble du parcours, durée lue par les jeunes dans Kiri:Moto et tenue dans leur suivi d'impression
7. **Modes de pilotage** : le rover fonctionne selon les modes ci-dessous ; comment on passe de l'un à l'autre, c'est à l'équipe de le décider
   - **Télécommande** — les cinq clés d'A1, sur la bande de l'équipe, égale au numéro de son tag
   - **Table, A1 : la table donne des ordres** — bande 83, groupe égal au numéro de son tag (1 à 20) ; cinq clés `avancer`, `reculer`, `gauche`, `droite`, `arreter`, valeur 0 à 1023 prise comme vitesse ; `avancer` le déplace d'au moins 5 cm en 1,5 s, `gauche` et `droite` tournent en sens opposés ; sans message depuis 1 s, il coupe ses moteurs. Vérifié par `arlab demo` : la table mesure le rover, puis le pilote le long d'une figure
   - **Table, B1 : la table donne des mesures** — *va plus loin, non exigé.* La table envoie `cap` (−180 à 180, degrés à tourner pour viser la cible, négatif à gauche, 10 Hz) et `dist` (0 à 999 cm, 2 Hz). Le cahier des charges dit **ce que la table envoie, pas ce qu'il faut en faire** : « voici ce que vous recevez — que pouvez-vous en faire ? » Les conditions (quand tourner, de quel côté, quand s'arrêter) sont à trouver par l'équipe. Testable sans la table : la télécommande, reprogrammée le temps des essais, envoie `cap` et `dist` à la main

La télécommande et la table en A1 envoient les mêmes messages : seule la bande change. Le contrôle par la table s'arrête à la revue de conception ; aucune épreuve n'est courue par la table.

**Liste 2 — Épreuves (S12)**

1. **Le parcours**, chronométré — slalom et pente, un rover à la fois, le meilleur temps gagne
2. **Le capture the flag**, avec l'échantillon posé debout au centre — toutes les équipes en même temps, sur la table, **pilotées à la main** à la télécommande, chaque équipe sur sa bande ; départ et arrivée dans une zone commune. Échantillon ramené debout dans la zone : **+2** pour l'équipe. Échantillon renversé : **−1** pour l'équipe qui l'a renversé, et l'animateur le remet debout au centre, à la main. **Trois manches, ou 15 minutes** au plus, remise en place des rovers et de l'échantillon comprise

**Matériaux libres** : carton, impression 3D, et tout matériau de récupération que l'équipe apporte ou trouve à l'atelier.

Chaque point de la liste 1 est une contrainte de conception. Chaque ligne de la liste 2 est un jeu. Un rover peut cocher toute la liste 1 et perdre les deux épreuves : c'est voulu, et ça se dit aux équipes dès la S5.

**« Debout, sans le renverser »** est ce qui fait de l'échantillon une contrainte de conception : poussé sans précaution, l'échantillon bascule. Il faut un pare-chocs, une fourche ou une pince.

→ [Fiche d'animation](s05.md) · [Page élève](../../docs/projets/rover/seances/s05-formez-votre-equipe.md) · [Cahier des charges, version jeunes](../../docs/projets/rover/cahier-des-charges.md)

## Séance 6 — Phase 2 — Exploration & création

**Titre :** Dessinez les pièces de votre rover
**Notions :** CAO par esquisse, extrusion et révolution · bibliothèques de pièces partagées : trouver, réemployer, modifier · choix du matériau, carton ou impression
**Livrable intermédiaire :** pièces de l'équipe dessinées et parties à l'impression, ou fabriquées en carton ou en récupération

*Le concept est posé en 30 minutes, dans Tinkercad : on dessine une pièce à partir d'une esquisse, par extrusion ou révolution, et à côté, des milliers de pièces existent déjà et se partagent. Le reste de la séance, chaque équipe fabrique ce qu'elle veut, en 3D, en carton ou en matériaux de récupération. Imprimer dès la S6 laisse deux ou trois itérations avant la revue de conception.*

→ [Fiche d'animation](s06.md) · [Page élève](../../docs/projets/rover/seances/s06-dessinez-vos-pieces.md)

## Séance 7 — Phase 2 — Exploration & création

**Titre :** Faites bouger une pièce avec un servomoteur
**Notions :** servomoteur : un angle, pas une vitesse · broches `S1` à `S8` de la DFR0548 · commande d'un actionneur depuis le programme
**Livrable intermédiaire :** servomoteur commandé par le programme, monté sur le rover si l'équipe en a l'usage

*Utile aux équipes qui choisissent de saisir ou soulever l'échantillon ; le cahier des charges permet de le pousser.*

→ [Fiche d'animation](s07.md) · [Page élève](../../docs/projets/rover/seances/s07-commandez-un-servomoteur.md)

## Séance 8 — Phase 2 — Exploration & création

**Titre :** Faites piloter votre rover par la table
**Notions :** protocole imposé A1 · bande et groupe · la valeur reçue devient une vitesse · gestionnaire radio qui ne bloque pas · arrêt sur silence
**Livrable intermédiaire :** rover conforme à A1, piloté par la table comme par sa télécommande

*Une démonstration courte : le code du rover de la S4 reçoit déjà les cinq clés d'A1. Quelques modifications suffisent pour que la table le pilote. Deux points à expliquer : la S4 a mis chacun sur sa bande parce que douze télécommandes émettaient en même temps ; sur la table, un seul émetteur parle à tous, et le groupe suffit à séparer les rovers. Et la valeur prise comme vitesse (0–1023 ramené à 0–255) était le bonus 3 de la S4 : ceux qui l'ont fait ont déjà une partie du travail.*

→ [Fiche d'animation](s08.md) · [Page élève](../../docs/projets/rover/seances/s08-pilote-par-la-table.md)

## Séance 9 — Phase 2 — Exploration & création

**Titre :** Guidez votre rover vers une cible
**Notions :** recevoir une mesure et non un ordre · décision à bord · condition sur un signe et un seuil · mode manuel et mode autonome
**Livrable intermédiaire :** rover qui réagit à `cap` et `dist`, testé avec un micro:bit émetteur

*B1 est détaillé sans donner la réponse : ce que la table envoie, et la question de ce qu'on peut en faire. C'est un « va plus loin » du cahier des charges ; les équipes qui ne le visent pas continuent leur conception.*

→ [Fiche d'animation](s09.md) · [Page élève](../../docs/projets/rover/seances/s09-guidez-votre-rover.md)

## Séance 10 — Phase 3 — Finalisation & valorisation

**Titre :** Votre rover face au cahier des charges
**Notions :** revue de conception · écart entre l'attendu et l'obtenu · essais et réglages
**Livrable intermédiaire :** liste 1 passée en revue, écarts relevés et corrections engagées

*La revue de conception compte une dizaine de minutes par équipe, soit 40 à 60 minutes pour 4 à 6 équipes. Les équipes qui attendent leur passage ou qui en sortent corrigent et s'entraînent sur le parcours. C'est l'exception à la règle des 30 minutes : la revue n'apporte pas de notion nouvelle.*

→ [Fiche d'animation](s10.md) · [Page élève](../../docs/projets/rover/seances/s10-revue-de-conception.md)

## Séance 11 — Phase 3 — Finalisation & valorisation

**Titre :** Présentez votre rover sur une page web
**Notions :** page web à partir d'un gabarit HTML · texte et image · justifier un choix de conception
**Livrable intermédiaire :** page de présentation du rover remplie

*Les photos et les choix doivent avoir été consignés au carnet depuis la S5 : sans eux, la page reste vide.*

→ [Fiche d'animation](s11.md) · [Page élève](../../docs/projets/rover/seances/s11-presentez-votre-rover.md)

## Séance 12 — Phase 3 — Finalisation & valorisation

**Titre :** Vos rovers en épreuve
**Notions :** démonstration · bilan de projet
**Livrable intermédiaire :** épreuves courues, bilan collectif

→ [Fiche d'animation](s12.md) · [Page élève](../../docs/projets/rover/seances/s12-vos-rovers-en-epreuve.md)

---

## Notes de préparation

**Principe de la phase 2.** Après la S5, chaque notion nouvelle tient en 30 minutes au plus ; le reste de la séance est à l'équipe, pour appliquer la notion au rover ou poursuivre sa conception.

**Protocoles de la table.** Seuls A1 et B1 sont retenus. B2 et B3 sont écartés pour l'instant, le temps d'en évaluer la complexité.

**Le découpage LP et le rythme réel ne coïncident pas.** Les phases LP sont 1–3 / 4–9 / 10–12 ; le parcours bascule de l'individuel au collectif entre la S4 et la S5. Ce n'est pas un problème — la S4 clôt le rover individuel à l'intérieur de la phase 2 — mais il faut le savoir en lisant le planning.

**Bloom.** Les cinq objectifs couvrent quatre niveaux : *Appliquer* (réaliser, câbler, programmer) sur la phase 1, *Analyser* (diagnostiquer) sur la phase 2, *Créer* et *Évaluer* (concevoir en équipe et justifier) sur les phases 2 et 3. La progression attendue par le guide LP est respectée.

**Sur la durée.** 12 × 1 h 45 dont plusieurs séances chargées. Mesuré au premier passage : S1, 2 jeunes sur 9 ont terminé ; S2, le groupe s'est arrêté avant les quatre autres mouvements. **Les séances 1 à 4 ont été redécoupées en conséquence** : le châssis passe en S2, les mouvements en S3 après la plaque — le défi du garage y devient un « va plus loin » —, la télécommande en S4. La S4 devient la plus chargée ; on laisse tel quel et on verra au bilan si elle déborde. Prévoir que la phase 2 absorbe du retard : c'est le rôle des temps libres après chaque notion.
