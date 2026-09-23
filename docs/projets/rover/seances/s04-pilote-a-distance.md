# Séance 4 — Pilote ton rover à distance

Tu poses ta plaque imprimée, tu transformes ta seconde carte en télécommande, et tu pilotes ton rover sans fil.

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

## 2. Comment piloter ton rover

Liste ce que tu veux commander : avancer, reculer, gauche, droite, stop…

Une voiture ne se conduit pas au bouton : elle a un **volant**. Tu le tournes un peu, elle tourne un peu ; tu le tournes à fond, elle braque. Un bouton, lui, ne connaît que deux états — appuyé ou relâché.

Ta carte porte un **accéléromètre**, qui mesure son inclinaison sur trois axes. Tu vas la pencher comme un volant.

> [!CAUTION] Cette carte-là ne monte jamais sur le rover
> C'est ta télécommande. Elle reste dans ton bac entre les séances.

## 3. Lis les valeurs du capteur

Nouveau projet MakeCode, nommé `telecommande`.

<figure class="screenshot" markdown>
![La fenêtre « Créer un projet » de MakeCode avec le nom telecommande](../../../assets/rover-s03/31-nouveau-projet-telecommande.png)
</figure>

**Regarde les chiffres avant de décider.** Dans `toujours`, écris les quatre valeurs de l'accéléromètre :

<figure class="screenshot" markdown>
![Le bloc toujours contenant quatre blocs « série écrire valeur » pour x, y, z et force](../../../assets/rover-s03/32-serie-ecrire-valeurs.png)
</figure>

> [!NOTE] La liaison série
> `série écrire valeur` envoie les chiffres à ton ordinateur par le câble USB. USB débranché, la carte mesure toujours — mais plus personne ne l'écoute.

Téléverse, garde le câble branché, puis clique sur **Afficher données Appareil**. Penche la carte dans tous les sens.

<figure class="screenshot" markdown>
![Le graphe des données de l'accéléromètre, quatre courbes qui réagissent aux mouvements](../../../assets/rover-s03/33-afficher-donnees.png)
</figure>

- [ ] Quelle courbe bouge quand tu penches vers l'avant ?
- [ ] Quelles valeurs quand la carte est à plat ?

## 4. Transforme la mesure en décision

Le capteur donne un nombre. Toi, tu veux une direction. Il te faut un **seuil** : à partir de quelle valeur décide-t-on que ça penche vraiment ?

Range d'abord la mesure dans une **variable**, `tangage`. Puis décide avec **`si … alors`**, dans **Logique**.

Pour afficher, prends **`allumer x y`** dans **LED** : il allume un point sur la grille de 5 × 5.

<figure markdown>
![Schéma du micro:bit : la grille de 5 sur 5 LED, colonnes numérotées 0 à 4 pour x, lignes numérotées 0 à 4 pour y, avec le repère X vers la droite et Y vers le bas](../../../assets/rover-s03/34-grille-led-xy.png)
<figcaption>`x` vers la droite, `y` vers le bas. Le coin en haut à gauche est `0,0`.</figcaption>
</figure>

<figure class="screenshot" markdown>
![Le programme : effacer l'écran, définir tangage à accélération y, si tangage inférieur à -200 allumer x 2 y 0, sinon si supérieur à 200 allumer x 2 y 4](../../../assets/rover-s03/35-programme-tangage.png)
<figcaption>−200 et 200 sont les seuils de ce rover. Trouve les tiens.</figcaption>
</figure>

> [!NOTE] Un point, pas une flèche
> `montrer la flèche` garde la main **400 ms** avant de rendre la suite du programme. Dans une boucle qui lit le capteur en continu, ta télécommande répond avec un temps de retard. `allumer x y` est instantané.

**Note tes seuils dans le carnet.**

### À toi : ajoute le roulis

`tangage` gère l'avant et l'arrière. Pour la gauche et la droite, crée une seconde variable `roulis` sur l'axe `x`, et remplis les deux `sinon si` qui attendent.

<figure class="screenshot" markdown>
![Le programme avec roulis défini et deux blocs sinon si encore sur « vrai », suivis d'un sinon vide](../../../assets/rover-s03/36-tangage-et-roulis.png)
<figcaption>Quatre directions, quatre branches. La cinquième est pour le repos.</figcaption>
</figure>

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Le programme complet : effacer l'écran en tête, tangage et roulis définis, quatre branches qui allument un point en haut, en bas, à gauche, à droite, et un sinon qui allume le centre](../../../assets/rover-s03/37-programme-complet.png)
</figure>

Le premier test vrai gagne, les suivants ne sont même pas lus.

`effacer l'écran` est **en tête de la boucle** : chaque tour éteint tout, puis rallume un seul point. Et le dernier `sinon` allume le centre — carte à plat, l'écran n'est jamais vide, et tu vois que ton programme tourne.

</details>

→ [Les capteurs, et la décision](../../../fiches/makecode-prise-en-main.md#les-capteurs-et-la-decision)

## 5. Deux machines qui ne se sont jamais parlé

Ta télécommande va envoyer des messages, ton rover va les écouter. Pour qu'ils se comprennent, il leur faut deux accords :

- **la même fréquence** — sinon ils ne s'entendent pas
- **le même vocabulaire** — sinon ils s'entendent sans se comprendre

Ces deux accords, c'est un **protocole**. Celui-ci t'est donné, et c'est volontaire : plus tard, ton rover devra obéir à la télécommande d'un coéquipier, et se faire comprendre d'un rover qui n'est pas le tien. Un protocole ne vaut que si tout le monde emploie le même.

## 6. La même fréquence

Dans la salle, une douzaine de télécommandes émettent en même temps. Pour ne pas piloter le rover du voisin — ni lui le tien — chacun prend **sa bande de fréquence**. La tienne, c'est **le numéro de ton ordinateur**.

Dans `au démarrage`, sur **tes deux cartes** :

<figure class="screenshot" markdown>
![Le bloc « au démarrage » contenant « radio régler la bande de fréquence 15 »](../../../assets/rover-s04/20-bande-de-frequence.png)
<figcaption>Ici, le poste 15. Toi, mets ton numéro.</figcaption>
</figure>

> [!CAUTION] La même des deux côtés
> Une carte sur la bande 3 n'entend pas une carte sur la bande 4.

> [!NOTE] Pourquoi la fréquence et pas le groupe
> `radio définir groupe` existe aussi, mais les cartes restent alors sur la même fréquence : elles s'entendent toutes et trient à l'arrivée. À douze qui émettent sans arrêt, les messages se gênent. Changer de bande, c'est parler ailleurs dans le spectre.

## 7. Le même vocabulaire

Reste dans `telecommande`. Ton programme allume déjà le bon point quand tu penches. Il va maintenant envoyer l'ordre qui va avec.

Dans la branche du haut, ajoute `envoyer la valeur … par radio` :

<figure class="screenshot" markdown>
![Le bloc « envoyer la valeur avancer = valeur absolue de tangage par radio » ajouté au-dessus de « allumer x 2 y 0 »](../../../assets/rover-s04/21-envoyer-avancer.png)
</figure>

Un message porte **une clé** et **une valeur**. La clé est le mot d'ordre. La valeur est un nombre qui l'accompagne — ici, de combien tu penches.

**Le protocole, à respecter au caractère près :**

| Quand tu penches | Clé | Valeur envoyée |
|---|---|---|
| Vers l'avant | `avancer` | valeur absolue de `tangage` |
| Vers l'arrière | `reculer` | valeur absolue de `tangage` |
| À gauche | `gauche` | valeur absolue de `roulis` |
| À droite | `droite` | valeur absolue de `roulis` |
| À plat | `arreter` | `0` |

> [!CAUTION] Huit caractères, pas un de plus
> Au-delà, la carte coupe la clé sans prévenir. `tournerAGauche` et `tournerADroite` arrivent toutes les deux comme `tournerA`. C'est la raison de ces cinq mots-là.

## 8. Tes cinq ordres

**À toi.** Complète les quatre autres branches en suivant le tableau. Puis ajoute une `pause (ms)` de `100` tout en bas du `toujours`.

> [!NOTE] Pourquoi une pause
> Sans elle, ta carte envoie des centaines de messages par seconde et le rover prend du retard à les traiter. Dix par seconde suffisent à conduire.

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Le programme de la télécommande : cinq branches à la suite, chacune envoyant sa clé par radio puis allumant son point, et une pause de 100 ms en fin de boucle](../../../assets/rover-s04/22-telecommande-complete.png)
</figure>

</details>

## 9. Ton rover écoute

Ouvre `rover`, celui de tes cinq fonctions.

Dans **Radio**, prends `quand une donnée est reçue par radio`. Il t'apporte deux choses : `nom` et `valeur`.

<figure class="screenshot" markdown>
![Le bloc « quand une donnée est reçue par radio » avec ses cinq branches encore vides](../../../assets/rover-s04/23-quand-une-donnee-est-recue.png)
</figure>

`nom` est un **texte**. Pour le comparer, prends dans **Logique** le bloc d'égalité à **cases blanches** — pas celui qui compare des nombres.

<figure class="screenshot" markdown>
![La section Comparaison de la catégorie Logique : deux blocs d'égalité et d'infériorité sur des zéros, et en dessous le bloc d'égalité sur deux cases de texte vides](../../../assets/rover-s04/24-comparaison-de-textes.png)
</figure>

## 10. La première branche

<figure class="screenshot" markdown>
![Dans le bloc de réception : si nom = avancer alors appel avancer, puis allumer x 2 y 0](../../../assets/rover-s04/25-premiere-branche.png)
</figure>

`si nom = "avancer"` → `appel avancer`. Ta fonction n'a pas bougé d'un bloc.

### À toi : les quatre autres

Ajoute `reculer`, `gauche`, `droite` et `arreter`. Allume dans chaque branche **le même point que ta télécommande** : c'est lui qui te dira que le message est arrivé.

Mets aussi `effacer l'écran` en tête, comme dans la télécommande.

Termine par un `sinon` qui **arrête les moteurs** et allume un point que tu n'utilises pour rien d'autre : un ordre incompris ne doit pas faire rouler ton rover, et tu dois pouvoir le reconnaître d'un coup d'œil.

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Le programme du rover : cinq branches qui comparent nom à chaque clé, appellent la fonction correspondante et allument son point, puis un sinon qui arrête les moteurs et allume le coin bas-droit](../../../assets/rover-s04/26-rover-complet.png)
</figure>

Les points sont les mêmes que sur la télécommande, aux mêmes endroits. C'est ce qui rend le contrôle possible d'un coup d'œil.

</details>

## 11. Pilote

Téléverse les deux programmes, débranche l'USB, passe sur accus.

> [!TIP] Le contrôle en un coup d'œil
> Penche ta télécommande et regarde **les deux écrans**.
>
> Même point des deux côtés : le message passe. Point allumé seulement sur la télécommande : le rover n'entend pas — vérifie ta bande de fréquence. Le point reste au centre des deux côtés : ce sont tes seuils.

## 12. Va plus loin

- **Trop sensible, ou pas assez ?** Deux nombres décident de ça dans ta télécommande. Trouve lesquels, et dans quel sens les faire varier.
- **Deux vitesses.** Lente ou rapide, selon un seuil d'inclinaison de plus.
- **La valeur arrive au rover, et personne ne s'en sert.** `valeur` dit de combien tu penches. Fais-en une vitesse — mais `speed` s'arrête à `255`, et ton inclinaison monte bien plus haut.

---

## Ce que tu dois avoir à la fin

- [ ] Ta plaque sur ton rover
- [ ] Une télécommande qui allume le bon point quand tu penches
- [ ] La même bande de fréquence sur tes deux cartes
- [ ] Les cinq clés du protocole, écrites au caractère près
- [ ] Les deux écrans qui allument le même point
- [ ] Ton rover qui avance, recule, tourne et s'arrête, sans fil
- [ ] Ton [carnet de bord](../../../carnet-de-bord/rover-s04.md) rempli

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md) · [Déboguer](../../../fiches/deboguer.md)

## Avant de partir

Tes **deux** cartes dans ton bac. Accus en charge.
