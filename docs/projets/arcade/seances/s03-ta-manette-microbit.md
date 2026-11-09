# Séance 3 — Ta manette micro:bit

1. **[Ton jeu parle à ta manette](#1-ton-jeu-parle-a-ta-manette)** : ton jeu envoie bien, mal et tes vies.
2. **[Regarde ton accéléromètre](#2-regarde-ton-accelerometre)** : tu as noté tes deux seuils.
3. **[Programme ta manette](#3-programme-ta-manette)** : ton micro:bit envoie haut, bas et A, et réagit aux mots du jeu.
4. **[Joue avec ta manette](#4-joue-avec-ta-manette)** : tu joues à ton jeu avec ton micro:bit en main.

## 1. Ton jeu parle à ta manette

**Ce que tu vas obtenir :** ton jeu envoie tes vies dès le départ, puis `bien` à chaque ennemi détruit, `mal` quand tu es touché, et tes vies à chaque changement.

Ouvre **[le parcours du jeu de tir](https://arcade.makecode.com/--skillmap?lang=fr#github:arbona-robin/tutoriels-arcade/jeu-de-tir)**, puis l'activité **Ta manette réagit**. Les blocs sont dans la catégorie **Manette**.

<details markdown>
<summary>Bloqué ? Le programme du jeu</summary>

```blocks
game.splash("Mon jeu de tir", "Appuie sur A pour jouer")
scene.setBackgroundColor(15)
let heros = sprites.create(img`
    . . . . . . . . . . . . . . . .
    . . . . 8 8 8 . . . . . . . . .
    . . . . 8 9 8 8 . . . . . . . .
    . . . . 8 9 9 8 8 . . . . . . .
    . 2 2 . 8 9 9 9 8 8 8 . . . . .
    . 4 2 8 8 9 9 9 9 9 8 8 8 . . .
    . 4 4 8 9 9 9 9 9 9 9 9 9 8 8 .
    . 5 4 8 9 9 9 1 1 9 9 9 9 9 8 8
    . 5 4 8 9 9 9 1 1 9 9 9 9 9 8 8
    . 4 4 8 9 9 9 9 9 9 9 9 9 8 8 .
    . 4 2 8 8 9 9 9 9 9 8 8 8 . . .
    . 2 2 . 8 9 9 9 8 8 8 . . . . .
    . . . . 8 9 9 8 8 . . . . . . .
    . . . . 8 9 8 8 . . . . . . . .
    . . . . 8 8 8 . . . . . . . . .
    . . . . . . . . . . . . . . . .
    `, SpriteKind.Player)
heros.setPosition(20, 60)
controller.moveSprite(heros, 0, 100)
heros.setStayInScreen(true)
info.setLife(3)
manette.afficher(info.life())
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    let tir = sprites.createProjectileFromSprite(img`
        . 5 5 .
        5 4 4 5
        . 5 5 .
        `, heros, 150, 0)
})
game.onUpdateInterval(900, function () {
    let ennemi = sprites.create(img`
        . . 2 2 2 2 . .
        . 2 2 2 2 2 2 .
        2 2 1 2 2 1 2 2
        2 2 f 2 2 f 2 2
        2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2
        . 2 . 2 2 . 2 .
        2 . . . . . . 2
        `, SpriteKind.Enemy)
    ennemi.setPosition(160, randint(10, 110))
    ennemi.vx = -40
    ennemi.setFlag(SpriteFlag.AutoDestroy, true)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.fire, 200)
    info.changeScoreBy(1)
    manette.reagir(ReactionManette.Bien)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeLifeBy(-1)
    scene.cameraShake(4, 500)
    manette.reagir(ReactionManette.Mal)
    manette.afficher(info.life())
})
game.onUpdateInterval(1000, function () {
    if (Math.percentChance(15)) {
        let coeur = sprites.create(img`
            . 2 2 . . 2 2 .
            2 3 2 2 2 2 2 2
            2 3 2 2 2 2 2 2
            2 2 2 2 2 2 2 2
            . 2 2 2 2 2 2 .
            . . 2 2 2 2 . .
            . . . 2 2 . . .
            `, SpriteKind.Food)
        coeur.setPosition(160, randint(10, 110))
        coeur.vx = -30
        coeur.setFlag(SpriteFlag.AutoDestroy, true)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeLifeBy(1)
    manette.afficher(info.life())
})
game.onUpdateInterval(3000, function () {
    let decor = sprites.create(img`
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . 4 4 4 4 4 4 . . . . . . . . .
        . . . . . . . 4 4 5 5 5 5 4 4 4 4 . . . . . . .
        . . . . . . 4 5 5 5 5 4 4 4 4 4 4 4 . . . . . .
        . . . . . 4 5 5 5 4 4 4 4 4 4 2 4 4 4 . . . . .
        . . . . 4 5 5 4 4 4 4 4 4 2 2 4 4 4 4 . . . . .
        . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 .
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 .
        . . . . 4 4 4 4 4 4 4 2 2 4 4 4 4 4 2 . . . . .
        . . . . . 4 4 4 4 4 2 2 4 4 4 4 4 2 . . . . . .
        . . . . . . 4 4 4 4 4 4 4 4 4 4 2 . . . . . . .
        . . . . . . . 4 4 4 4 4 4 4 2 2 . . . . . . . .
        . . . . . . . . . 2 2 2 2 2 . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . . . . . . . . . .
        `, SpriteKind.Player)
    decor.setPosition(160, randint(0, 120))
    decor.vx = -15
    decor.z = -1
    decor.setFlag(SpriteFlag.Ghost, true)
    decor.setFlag(SpriteFlag.AutoDestroy, true)
})
```

</details>

À la fin, clique sur **Partager** et copie le nouveau lien de ton jeu.

## 2. Regarde ton accéléromètre

**Ce que tu vas obtenir :** les deux valeurs à partir desquelles ta manette est vraiment penchée, vers l'avant et vers l'arrière.

Nouveau projet MakeCode micro:bit, nommé `accelerometre`. Dans `toujours`, écris la valeur `y` de l'accéléromètre (avant, arrière).

`série écrire valeur` est dans **Avancé** → **Communication Série**, `accélération (mg)` dans **Entrée**.

```blocks
basic.forever(function () {
    serial.writeValue("y", input.acceleration(Dimension.Y))
})
```

Télécharge, garde le câble branché, puis clique sur **Afficher données Appareil**. Incline ta carte et regarde la courbe de `y`.

| Tu inclines la carte | La courbe monte ou descend ? | À partir de quelle valeur est-elle vraiment penchée ? |
|---|---|---|
| Vers l'avant | | |
| Vers l'arrière | | |

Ces deux valeurs sont tes **seuils**. Note-les, puis ferme cet onglet.

## 3. Programme ta manette

**Ce que tu vas obtenir :** ton micro:bit envoie `haut`, `bas` et `A`, et joue un son ou affiche une icône pour chaque mot reçu du jeu.

Ouvre **[le tutoriel de la manette](https://makecode.microbit.org/?lang=fr#tutorial:https://github.com/arbona-robin/tutoriels-microbit/manette)**, avec tes seuils sous la main.

> [!NOTE] La liaison série, deux fois
> Elle t'a d'abord montré les valeurs de ton accéléromètre dans MakeCode. Maintenant, elle transporte les mots entre ta manette et ton jeu. Un seul programme peut l'utiliser à la fois.

<details markdown>
<summary>Bloqué ? Le programme de la manette</summary>

```blocks
serial.setRxBufferSize(128)
basic.forever(function () {
    if (input.acceleration(Dimension.Y) < -300) {
        serial.writeLine("haut")
    } else if (input.acceleration(Dimension.Y) > 300) {
        serial.writeLine("bas")
    }
    if (input.buttonIsPressed(Button.A)) {
        serial.writeLine("A")
    }
    basic.pause(20)
})
basic.forever(function () {
    let mot = serial.readUntil(serial.delimiters(Delimiters.NewLine))
    if (mot == "bien") {
        music.play(music.tonePlayable(1319, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
        basic.showIcon(IconNames.Yes)
    } else if (mot == "mal") {
        music.play(music.tonePlayable(131, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
        basic.showIcon(IconNames.No)
    } else {
        basic.showString(mot)
    }
})
```

</details>

À la fin du tutoriel, télécharge, puis ferme l'onglet.

## 4. Joue avec ta manette

**Ce que tu vas obtenir :** ton héros suit ta manette, et ta manette réagit à ton jeu.

> [!CAUTION] Ferme tous les onglets MakeCode micro:bit
> Un onglet ouvert garde la liaison série et vole des lettres aux mots de ta manette.

1. Ouvre **[la page relais](../../../relais/index.html)** dans Chrome.
2. Colle le lien de ton jeu, puis clique sur **Charger**.
3. Clique sur **Connecter la manette** et choisis ton micro:bit dans la liste.

> [!TIP] Ça marche si…
> Ton héros monte et descend avec ta manette, et ta manette affiche ✔ à chaque ennemi détruit et tes vies quand tu es touché. Trop sensible, ou pas assez ? Rouvre le projet **Ta manette** dans MakeCode, change tes seuils, télécharge, et referme l'onglet.

> [!IMPORTANT] Point de contrôle
> Joue une partie devant l'animateur, avec ta manette.

## Va plus loin

- **Un bip à chaque tir.** Dans ton jeu, ajoute `manette réagir bip` dans `quand bouton A est appuyé`. Dans ta manette, ajoute un `sinon si mot = "bip"` qui joue une note courte.
- **Tes sons à toi.** Change les tonalités et les icônes de ta manette : chaque manette réagit à sa façon aux mêmes mots.
