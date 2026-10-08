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

<figure markdown>
![Le support de la lampe à plat : une bande de carton rainurée, deux bandes de cuivre collées en travers, le micro:bit tenu par deux élastiques](../../../assets/objets-connectes-s01/01-support-a-plat.jpg)
</figure>

<span class="todo-media">[plan de découpe du support]</span>

Plie le support le long des rainures. Le micro:bit se tient par deux élastiques, écran vers l'avant ; le boîtier de piles derrière, par deux élastiques aussi. Branche-le au micro:bit.

<div class="photo-row" markdown>

<figure markdown>
![Le support monté, vu de trois quarts : les deux bandes de cuivre sur le dessus, le micro:bit en bas, devant](../../../assets/objets-connectes-s01/02-support-monte.jpg)
</figure>

<figure markdown>
![Le dos du support : le boîtier de piles tenu par deux élastiques](../../../assets/objets-connectes-s01/03-dos-boitier-piles.jpg)
</figure>

</div>

### La LED

<figure markdown>
![Une LED jaune dont les deux pattes sont repliées et enroulées en boucle](../../../assets/objets-connectes-s01/04-led-pattes-enroulees.jpg)
</figure>

Repère la **patte longue** : c'est le `+`. Puis replie et enroule chaque patte en boucle : elle touchera mieux le cuivre.

### Le micro:bit comme une pile

Une pince sur `3V`, une pince sur `GND`, et l'autre bout de chacune sur une bande de cuivre. Retiens quelle bande est reliée à `3V`.

<div class="photo-row" markdown>

<figure markdown>
![Une pince verte sur la broche GND, une pince rouge sur la broche 3V](../../../assets/objets-connectes-s01/05-pinces-3v-gnd.jpg)
</figure>

<figure markdown>
![Les deux pinces vont des broches du micro:bit aux deux bandes de cuivre, une pince par bande](../../../assets/objets-connectes-s01/06-bandes-reliees-3v-gnd.jpg)
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

## Va plus loin

- **Une animation et un son.** Quand on touche les bandes, plusieurs icônes à la suite, et un son, dans **Musique**.
