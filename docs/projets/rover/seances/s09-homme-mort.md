# Séance 9 — Le dispositif de l'homme mort

> [!NOTE] Nouveau concept : l'homme mort
> Dans un train, le conducteur appuie régulièrement sur une pédale ; s'il ne le fait plus, le train freine seul. Un rover qui ne reçoit plus de message pendant une seconde s'arrête de la même façon. L'animateur le montre en début de séance.
>
> → [S'arrêter quand le signal se perd](../../../fiches/makecode-prise-en-main.md#sarreter-quand-le-signal-se-perd)

1. **[Votre rover s'arrête seul](#1-votre-rover-sarrete-seul)** : télécommande éteinte, il s'arrête en une seconde.

## 1. Votre rover s'arrête seul

**Ce que vous allez obtenir :** tu éteins ta télécommande pendant que ton rover roule, il s'arrête en une seconde.

Si la télécommande s'éteint ou si le rover sort de sa portée, il ne reçoit plus rien et garde son dernier ordre. Le cahier des charges demande qu'il s'arrête.

Ton rover note **l'heure de chaque message**, et vérifie sans arrêt depuis combien de temps il n'en a pas reçu.

`temps d’exécution (ms)`, dans **Entrée**, donne le nombre de millisecondes depuis l'allumage de la carte : c'est l'horloge du rover.

Le programme se partage en deux :

- **le gestionnaire range** : le mot reçu dans `ordre`, l'heure dans `dernierMessage`, et les vitesses ;
- **`toujours` agit** : plus de `1000` ms depuis `dernierMessage`, il arrête les moteurs ; sinon, il obéit à `ordre`.

```blocks
function avancer () {
    motor.MotorRun(motor.Motors.M1, motor.Dir.CW, vM1)
    motor.MotorRun(motor.Motors.M2, motor.Dir.CW, vM2)
}
function arreter () {
    motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 0)
    motor.MotorRun(motor.Motors.M2, motor.Dir.CW, 0)
}
radio.onReceivedValue(function (name, value) {
    ordre = name
    dernierMessage = input.runningTime()
    vitesse = Math.map(value, 0, 1023, 0, 255)
    vM1 = 20 + vitesse
    vM2 = vitesse
})
basic.forever(function () {
    basic.clearScreen()
    if (input.runningTime() - dernierMessage > 1000) {
        arreter()
    } else if (ordre == "avancer") {
        avancer()
        led.plot(2, 0)
    }
})
let vM2 = 0
let vM1 = 0
let vitesse = 0
let dernierMessage = 0
let ordre = ""
```

`temps d’exécution (ms) − dernierMessage` : le temps passé depuis le dernier message.

> [!NOTE] Pas de pause dans le gestionnaire
> La carte ne garde que quatre messages en attente. Si le gestionnaire attend, les suivants sont perdus.

**À toi.** Les quatre autres branches vont dans `toujours`, en `sinon si` à la suite de `avancer`, et testent `ordre` au lieu de `nom`.

Testez à la télécommande : rover qui roule, télécommande éteinte.

## Va plus loin

- **Un témoin du silence.** Quand ton rover s'arrête faute de message, allume un point que tu n'utilises pour rien d'autre : tu sauras pourquoi il s'est arrêté.

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md) · [Déboguer](../../../fiches/deboguer.md)
