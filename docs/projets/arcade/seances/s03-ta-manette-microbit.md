# Séance 3 — Ta manette micro:bit

1. **[Programme ta manette](#1-programme-ta-manette)** : ton micro:bit envoie haut, bas et A, et réagit aux mots du jeu.
2. **[Ton jeu parle à ta manette](#2-ton-jeu-parle-a-ta-manette)** : ton jeu envoie bien, mal et tes vies.
3. **[Joue avec ta manette](#3-joue-avec-ta-manette)** : tu joues à ton jeu avec ton micro:bit en main.

## 1. Programme ta manette

**Ce que tu vas obtenir :** ton micro:bit envoie un mot à chaque geste (haut, bas, A), et joue un son ou affiche une icône pour chaque mot reçu du jeu.

Dans Chrome, ouvre **[le tutoriel de la manette](https://makecode.microbit.org/?lang=fr#tutorial:https://github.com/arbona-robin/tutoriels-microbit/manette)**.

- Ta manette et ton jeu se parlent par **mots**, un par ligne : `haut`, `bas`, `A` de la manette vers le jeu, `bien`, `mal` et un chiffre du jeu vers la manette.
- Les blocs `série` sont dans **Avancé** → **Communication série**.
- Deux `toujours` tournent en même temps : l'un envoie tes gestes, l'autre écoute le jeu.

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

Branche ton micro:bit et clique sur **Télécharger**.

## 2. Ton jeu parle à ta manette

**Ce que tu vas obtenir :** ton jeu envoie `bien` à chaque ennemi détruit, `mal` quand tu es touché, et le nombre de tes vies.

Ouvre **[le parcours du jeu de tir](https://arcade.makecode.com/--skillmap?lang=fr#github:arbona-robin/tutoriels-arcade/jeu-de-tir)**, puis l'activité **Ta manette réagit**. Les blocs sont dans la catégorie **Manette**.

<details markdown>
<summary>Bloqué ? Le programme complet</summary>

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

À la fin, clique sur **Partager** et copie le lien de ton jeu.

## 3. Joue avec ta manette

**Ce que tu vas obtenir :** ton héros monte et descend quand tu inclines ta manette, et tire quand tu appuies sur A.

> [!CAUTION] Ferme l'onglet MakeCode micro:bit
> Tant qu'il est ouvert, il garde la liaison avec ton micro:bit et vole des lettres aux mots de ta manette.

1. Ouvre **[la page relais](../../../relais/index.html)** dans Chrome.
2. Colle le lien de ton jeu, puis clique sur **Charger**.
3. Clique sur **Connecter la manette** et choisis ton micro:bit dans la liste.

La page relais transmet les mots de ta manette à ton jeu, et ceux de ton jeu à ta manette. Le jeu se tait : les sons, c'est ta manette qui les joue.

> [!TIP] Ça marche si…
> Ton héros suit ta manette, et ta manette affiche ✔ à chaque ennemi détruit et tes vies quand tu es touché.

> [!IMPORTANT] Point de contrôle
> Joue une partie devant l'animateur, avec ta manette.

## Va plus loin

- **Un bip à chaque tir.** Dans ton jeu, ajoute `manette réagir bip` dans `quand bouton A est appuyé`. Dans ta manette, ajoute un `sinon si mot = "bip"` qui joue une note courte.
- **Tes sons à toi.** Change les tonalités et les icônes de ta manette : chaque manette réagit à sa façon aux mêmes mots.
