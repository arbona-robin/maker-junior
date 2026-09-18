# Séance 2 — Ton rover obéit

Ton rover apprend cinq mouvements, tu le règles pour qu'il roule droit, et tu l'envoies au garage.

## 1. Termine ton rover

Tu n'as pas fini la séance 1 ? Reprends où tu t'es arrêté : [fabrique ton châssis](s01-base-motrice.md#9-fabrique-ton-chassis), puis [monte ton rover](s01-base-motrice.md#10-monte-ton-rover).

> [!IMPORTANT] Point de contrôle
> Fais valider ton montage avant de coder. Tout le réglage d'aujourd'hui repose dessus.

## 2. Les deux roues dans le même sens

Pose ton rover **sur l'arrière, roues en l'air**, dans la boîte de test. Lance ton programme de la séance 1.

<figure markdown>
![Le rover posé sur son pack d'accus, les deux roues en l'air, dans une boîte en carton](../../../assets/rover-s02/01-rover-sur-arriere-roues-en-lair.jpg)
<figcaption>Roues en l'air : tu vois les deux sens sans courir après ton rover.</figcaption>
</figure>

- [ ] Les deux roues tournent dans le même sens
- [ ] Sinon, inverse les deux fils d'un moteur, ou passe son bloc en `CCW`

## 3. Ta première fonction

Une fonction est un bloc que tu fabriques, que tu nommes, et que tu réutilises ensuite par son nom.

**Fonctions** → **Créer une fonction…**

<figure class="screenshot" markdown>
![La catégorie Fonctions dépliée dans MakeCode, avec le bouton « Créer une fonction… »](../../../assets/rover-s02/20-categorie-fonctions.png)
</figure>

Appelle-la `avancer`, puis **Terminé**.

<figure class="screenshot" markdown>
![La fenêtre « Modifier la fonction » avec le nom avancer en cours de saisie](../../../assets/rover-s02/21-creer-fonction-avancer.png)
</figure>

Glisse tes deux blocs `Motor` dans la fonction. Reprends **Fonctions** : le bloc `appel avancer` est apparu — mets-le dans `toujours`, à la place des blocs que tu viens de déplacer.

<figure class="screenshot" markdown>
![La fonction avancer contenant Motor M1 et Motor M2, et le bloc appel avancer placé dans toujours](../../../assets/rover-s02/23-fonction-avancer-appelee.png)
</figure>

> [!NOTE] Pourquoi s'embêter
> Un programme se lit comme une phrase : `appel avancer` se comprend sans lire le détail. Tu réutiliseras ces fonctions telles quelles quand ton rover aura une télécommande.

## 4. Fais-le rouler droit

Ton rover tire d'un côté. **Regarde la mécanique avant de toucher au code.**

- [ ] La languette arrière glisse sans frotter d'un côté
- [ ] Le rover est d'aplomb, il ne se balance pas
- [ ] Les deux moteurs sont bien plaqués contre les rabats, parallèles
- [ ] Les roues sont enfoncées à fond et ne voilent pas
- [ ] Le pack d'accus est centré

Il dévie encore ? Alors les deux moteurs ne tournent pas exactement à la même vitesse. Mets-les **tous les deux à 80**, puis monte celui qui est le plus lent, 5 par 5, jusqu'à ce que le rover suive son couloir.

> [!NOTE] Il n'y a pas de bonne valeur
> Chaque moteur est unique. Sur le rover des photos, l'équilibre tombe à 110 ; le tien sera ailleurs, entre 80 et 120. **Note tes deux valeurs dans le carnet.**

<span class="todo-media">[photo : le banc d'essai marqué au scotch — couloirs, ligne de départ, repère en L, ligne des 2 mètres]</span>

Sur le banc : rover calé sur le repère en L, départ, et tu mesures de combien il a dévié à l'arrivée. **Trois passages** — l'écart change à chaque fois, et c'est déjà une information.

> [!TIP] Parfait n'existe pas
> Vise « il ne mord pas les limites de son couloir sur 2 mètres ». Le reste se rattrapera à la télécommande.

Mesure aussi ta **vitesse minimale** : descends la valeur jusqu'à ce que le rover refuse de démarrer, alors qu'une pichenette suffit à le lancer. Note-la.

→ [Rouler droit et tourner](../../../fiches/rouler-droit.md)

## 5. Les quatre autres mouvements

Fabrique `reculer`, `tournerAGauche`, `tournerADroite` et `arreter`, sur le même modèle.

Pour tourner, essaie les deux façons et garde celle que tu préfères :

- les deux moteurs en sens opposés — le rover **pivote sur place**
- un seul côté ralenti — le rover décrit une **courbe**

<figure class="screenshot" markdown>
![Le programme avec les cinq fonctions repliées et le bloc toujours qui les appelle l'une après l'autre](../../../assets/rover-s02/24-programme-cinq-fonctions.png)
<figcaption>Les cinq fonctions, appelées l'une après l'autre.</figcaption>
</figure>

<details markdown>
<summary>Et pour arrêter ?</summary>

Sur les photos, `arreter` contient les deux blocs `Motor` à `speed 0`. `Motor Stop All` fait la même chose en un seul bloc — les deux se valent.

→ [L'extension DF-Driver](../../../fiches/extension-df-driver.md)

</details>

## 6. Le défi du retour au garage

<span class="todo-media">[photo : le parcours du défi — zone de départ/arrivée, point de départ, zone intermédiaire, obstacle au milieu]</span>

Ton rover doit atteindre la **zone intermédiaire**, contourner l'obstacle, et revenir dans la **zone de départ**. Trois fois de suite, avec le même programme.

Deux changements dans ton code :

1. **Supprime le bloc `toujours`.** Tu ne veux plus que ça tourne sans fin.
2. Prends `lorsque le bouton A est pressé`, et mets dedans `répéter 3 fois` — dans la catégorie **Boucles**.

<figure class="screenshot" markdown>
![La catégorie Boucles dépliée, avec le bloc « répéter 4 fois / faire » en vert](../../../assets/rover-s02/25-categorie-boucles.png)
</figure>

Dans la boucle : ta manœuvre, puis une pause assez longue pour que tu aies le temps de **replacer ton rover sur le point de départ**.

**Réussi si 2 passages sur 3 reviennent dans la zone.** On ne compte pas le meilleur des trois : on compte la régularité.

> [!NOTE] Ton rover ne sait pas où il est
> Il obéit à des durées, pas à des positions. Rien n'a changé entre deux passages, et pourtant il ne s'arrête pas au même endroit.

Note tes trois résultats dans le carnet.

---

## Ce que tu dois avoir à la fin

- [ ] Rover terminé, les deux roues dans le même sens
- [ ] Cinq fonctions : `avancer`, `reculer`, `tournerAGauche`, `tournerADroite`, `arreter`
- [ ] Il roule droit sur 2 mètres sans mordre son couloir
- [ ] Le défi tenté, les trois résultats notés
- [ ] Ton [carnet de bord](../../../carnet-de-bord/rover-s02.md) rempli

## Avant de partir

Matériel dans ton bac, chutes triées, **cutter rendu**, banc dégagé, accus en charge.
