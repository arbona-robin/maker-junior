# Objets connectés — Le pont et le tableau de bord

Le pont est un micro:bit branché en USB à l'ordinateur de l'animateur. Il écoute la bande `40` et recopie chaque message radio sur le port série. Le tableau de bord, une page web, lit ce port série et affiche chaque micro:bit et ses mesures.

Le tableau de bord : [`docs/tableau-de-bord/index.html`](../../docs/tableau-de-bord/index.html), publié sur le site. Il s'ouvre dans Chrome ou Edge, les seuls navigateurs qui lisent le port série.

## Le programme du pont

MakeCode → **Nouveau projet** `pont` → onglet **JavaScript** → coller, puis repasser en **Blocs** si besoin.

```ts
// Le pont : recopie la radio sur le port série, et l'inverse pour les interrupteurs.
radio.setFrequencyBand(40)
basic.showIcon(IconNames.Yes)

// Radio → page : « numéro de série,clé,valeur,signal »
radio.onReceivedValue(function (name, value) {
    serial.writeLine(
        radio.receivedPacket(RadioPacketProperty.SerialNumber) + "," +
        name + "," + value + "," +
        radio.receivedPacket(RadioPacketProperty.SignalStrength))
    led.toggle(2, 2)
})

// Page → radio : « clé,valeur », pour les clés qui commencent par inter
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    let parties = serial.readUntil(serial.delimiters(Delimiters.NewLine)).split(",")
    if (parties.length == 2) {
        radio.sendValue(parties[0], parseFloat(parties[1]))
        led.toggle(0, 0)
    }
})
```

Le point central de l'écran clignote à chaque message reçu, le coin en haut à gauche à chaque ordre envoyé.

## Le contrat entre le pont et la page

| Sens | Une ligne par message | Exemple |
|---|---|---|
| Pont → page | `numéro de série,clé,valeur,signal` | `-1934561230,temp,21,-62` |
| Page → pont | `clé,valeur` | `interA,1` |

Le numéro de série vaut `0` quand l'émetteur n'a pas `radio émettre le numéro de série` : la page affiche alors une carte d'alerte « Sans numéro de série ».

## Ce que fait la page

- Une carte par micro:bit, ajoutée à son premier message. Le nom se change en cliquant dessus, et reste mémorisé dans le navigateur.
- Une mesure par clé, affichée selon le début de la clé : la table est dans le [catalogue](../../docs/projets/objets-connectes/catalogue.md#la-langue-commune), et dans `AFFICHAGES` en tête du script de la page.
- Hors ligne après 30 secondes sans message : la carte pâlit et passe en fin de grille.
- La force du signal en barres, utile pour tester la portée en séance 9.
- Le journal de tous les messages, avec un filtre par micro:bit et une pause. Les messages des lampes (`tous`, `tour`) n'y apparaissent qu'en gris, sans carte.
- **Projection** masque le journal et agrandit les cartes.
- **Mode démo** fait apparaître six faux micro:bit, sans pont. L'adresse `…/tableau-de-bord/?demo` le lance directement.
- Un bandeau « Pont débranché » quand on retire le câble : l'affichage se fige, les objets continuent.

## Avant la séance 6

1. Programmer le pont, le brancher, ouvrir le tableau de bord, **Connecter le pont**.
2. Allumer un micro:bit de test qui émet `temp` toutes les 5 secondes, numéro de série compris : sa carte doit apparaître.
3. Basculer un interrupteur `inter` en mode démo, puis avec un vrai micro:bit qui l'écoute.
