# Séance 8 — Faites fonctionner votre produit et montrez ses données

Vous câblez et programmez votre produit. Il envoie ses mesures, et elles s'affichent sur le tableau de bord.

## 1. Le schéma d'abord

<span class="todo-media">[photo : un schéma de câblage dessiné à la main, composants, broches, alimentation]</span>

Avant de toucher un fil, dessinez le schéma : chaque composant, sa broche, son alimentation, la masse commune.

→ [Câbler un circuit : le schéma de câblage](../../../fiches/cabler-un-circuit.md#le-schema-de-cablage)

## 2. L'alimentation

| Votre produit | Son alimentation |
|---|---|
| Fixe, près d'une prise | Adaptateur secteur USB 5 V |
| Mobile, ou loin d'une prise | Boîtier d'accus |

> [!CAUTION] Jamais les deux à la fois
> Secteur **ou** accus, pas les deux branchés ensemble.

Un moteur ou un servomoteur ne se branche jamais sur une broche du micro:bit : il passe par la carte DFR0548.

## 3. Câblez

<span class="todo-media">[photo : un câblage propre, fils étiquetés]</span>

Un fil par fonction. Étiquetez-les : dans trois semaines, vous ne vous en souviendrez plus.

> [!IMPORTANT] Point de contrôle
> Faites vérifier votre câblage contre votre schéma avant la première mise sous tension.

## 4. Programmez

Comme la lampe : mesurer, décider, agir.

1. La mesure, rangée dans une variable.
2. La décision, avec un seuil et un état si votre produit déclenche une alerte.
3. L'action.

## 5. Émettez

Dans `au démarrage` :

<span class="todo-media">[capture : au démarrage → radio régler la bande de fréquence 40, radio émettre le numéro de série vrai]</span>

Puis, toutes les 5 à 10 secondes, une clé par mesure :

```
envoyer la valeur "temp" = température (°C)
```

Choisissez vos clés dans les clés connues : le tableau de bord saura comment les afficher.

→ [Le catalogue : la langue commune](../catalogue.md#la-langue-commune)

> [!TIP] Économisez les accus
> Pas d'émission dans `toujours` sans pause. Écran éteint quand il n'a rien à dire.

## 6. Le tableau de bord

<span class="todo-media">[capture : le tableau de bord, un bloc par micro:bit, une jauge, un voyant, une courbe]</span>

Le **pont** est un micro:bit branché en USB à l'ordinateur de l'animateur. Il écoute la bande `40` et recopie chaque message vers le tableau de bord.

Votre micro:bit apparaît dès son premier message. Donnez-lui le nom de votre produit.

> [!TIP] Il n'apparaît pas ?
> `radio émettre le numéro de série` est-il dans `au démarrage` ? La bande est-elle la `40` ?

> [!NOTE] Le système et sa supervision
> Débranchez le pont : le tableau de bord se fige, mais vos produits continuent de fonctionner. Le tableau de bord regarde le système, il ne le commande pas.

L'affichage ne convient pas à votre mesure ? Changez de clé.

## 7. Le chemin de la donnée

Suivez votre mesure à voix haute : capteur, micro:bit, radio, pont, ordinateur, tableau de bord.

## 8. Va plus loin

<details markdown>
<summary>Un interrupteur sur le tableau de bord</summary>

Une clé `inter` suivie de la lettre de votre équipe (`interA`) s'affiche comme un interrupteur. Votre produit l'écoute aussi, avec `quand une donnée est reçue`. Il doit fonctionner sans : l'ordre ne fait que forcer un état.

→ [Le catalogue : la langue commune](../catalogue.md#la-langue-commune)

</details>

---

## Ce que vous devez avoir à la fin

- [ ] Le schéma de câblage
- [ ] Le produit câblé, qui mesure, décide et agit
- [ ] Votre micro:bit en ligne sur le tableau de bord, avec son nom
- [ ] Vos mesures affichées, toutes les 5 à 10 secondes
- [ ] Ton [carnet de bord](../../../carnet-de-bord/objets-connectes-s08.md) rempli

## Avant de partir

Produit éteint, accus en charge, schéma dans le bac de l'équipe.
