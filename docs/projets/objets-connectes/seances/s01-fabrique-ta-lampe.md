# Séance 1 — Fabrique ta lampe et allume-la

1. **[Monte ta lampe et allume la LED](#1-monte-ta-lampe-et-allume-la-led)** : le micro:bit sert de pile, la LED s'allume.
2. **[Le programme commande la LED](#2-le-programme-commande-la-led)** : la LED clignote.
3. **[Les bandes deviennent un bouton](#3-les-bandes-deviennent-un-bouton)** : tu touches le cuivre, une icône s'affiche.

## 1. Monte ta lampe et allume la LED

**Ce que tu vas obtenir :**

<figure markdown>
![La LED posée à cheval sur les deux bandes de cuivre, allumée](../../../assets/objets-connectes-s01/07-led-allumee-3v.jpg)
</figure>

### Le support

<figure class="plan" markdown>
![Plan de découpe du support de la lampe : une bande de carton de 285 sur 70 mm, pliée en cinq sections : un montant de 80 mm qui porte le micro:bit et deux pistes de cuivre, P2 de 70 mm et GND de 86 mm, le dessus de 40 mm avec deux bandes de cuivre de 62 mm, à 6 et 22 mm du pli, un montant de 80 mm, la base de 65 mm, et un rabat de 20 mm](../../../assets/plans/lampe-support-v5.png)
</figure>

Imprime [le plan (PDF)](../../../assets/plans/lampe-support-v5.pdf) en A4, **à 100 %**. Colle-le sur le carton : la face imprimée sera l'intérieur de ta lampe.

<figure markdown>
![Le plan imprimé posé sur le carton, sur le tapis de découpe, avec la règle à rebord et l'outil de découpe](../../../assets/objets-connectes-s01/01-plan-sur-carton.jpg)
</figure>

Trait plein : tu découpes, à la règle. Pointillé : tu plies. Le rabat passe sous la première section, collé ou scotché.

> [!CAUTION] L'outil de découpe
> - Règle métallique **à rebord**, toujours.
> - Doigts **posés sur la règle, derrière le rebord**.
> - **Plusieurs passes légères**, sans forcer.
> - **Protection de lame remise** dès que tu poses l'outil.

<div class="photo-row" markdown>

<figure markdown>
![Les deux mains sur la règle à rebord, l'outil de découpe suit le trait du plan](../../../assets/objets-connectes-s01/02-decoupe-a-la-regle.jpg)
</figure>

<figure markdown>
![Le support découpé et plié, face imprimée à l'intérieur](../../../assets/objets-connectes-s01/03-support-plie.jpg)
</figure>

</div>

→ [Tracer, découper, plier le carton](../../../fiches/carton-tracer-decouper-plier.md)

### Les deux bandes de cuivre

Sur le dessus, deux vis sont dessinées, une par bande. Pique chacune avec une punaise, depuis l'intérieur : les trous traversent le carton.

Retourne le support. Colle une bande de cuivre de 62 mm sur chaque trou, face extérieure : la bande `bouton` et la bande `masse`.

<figure markdown>
![Les deux bandes de cuivre collées sur le dessus, face extérieure ; la pointe de la punaise ressort au milieu d'une bande](../../../assets/objets-connectes-s01/11-bandes-exterieures.jpg)
</figure>

Le micro:bit se pose sur le premier montant, écran vers l'extérieur, tenu par deux élastiques. Il sera vissé à la séance 2.

### La LED

<figure markdown>
![Une LED jaune dont les deux pattes sont repliées et enroulées en boucle](../../../assets/objets-connectes-s01/04-led-pattes-enroulees.jpg)
</figure>

Repère la **patte longue** : c'est le `+`. Puis replie et enroule chaque patte en boucle : elle touchera mieux le cuivre.

### Le micro:bit comme une pile

Une pince sur `3V`, une pince sur `GND`, et l'autre bout de chacune sur une bande de cuivre. Retiens quelle bande est reliée à `3V`.

<div class="photo-row" markdown>

<figure markdown>
![Une pince verte sur la broche GND, une pince rouge sur la broche 3V du micro:bit](../../../assets/objets-connectes-s01/05-pinces-3v-gnd.jpg)
</figure>

<figure markdown>
![Les deux pinces au bout des deux bandes de cuivre, une pince par bande](../../../assets/objets-connectes-s01/06-bandes-reliees-3v-gnd.jpg)
</figure>

</div>

Pose la LED à cheval sur les deux bandes, une boucle sur chacune. Elle ne s'allume pas ? Retourne-la : patte longue côté `3V`.

→ [Câbler un circuit](../../../fiches/cabler-un-circuit.md)

> [!IMPORTANT] Point de contrôle
> Montre ta LED allumée, et dis quelle patte est sur la bande reliée à `3V`.

## 2. Le programme commande la LED

**Ce que tu vas obtenir :**

<video controls playsinline preload="metadata" src="../../../../assets/objets-connectes-s01/video-clignotement.mp4"></video>

Déplace la pince de `3V` à `2`. La LED s'éteint : la broche `P2` n'envoie rien tant qu'aucun programme ne le lui demande.

<figure markdown>
![La LED à cheval sur les bandes, éteinte](../../../assets/objets-connectes-s01/09-led-eteinte-sans-programme.jpg)
</figure>

[makecode.microbit.org](https://makecode.microbit.org) → **Nouveau projet** → nomme-le `lampe`.

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md)

Dans `au démarrage` : `écrire sur la broche P2 la valeur 1`, dans **Broches**, sous **Avancé**. Téléverse : la LED s'allume.

```blocks
pins.digitalWritePin(DigitalPin.P2, 1)
```

<figure markdown>
![La LED allumée sur les bandes de cuivre, micro:bit branché en USB](../../../assets/objets-connectes-s01/10-led-allumee-par-programme.jpg)
</figure>

`1`, la broche envoie du courant ; `0`, elle n'envoie rien. `P2` est une **sortie** : c'est le programme qui décide.

**À toi.** La LED s'allume une demi-seconde, s'éteint une demi-seconde, sans fin. Il te faut `toujours` et `pause (ms)`, dans **Base**, et le bloc de la broche.

<details markdown>
<summary>La solution</summary>

```blocks
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(500)
})
```

</details>

> [!TIP] Ça marche si…
> La LED clignote, au rythme d'une demi-seconde.

## 3. Les bandes deviennent un bouton

**Ce que tu vas obtenir :**

<video controls playsinline preload="metadata" src="../../../../assets/objets-connectes-s01/video-toucher-coeur.mp4"></video>

Enlève la LED. Garde les deux pinces : une sur `GND`, une sur `2`. Cette fois, `P2` est une **entrée** : le programme lit ce qui y arrive.

Dans `toujours` : `série écrire valeur`, dans **Avancé** → **Communication Série**, avec `lire la broche analogique P2`, dans **Broches**. Nomme la valeur `p2`.

```blocks
basic.forever(function () {
    serial.writeValue("p2", pins.analogReadPin(AnalogPin.P2))
})
```

Téléverse, USB branché, puis **Afficher données Appareil**. Pose un doigt à cheval sur les deux bandes, et regarde la courbe.

<figure class="screenshot" markdown>
![La courbe de p2 : autour de 660 au repos, elle tombe vers 280 à chaque fois que le doigt touche les bandes](../../../assets/objets-connectes-s01/24-afficher-donnees-toucher.png)
</figure>

Ton doigt relie les deux bandes : la valeur chute. Note ta valeur au repos et ta valeur quand tu touches.

**À toi.** Quand la valeur passe sous un seuil choisi entre tes deux valeurs, le micro:bit affiche une icône. Il te faut `si … alors` et une comparaison, dans **Logique**, et `montrer l'icône`, dans **Base**.

<details markdown>
<summary>La solution</summary>

```blocks
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P2) < 300) {
        basic.showIcon(IconNames.Heart)
    } else {
        basic.clearScreen()
    }
})
```

`300` est le seuil de ce montage. Prends le tien, d'après tes valeurs.

</details>

> [!IMPORTANT] Point de contrôle
> Montre ton bouton en cuivre à l'animateur : l'icône au toucher, rien au repos.

Le micro:bit a ce test tout fait : `lorsque la broche P2 est activée`, dans **Entrée**. Il compare lui-même la valeur à un seuil, et se déclenche une fois à chaque toucher : ici, le cœur s'affiche une seconde, puis s'efface. Tu t'en serviras en séance 3.

```blocks
input.onPinPressed(TouchPin.P2, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(1000)
    basic.clearScreen()
})
```

## Va plus loin

- **Une animation et un son.** Quand on touche les bandes, plusieurs icônes à la suite, et un son, dans **Musique**.
