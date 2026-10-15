# Séance 5 — Fais parler les lampes entre elles

1. **[Le message pour tous](#1-le-message-pour-tous)** : un appui, et toutes les lampes s'allument.
2. **[La vague, avec un chef](#2-la-vague-avec-un-chef)** : le chef appelle les lampes une par une.
3. **[La vague, en relais](#3-la-vague-en-relais)** : chaque lampe passe le tour à la suivante.

## 1. Le message pour tous

**Ce que tu vas obtenir :** tu appuies sur `A`, toutes les lampes de la salle s'allument ; sur `B`, elles s'éteignent.

Accroche ton emblème à la lampe, par un élastique dans son trou.

<span class="todo-media">[photo : l'emblème imprimé accroché à la lampe par un élastique]</span>

L'animateur te donne un numéro, de 1 à 12. Colle-le sur ta lampe.

Duplique ton projet `lampe` en `lampe-radio`, et vide le bloc `toujours` : ton ambiance reste, le mode nuit s'en va.

Toutes les lampes sont sur la **bande 40** : chacune entend tous les messages. Dans `au démarrage`, la bande, dans **Radio**, et ton numéro dans une variable :

```blocks
radio.setFrequencyBand(40)
numero = 7
```

**À toi.** Bouton `A` : envoie `tous` = `1`. Bouton `B` : envoie `tous` = `0`. Quand ta lampe reçoit `tous`, elle allume son ambiance ou s'éteint. Il te faut `envoyer la valeur … = …` et `quand une donnée est reçue par radio`, dans **Radio**.

<details markdown>
<summary>La solution</summary>

```blocks
input.onButtonPressed(Button.A, function () {
    radio.sendValue("tous", 1)
})
input.onButtonPressed(Button.B, function () {
    radio.sendValue("tous", 0)
})
radio.onReceivedValue(function (name, value) {
    if (name == "tous") {
        if (value == 1) {
            strip.setColor(0xff8c00)
            strip.show()
        } else {
            strip.clear()
            strip.show()
        }
    }
})
let strip: neopixelExtended.Strip = null
```

</details>

→ [Envoyer, recevoir](../../../fiches/makecode-prise-en-main.md#envoyer-recevoir)

## 2. La vague, avec un chef

**Ce que tu vas obtenir :** les lampes s'allument l'une après l'autre, appelées par le micro:bit de l'animateur.

Une seule clé : `tour`. Sa valeur est le numéro de la lampe qui s'allume. Toutes les lampes entendent `tour` = `7`, une seule réagit : la 7. L'adresse est dans la valeur.

**À toi.** Quand ta lampe reçoit `tour` = ton numéro, elle s'allume 1 seconde, puis s'éteint.

<details markdown>
<summary>La solution</summary>

```blocks
radio.onReceivedValue(function (name, value) {
    if (name == "tour" && value == numero) {
        strip.setColor(0xff8c00)
        strip.show()
        basic.pause(1000)
        strip.clear()
        strip.show()
    }
})
let numero = 0
let strip: neopixelExtended.Strip = null
```

</details>

Ici, la pause est dans le gestionnaire : d'habitude à éviter, elle passe parce qu'un seul message arrive à la fois.

Le chef envoie `tour` = 1, puis 2, puis 3…

<span class="todo-media">[vidéo : la vague menée par le chef, six lampes]</span>

## 3. La vague, en relais

**Ce que tu vas obtenir :** la vague passe de lampe en lampe, sans chef.

**À toi.** Après ta seconde allumée, envoie `tour` = ton numéro + 1. La première lampe démarre au bouton `A`.

<details markdown>
<summary>La solution</summary>

```blocks
radio.onReceivedValue(function (name, value) {
    if (name == "tour" && value == numero) {
        strip.setColor(0xff8c00)
        strip.show()
        basic.pause(1000)
        strip.clear()
        strip.show()
        radio.sendValue("tour", numero + 1)
    }
})
let numero = 0
let strip: neopixelExtended.Strip = null
```

</details>

Essayez à trois ou quatre, numéros qui se suivent. Puis éteignez une lampe au milieu : que se passe-t-il ? Et avec le chef, que se passait-il ?

> [!IMPORTANT] Point de contrôle
> Ta lampe réagit à `tous` et à son tour, et la vague passe dans ton groupe.

Pour finir : les douze lampes, lumière éteinte.

## Va plus loin

- **Réparer la chaîne.** Après avoir passé le tour, attends 2 secondes. Si tu n'as pas entendu le `tour` suivant, envoie `tour` = ton numéro + 2.
- **Une couleur pour une seule lampe.** L'adresse dans la clé : `lampe7` veut dire « pour la lampe 7 ». À la réception, compare `nom` à `lampe` suivi de ton numéro, avec `joindre` (**Texte**). Une clé fait 8 caractères au plus.
