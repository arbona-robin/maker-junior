# Séance 8 — Pilotez votre rover en vitesse

> [!NOTE] Nouveau concept : une clé et une valeur
> Un message radio peut porter un mot **et** un nombre. Votre télécommande enverra chaque mot avec une vitesse : plus on penche, plus le rover va vite. L'animateur le montre en début de séance.
>
> → [Envoyer, recevoir](../../../fiches/makecode-prise-en-main.md#envoyer-recevoir)

1. **[La télécommande envoie la vitesse](#1-la-telecommande-envoie-la-vitesse)** : chaque mot part avec un nombre, d'autant plus grand que tu penches.
2. **[Le rover prend la vitesse](#2-le-rover-prend-la-vitesse)** : tu penches un peu, il roule doucement ; tu penches fort, il accélère.

Répartissez-vous le travail : la télécommande d'un côté, le rover de l'autre. Pas le temps de tout faire ? Commencez par ce qui compte le plus pour votre rover.

## 1. La télécommande envoie la vitesse

**Ce que tu vas obtenir :** ta télécommande envoie chaque mot avec un nombre, d'autant plus grand que tu penches.

Ta télécommande va envoyer chaque mot avec une **valeur** de `0` à `1023` : la vitesse. Elle le fait avec `envoyer la valeur … = …`, dans **Radio**. La valeur, c'est l'inclinaison : `valeur absolue`, dans **Maths**, la rend positive dans les deux sens.

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
## 2. Le rover prend la vitesse

**Ce que tu vas obtenir :** tu penches un peu, ton rover roule doucement ; tu penches fort, il accélère.

Avec la nouvelle télécommande, ton rover n'obéit plus : son gestionnaire attend encore un mot seul. Il lui faut l'autre `quand une donnée est reçue par radio`, celui qui apporte `nom` et `valeur`. La valeur va de `0` à `1023`, tes moteurs de `0` à `255` : `projeter`, dans **Maths**, passe de l'un à l'autre.

Le rover, avec sa première branche et sa première fonction transformées :

```blocks
function avancer () {
    motor.MotorRun(motor.Motors.M1, motor.Dir.CW, vM1)
    motor.MotorRun(motor.Motors.M2, motor.Dir.CW, vM2)
}
radio.onReceivedValue(function (name, value) {
    vitesse = Math.map(value, 0, 1023, 0, 255)
    vM1 = 20 + vitesse
    vM2 = vitesse
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

## Va plus loin

- **Le démarrage en douceur.** Penché juste au seuil, ton rover bourdonne sans partir. Projette vers ta vitesse minimale de la séance 2 plutôt que vers `0`.

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md) · [Déboguer](../../../fiches/deboguer.md)
