# Séance 3 — Ta manette micro:bit

1. **[Ta manette envoie tes gestes](#1-ta-manette-envoie-tes-gestes)** : ton micro:bit envoie haut, bas et A.
2. **[Joue avec ta manette](#2-joue-avec-ta-manette)** : ton héros suit ta manette.
3. **[Ton jeu parle à ta manette](#3-ton-jeu-parle-a-ta-manette)** : ton jeu envoie bien, mal et tes vies.
4. **[Ta manette écoute ton jeu](#4-ta-manette-ecoute-ton-jeu)** : ta manette sonne, s'allume et affiche tes vies.

## 1. Ta manette envoie tes gestes

**Ce que tu vas obtenir :** ton micro:bit envoie `haut` quand tu l'inclines vers l'avant, `bas` vers l'arrière, et `A` quand tu appuies sur A.

### Regarde ton accéléromètre

**Regarde les chiffres avant de décider.** Nouveau projet MakeCode micro:bit, nommé `accelerometre`. Dans `toujours`, écris la valeur `y` de l'accéléromètre (avant, arrière).

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

Ces deux valeurs sont tes **seuils**.

### Programme ta manette

Ouvre **[le tutoriel de la manette](https://makecode.microbit.org/?lang=fr#tutorial:https://github.com/arbona-robin/tutoriels-microbit/manette)**, jusqu'à l'étape **Teste ta manette**.

> [!NOTE] La liaison série, deux fois
> Elle t'a d'abord montré les valeurs de ton accéléromètre dans MakeCode. Maintenant, elle transporte tes mots vers le jeu. Un seul programme peut l'utiliser à la fois.

<details markdown>
<summary>Bloqué ? Le programme de cette étape</summary>

```blocks
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
```

</details>

## 2. Joue avec ta manette

**Ce que tu vas obtenir :** ton héros monte et descend quand tu inclines ta manette, et tire quand tu appuies sur A.

> [!CAUTION] Déconnecte MakeCode
> Dans l'onglet du tutoriel : **⋯** à côté de **Télécharger**, puis **Déconnecter**. Sinon, MakeCode garde la liaison série et vole des lettres aux mots de ta manette.

1. Ouvre **[la page relais](../../../relais/index.html)** dans Chrome.
2. Colle le lien de ton jeu de la séance 2, puis clique sur **Charger**.
3. Clique sur **Connecter la manette** et choisis ton micro:bit dans la liste.

> [!TIP] Ça marche si…
> Ton héros suit ta manette. Trop sensible, ou pas assez ? Change tes seuils dans le tutoriel.

## 3. Ton jeu parle à ta manette

**Ce que tu vas obtenir :** ton jeu envoie `bien` à chaque ennemi détruit, `mal` quand tu es touché, et le nombre de tes vies.

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

## 4. Ta manette écoute ton jeu

**Ce que tu vas obtenir :** ta manette joue un son et affiche une icône à chaque ennemi détruit et à chaque choc, et affiche tes vies.

Reviens dans l'onglet du tutoriel de la manette, et reprends après **Teste ta manette**.

- Un deuxième `toujours` écoute le jeu pendant que le premier envoie tes gestes.
- `série lire jusque nouvelle ligne` attend un mot et le range dans la variable `mot`.

<details markdown>
<summary>Bloqué ? Le programme complet de la manette</summary>

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

Télécharge, déconnecte MakeCode, puis colle le nouveau lien de ton jeu dans la page relais et rejoue.

> [!TIP] Ça marche si…
> Ta manette affiche ✔ à chaque ennemi détruit, et tes vies quand tu es touché.

> [!IMPORTANT] Point de contrôle
> Joue une partie devant l'animateur, avec ta manette.

## Va plus loin

- **Un bip à chaque tir.** Dans ton jeu, ajoute `manette réagir bip` dans `quand bouton A est appuyé`. Dans ta manette, ajoute un `sinon si mot = "bip"` qui joue une note courte.
- **Tes sons à toi.** Change les tonalités et les icônes de ta manette : chaque manette réagit à sa façon aux mêmes mots.
