# Séance 8 — Faites piloter votre rover par la table

> [!NOTE] Nouveau concept : une clé et une valeur
> Un message radio peut porter un mot **et** un nombre. La table envoie vos cinq mots, chacun avec une vitesse de `0` à `1023`. L'animateur le montre en début de séance.
>
> → [Envoyer, recevoir](../../../fiches/makecode-prise-en-main.md#envoyer-recevoir)

1. **[Ce que demande la table](#1-ce-que-demande-la-table)** : votre programme comprend la table.
2. **[Passez sur la table](#2-passez-sur-la-table)** : la table pilote votre rover le long d'une figure.

## 1. Ce que demande la table

**Ce que vous allez obtenir :** un programme qui comprend la table.

<video controls playsinline preload="metadata" src="../../../../assets/rover-s08/video-table-pilote.mp4"></video>

La table parle à tous les rovers sur la bande `83`. Le **groupe** dit à qui le message s'adresse : c'est votre numéro. `radio définir groupe` est dans **Radio**.

Votre rover doit recevoir `nom` et `valeur`, et passer de la télécommande à la table. Le cahier des charges dit le reste.

→ [Le cahier des charges](../cahier-des-charges.md#le-pilotage)

**À vous.** Répartissez-vous le travail : la télécommande, le rover, le changement de mode. Pas le temps de tout faire ? Commencez par ce qui compte le plus pour votre rover.

### La télécommande envoie la vitesse

La table envoie les cinq mots de ta télécommande, chacun avec une **valeur** de `0` à `1023` : la vitesse. Ta télécommande va faire pareil, avec `envoyer la valeur … = …`, dans **Radio**. La valeur, c'est l'inclinaison : `valeur absolue`, dans **Maths**, la rend positive dans les deux sens.

```blocks
basic.forever(function () {
    basic.clearScreen()
    if (input.acceleration(Dimension.Y) < -200) {
        radio.sendValue("avancer", Math.abs(input.acceleration(Dimension.Y)))
        led.plot(2, 0)
    } else if (input.acceleration(Dimension.Y) > 200) {
        radio.sendString("reculer")
        led.plot(2, 4)
    } else if (input.acceleration(Dimension.X) < -200) {
        radio.sendString("gauche")
        led.plot(0, 2)
    } else if (input.acceleration(Dimension.X) > 200) {
        radio.sendString("droite")
        led.plot(4, 2)
    } else {
        radio.sendString("arreter")
        led.plot(2, 2)
    }
    basic.pause(100)
})
```

La première branche est faite, les quatre autres envoient encore un mot seul.

**À toi.** Les quatre autres branches se font de même. Vers l'avant et l'arrière, la valeur vient de `y` ; à gauche et à droite, de `x`. Pour `arreter`, `0`. Les mots de votre servomoteur aussi, si vous en avez un.

> [!CAUTION] Un mot fait 8 caractères au plus
> Au-delà, la carte le coupe sans prévenir. Les cinq mots du protocole tiennent tous dedans.

Ton rover n'obéit plus : il attend encore un mot seul.

### Le rover prend la vitesse

Ton rover a besoin de l'autre `quand une donnée est reçue par radio`, celui qui apporte `nom` et `valeur`. La valeur va de `0` à `1023`, tes moteurs de `0` à `255` : `projeter`, dans **Maths**, passe de l'un à l'autre. `limiter`, lui aussi dans **Maths**, garde une vitesse entre `0` et `255`.

Le rover, avec sa première branche et sa première fonction transformées :

```blocks
function avancer () {
    motor.MotorRun(motor.Motors.M1, motor.Dir.CW, vM1)
    motor.MotorRun(motor.Motors.M2, motor.Dir.CW, vM2)
}
radio.onReceivedValue(function (name, value) {
    vitesse = Math.map(value, 0, 1023, 0, 255)
    vM1 = Math.constrain(20 + vitesse, 0, 255)
    vM2 = Math.constrain(vitesse, 0, 255)
    basic.clearScreen()
    if (name == "avancer") {
        avancer()
        led.plot(2, 0)
    }
})
let vM2 = 0
let vM1 = 0
let vitesse = 0
```

- `vitesse` : la valeur reçue, ramenée à `0`–`255`.
- `vM1` et `vM2` : une vitesse par moteur. Ta compensation de la séance 2 devient un écart, ici `20 +` pour `M1`, le plus lent sur ce rover.
- `avancer` lit `vM1` et `vM2` au lieu de vitesses écrites en chiffres.

**À toi.** Pour les quatre autres : les branches vont dans le nouveau gestionnaire et comparent `nom` au lieu de `receivedString`, les fonctions lisent `vM1` et `vM2`. L'ancien gestionnaire se supprime.

### Le changement de mode

Un bouton par source : `A` pour la table, `B` pour la télécommande. Ici, l'équipe 10 :

```blocks
input.onButtonPressed(Button.A, function () {
    radio.setFrequencyBand(83)
    radio.setGroup(10)
})
input.onButtonPressed(Button.B, function () {
    radio.setFrequencyBand(10)
    radio.setGroup(0)
})
```

Une variable `mode` : `1` avec `A`, `0` avec `B`. Dans `toujours`, juste après `effacer l'écran`, un point témoin par mode : `0,0` et `4,0`. Deux programmes, un par mode, c'est permis aussi.

> [!TIP] Tester sans la table
> Mets ta télécommande sur la bande `83` et votre groupe. Si le rover lui obéit, il obéira à la table.

## 2. Passez sur la table

**Ce que vous allez obtenir :** votre rover suit la figure de la table.

Une équipe à la fois, dans l'ordre du tableau. La table vérifie :

- `avancer` : 5 cm au moins en 1,5 s
- `gauche` et `droite` : deux sens opposés

L'arrêt quand la table se tait, c'est pour la séance 9.

## Va plus loin

- **Le démarrage en douceur.** Penché juste au seuil, ton rover bourdonne sans partir. Projette vers ta vitesse minimale de la séance 2 plutôt que vers `0`.

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md) · [Déboguer](../../../fiches/deboguer.md)
