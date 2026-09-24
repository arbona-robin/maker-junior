# Séance 9 — Guidez votre rover vers une cible

La table ne donne plus d'ordres : elle envoie des mesures. C'est votre rover qui décide. Ce mode est un « pour aller plus loin » du cahier des charges.

## 1. Ce que la table envoie

| Clé | Valeur | Ce que c'est | Combien de fois par seconde |
|---|---|---|---|
| `cap` | de `-180` à `180` | de combien de degrés tourner pour viser la cible (négatif : à gauche) | 10 |
| `dist` | de `0` à `999` | la distance à la cible, en centimètres | 2 |

## 2. Jouez la table

Un de vous a les yeux bandés : c'est le rover. Un autre joue la table. Il ne dit que deux choses : le cap (« moins 40 ») et la distance (« 120 »).

<span class="todo-media">[photo : un jeune les yeux bandés, un autre qui annonce le cap et la distance]</span>

Après chaque essai, notez au carnet ce que le rover a fait :

- quand le cap était négatif ?
- quand il était proche de zéro ?
- quand la distance était petite ?

Ce sont les règles de votre programme.

## 3. Fabriquez une table de poche

Votre télécommande peut jouer la table le temps des essais : elle envoie `cap` et `dist` sur la bande `83`, avec votre groupe.

Deux façons de faire :

- un projet à part, `table-de-poche`, que tu téléverses le temps des essais ;
- un mode de plus dans ta télécommande. Les boutons `A` et `B` servent déjà : change de mode avec le logo.

→ [Changer de mode](../../../fiches/makecode-prise-en-main.md#changer-de-mode)

### À toi : le faux émetteur

L'inclinaison donne le cap. Les boutons `A` et `B` font baisser et monter la distance.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : toujours → envoyer la valeur cap = roulis ÷ 5 ; boutons A et B qui font varier dist et l'envoient]</span>

</details>

## 4. Écrivez le mode guidage

À partir de vos règles, écrivez ce que fait le rover quand il reçoit `cap` et `dist`. Testez avec votre faux émetteur.

> [!NOTE] Deux vitesses d'arrivée
> `cap` arrive 10 fois par seconde, `dist` seulement 2 fois. Ne faites pas attendre l'un à cause de l'autre.

> [!TIP] Il oscille ?
> S'il tourne à droite, puis à gauche, puis à droite, sans jamais avancer : regardez ce qu'il fait quand le cap est proche de zéro.

## 5. Passez sur la table

Une équipe à la fois. La table choisit une cible : votre rover doit la rejoindre.

Le silence d'une seconde s'applique toujours : sans message, le rover s'arrête.

## Vous ne visez pas le guidage ?

Avancez sur le cahier des charges : la pente, l'échantillon, vos pièces. Et commencez à cocher le [cahier des charges](../cahier-des-charges.md).

---

## Ce que vous devez avoir à la fin

- [ ] Vos règles de guidage notées au carnet
- [ ] Un faux émetteur qui envoie `cap` et `dist`
- [ ] Un rover qui tourne du bon côté, avance, et s'arrête près de la cible
- [ ] Ou : un point du cahier des charges avancé, et le cahier des charges commencé
- [ ] Ton [carnet de bord](../../../carnet-de-bord/rover-s09.md) rempli

## Avant de partir

Projet à part : téléverse de nouveau le programme de pilotage sur ta télécommande. Mode de plus : repasse-la en mode pilotage. Accus en charge.
