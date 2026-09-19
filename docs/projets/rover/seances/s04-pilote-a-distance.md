# Séance 4 — Pilote ton rover à distance

Tu poses ta plaque imprimée, tu construis le protocole qui relie tes deux cartes, et tu pilotes ton rover sans fil.

## 1. Récupère ta plaque

<div class="photo-row" markdown>

<figure markdown>
![La première couche de la plaque en cours d'impression, la buse de l'imprimante en train de déposer le plastique](../../../assets/rover-s04/01-impression-premiere-couche.jpg)
</figure>

<figure markdown>
![La plaque bleue terminée sur le plateau de l'imprimante, le nom robrov découpé dedans](../../../assets/rover-s04/02-plaque-imprimee.jpg)
</figure>

<figure markdown>
![La plaque sanglée par deux élastiques à l'avant du rover, entre les deux roues](../../../assets/rover-s04/03-plaque-sur-le-rover.jpg)
</figure>

</div>

Regarde-la de près avant de la monter : les couches, les lettres, ce qui a bavé. Puis glisse-la sous les élastiques déjà en place sur ton rover.

## 2. Deux machines qui ne se sont jamais parlé

Ta télécommande va envoyer des messages, ton rover va les écouter. Pour qu'ils se comprennent, il leur faut deux accords :

- **le même groupe** — sinon ils ne s'entendent pas
- **le même vocabulaire** — sinon ils s'entendent sans se comprendre

Ces deux accords, c'est un **protocole**. C'est à toi de le définir.

## 3. Le même groupe

Dans la salle, une douzaine de télécommandes émettent en même temps. Pour ne pas piloter le rover du voisin — ni lui le tien — chacun choisit son **groupe**. Le tien, c'est **le numéro de ton ordinateur**.

Dans `au démarrage`, sur **tes deux cartes** :

<figure class="screenshot" markdown>
![Le bloc « au démarrage » contenant « radio définir groupe 75 », et le curseur qui sert à régler le numéro](../../../assets/rover-s04/20-groupe-radio.png)
<figcaption>Ici, le poste 75. Toi, mets ton numéro.</figcaption>
</figure>

> [!CAUTION] Le même des deux côtés
> Une carte sur le groupe 3 n'entend pas une carte sur le groupe 4.

## 4. Le même vocabulaire

Reste dans `telecommande`. Ton programme affiche déjà une flèche quand tu penches. Il va maintenant envoyer l'ordre qui va avec.

Dans la branche qui affiche la flèche Nord, ajoute `envoyer la valeur … par radio` :

<figure class="screenshot" markdown>
![Le bloc « envoyer la valeur avancer = valeur absolue de tangage par radio » ajouté sous « montrer la flèche Nord »](../../../assets/rover-s04/21-envoyer-avancer.png)
</figure>

Un message porte **une clé** et **une valeur**. La clé est le mot d'ordre : `avancer`. La valeur est un nombre qui voyage avec — ici, de combien tu penches.

> [!CAUTION] Huit caractères, pas un de plus
> Au-delà, la carte coupe la clé sans prévenir. `tournerAGauche` et `tournerADroite` arrivent toutes les deux comme `tournerA`.

Prends des clés courtes : `avancer`, `reculer`, `gauche`, `droite`, `arreter`.

## 5. Tes cinq ordres, à plat

Complète les quatre autres branches, une par direction.

Profites-en pour **mettre tes tests à plat** : les `si` imbriqués de la séance 3 deviennent une seule suite de `sinon si`.

> [!NOTE] Pourquoi c'est la même chose
> Les conditions sont lues **dans l'ordre**, et la première qui est vraie gagne — les suivantes ne sont même pas regardées. Imbriqué ou à plat, le rover reçoit les mêmes ordres. À plat se relit.

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Le programme de la télécommande : cinq branches sinon si à la suite, chacune affichant une flèche et envoyant sa clé par radio](../../../assets/rover-s04/23-telecommande-complete.png)
</figure>

</details>

## 6. Ton rover écoute

Ouvre `rover`, celui de la séance 2 et de ses cinq fonctions.

Dans **Radio**, prends `quand une donnée est reçue par radio`. Il t'apporte deux choses : `nom` et `valeur`.

Pour comparer deux textes, il te faut le bloc de comparaison à **cases blanches**, dans **Logique** — pas celui qui compare des nombres.

<figure class="screenshot" markdown>
![La catégorie Logique ouverte sur le bloc de comparaison de textes, à côté du bloc « quand une donnée est reçue par radio » encore vide](../../../assets/rover-s04/24-quand-une-donnee-est-recue.png)
</figure>

## 7. La première branche

<figure class="screenshot" markdown>
![Dans le bloc de réception : si nom = avancer alors appel avancer](../../../assets/rover-s04/25-premiere-branche.png)
</figure>

`si nom = "avancer"` → `appel avancer`. Ta fonction de la séance 2 n'a pas bougé d'un bloc.

### À toi : les quatre autres

Ajoute `reculer`, `gauche`, `droite` et `arreter`. Fais afficher **une flèche** dans chaque branche : c'est elle qui te dira que le message est arrivé.

Termine par un `sinon`, tout en bas. Il attrape les clés qui ne correspondent à aucune de tes branches — une faute de frappe, une clé trop longue, le message d'un voisin. Fais-lui afficher une croix : « j'ai reçu quelque chose, je n'ai pas compris » n'est pas la même panne que « je ne reçois rien », et ça ne se cherche pas au même endroit.

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Le programme du rover : cinq branches qui comparent nom à chaque clé, appellent la fonction correspondante et affichent une flèche, puis un sinon qui affiche une icône](../../../assets/rover-s04/26-rover-complet.png)
</figure>

Les flèches sont les mêmes que sur la télécommande, dans le même ordre. C'est ce qui rend le contrôle possible d'un coup d'œil.

</details>

## 8. Pilote

Téléverse les deux programmes, débranche l'USB, passe sur accus.

> [!TIP] Le contrôle en un coup d'œil
> Penche ta télécommande et regarde **les deux écrans**.
>
> Même flèche des deux côtés : le message passe. Flèche seulement sur la télécommande : le rover n'entend pas — vérifie ton groupe. Aucune flèche nulle part : ce sont tes seuils.

## 9. Va plus loin

- **Trop sensible, ou pas assez ?** Deux nombres décident de ça dans ta télécommande. Trouve lesquels, et dans quel sens les faire varier.
- **Deux vitesses.** Lente ou rapide, selon un seuil d'inclinaison de plus.
- **La valeur voyage, et personne ne s'en sert.** Côté rover, `valeur` dit de combien tu penches. Fais-en une vitesse — mais `speed` s'arrête à `255`, et ton inclinaison monte bien plus haut.
- **Une manœuvre au bouton.** `lorsque le bouton A est pressé` envoie une clé de plus. Côté rover, une branche de plus — et une manœuvre entière qui se déroule toute seule.
- **Invente ta figure** : demi-tour, créneau, huit. Puis donne-lui un nom de huit caractères.

---

## Ce que tu dois avoir à la fin

- [ ] Ta plaque sur ton rover
- [ ] Le même groupe radio sur tes deux cartes
- [ ] Cinq clés de huit caractères maximum, notées au carnet
- [ ] Les deux écrans qui affichent la même flèche
- [ ] Ton rover qui avance, recule, tourne et s'arrête, sans fil
- [ ] Ton [carnet de bord](../../../carnet-de-bord/rover-s04.md) rempli

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md) · [Déboguer](../../../fiches/deboguer.md)

## Avant de partir

Tes **deux** cartes dans ton bac. Accus en charge.
