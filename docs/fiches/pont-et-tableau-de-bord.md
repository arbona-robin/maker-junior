# Installer le pont et le tableau de bord

Le tableau de bord affiche les mesures de tes micro:bit et commande leurs interrupteurs. Pour le faire marcher chez toi, il te faut :

- un micro:bit de plus, le **pont**, branché en USB à l'ordinateur
- **Chrome** ou **Edge** : ce sont les seuls navigateurs qui lisent le port USB

Le pont écoute la bande `40` et recopie chaque message radio dans le câble USB. Dans l'autre sens, il envoie à la radio les ordres des interrupteurs.

<figure markdown>
![Le chemin d'un message : la lampe 7 envoie lum et inter7 par radio au pont, toutes les 5 secondes ; le pont, branché en USB, les passe au tableau de bord ; dans l'autre sens, le tableau de bord envoie inter7 = 0, que toutes les lampes entendent et auquel seule la 7 réagit. Pont débranché, l'écran se fige, la lampe continue seule.](../assets/objets-connectes-s05/03-schema-chemin-message.png)
</figure>

## Programme le pont

MakeCode → **Nouveau projet** `pont` → onglet **JavaScript** → colle ce code → **Télécharger**.

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

// Page → radio : « clé,valeur », pour les interrupteurs
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    let parties = serial.readUntil(serial.delimiters(Delimiters.NewLine)).split(",")
    if (parties.length == 2) {
        radio.sendValue(parties[0], parseFloat(parties[1]))
        led.toggle(0, 0)
    }
})
```

Le point central de l'écran clignote à chaque message reçu, le coin en haut à gauche à chaque ordre envoyé.

> [!CAUTION] Ferme MakeCode
> Après le téléchargement, l'onglet MakeCode reste connecté au pont et lui prend une partie des messages. Ferme l'onglet, ou **⋯** à côté de **Télécharger** → **Déconnecter**.

## Ouvre le tableau de bord

Ouvre le [tableau de bord](../tableau-de-bord/index.html) dans Chrome ou Edge, clique sur **Connecter le pont**, et choisis ton micro:bit dans la liste.

Chaque micro:bit qui émet apparaît dès son premier message. Pour qu'il s'affiche, il émet sur la bande `40`, avec son numéro de série et une clé connue.

→ [La langue commune](../projets/objets-connectes/catalogue.md#la-langue-commune)

Sans pont, **Mode démo** fait apparaître de faux micro:bit.

## Quand rien ne s'affiche

- **Pas de coche sur le pont :** son programme n'est pas téléchargé.
- **Le point central du pont ne clignote pas :** aucun message n'arrive. Vérifie la bande `40` sur le micro:bit qui émet.
- **Il clignote, mais aucune carte n'apparaît :** le micro:bit qui émet n'a pas `radio régler le numéro de série de transmission` dans `au démarrage`.
- **« Ligne illisible » dans le journal, ou un même micro:bit sous plusieurs numéros :** un onglet MakeCode est encore ouvert.
- **Bandeau « Pont débranché » :** le câble USB a bougé. Rebranche-le, puis **Reconnecter le pont**.
