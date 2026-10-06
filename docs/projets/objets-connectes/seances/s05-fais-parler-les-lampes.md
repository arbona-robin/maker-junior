# Séance 5 — Fais parler les lampes entre elles

Tu accroches ton emblème. Puis ta lampe parle par radio aux autres lampes, et la lumière passe de lampe en lampe.

## 1. Accroche ton emblème

<span class="todo-media">[photo : l'emblème imprimé accroché à la lampe par un élastique]</span>

Un élastique dans le trou d'accroche, autour de la lampe.

## 2. Ton numéro

L'animateur te donne un numéro, de 1 à 12. Colle-le sur ta lampe.

## 3. Une bande pour tous

Duplique ton projet `lampe` en `lampe-radio`, et vide le bloc `toujours` : ton ambiance reste, le mode nuit s'en va.

Toutes les lampes sont sur la **bande 40**. Dans `au démarrage` :

<span class="todo-media">[capture : au démarrage → radio régler la bande de fréquence 40, définir numero à 7]</span>

> [!NOTE] Qui écoute ?
> Sur la même bande, toutes les lampes entendent tous les messages.

→ [Prendre en main MakeCode : la radio](../../../fiches/makecode-prise-en-main.md#la-radio)

## 4. Le message pour tous

**À toi.** Bouton `A` : envoie `tous` = `1`. Bouton `B` : envoie `tous` = `0`. Quand ta lampe reçoit `tous`, elle allume son ambiance ou s'éteint. Il te faut **Radio** et `si … alors` (**Logique**).

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : lorsque le bouton A est pressé → envoyer la valeur "tous" = 1 ; quand une donnée est reçue par radio → si nom = "tous" alors si valeur = 1 ambiance, sinon éteindre]</span>

</details>

Un appui, et toutes les lampes répondent. C'est un message **diffusé**.

## 5. La vague, avec un chef

Une seule clé : `tour`. Sa valeur est le numéro de la lampe qui s'allume.

**À toi.** Quand ta lampe reçoit `tour` = ton numéro, elle s'allume 1 seconde, puis s'éteint.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : si nom = "tour" et valeur = numero alors ambiance, pause 1000 ms, éteindre]</span>

</details>

> [!NOTE] Un message adressé
> Toutes les lampes entendent `tour` = 7. Une seule réagit : la 7. L'adresse est dans la valeur.

Le micro:bit de l'animateur, le chef, envoie `tour` = 1, puis 2, puis 3…

<span class="todo-media">[vidéo : la vague menée par le chef, six lampes]</span>

Et si le chef s'éteint ?

## 6. La vague, en relais

Plus de chef. Chaque lampe, quand elle a fini, passe le tour à la suivante.

**À toi.** Après ta seconde allumée, envoie `tour` = ton numéro + 1. La première lampe démarre au bouton `A`.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : ambiance, pause 1000 ms, éteindre, envoyer la valeur "tour" = numero + 1]</span>

</details>

Essayez à trois ou quatre, numéros qui se suivent.

> [!TIP] Une lampe éteinte
> Éteins une lampe au milieu. Que se passe-t-il ? Et avec le chef, que se passait-il ?

> [!IMPORTANT] Point de contrôle
> Ta lampe réagit à `tous` et à son tour, et la vague passe dans ton groupe.

## 7. Le bouquet

Les douze lampes, lumière éteinte.

## 8. Va plus loin

<details markdown>
<summary>Réparer la chaîne</summary>

Après avoir passé le tour, attends 2 secondes. Si tu n'as pas entendu le `tour` suivant, envoie `tour` = ton numéro + 2.

</details>

<details markdown>
<summary>Une couleur pour une seule lampe</summary>

Mets l'adresse dans la clé : `lampe7` veut dire « pour la lampe 7 », et la valeur est une couleur. À la réception, compare `nom` à `lampe` suivi de ton numéro, avec `joindre` (**Texte**). Une clé fait 8 caractères au plus.

</details>

---

## Ce que tu dois avoir à la fin

- [ ] Ton emblème accroché
- [ ] Ta lampe qui réagit à `tous` et à son tour
- [ ] La vague, au moins en groupe
- [ ] Ton [carnet de bord](../../../carnet-de-bord/objets-connectes-s05.md) rempli : le permis d'objet connecté

## Avant de partir

Lampe dans ton bac, accus en charge.
