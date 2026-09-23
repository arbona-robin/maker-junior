# Séance 1 — Fabrique et monte la base motrice

Tu repars avec une base de rover qui roule. D'abord l'électronique, testée sur la table : une erreur s'y répare sans rien démonter. Ensuite le châssis, et le montage.

## 1. Le moteur tout seul

<figure markdown>
![Un moteur TT branché en direct sur un bloc d'accus, à l'intérieur de la boîte en carton de test](../../../assets/rover-s01/15-moteur-sur-accus.jpg)
</figure>

Branché sur les accus, il tourne à fond, dans un seul sens.

## 2. Pourquoi une carte entre les deux

<figure markdown>
![La carte DFR0548 avec son micro:bit, reliée à deux moteurs et à un pack d'accus, le tout posé dans la boîte de test](../../../assets/rover-s01/16-electronique-vue-ensemble.jpg)
</figure>

> [!NOTE] Le micro:bit commande, la carte exécute
> Une broche du micro:bit allume une LED, pas un moteur. La carte prend l'énergie des accus, et règle sens et vitesse sur ordre du micro:bit.

→ [La carte DFR0548 et ses blocs](../../../fiches/carte-dfr0548.md)

## 3. Assemble ton électronique

Interrupteur de la carte sur **off** pendant tout le câblage.

### Le micro:bit sur la carte

<figure markdown>
![Le micro:bit en train d'être enfiché dans le connecteur de la carte d'extension, écran vers l'extérieur](../../../assets/rover-s01/17-microbit-sur-carte.jpg)
</figure>

**Écran vers l'extérieur.** S'il résiste, il est à l'envers : ne force pas.

### Les moteurs sur les borniers

<figure markdown>
![Un fil de moteur glissé dans le bornier, tournevis sur la vis](../../../assets/rover-s01/18-fil-dans-bornier.jpg)
</figure>

Moteur **gauche** → `M1`, moteur **droit** → `M2`. L'ordre des deux fils n'a pas d'importance pour l'instant.

<figure markdown>
![Une main tire doucement sur un fil vissé dans le bornier pour vérifier qu'il tient](../../../assets/rover-s01/19-test-traction.jpg)
</figure>

Tire sur chaque fil : s'il ressort, resserre.

### Le pack d'accus

Rouge sur `+`, noir sur `−`, dans le petit bornier marqué `3.5~5.5V`.

> [!CAUTION] La polarité ne se rattrape pas
> Une inversion peut détruire la carte. Vérifie deux fois.

> [!IMPORTANT] Point de contrôle
> Fais valider ton câblage avant de mettre sous tension.

## 4. Ouvre MakeCode

[makecode.microbit.org](https://makecode.microbit.org) → **Nouveau projet** → nomme-le `rover`.

<figure class="screenshot" markdown>
![La page d'accueil de MakeCode avec la section « Mes projets » et le bouton « Nouveau projet »](../../../assets/rover-s01/20-makecode-accueil.png)
</figure>

<figure class="screenshot" markdown>
![La fenêtre « Créer un projet » avec le nom rover saisi](../../../assets/rover-s01/21-nouveau-projet-rover.png)
</figure>

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md)

## 5. Ton premier programme

Dans `au démarrage` : une icône (**Base**) et un son (**Musique**).

<figure class="screenshot" markdown>
![Le bloc « au démarrage » contenant « montrer l'icône » et « jouer gloussement jusqu'à la fin », et un bloc « toujours » vide à côté](../../../assets/rover-s01/22-au-demarrage-icone-son.png)
</figure>

Branche l'USB, clique sur **Télécharger**, suis les instructions.

<figure class="screenshot" markdown>
![La fenêtre « 1. Connectez votre micro:bit à votre ordinateur »](../../../assets/rover-s01/28-televersement.png)
</figure>

> [!NOTE] Pourquoi une icône et un son
> Ils te prouvent que **ton** programme tourne. Si plus tard rien ne bouge, tu sauras que le problème n'est pas là.

## 6. Fais clignoter l'écran

`toujours` répète son contenu sans fin.

**À toi.** En boucle : flèche vers le haut pendant 1 seconde, écran éteint pendant 1 seconde. Tous les blocs sont dans **Base**.

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Le bloc « toujours » contenant : montrer la flèche Nord, pause 1000 ms, effacer l'écran, pause 1000 ms](../../../assets/rover-s01/23-programme-clignotant.png)
<figcaption>1000 ms = 1 seconde.</figcaption>
</figure>

</details>

<details markdown>
<summary>Pour aller plus loin — en Python</summary>

En haut, bascule de **Blocs** à **Python** : c'est le même programme.

<figure class="screenshot" markdown>
![Le même programme affiché en Python dans MakeCode](../../../assets/rover-s01/24-vue-python.png)
</figure>

</details>

## 7. Ajoute l'extension DF-Driver

**Extensions** → colle cette adresse → clique sur « motor ».

```
https://github.com/DFRobot/pxt-motor
```

<figure class="screenshot" markdown>
![La fenêtre Extensions avec l'URL collée et la carte « motor » dans les résultats](../../../assets/rover-s01/25-extension-url-collee.png)
</figure>

L'avertissement « non approuvée par Microsoft » est normal : l'extension vient du fabricant de la carte.

<figure class="screenshot" markdown>
![La catégorie DF-Driver dépliée, montrant les blocs Servo, Motor et Stepper en orange](../../../assets/rover-s01/26-categorie-df-driver.png)
<figcaption>La catégorie DF-Driver apparaît.</figcaption>
</figure>

→ [La carte DFR0548 et ses blocs](../../../fiches/carte-dfr0548.md#lextension-df-driver)

## 8. Fais tourner les moteurs

Ajoute les blocs moteurs à ton programme :

<figure class="screenshot" markdown>
![Le programme complet : toujours → montrer la flèche Nord, Motor M1 CW 100, Motor M2 CW 100, pause 1000, effacer l'écran, Motor Stop All, pause 1000](../../../assets/rover-s01/27-programme-moteurs.png)
</figure>

Téléverse. Les moteurs ne tournent pas encore : ils ont besoin des accus.

> [!CAUTION] Un moteur alimenté part tout seul
> Tout dans la **boîte de test** avant d'allumer, aujourd'hui et à chaque séance. Tiens le câble USB.

Interrupteur sur **on**, puis vérifie :

- [ ] Les deux moteurs tournent, puis s'arrêtent ensemble
- [ ] Tu sais lequel est sur `M1` (sors le bloc `M2` pour voir) : marque-le au ruban
- [ ] Aucun fil ne sort de son bornier

<figure markdown>
<video controls playsinline preload="metadata" src="../../../../assets/rover-s01/video-test-moteurs.mp4"></video>
<figcaption>Ce que tu dois obtenir.</figcaption>
</figure>

> [!TIP] La flèche s'affiche, mais rien ne tourne ?
> Le problème n'est pas dans le code. Vérifie l'interrupteur, les fils, les accus.

→ [Déboguer](../../../fiches/deboguer.md)

> [!IMPORTANT] Point de contrôle
> Fais valider ton électronique. Puis interrupteur sur **off**, USB débranché.

## 9. Fabrique ton châssis

<figure class="plan" markdown>
![Plan de découpe du châssis : plaque de 175 sur 70 mm, cotes horizontales 35, 20, 65, 20, 35 mm et verticales 20, 30, 20 mm, deux rectangles à découper placés à 10 mm des bords, lignes de pli en pointillés](../../../assets/plans/rover-base-chassis-v0.3.png)
</figure>

Trait plein : tu découpes. Pointillé : tu plies.

### Reporte le plan

Imprime [le plan (PDF)](../../../assets/plans/rover-base-chassis-v0.3.pdf) **à 100 %**. Vérifie à la règle : le grand côté fait 175 mm.

<details markdown>
<summary>Pas d'imprimante ? Recopie le plan</summary>

Sur papier quadrillé 5 × 5 mm. **Compte les carreaux, ne mesure pas** : la plaque en fait 35 × 14.

Le fichier source : [SVG](../../../assets/plans/rover-base-chassis-v0.3.svg).

</details>

Colle la feuille sur la face **intérieure** des plis.

<figure markdown>
![Le poste de découpe : tapis vert, plaque de carton, plan imprimé, règle métallique à rebord et outil de découpe posés à côté](../../../assets/rover-s01/01-plan-sur-carton.jpg)
</figure>

### Découpe

> [!CAUTION] L'outil de découpe
> - Règle métallique **à rebord**, toujours.
> - Doigts **posés sur la règle, derrière le rebord**.
> - **Plusieurs passes légères**, sans forcer.
> - **Protection de lame remise** dès que tu poses l'outil.

<figure markdown>
![Découpe : les doigts sont posés à plat sur la règle, derrière le rebord relevé, et la lame passe de l'autre côté du rebord](../../../assets/rover-s01/02-decoupe-regle-a-rebord.jpg)
<figcaption>Le rebord relevé est ce qui sépare tes doigts de la lame.</figcaption>
</figure>

→ [Tracer, découper, plier le carton](../../../fiches/carton-tracer-decouper-plier.md#decouper)

### Plie

Règle **sur sa tranche**, pas à plat, le long du pointillé : appuie fort, puis plie contre la règle. Les rabats doivent tenir d'équerre tout seuls.

→ [Tracer, découper, plier le carton](../../../fiches/carton-tracer-decouper-plier.md)

## 10. Monte ton rover

### Les moteurs

Moteurs entre les rabats, axes parallèles, `M1` à gauche. Deux élastiques croisés.

<div class="photo-row" markdown>
<figure markdown>
![Le châssis plié avec les deux moteurs TT posés](../../../assets/rover-s01/03-chassis-plie-moteurs.jpg)
</figure>
<figure markdown>
![Vue de dessus des deux moteurs positionnés sur le châssis](../../../assets/rover-s01/04-moteurs-positionnes.jpg)
</figure>
<figure markdown>
![Les rabats latéraux relevés autour des moteurs](../../../assets/rover-s01/05-rabats-lateraux-releves.jpg)
</figure>
</div>

<figure markdown>
![Les moteurs bloqués par deux élastiques croisés](../../../assets/rover-s01/06-moteurs-bloques-elastiques.jpg)
</figure>

Appuie sur un axe : si le moteur bouge dans son logement, resserre.

### La carte et les accus

Carte sur l'étage du haut, accus par-dessus, un élastique. Fils ni coincés ni tendus.

<div class="photo-row" markdown>
<figure markdown>
![La carte DFR0548 avec le micro:bit posée sur le châssis](../../../assets/rover-s01/07-carte-dfr0548-montee.jpg)
</figure>
<figure markdown>
![Le pack d'accus posé, un élastique tendu au-dessus](../../../assets/rover-s01/08-batterie-pose-elastique.jpg)
</figure>
<figure markdown>
![Le pack d'accus sanglé par un élastique](../../../assets/rover-s01/09-batterie-fixee.jpg)
</figure>
</div>

### Les roues

Languette arrière rabattue dessous et scotchée : c'est ta roue folle. Enfonce les deux roues sur les axes.

<figure markdown>
![La languette arrière rabattue sous le châssis et maintenue au ruban adhésif](../../../assets/rover-s01/10-languette-arriere-scotchee.jpg)
</figure>

<div class="photo-row" markdown>
<figure markdown>
![Une roue jaune et noire posée sur le tapis de découpe](../../../assets/rover-s01/12-roue-tt.jpg)
</figure>
<figure markdown>
![Vue de dessous du rover, une roue montée](../../../assets/rover-s01/11-vue-dessous-roue.jpg)
</figure>
<figure markdown>
![Le rover terminé, vu de trois quarts](../../../assets/rover-s01/13-rover-termine.jpg)
</figure>
</div>

### Règle le sens de rotation

Rover dans la boîte de test, interrupteur sur **on**. Un moteur tourne à l'envers : c'est normal. Inverse ses deux fils, ou passe son bloc en `CCW`. **Note ton choix dans le carnet.**

<figure markdown>
<video controls playsinline preload="metadata" src="../../../../assets/rover-s01/video-rover-roule.mp4"></video>
<figcaption>USB débranché : le programme vit dans la carte.</figcaption>
</figure>

---

## Ce que tu dois avoir à la fin

- [ ] Électronique testée, moteur `M1` repéré
- [ ] Châssis découpé, rabats d'équerre
- [ ] Moteurs fixés, roues qui tournent librement
- [ ] Carte et accus sanglés
- [ ] Les deux roues poussent dans le même sens
- [ ] Le rover roule sans l'ordinateur
- [ ] Ton [carnet de bord](../../../carnet-de-bord/rover-s01.md) rempli

## Avant de partir

Matériel dans ton bac, chutes triées, **outil de découpe rendu**, accus en charge.
