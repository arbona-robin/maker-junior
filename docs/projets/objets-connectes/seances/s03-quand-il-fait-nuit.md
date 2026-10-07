# Séance 3 — Fais-la s'allumer quand il fait nuit

Ta lampe mesure la lumière de la pièce. Tu choisis à partir de quand il fait nuit, et elle s'allume toute seule.

## 1. Le capteur de lumière

Le micro:bit mesure la lumière avec son écran. La valeur va de `0` (noir) à `255` (pleine lumière).

> [!NOTE] Un capteur donne un nombre
> Il ne dit pas « il fait nuit ». C'est toi qui décides à partir de quel nombre il fait nuit.

→ [Prendre en main MakeCode : le capteur de lumière](../../../fiches/makecode-prise-en-main.md#le-capteur-de-lumiere)

## 2. Regarde les valeurs

Nouveau projet : `lumiere`. Dans `toujours` :

<span class="todo-media">[capture : toujours → série écrire valeur "lumiere" = niveau d'intensité lumineuse, pause 200 ms]</span>

Téléverse, USB branché, puis **Afficher données Appareil**.

<span class="todo-media">[capture : la courbe de la lumière dans Afficher données, avec un creux quand la main couvre la carte]</span>

> [!CAUTION] L'écran reste éteint
> Le capteur, c'est l'écran. Une icône affichée pendant la mesure fausse la valeur.

## 3. Relève tes valeurs

Note au carnet la valeur :

- dans la salle éclairée
- la main au-dessus de la carte
- près de la fenêtre
- lumière de la salle éteinte

## 4. Choisis ton seuil

Ton seuil est entre la pénombre et la salle éclairée. Il dépend de l'endroit où tu poseras ta lampe : le tien n'est pas celui du voisin.

Note-le au carnet.

## 5. La décision

Retour dans ton projet `lampe`.

**À toi.** Dans `toujours` : si la lumière est sous ton seuil, affiche ton ambiance. Sinon, éteins la matrice.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : toujours → si niveau d'intensité lumineuse < seuil alors ambiance, sinon strip clear all colors et strip show changes]</span>

</details>

Couvre la carte. Regarde ton animation.

## 6. Le piège

Ton animation redémarre au début à chaque tour de `toujours`. La lampe hoquette.

> [!NOTE] L'état
> La lampe doit se souvenir si elle est allumée ou éteinte. Une variable, `allumee`, qui vaut `0` ou `1`, garde cet **état**.

On ne s'allume que si :

- il fait sombre
- **et** la lampe était éteinte.

Puis `allumee` passe à `1`. Même chose dans l'autre sens.

**À toi.** Ajoute la variable `allumee` à ton programme.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : si lumière < seuil et allumee = 0 alors ambiance, définir allumee à 1 ; sinon si lumière > seuil et allumee = 1 alors éteindre, définir allumee à 0]</span>

Le même raisonnement sert à toutes les alertes : on s'arme, on se désarme.

→ [Prendre en main MakeCode : ne réagir qu'au changement](../../../fiches/makecode-prise-en-main.md#4-ne-reagis-quau-changement)

</details>

## 7. Elle s'allume, elle s'éteint, elle s'allume…

Si ta matrice éclaire l'écran du micro:bit, la lampe se voit elle-même : elle s'allume, mesure sa propre lumière, s'éteint, et recommence.

<span class="todo-media">[photo : la lampe, micro:bit à l'avant, écran tourné vers la pièce]</span>

L'écran du micro:bit regarde la pièce, pas la lampe. Masque la lumière qui passe vers lui si besoin.

> [!IMPORTANT] Point de contrôle
> Couvre ta lampe : elle s'allume une fois. Découvre-la : elle s'éteint une fois.

## 8. Va plus loin

<details markdown>
<summary>Deux seuils au lieu d'un</summary>

À la limite, la valeur oscille et la lampe clignote. Avec un seuil pour s'allumer (`40`) et un autre pour s'éteindre (`60`), entre les deux elle ne bouge pas. Ça s'appelle l'**hystérésis**.

</details>

<details markdown>
<summary>Un réveil en douceur</summary>

Fais monter la luminosité petit à petit à l'allumage, avec un son du haut-parleur de la carte.

</details>

---

## Ce que tu dois avoir à la fin

- [ ] Tes valeurs et ton seuil notés au carnet
- [ ] La lampe qui s'allume seule dans le noir, et s'éteint à la lumière
- [ ] La variable `allumee` : plus de hoquet
- [ ] Ton [carnet de bord](../../../carnet-de-bord/objets-connectes-s03.md) rempli

## Avant de partir

Lampe dans ton bac, accus en charge.
