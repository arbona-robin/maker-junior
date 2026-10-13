# Séance 7 — Le servomoteur

> [!NOTE] Nouveau concept : le servomoteur
> Un moteur qui va à un angle, entre 0 et 180°, et s'y tient. Pour une pince, un bras, une trappe. L'animateur le montre en début de séance.
>
> → [Le servomoteur](../../../fiches/carte-dfr0548.md#le-servomoteur)

1. **[Essayez-le](#1-essayez-le)** : le bras va à l'angle que vous lui donnez.
2. **[Montez-le et commandez-le](#2-montez-le-et-commandez-le)** : des mots de plus sur la télécommande, et la pièce bouge.

## 1. Essayez-le

**Ce que vous allez obtenir :** bouton `A`, le bras va de 0° à 180° et revient.

> [!CAUTION] Accus débranchés
> - Branche et débranche toujours accus coupés.
> - Ne force pas le bras d'un servomoteur alimenté : ses engrenages cassent.

Branchez vos deux servomoteurs, fil orange côté rangée verte, fil marron côté rangée noire, et faites-les balayer, comme dans la fiche. Essayez d'autres angles : où le bras s'arrête-t-il vraiment ?

Votre croquis le prévoit pour saisir ou soulever l'échantillon ? Passez à l'étape 2. Votre rover pousse l'échantillon ? Pas besoin de servomoteur : montez vos pièces imprimées, ou avancez votre châssis. Vous changez d'avis en l'essayant ? Écrivez-le dans « Nos décisions ».

## 2. Montez-le et commandez-le

**Ce que vous allez obtenir :** un geste sur la télécommande, et la pièce bouge.

Ajoutez des mots au protocole, au moins un par position : par exemple `ouvrir` et `fermer`. La télécommande les envoie comme les cinq autres.

> [!CAUTION] Une branche par mot
> Dans le rover, avant le `sinon`. Sinon, le rover s'arrête à chaque appui.
