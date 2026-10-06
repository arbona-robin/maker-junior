# Séance 2 — Compose la lumière de ta lampe

Ta lampe reçoit une matrice de 64 LED de couleur. Tu la câbles, tu choisis tes couleurs et tu composes une animation.

## 1. La matrice

<span class="todo-media">[photo : la matrice 8 × 8, face LED et face arrière avec ses broches DIN, VCC, GND]</span>

64 LED, et un seul fil de données. Chaque LED porte un **numéro**, de 0 à 63.

> [!NOTE] Une couleur, c'est trois nombres
> Rouge, vert, bleu, chacun de 0 à 255. `255, 0, 255` donne du violet.

→ [La matrice de LED RGB](../../../fiches/matrice-rgb.md)

## 2. Câble-la

La matrice prend son énergie au pack d'accus. Le micro:bit ne lui envoie que le signal.

<span class="todo-media">[photo : les deux bornes à levier, avec les fils du pack, de la matrice et du GND du micro:bit]</span>

1. Une borne pour le `+` : le fil rouge du pack et `VCC`.
2. Une borne pour le `−` : le fil noir du pack, `GND`, et un fil vers la broche `GND` du micro:bit.
3. `DIN` sur `P1`, par un câble à pinces. `P2` reste à ton bouton de cuivre.

**Ne branche pas encore le pack.**

> [!NOTE] La masse commune
> Le signal de `P1` se mesure par rapport au `GND` du micro:bit. Si la matrice ne partage pas ce `GND`, elle reçoit un signal sans référence.

→ [Câbler un circuit](../../../fiches/cabler-un-circuit.md#la-masse-commune)

## 3. L'extension

Dans ton projet `lampe` : **Extensions** → cherche `neopixel` → clique dessus.

<span class="todo-media">[capture : la fenêtre Extensions, avec la carte neopixel]</span>

## 4. Le premier programme

<span class="todo-media">[capture : au démarrage → définir bande à NeoPixel at pin P1 with 64 leds, bande régler luminosité 50, bande afficher la couleur rouge]</span>

> [!CAUTION] La luminosité d'abord
> `régler luminosité` à **50** dans le premier programme, avant de brancher le pack. À fond, la matrice tire trop de courant, et la carte redémarre.

Téléverse. Puis branche le pack.

> [!IMPORTANT] Point de contrôle
> Fais vérifier ton câblage et ta luminosité avant de brancher le pack.

> [!TIP] Rien ne s'allume ?
> `DIN`, pas `DOUT`. Puis le fil vers `D`.

## 5. Une LED choisie

Chaque LED a un numéro. Sur la ligne 4, colonne 5, c'est la LED **37** :

```
index = ligne × 8 + colonne
```

<span class="todo-media">[photo ou schéma : la matrice avec les numéros de ligne et de colonne, la LED 37 allumée]</span>

**À toi.** Allume la LED de la ligne 2, colonne 6, en violet. Les autres restent éteintes.

<details markdown>
<summary>La solution</summary>

`2 × 8 + 6 = 22`.

<span class="todo-media">[capture : bande effacer, bande set pixel color at 22 to violet, bande afficher]</span>

</details>

> [!NOTE] `afficher`
> `set pixel color` prépare la couleur. Rien ne change sur la matrice avant `bande afficher`.

## 6. Une ligne entière

**À toi.** Allume toute la ligne 3 en bleu, avec une boucle sur la colonne.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : pour colonne de 0 à 7 → set pixel color at 3 × 8 + colonne to bleu, puis bande afficher]</span>

</details>

## 7. Ton ambiance

Compose la lumière de ta lampe. Quelques idées :

- toutes les LED d'une couleur choisie
- un dégradé
- une respiration lente : la luminosité qui monte et descend
- un motif dessiné

<span class="todo-media">[photo : trois ambiances différentes]</span>

Garde ton ambiance dans ton programme.

## 8. La matrice sur la lampe

<span class="todo-media">[photo : la matrice tenue sur la lampe par deux élastiques, papier calque devant]</span>

Deux élastiques tiennent la matrice. Le papier calque devant adoucit la lumière.

Le micro:bit reste à l'avant, **écran vers la pièce**.

---

## Ce que tu dois avoir à la fin

- [ ] La matrice câblée, masse commune comprise
- [ ] La luminosité réglée dans le programme
- [ ] Ta couleur et ton animation
- [ ] La matrice fixée sur la lampe
- [ ] Ton [carnet de bord](../../../carnet-de-bord/objets-connectes-s02.md) rempli

## Avant de partir

Débranche le pack d'une borne. Lampe dans ton bac, accus en charge.
