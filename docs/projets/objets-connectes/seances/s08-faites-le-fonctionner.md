# Séance 8 — Faites fonctionner votre produit et montrez ses données

> [!NOTE] Nouveau concept : la puissance et la portée
> Plus un micro:bit émet fort, plus il porte loin, et plus il vide ses accus. Sur le tableau de bord, les barres de chaque carte montrent la force du signal reçu par le pont. L'animateur le montre en début de séance.
>
> → [La puissance et la portée](../../../fiches/makecode-prise-en-main.md#la-puissance-et-la-portee)

1. **[Câblez](#1-cablez)** : selon votre schéma, alimentation comprise.
2. **[Programmez et émettez](#2-programmez-et-emettez)** : votre produit mesure, décide, agit, et envoie ses mesures.
3. **[Sur le tableau de bord](#3-sur-le-tableau-de-bord)** : votre micro:bit en ligne, ses mesures affichées, sa puissance réglée.

## 1. Câblez

**Ce que vous allez obtenir :** votre produit câblé, vérifié avant la première mise sous tension.

<span class="todo-media">[photo : un schéma de câblage dessiné à la main, composants, broches, alimentation]</span>

Avant de toucher un fil, dessinez le schéma : chaque composant, sa broche, son alimentation, la masse commune.

→ [Le schéma de câblage](../../../fiches/cabler-un-circuit.md#le-schema-de-cablage)

| Votre produit | Son alimentation |
|---|---|
| Fixe, près d'une prise | Adaptateur secteur USB 5 V |
| Mobile, ou loin d'une prise | Boîtier d'accus |

> [!CAUTION] Jamais les deux à la fois
> Secteur **ou** accus, pas les deux branchés ensemble. Un moteur ou un servomoteur passe toujours par la carte DFR0548, jamais par une broche du micro:bit.

Un fil par fonction, étiqueté.

<span class="todo-media">[photo : un câblage propre, fils étiquetés]</span>

> [!IMPORTANT] Point de contrôle
> Faites vérifier votre câblage contre votre schéma avant la première mise sous tension.

## 2. Programmez et émettez

**Ce que vous allez obtenir :** votre produit mesure, décide, agit, et envoie une mesure toutes les 5 à 10 secondes.

Comme la lampe : la mesure, la décision avec un seuil, et un état si votre produit déclenche une alerte, puis l'action.

Pour émettre, comme vos lampes en séance 5 : la bande `40`, `radio régler le numéro de série de transmission`, puis une clé par mesure, toutes les 5 à 10 secondes. Par exemple, pour une température :

```blocks
radio.setFrequencyBand(40)
radio.setTransmitSerialNumber(true)
basic.forever(function () {
    radio.sendValue("temp", input.temperature())
    basic.pause(5000)
})
```

Choisissez vos clés dans les clés connues : le tableau de bord saura comment les afficher.

→ [La langue commune](../catalogue.md#la-langue-commune)

> [!TIP] Économisez les accus
> Pas d'émission sans pause. Écran éteint quand il n'a rien à dire.

## 3. Sur le tableau de bord

**Ce que vous allez obtenir :**

<figure class="screenshot" markdown>
![Le tableau de bord : un bloc par micro:bit en ligne, avec son nom et ses mesures en jauge, en courbe ou en voyant, et à droite le journal des messages reçus](../../../assets/objets-connectes-s06/20-tableau-de-bord.png)
</figure>

Votre micro:bit apparaît dès son premier message. Donnez-lui le nom de votre produit. L'affichage ne convient pas à votre mesure ? Changez de clé.

> [!TIP] Il n'apparaît pas ?
> `radio régler le numéro de série de transmission` est-il dans `au démarrage` ? La bande est-elle la `40` ?

### Réglez la puissance

`radio définir puissance de transmission`, dans **Radio**, dans `au démarrage` : de `0` à `7`. Essayez `7`, puis `1`, et regardez les barres de votre carte.

Gardez la puissance la plus basse qui laisse **au moins deux barres**. Vous la vérifierez depuis l'emplacement, en séance 9.

## Va plus loin

- **Un interrupteur sur le tableau de bord.** Comme pour vos lampes : une clé `inter` suivie de la lettre de votre équipe (`interA`) s'affiche comme un interrupteur, et votre produit l'écoute avec `quand une donnée est reçue par radio`. Il doit fonctionner sans : l'ordre ne fait que forcer un état.
