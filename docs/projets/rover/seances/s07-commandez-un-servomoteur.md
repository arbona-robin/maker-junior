# Séance 7 — Faites bouger une pièce avec un servomoteur

Vous branchez deux servomoteurs, vous les commandez à l'angle près, et vous décidez s'il sert votre rover.

## 1. Récupérez vos pièces imprimées

Regardez-les : sont-elles conformes à votre dessin ? Notez au carnet la durée qu'elles ont consommée.

## 2. Un moteur qui va à une position

Le moteur des roues tourne sans s'arrêter. Le **servomoteur**, lui, va à l'angle que tu lui donnes, entre 0 et 180°, et il s'y tient.

<figure markdown>
![Deux servomoteurs, un bleu et un noir, chacun avec son bras en plastique blanc, reliés par leurs câbles orange, rouge et marron à la carte du rover](../../../assets/rover-s07/01-deux-servomoteurs.jpg)
</figure>

## 3. Branchez-le

> [!CAUTION] Accus débranchés
> - Branche et débranche toujours accus coupés.
> - Ne force pas le bras d'un servomoteur alimenté : ses engrenages cassent.

Un servomoteur sur `S8`, l'autre sur `S7`. Le connecteur a un sens : fil orange côté vert, fil marron côté noir.

<figure markdown>
![Les deux connecteurs enfichés sur les broches S8 et S7 de la carte, fil orange en haut sur la rangée verte, fil marron en bas sur la rangée noire](../../../assets/rover-s07/02-branchement-s7-s8.jpg)
</figure>

→ [La carte DFR0548 et ses blocs](../../../fiches/carte-dfr0548.md)

## 4. Commandez-le

Nouveau projet `test-moteur`. Dans **DF-Driver**, prends `Servo S1 degree 0`. Choisis la broche, `S8` ; le nombre est l'angle.

<figure class="screenshot" markdown>
![La catégorie DF-Driver dépliée, le bloc Servo S1 degree 0 en tête](../../../assets/rover-s01/26-categorie-df-driver.png)
</figure>

### À toi : le balayage

Bouton `A` : le bras de `S8` va de 0° à 180° et revient, quatre fois, une seconde à chaque position. Puis celui de `S7`, pareil.

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Lorsque le bouton A est pressé : répéter 4 fois Servo S8 degree 0, pause 1000, Servo S8 degree 180, pause 1000 ; puis la même boucle pour S7](../../../assets/rover-s07/20-programme-balayage.png)
</figure>

</details>

Essaie d'autres angles. Où ton bras s'arrête-t-il vraiment ?

## 5. Votre rover en a-t-il besoin ?

Relisez votre croquis de la séance 5. Pousser l'échantillon est permis ; le saisir ou le soulever demande un servomoteur. Le cahier des charges en autorise deux.

Écrivez votre décision au carnet, avec la raison.

## 6. Commandez-le depuis la télécommande

Si vous l'utilisez : ajoutez une clé au protocole, par exemple `pince`.

> [!CAUTION] Huit caractères au plus
> Et une branche pour elle dans le rover, avant le `sinon`. Sinon, le rover s'arrête à chaque appui.

La table n'envoie pas cette clé : elle ne sert qu'avec la télécommande.

---

## Ce que vous devez avoir à la fin

- [ ] Deux servomoteurs qui balaient de 0° à 180°
- [ ] Votre décision notée : servomoteur ou pas, et pourquoi
- [ ] Si oui : le servomoteur monté et commandé depuis la télécommande
- [ ] Ton [carnet de bord](../../../carnet-de-bord/rover-s07.md) rempli

## Avant de partir

Servomoteurs et vis dans le bac de l'équipe. Accus en charge.
