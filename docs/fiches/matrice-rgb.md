# La matrice de LED RGB

64 LED de couleur sur une carte de 8 × 8, pilotées par un seul fil de données. Chacune porte un numéro, et chacune peut prendre n'importe quelle couleur.

<span class="todo-media">[photo : la matrice, face LED et face arrière avec les broches repérées]</span>

## Les trois fils

| Broche | Va sur |
|---|---|
| `VCC` | Le `+` du pack d'accus |
| `GND` | Le `−` du pack d'accus, **et** le `GND` du micro:bit |
| `DIN` | Une broche du micro:bit, `P1` sur la lampe |

La matrice prend son énergie au pack. Le micro:bit ne lui envoie que le signal.

> [!CAUTION] Lis la sérigraphie
> L'ordre des broches change d'un modèle à l'autre. Le signal entre par `DIN`, pas par `DOUT`.

→ [Câbler un circuit : la masse commune](cabler-un-circuit.md#la-masse-commune)

## L'extension

Dans MakeCode : **Extensions** → cherche `neopixel`. Une catégorie **Neopixel** apparaît.

<span class="todo-media">[capture : la catégorie Neopixel dépliée]</span>

Le premier bloc, dans `au démarrage`, dit où est branchée la matrice et combien elle a de LED : `P1`, `64`.

## La luminosité

> [!CAUTION] Règle-la en premier
> 64 LED en blanc à fond tirent près de 4 ampères. Les accus ne suivent pas : la carte redémarre, les couleurs deviennent fausses. `régler luminosité` à **50** sur 255, dans `au démarrage`, avant toute couleur.

À 50, la lumière est aussi plus douce, et c'est ce qu'on veut d'une lampe.

Des couleurs fausses ou un scintillement en fin de séance : les accus faiblissent.

## Le numéro d'une LED

Les LED sont numérotées de `0` à `63`, ligne par ligne.

```
index = ligne × 8 + colonne
```

La LED de la ligne 4, colonne 5 est la n° `37`. Lignes et colonnes commencent à `0`.

<span class="todo-media">[schéma : la grille 8 × 8 avec les numéros de ligne, de colonne, et quelques index]</span>

> [!NOTE] Comme l'écran du micro:bit
> L'écran 5 × 5 est aussi une matrice : on y allume un point par `x` et `y`. Ici, on calcule un numéro.

## La couleur

Trois nombres, de 0 à 255 : **rouge**, **vert**, **bleu**.

| Couleur | Rouge | Vert | Bleu |
|---|---|---|---|
| Rouge | 255 | 0 | 0 |
| Violet | 255 | 0 | 255 |
| Orange | 255 | 100 | 0 |
| Blanc chaud | 255 | 180 | 100 |

## Préparer, puis afficher

`set pixel color` prépare la couleur d'une LED. **Rien ne change sur la matrice avant `afficher`.** On prépare toutes les LED, puis on affiche une fois.

→ [Prendre en main MakeCode](makecode-prise-en-main.md) · [Déboguer](deboguer.md)
