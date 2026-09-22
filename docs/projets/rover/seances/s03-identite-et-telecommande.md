# Séance 3 — Ton identité, et le problème de la télécommande

Tu dessines la plaque qui portera ton nom, tu l'envoies à l'impression, puis tu commences la conception de ta télécommande.

## 1. Rejoins la classe Tinkercad

Va sur [tinkercad.com/joinclass](https://www.tinkercad.com/joinclass), entre le **code de classe** que donne l'animateur, puis ton **identifiant d'élève**.

<figure class="screenshot" markdown>
![La fenêtre « Rejoindre une classe » de Tinkercad, avec le champ pour le code fourni par l'enseignant](../../../assets/rover-s03/20-rejoindre-une-classe.png)
</figure>

## 2. Dessine ta plaque

Immatriculation sur le rover aujourd'hui, porte-clés quand il sera démonté : dessine-la en pensant aux deux.

Pose une **Boîte**, et règle-la à **70 × 20 × 2 mm**.

<figure class="screenshot" markdown>
![Le panneau Propriétés d'une boîte dans Tinkercad, réglé sur longueur 20, largeur 70, hauteur 2](../../../assets/rover-s03/21-boite-70-20-2.png)
</figure>

> [!CAUTION] Le gabarit est une contrainte de groupe
> Toutes les plaques doivent tenir sur **un seul plateau d'imprimante**. Une plaque hors cotes ne part pas à l'impression, et tu repars sans rien.

Ajoute une forme **Texte**, tape ton nom, pose-la sur la plaque.

<figure class="screenshot" markdown>
![La forme Texte « robrov » posée sur la plaque, avec son panneau de propriétés](../../../assets/rover-s03/22-texte-sur-la-plaque.png)
</figure>

Centre-la avec l'outil **Aligner**, pas à l'œil.

<figure class="screenshot" markdown>
![L'outil d'alignement de Tinkercad, avec ses poignées pour centrer les formes sélectionnées](../../../assets/rover-s03/23-outils-alignement.png)
</figure>

Passe en vue **de face** : ton texte est posé **au-dessus** de la plaque. Descends-le avec la poignée d'altitude jusqu'à ce qu'il la traverse de part en part.

<figure class="screenshot" markdown>
![Vue de face : le texte rouge repose sur le dessus de la plaque beige, avec la poignée d'altitude qui permet de le faire descendre](../../../assets/rover-s03/24-vue-de-face-altitude.png)
</figure>

Passe le texte en **Perçage** : il devient transparent. Il ne s'imprimera pas, il creusera.

<figure class="screenshot" markdown>
![Le panneau Texte avec la bascule Solide / Perçage, Perçage sélectionné, et les lettres devenues transparentes sur la plaque](../../../assets/rover-s03/25-texte-en-percage.png)
</figure>

Sélectionne la plaque et le texte, puis **Regroupe** — <kbd>Ctrl</kbd> + <kbd>G</kbd>. L'icône est **le carré et le rond soudés en une seule forme bleue**.

<figure class="screenshot" markdown>
![Le panneau Union avec l'infobulle « Regrouper en union, Ctrl + G » et les trois icônes de groupement, celle du milieu sélectionnée](../../../assets/rover-s03/26-regrouper-en-union.png)
<figcaption>À gauche, les formes restent séparées. Au milieu, elles fusionnent. À droite, l'une creuse l'autre.</figcaption>
</figure>

Tes lettres sont découpées dans la plaque.

## 3. Ajoute ton trou de porte-clés

Il en faut **deux, l'un dans l'autre**.

Le premier reste **Solide** : pose-le à l'extrémité de la plaque, débordant du bord. C'est lui qui fabrique l'oreille arrondie.

<figure class="screenshot" markdown>
![Un cylindre solide orange posé à l'extrémité de la plaque, qu'il déborde](../../../assets/rover-s03/27-cylindre-du-trou.png)
</figure>

Le second passe en **Perçage** : plus petit, centré dans le premier — avec l'outil Aligner. C'est lui qui fait le trou.

> [!TIP] Laisse de la matière
> Au moins **3 mm** entre le trou et le bord de l'oreille. Sinon l'anneau arrache le coin au premier trousseau de clés.

Sélectionne tout et **regroupe** une dernière fois : le trou est creusé pour de bon.

<figure class="screenshot" markdown>
![La plaque regroupée en une seule pièce orange : l'oreille arrondie, le texte découpé et le trou](../../../assets/rover-s03/28-plaque-regroupee.png)
</figure>

## 4. Vérifie avant d'exporter

Ton imprimante empile des couches de plastique, de bas en haut, et ne pose rien dans le vide.

Regarde ta plaque et réponds à deux questions.

**Est-ce que tout tient ?** Cherche les morceaux qui ne touchent plus rien. L'intérieur des lettres fermées — `o`, `b`, `a`, `d` — n'est relié à rien.

<figure class="screenshot" markdown>
![Dans Tinkercad, les intérieurs des lettres o et b apparaissent comme des îlots détachés du reste de la plaque](../../../assets/rover-s03/29-contreformes-a-traiter.png)
<figcaption>Ils tombent, ou ils s'impriment tout seuls à côté.</figcaption>
</figure>

Deux façons de corriger :

- **Relie** l'îlot au reste de la plaque par un petit pont de matière
- **Efface-le** : pose un cylindre en perçage par-dessus, la lettre devient une boucle ouverte

**Est-ce que tout s'imprime ?** Rien ne doit flotter au-dessus du vide.

Deux fois oui ? Tu peux exporter.

## 5. Exporte ta plaque

**Exporter** → **La forme sélectionnée** → **.STL**

<figure class="screenshot" markdown>
![La fenêtre d'export de Tinkercad, avec les formats OBJ, STL, GLTF et SVG](../../../assets/rover-s03/30-exporter-en-stl.png)
</figure>

Nomme le fichier `prenom-plaque.stl` et dépose-le où l'animateur te l'indique.

> [!IMPORTANT] Point de contrôle
> Fais valider ta plaque avant d'exporter. Après, elle part à l'impression telle quelle.

→ [Modéliser et imprimer en 3D](../../../fiches/modeliser-imprimer-3d.md)

## 6. Combien d'ordres pour ton rover ?

Liste ce que tu veux commander : avancer, reculer, gauche, droite, stop…

Puis les entrées de ta carte : les boutons `A` et `B`, les deux à la fois, le logo tactile, les broches `P0`, `P1`, `P2`. Il y en a assez.

Mais essaie de conduire en appuyant sur des boutons. Ta carte porte aussi un **accéléromètre**, qui mesure son inclinaison sur trois axes.

> [!CAUTION] Cette carte-là ne monte jamais sur le rover
> C'est ta télécommande. Elle reste dans ton bac entre les séances.

## 7. Lis les valeurs du capteur

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

## 8. Transforme la mesure en décision

Le capteur donne un nombre. Toi, tu veux une direction. Il te faut un **seuil** : à partir de quelle valeur décide-t-on que ça penche vraiment ?

Range d'abord la mesure dans une **variable**, `tangage`. Puis décide avec **`si … alors`**, dans **Logique**.

Pour afficher, prends **`allumer x y`** dans **LED** : il allume un point sur la grille de 5 × 5. `x` va de `0` à gauche à `4` à droite, `y` de `0` en haut à `4` en bas.

<figure class="screenshot" markdown>
![Le programme : effacer l'écran, définir tangage à accélération y, si tangage inférieur à -200 allumer x 2 y 0, sinon si supérieur à 200 allumer x 2 y 4](../../../assets/rover-s03/34-programme-tangage.png)
<figcaption>−200 et 200 sont les seuils de ce rover. Trouve les tiens.</figcaption>
</figure>

> [!NOTE] Un point, pas une flèche
> `montrer la flèche` garde la main **400 ms** avant de rendre la suite du programme. Dans une boucle qui lit le capteur en continu, ta télécommande répond avec un temps de retard. `allumer x y` est instantané.

**Note tes seuils dans le carnet** : la séance 4 les reprendra tels quels.

### À toi : ajoute le roulis

`tangage` gère l'avant et l'arrière. Pour la gauche et la droite, crée une seconde variable `roulis` sur l'axe `x`, et remplis les deux `sinon si` qui attendent.

<figure class="screenshot" markdown>
![Le programme avec roulis défini et deux blocs sinon si encore sur « vrai », suivis d'un sinon vide](../../../assets/rover-s03/35-tangage-et-roulis.png)
<figcaption>Quatre directions, quatre branches. La cinquième est pour le repos.</figcaption>
</figure>

<details markdown>
<summary>La solution</summary>

<figure class="screenshot" markdown>
![Le programme complet : effacer l'écran en tête, tangage et roulis définis, quatre branches qui allument un point en haut, en bas, à gauche, à droite, et un sinon qui allume le centre](../../../assets/rover-s03/36-programme-complet.png)
</figure>

Le premier test vrai gagne, les suivants ne sont même pas lus.

`effacer l'écran` est **en tête de la boucle** : chaque tour éteint tout, puis rallume un seul point. Et le dernier `sinon` allume le centre — carte à plat, l'écran n'est jamais vide, et tu vois que ton programme tourne.

</details>

→ [Les capteurs, et la décision](../../../fiches/makecode-prise-en-main.md#les-capteurs-et-la-decision)

---

## Ce que tu dois avoir à la fin

- [ ] Ta plaque exportée, nommée `prenom-plaque.stl`, déposée au bon endroit
- [ ] Aucun îlot détaché dans tes lettres fermées
- [ ] Tes cotes respectées : 70 × 20 × 2 mm
- [ ] Ta seconde carte reconnue comme ta télécommande
- [ ] Un programme qui allume le bon point quand tu penches
- [ ] Tes seuils notés dans ton [carnet de bord](../../../carnet-de-bord/rover-s03.md)

## Avant de partir

Seconde carte dans ton bac — **elle revient la semaine prochaine**. Accus en charge. Un coup d'œil à l'imprimante en sortant.
