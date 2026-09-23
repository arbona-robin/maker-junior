# Rouler droit et tourner

Un rover à deux roues motrices n'a pas de volant. Tous ses mouvements — avancer, tourner, pivoter — viennent d'une seule chose : **la différence de vitesse entre ses deux roues**.

## Les façons de tourner

> [!NOTE] La direction différentielle
> Les deux roues à la même vitesse, dans le même sens : le rover avance droit.
> Une différence entre les deux : il tourne. Plus la différence est grande, plus il tourne court.

| Ce que tu fais | Ce que le rover fait |
|---|---|
| Les deux roues en avant, même vitesse | Il avance droit |
| Une roue plus lente que l'autre | Il décrit une **courbe** |
| Une roue à l'arrêt | Il **pivote autour de cette roue** |
| Les deux roues en sens opposés | Il pivote sur place |

> [!IMPORTANT] La convention du parcours
> On tourne toujours de la même façon : **une roue à l'arrêt, l'autre en marche**. C'est ce que font `tournerAGauche` et `tournerADroite`, de la séance 2 jusqu'aux missions.
>
> La raison est le pilotage. Le rover tourne **en avançant**, donc tu corriges ta trajectoire vers ce que tu veux atteindre sans t'arrêter — c'est le plus proche d'un volant qu'un rover à deux roues puisse faire. Le pivot sur place, lui, demande trois gestes : s'arrêter, tourner, repartir.

## Ton rover ne roule pas droit

C'est normal, et ce n'est pas une panne. Deux moteurs identiques ne tournent jamais exactement à la même vitesse, et un châssis n'est jamais parfaitement symétrique.

**Cherche la mécanique en premier.** Compenser dans le code un moteur mal fixé tient jusqu'au premier choc.

1. **La languette arrière** frotte-t-elle, ou traîne-t-elle d'un côté ?
2. **Le rover est-il d'aplomb ?** Pose-le sur une table plane : il ne doit pas se balancer.
3. **Les moteurs sont-ils parallèles ?** Bien plaqués contre les rabats, tous les deux.
4. **Les roues sont-elles enfoncées à fond ?** Fais tourner une roue en l'air et regarde-la de face : si elle voile, elle est mal emmanchée.
5. **Le pack d'accus est-il centré ?** Tout le poids est là.

## Compenser dans le code

Si le rover dévie encore une fois la mécanique vérifiée, ses deux moteurs ne tournent pas à la même vitesse. On rattrape en leur donnant des valeurs différentes.

**Mets les deux à 80.** Puis monte la valeur du moteur le plus lent, **5 par 5**, et refais un passage à chaque fois.

> [!TIP] Il n'y a pas de bonne valeur
> Chaque moteur est unique. L'équilibre se trouve quelque part entre 80 et 120, et il est **propre à ton rover**. Recopier les valeurs d'un camarade ne marche pas.

Note tes deux valeurs dans ton carnet de bord : tu les reprendras à chaque séance, et elles bougeront quand ton rover sera plus lourd.

## Mesurer l'écart

Un rover qui « a l'air de rouler droit » ne se règle pas. Il faut une mesure, et la même à chaque fois.

- **Un point de départ matérialisé** — un repère en L, pour reposer le rover exactement pareil
- **Une distance fixe** — 1,50 m sur le banc
- **Un écart mesuré à l'arrivée**, par rapport à la ligne du banc
- **Trois passages**, pas un

> [!NOTE] Les trois passages ne donnent pas le même résultat
> Un rover ne fait jamais deux fois exactement la même chose, même sans rien changer. C'est pour ça qu'on compte trois passages et pas un.

Vise moins d'une largeur de rover d'écart au bout d'1,50 m. Le zéro parfait n'existe pas, et il n'est pas nécessaire : au pilotage, c'est ta main qui corrigera.

## La vitesse minimale de démarrage

En dessous d'une certaine valeur, ton rover ne démarre pas — mais si tu le pousses d'une pichenette, il continue de rouler.

> [!NOTE] Pourquoi
> Il faut plus de force pour décoller un objet immobile que pour l'entretenir en mouvement. Sous cette valeur, les moteurs bourdonnent sans vaincre le frottement de départ.

Mesure-la : descends la vitesse petit à petit jusqu'à ce que le rover refuse de partir tout seul. **Cette valeur est ton plancher** — ne programme jamais en dessous.

Elle remonte quand le rover s'alourdit, et quand les accus faiblissent en fin de séance.

→ [Déboguer](deboguer.md) · [La carte DFR0548 et ses blocs](carte-dfr0548.md)
