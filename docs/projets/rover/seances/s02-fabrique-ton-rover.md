# Séance 2 — Fabrique ton rover et fais-le rouler droit

1. **[Fabrique ton châssis](#1-fabrique-ton-chassis)** : découpé, plié, les rabats d'équerre.
2. **[Monte ton rover](#2-monte-ton-rover)** : tout tient, et les deux roues tournent dans le même sens.
3. **[Ta première fonction](#3-ta-premiere-fonction)** : `avancer`, appelée dans `toujours`.
4. **[Fais-le rouler droit](#4-fais-le-rouler-droit)** : moins d'une largeur de rover d'écart sur 1,50 m.

## 1. Fabrique ton châssis

<figure class="plan" markdown>
![Plan de découpe du châssis : plaque de 175 sur 70 mm, cotes horizontales 35, 20, 65, 20, 35 mm et verticales 20, 30, 20 mm, deux rectangles à découper placés à 10 mm des bords, lignes de pli en pointillés](../../../assets/plans/rover-base-chassis-v0.3.png)
</figure>

Trait plein : tu découpes. Pointillé : tu plies.

### Reporte le plan

Imprime [le plan (PDF)](../../../assets/plans/rover-base-chassis-v0.3.pdf) **à 100 %**. Vérifie à la règle : le grand côté fait 175 mm.

<details markdown>
<summary>Pas d'imprimante ? Recopie le plan</summary>

Sur papier quadrillé 5 × 5 mm. **Compte les carreaux** : la plaque en fait 35 × 14.

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

### Plie

Règle **sur sa tranche**, pas à plat, le long du pointillé : appuie fort, puis plie contre la règle.

→ [Tracer, découper, plier le carton](../../../fiches/carton-tracer-decouper-plier.md)

> [!TIP] Ça marche si…
> Les rabats tiennent d'équerre tout seuls.

## 2. Monte ton rover

**Ce que tu vas obtenir :**

<figure markdown>
![Le rover terminé, vu de trois quarts](../../../assets/rover-s01/13-rover-termine.jpg)
</figure>

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
</div>

### Les deux roues dans le même sens

Pose ton rover **sur l'arrière, roues en l'air**, dans la boîte de test. Lance ton programme de la séance 1.

<figure markdown>
![Le rover posé sur son pack d'accus, les deux roues en l'air, dans une boîte en carton](../../../assets/rover-s02/01-rover-sur-arriere-roues-en-lair.jpg)
<figcaption>Roues en l'air : tu vois les deux sens sans courir après ton rover.</figcaption>
</figure>

Un moteur tourne à l'envers : c'est normal. Inverse ses deux fils, ou passe son bloc en `CCW`.

<figure markdown>
<video controls playsinline preload="metadata" src="../../../../assets/rover-s01/video-rover-roule.mp4"></video>
<figcaption>USB débranché : le programme vit dans la carte.</figcaption>
</figure>

> [!IMPORTANT] Point de contrôle
> Fais valider ton montage avant de passer au code.

## 3. Ta première fonction

**Ce que tu vas obtenir :** tes deux blocs moteurs rangés dans un bloc à toi, `avancer`.

**Avancé** → **Fonctions** → **Créer une fonction…**

<figure class="screenshot" markdown>
![La catégorie Fonctions dépliée dans MakeCode, avec le bouton « Créer une fonction… »](../../../assets/rover-s02/20-categorie-fonctions.png)
</figure>

Appelle-la `avancer`, puis **Terminé**.

<figure class="screenshot" markdown>
![La fenêtre « Modifier la fonction » avec le nom avancer en cours de saisie](../../../assets/rover-s02/21-creer-fonction-avancer.png)
</figure>

Glisse tes deux blocs `Motor` dans la fonction. Reprends **Fonctions** : le bloc `appel avancer` est apparu. Mets-le dans `toujours`, à la place des blocs que tu viens de déplacer.

```blocks
function avancer () {
    motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 110)
    motor.MotorRun(motor.Motors.M2, motor.Dir.CW, 110)
}
basic.showIcon(IconNames.Happy)
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
basic.forever(function () {
    basic.showArrow(ArrowNames.North)
    avancer()
    basic.pause(1000)
    basic.clearScreen()
    motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 0)
    motor.MotorRun(motor.Motors.M2, motor.Dir.CW, 0)
})
```

> [!TIP] Ça marche si…
> Ton rover fait exactement la même chose qu'avant : le programme est rangé autrement, il n'a pas changé.

## 4. Fais-le rouler droit

**Ce que tu vas obtenir :** sur 1,50 m, ton rover s'écarte de la ligne de moins d'une largeur de rover.

Ton rover tire d'un côté. **Regarde la mécanique avant de toucher au code.**

- [ ] La languette arrière glisse sans frotter d'un côté
- [ ] Le rover est d'aplomb, il ne se balance pas
- [ ] Les deux moteurs sont bien plaqués contre les rabats, parallèles
- [ ] Les roues sont enfoncées à fond et ne voilent pas
- [ ] Le pack d'accus est centré

Il dévie encore ? Alors les deux moteurs ne tournent pas exactement à la même vitesse. Mets-les **tous les deux à 80**, puis monte celui qui est le plus lent, 5 par 5, jusqu'à ce que le rover suive la ligne.

> [!NOTE] Il n'y a pas de bonne valeur
> Chaque moteur est unique. Sur le rover des photos, l'équilibre tombe à 110 ; le tien sera ailleurs, entre 80 et 120.

<figure markdown>
![Le banc d'essai : une longue bande d'adhésif noir tendue au sol, un repère en L à son extrémité, et le rover calé dedans avant le départ](../../../assets/rover-s02/02-banc-dessai.jpg)
<figcaption>Le L cale le rover au départ, toujours au même endroit.</figcaption>
</figure>

Cale ton rover dans le L, lance-le, et mesure de combien il s'est écarté de la ligne au bout d'**1,50 m**. Fais trois passages : l'écart change à chaque fois.

Mesure aussi ta **vitesse minimale** : descends la valeur jusqu'à ce que le rover refuse de démarrer, alors qu'une pichenette suffit à le lancer. Note-la.

→ [Rouler droit et tourner](../../../fiches/rouler-droit.md)

> [!IMPORTANT] Point de contrôle
> Montre un passage à l'animateur.
