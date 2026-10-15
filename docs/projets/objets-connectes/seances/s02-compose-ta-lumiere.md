# Séance 2 — Compose la lumière de ta lampe

1. **[Termine ta lampe](#1-termine-ta-lampe)** : les pistes de cuivre, les vis, le micro:bit et la matrice en place.
2. **[Allume-la et dessine ton image](#2-allume-la-et-dessine-ton-image)** : ton image sur la matrice.

## 1. Termine ta lampe

**Ce que tu vas obtenir :**

<video class="portrait" controls playsinline preload="metadata" src="../../../../assets/objets-connectes-s02/video-coeur.mp4"></video>

Tout le câblage de ta lampe tient sur ce schéma. Garde-le sous les yeux pendant le montage.

<figure class="plan" markdown>
![Schéma du montage : le + du pack, trois accus et une fausse pile, va sur V de la matrice ; P1 va sur DI par l'écrou 1 ; P2 va à la bande bouton par sa piste et sa vis ; GND va à la bande masse par sa piste, et l'écrou GND réunit G de la matrice et le − du pack, c'est la masse commune ; le micro:bit est alimenté par son boîtier 2 × AAA](../../../assets/objets-connectes-s02/03-schema-montage.png)
</figure>

### Les pistes et les vis

> [!NOTE] Pourquoi des pistes de cuivre ?
> Le premier prototype de la lampe tenait avec 9 câbles, qui se décrochaient et s'emmêlaient. Les pistes et les vis font le même travail : il ne reste que 3 câbles, ceux de la matrice.

<div class="photo-row" markdown>

<figure markdown>
![Avant : le premier prototype, micro:bit et pack d'accus noyés sous les câbles à pinces](../../../assets/objets-connectes-s02/00-avant-neuf-cables.jpg)
</figure>

<figure markdown>
![Après : la lampe montée, la matrice sur son montant, trois câbles seulement](../../../assets/objets-connectes-s02/14-apres-trois-cables.jpg)
</figure>

</div>

Colle les deux pistes de cuivre sur la face intérieure.

Avec la punaise, perce les cinq trous où passent les vis, à travers le cuivre et le carton : les deux trous des bandes, puis les trois anneaux du micro:bit, `2`, `1` et `GND`. Puis agrandis-les.

<figure markdown>
![Les deux pistes collées sur la face intérieure ; la punaise agrandit le trou au bout d'une piste](../../../assets/objets-connectes-s02/05-punaise-agrandit-trou.jpg)
</figure>

Une vis par trou, tête à l'extérieur. Pour le micro:bit, une entretoise entre la carte et le carton. À l'intérieur, une rondelle sur le cuivre, puis l'écrou, serré.

<figure markdown>
![La face intérieure : chaque piste tenue par une vis, une rondelle et un écrou à chaque bout](../../../assets/objets-connectes-s02/04-pistes-interieures.jpg)
</figure>

<div class="photo-row" markdown>

<figure markdown>
![La face extérieure du montant : deux entretoises en plastique vissées, prêtes à recevoir le micro:bit](../../../assets/objets-connectes-s02/06-entretoises.jpg)
<figcaption>Les entretoises : de petits tubes qui tiennent le micro:bit à distance du carton.</figcaption>
</figure>

<figure markdown>
![La face extérieure : les deux bandes de cuivre et le micro:bit, tenus par leurs vis](../../../assets/objets-connectes-s02/07-microbit-visse.jpg)
</figure>

</div>

Chaque bande du dessus est maintenant reliée à son anneau du micro:bit : la bande `bouton` à `P2`, la bande `masse` à `GND`.

Vérifie-le au multimètre, en mode continuité : une pointe sur la vis d'une bande, l'autre sur l'anneau du micro:bit. Il bipe : le courant passe. Fais-le pour les deux bandes.

<figure markdown>
![Le multimètre en mode continuité, une pointe sur la vis d'une bande, l'autre sur l'anneau du micro:bit](../../../assets/objets-connectes-s02/08-continuite-multimetre.jpg)
</figure>

> [!IMPORTANT] Point de contrôle
> Refais ta vérification devant l'animateur : deux bips, un par bande.

### La matrice et le pack

Trois broches, au dos de la matrice, et un câble Dupont femelle / pince crocodile sur chacune :

<figure markdown>
![Le dos de la matrice 8 × 8, avec ses broches repérées DI, G, V, et trois câbles Dupont branchés : jaune sur DI, noir sur G, rouge sur V](../../../assets/objets-connectes-s02/02-dos-matrice-broches.jpg)
</figure>

D'abord, glisse le fil `−` du pack sous la rondelle de l'écrou de `GND`, et resserre. Puis les trois pinces :

1. `DI` sur l'écrou de l'anneau `1`.
2. `G` sur l'écrou de `GND` : la matrice, le pack et le micro:bit partagent la même masse.
3. `V` sur le fil `+` du pack.

<div class="photo-row" markdown>

<figure markdown>
![Le fil noir du pack glissé sous la rondelle de l'écrou GND](../../../assets/objets-connectes-s02/10-moins-du-pack.jpg)
</figure>

<figure markdown>
![La face intérieure : une pince jaune sur l'écrou de l'anneau 1, une pince noire sur l'écrou de GND](../../../assets/objets-connectes-s02/09-pinces-ecrous.jpg)
</figure>

</div>

Le pack reçoit **trois accus et une fausse pile** : un cylindre imprimé en 3D, entouré d'une bande de cuivre d'un bout à l'autre. Elle laisse passer le courant sans en fournir. Avec quatre accus, la matrice ne comprend plus le signal du micro:bit quand il est sur piles.

<div class="photo-row" markdown>

<figure markdown>
![La fausse pile : un cylindre jaune imprimé en 3D, une bande de cuivre collée dans sa rainure](../../../assets/objets-connectes-s02/15-fausse-pile.jpg)
</figure>

<figure markdown>
![Le pack ouvert : trois accus et la fausse pile jaune](../../../assets/objets-connectes-s02/16-pack-trois-accus.jpg)
</figure>

</div>

→ [Pourquoi trois accus](../../../fiches/matrice-rgb.md#trois-accus-et-une-fausse-pile)

**Ne mets pas encore les piles dans le pack.**

> [!CAUTION] Les fils du pack
> Le fil `+` et le fil `−` du pack ne se touchent jamais.

La matrice se pose sur le second montant, tenue par un élastique. Le pack va à l'intérieur, sur la base. Le micro:bit reste à l'avant, **écran vers la pièce** : la séance 3 en a besoin.

<figure markdown>
![La matrice tenue sur le montant par un élastique](../../../assets/objets-connectes-s02/12-matrice-elastique.jpg)
</figure>

→ [La matrice de LED RGB](../../../fiches/matrice-rgb.md) · [La masse commune](../../../fiches/cabler-un-circuit.md#la-masse-commune)

## 2. Allume-la et dessine ton image

**Ce que tu vas obtenir :** ton image sur la matrice.

<figure markdown>
![La lampe allumée affiche un visage souriant en blanc ; derrière, MakeCode montre la même grille dans le bloc set NeoPixel 8x8](../../../assets/objets-connectes-s02/03-matrice-visage.jpg)
</figure>

Dans ton projet `lampe` : **Extensions** → colle l'adresse `https://github.com/arbona-robin/pxt-neopixel-matrix-extension` → clique sur la carte **neopixel-extended**.

<figure class="screenshot" markdown>
![La fenêtre Extensions de MakeCode : l'adresse de l'extension collée dans la recherche, et la carte neopixel-extended trouvée](../../../assets/objets-connectes-s02/20-extension-neopixel.png)
</figure>

Les blocs sont dans la catégorie **neopixel-extended**, en anglais : cherche-les tels qu'ils sont écrits. Dans `au démarrage` : la matrice, sa luminosité, et `set NeoPixel matrix layout to row by row`, parce que ta matrice est câblée ligne par ligne.

```blocks
let strip = neopixelExtended.create(DigitalPin.P1, 64, neopixelExtended.Format.RGB)
strip.setBrightness(50)
strip.setMatrixLayout(neopixelExtended.MatrixLayout.RowByRow)
```

> [!IMPORTANT] Point de contrôle
> `set brightness` à **50** : à fond, la matrice tire trop de courant et la carte redémarre. Fais vérifier ton câblage et ta luminosité, puis mets les piles dans le pack.

**À toi : dessine ton image.** Un motif, une icône, un visage. À la suite, `set NeoPixel 8x8` : une grille de 8 × 8, une couleur par case. Puis `show changes`.

<details markdown>
<summary>La solution</summary>

Un exemple : un visage.

```blocks
let strip = neopixelExtended.create(DigitalPin.P1, 64, neopixelExtended.Format.RGB)
strip.setBrightness(50)
strip.setMatrixLayout(neopixelExtended.MatrixLayout.RowByRow)
strip.setMatrix64(
    neopixelExtended.rowOf8(0x000000, 0x000000, 0xffff00, 0xffff00, 0xffff00, 0xffff00, 0x000000, 0x000000),
    neopixelExtended.rowOf8(0x000000, 0xffff00, 0x000000, 0x000000, 0x000000, 0x000000, 0xffff00, 0x000000),
    neopixelExtended.rowOf8(0xffff00, 0x000000, 0xffff00, 0x000000, 0x000000, 0xffff00, 0x000000, 0xffff00),
    neopixelExtended.rowOf8(0xffff00, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xffff00),
    neopixelExtended.rowOf8(0xffff00, 0x000000, 0xffff00, 0x000000, 0x000000, 0xffff00, 0x000000, 0xffff00),
    neopixelExtended.rowOf8(0xffff00, 0x000000, 0x000000, 0xffff00, 0xffff00, 0x000000, 0x000000, 0xffff00),
    neopixelExtended.rowOf8(0x000000, 0xffff00, 0x000000, 0x000000, 0x000000, 0x000000, 0xffff00, 0x000000),
    neopixelExtended.rowOf8(0x000000, 0x000000, 0xffff00, 0xffff00, 0xffff00, 0xffff00, 0x000000, 0x000000)
)
strip.show()
```

Pour éteindre toutes les cases grises d'un coup : passe en **JavaScript**, ouvre « Rechercher et remplacer » (`Ctrl` + `H`), remplace `0x888888` par `0x000000`, puis reviens aux **Blocs**.

</details>

`set NeoPixel 8x8` prépare l'image : rien ne change sur la matrice avant `show changes`. Une case laissée en gris s'allume en gris ; pour l'éteindre, choisis le noir. Téléverse.

> [!TIP] Rien ne s'allume ?
> `DI` sur l'écrou de l'anneau `1` ? Le fil `−` du pack bien serré sous la rondelle de `GND` ?

## Va plus loin

- **Un cœur qui bat.** Quatre images dans `toujours`, 200 ms chacune : grand, moyen, petit, moyen. L'image intermédiaire rend le mouvement plus doux.
- **Un diffuseur.** Une simple feuille de papier devant la matrice : les 64 points se fondent en une seule lumière.
- **Crée ta propre animation.** Plusieurs images à la suite, chacune avec son `show changes` et sa pause.

<details markdown>
<summary>La solution du cœur</summary>

```blocks
basic.forever(function () {
    strip.setMatrix64(
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000),
        neopixelExtended.rowOf8(0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000),
        neopixelExtended.rowOf8(0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000)
    )
    strip.show()
    basic.pause(200)
    strip.setMatrix64(
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000)
    )
    strip.show()
    basic.pause(200)
    strip.setMatrix64(
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000)
    )
    strip.show()
    basic.pause(200)
    strip.setMatrix64(
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0xff0000, 0xff0000, 0x000000, 0x000000, 0x000000),
        neopixelExtended.rowOf8(0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000)
    )
    strip.show()
    basic.pause(200)
})
let strip: neopixelExtended.Strip = null
```

Une image intermédiaire rend le mouvement plus doux : le cœur se gonfle et se dégonfle, au lieu de sauter d'une taille à l'autre.

</details>
