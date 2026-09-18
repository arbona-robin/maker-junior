# Séance 3 — Ton identité, et le problème de la télécommande

Tu dessines la plaque qui portera ton nom, tu la lances à l'impression, et tu attaques une énigme : comment commander un rover avec seulement deux boutons ?

## 1. Rejoins la classe Tinkercad

Va sur [tinkercad.com/joinclass](https://www.tinkercad.com/joinclass), entre le **code de classe** que donne l'animateur, puis ton **identifiant d'élève**.

<figure class="screenshot" markdown>
![La fenêtre « Rejoindre une classe » de Tinkercad, avec le champ pour le code fourni par l'enseignant](../../../assets/rover-s03/20-rejoindre-une-classe.png)
</figure>

Pas d'adresse mail à donner : c'est l'animateur qui a créé ton compte.

## 2. Dessine ta plaque

Ta plaque a deux vies : **immatriculation** sur le rover aujourd'hui, **porte-clés** quand le rover sera démonté. Dessine-la en pensant aux deux.

Pose une **Boîte**, et règle-la à **70 × 20 × 2 mm**.

<figure class="screenshot" markdown>
![Le panneau Propriétés d'une boîte dans Tinkercad, réglé sur longueur 20, largeur 70, hauteur 2](../../../assets/rover-s03/23-boite-70-20-2.png)
<figcaption>Ces trois valeurs ne se négocient pas : c'est le gabarit.</figcaption>
</figure>

Ajoute une forme **Texte**, tape ton nom, pose-la sur la plaque.

<figure class="screenshot" markdown>
![La forme Texte « robrov » posée sur la plaque, avec son panneau de propriétés](../../../assets/rover-s03/24-texte-sur-la-plaque.png)
</figure>

Centre-la avec l'outil **Aligner** plutôt qu'à l'œil : tu sélectionnes la plaque et le texte, et tu cliques sur la poignée du milieu.

<figure class="screenshot" markdown>
![L'outil d'alignement de Tinkercad, avec ses poignées pour centrer les formes sélectionnées](../../../assets/rover-s03/25-outils-alignement.png)
</figure>

> [!CAUTION] Le gabarit est une contrainte de groupe
> Toutes les plaques doivent tenir sur **un seul plateau d'imprimante**. Une plaque hors cotes ne part pas à l'impression, et tu repars sans rien.

Si tu laisses ton texte en relief, il ne dépasse pas de **plus de 2 mm**, et seulement par endroits.

## 3. Le piège des lettres fermées

Si tu passes ton texte en **Perçage**, les lettres sont découpées à travers la plaque — et l'intérieur des lettres fermées comme `o`, `b`, `a`, `d` ne tient plus à rien.

<figure class="screenshot" markdown>
![Dans Tinkercad, les intérieurs des lettres o et b apparaissent comme des îlots détachés du reste de la plaque](../../../assets/rover-s03/26-contreformes-a-traiter.png)
<figcaption>Ces îlots ne sont reliés à rien : ils tombent, ou ils s'impriment tout seuls à côté.</figcaption>
</figure>

Deux solutions, au choix :

- **Relie-les** au reste de la plaque par un petit pont de matière
- **Efface-les** : pose un cylindre en perçage par-dessus, la lettre devient une simple boucle ouverte

Regarde ta plaque **de face** avant de continuer : c'est la seule vue qui montre les épaisseurs.

<figure class="screenshot" markdown>
![Vue de face de la plaque dans Tinkercad, montrant l'épaisseur et le relief du texte](../../../assets/rover-s03/27-vue-de-face-relief.png)
</figure>

## 4. Ajoute ton trou de porte-clés

Pose un **Cylindre**, place-le près d'un bord, et passe-le en **Perçage**.

<figure class="screenshot" markdown>
![Un cylindre posé à l'extrémité de la plaque dans Tinkercad](../../../assets/rover-s03/28-cylindre-du-trou.png)
</figure>

> [!TIP] Laisse de la matière
> Au moins **3 mm** entre le trou et le bord. Sinon l'anneau arrache le coin au premier trousseau de clés.

Sélectionne tout, puis **Regrouper** — <kbd>Ctrl</kbd> + <kbd>G</kbd>. Ta plaque devient une seule pièce.

<figure class="screenshot" markdown>
![Le bouton Regrouper en union dans Tinkercad, avec la plaque et son texte fusionnés](../../../assets/rover-s03/29-regrouper-en-union.png)
</figure>

## 5. Exporte ta plaque

**Exporter** → **La forme sélectionnée** → **.STL**

<figure class="screenshot" markdown>
![La fenêtre d'export de Tinkercad, avec les formats OBJ, STL, GLTF et SVG](../../../assets/rover-s03/30-exporter-en-stl.png)
</figure>

Nomme le fichier `prenom-plaque.stl` et dépose-le où l'animateur te l'indique.

> [!TIP] Vérifie l'extension
> Selon le navigateur, le `.stl` saute au téléchargement. Si ton fichier n'a pas d'extension, ajoute-la à la main.

> [!IMPORTANT] Point de contrôle
> Fais vérifier tes cotes, ton trou et ton nom avant d'exporter. Après, la plaque part à l'impression telle quelle.

## 6. De l'écran à l'objet

L'imprimante n'enlève pas de matière : elle **empile des couches** de plastique fondu.

<div class="photo-row" markdown>

![La buse de l'imprimante traçant la première couche de la plaque sur le plateau](../../../assets/rover-s03/01-impression-premiere-couche.jpg)

![La plaque « robrov » imprimée en bleu, encore sur le plateau](../../../assets/rover-s03/02-plaque-imprimee.jpg)

![La plaque bleue fixée par deux élastiques sur le châssis du rover](../../../assets/rover-s03/03-plaque-sur-le-rover.jpg)

</div>

> [!NOTE] Une pièce casse entre ses couches
> C'est sa direction faible. Tu t'en souviendras quand tu dessineras les supports de ton mécanisme.

→ [Modéliser et imprimer en 3D](../../../fiches/modeliser-imprimer-3d.md)

## 7. Combien d'ordres pour ton rover ?

Ta télécommande aura **deux boutons**. A, B, et A+B : trois possibilités.

Compte les ordres que tu veux vraiment envoyer — avancer, reculer, gauche, droite, stop… Ça ne rentre pas.

Alors cherche autre chose dans la carte. Elle sait aussi **sentir comment tu la tiens**.

> [!CAUTION] Cette carte-là ne monte jamais sur le rover
> C'est ta télécommande. Elle reste dans ton bac entre les séances.

## 8. Regarde ce que dit le capteur

Nouveau projet MakeCode, nommé `telecommande`.

<figure class="screenshot" markdown>
![La fenêtre « Créer un projet » de MakeCode avec le nom telecommande](../../../assets/rover-s03/32-nouveau-projet-telecommande.png)
</figure>

Avant de décider quoi que ce soit, **regarde les chiffres**. Dans `toujours`, écris les quatre valeurs de l'accéléromètre :

<figure class="screenshot" markdown>
![Le bloc toujours contenant quatre blocs « série écrire valeur » pour x, y, z et force](../../../assets/rover-s03/33-serie-ecrire-valeurs.png)
</figure>

Téléverse, puis clique sur **Afficher données Appareil**. Penche la carte dans tous les sens et regarde les courbes bouger.

<figure class="screenshot" markdown>
![Le graphe des données de l'accéléromètre, quatre courbes qui réagissent aux mouvements](../../../assets/rover-s03/34-afficher-donnees.png)
</figure>

- [ ] Quelle courbe bouge quand tu penches vers l'avant ?
- [ ] Quelles valeurs quand la carte est à plat ?

## 9. Transforme la mesure en décision

Le capteur donne un nombre. Toi, tu veux une direction. Il te faut un **seuil** : à partir de quelle valeur décide-t-on que ça penche vraiment ?

Range d'abord la mesure dans une variable `tangage`, puis décide :

<figure class="screenshot" markdown>
![Le programme : définir tangage à accélération y, si tangage inférieur à -100 montrer flèche Nord, sinon si supérieur à 100 montrer flèche Sud, sinon effacer l'écran](../../../assets/rover-s03/37-programme-tangage.png)
<figcaption>−100 et 100 sont les seuils de ce rover. Trouve les tiens.</figcaption>
</figure>

**Note tes seuils dans le carnet** : la séance 4 les reprendra tels quels.

→ [D'une mesure à une décision](../../../fiches/mesure-vers-decision.md)

---

## Ce que tu dois avoir à la fin

- [ ] Ta plaque exportée, nommée `prenom-plaque.stl`, déposée au bon endroit
- [ ] Aucun îlot détaché dans tes lettres fermées
- [ ] Tes cotes respectées : 70 × 20 × 2 mm
- [ ] Ta seconde carte reconnue comme ta télécommande
- [ ] Un programme qui affiche une flèche quand tu penches
- [ ] Tes seuils notés dans ton [carnet de bord](../../../carnet-de-bord/rover-s03.md)

## Avant de partir

Seconde carte dans ton bac — **elle revient la semaine prochaine**. Accus en charge. Un coup d'œil à l'imprimante en sortant.
