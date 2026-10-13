# Séance 3 — Fais-la s'allumer quand il fait nuit

1. **[Regarde les valeurs](#1-regarde-les-valeurs)** : tu sais ce que mesure ta carte, du plein jour au noir, et tu choisis ton seuil.
2. **[La décision](#2-la-decision)** : sous ton seuil, la lampe s'allume ; au-dessus, elle s'éteint.
3. **[Une seule fois](#3-une-seule-fois)** : couverte, la lampe s'allume une fois, sans hoqueter.

## 1. Regarde les valeurs

**Ce que tu vas obtenir :** tes valeurs, de la salle éclairée au noir, et ton seuil.

Le micro:bit mesure la lumière avec **son écran** : `niveau d'intensité lumineuse`, dans **Entrée**, de `0` (noir) à `255` (pleine lumière).

Nouveau projet : `lumiere`. Dans `toujours` :

```blocks
basic.forever(function () {
    serial.writeValue("lumiere", input.lightLevel())
    basic.pause(200)
})
```

Téléverse, USB branché, puis **Afficher données Appareil**.

<span class="todo-media">[capture : la courbe de la lumière dans Afficher données, avec un creux quand la main couvre la carte]</span>

> [!CAUTION] L'écran reste éteint
> Le capteur, c'est l'écran. Une icône affichée pendant la mesure fausse la valeur.

Remplis ce tableau :

| Où | Valeur |
|---|---|
| Salle éclairée | |
| Main au-dessus de la carte | |
| Près de la fenêtre | |
| Lumière de la salle éteinte | |

Ton seuil est entre la pénombre et la salle éclairée. Il dépend de l'endroit où tu poseras ta lampe : le tien n'est pas celui du voisin.

→ [Le capteur de lumière](../../../fiches/makecode-prise-en-main.md#le-capteur-de-lumiere)

## 2. La décision

**Ce que tu vas obtenir :** tu couvres la carte, la matrice s'allume ; tu la découvres, elle s'éteint.

Retour dans ton projet `lampe`.

**À toi.** Dans `toujours` : si la lumière est sous ton seuil, allume ton ambiance. Sinon, éteins la matrice avec `clear all colors` et `show changes`.

<details markdown>
<summary>La solution</summary>

```blocks
basic.forever(function () {
    if (input.lightLevel() < 40) {
        strip.setColor(0xff8000)
        strip.show()
    } else {
        strip.clear()
        strip.show()
    }
})
let strip: neopixelExtended.Strip = null
```

`40` est le seuil de ce montage. Prends le tien.

</details>

## 3. Une seule fois

**Ce que tu vas obtenir :** couverte, ta lampe s'allume une fois ; découverte, elle s'éteint une fois.

Si ton ambiance est une animation, elle redémarre au début à chaque tour de `toujours` : la lampe hoquette. Il faut qu'elle se souvienne si elle est déjà allumée.

Une variable, `allumee`, qui vaut `0` ou `1`, garde cet **état**. La lampe ne s'allume que s'il fait sombre **et** qu'elle était éteinte ; puis `allumee` passe à `1`. Même chose dans l'autre sens.

**À toi.** Ajoute la variable `allumee` à ton programme. Une variable se crée dans **Variables** → **Créer une variable…**.

<details markdown>
<summary>La solution</summary>

```blocks
basic.forever(function () {
    if (input.lightLevel() < 40 && allumee == 0) {
        strip.setColor(0xff8000)
        strip.show()
        allumee = 1
    } else if (input.lightLevel() > 40 && allumee == 1) {
        strip.clear()
        strip.show()
        allumee = 0
    }
})
let allumee = 0
let strip: neopixelExtended.Strip = null
```

→ [Ne réagis qu'au changement](../../../fiches/makecode-prise-en-main.md#4-ne-reagis-quau-changement)

</details>

Si ta matrice éclaire l'écran du micro:bit, la lampe se voit elle-même : elle s'allume, mesure sa propre lumière, s'éteint, et recommence. L'écran du micro:bit regarde la pièce, pas la lampe.

<span class="todo-media">[photo : la lampe, micro:bit à l'avant, écran tourné vers la pièce]</span>

> [!IMPORTANT] Point de contrôle
> Couvre ta lampe : elle s'allume une fois. Découvre-la : elle s'éteint une fois.

## Va plus loin

- **Deux seuils.** À la limite, la valeur oscille et la lampe clignote. Un seuil pour s'allumer (`40`), un autre pour s'éteindre (`60`) : entre les deux, elle ne bouge pas.
- **Un réveil en douceur.** La luminosité monte petit à petit à l'allumage, avec un son.
