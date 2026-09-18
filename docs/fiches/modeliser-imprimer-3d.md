# Modéliser et imprimer en 3D

Dessiner une pièce à l'écran et la tenir dans la main une heure plus tard. Entre les deux, deux outils : **Tinkercad** pour dessiner, **le slicer** pour traduire.

## Tinkercad

Tu te connectes par [tinkercad.com/joinclass](https://www.tinkercad.com/joinclass), avec le code de classe et ton identifiant d'élève. Pas d'adresse mail : les comptes sont créés par l'animateur.

<figure class="screenshot" markdown>
![Le tableau de bord Tinkercad, avec le bouton « Créer une première conception 3D »](../assets/rover-s03/21-tinkercad-accueil.png)
</figure>

**Conceptions 3D** → **Créer** ouvre le *plan de construction* : la grille sur laquelle tu poses tes formes. Les unités sont des **millimètres**.

<figure class="screenshot" markdown>
![Le plan de construction vide de Tinkercad, avec la palette des formes simples à droite](../assets/rover-s03/22-plan-de-construction.png)
</figure>

### Les quatre gestes

**Poser une forme** — tu la fais glisser de la palette vers le plan.

**La coter** — le panneau de propriétés donne longueur, largeur, hauteur. Tape les valeurs, ne les ajuste pas à la souris : la souris ne tombe jamais juste.

**Percer** — toute forme peut passer de **Solide** à **Perçage**. Une forme en perçage ne s'imprime pas : elle creuse ce qu'elle touche. C'est comme ça qu'on fait un trou.

**Regrouper** — <kbd>Ctrl</kbd> + <kbd>G</kbd>. Les formes sélectionnées deviennent une seule pièce, et les perçages sont creusés pour de bon.

> [!TIP] Regroupe en dernier
> Tant que tu n'as pas regroupé, tu peux tout déplacer et tout recoter. Après, c'est un bloc.

### Les îlots détachés

Dès que tu perces une forme de part en part, demande-toi **ce qui reste accroché à quoi**.

Le cas classique est le texte découpé : l'intérieur des lettres fermées — `o`, `b`, `a`, `d`, `p` — n'est relié à rien. Sur l'écran, ça se voit à peine. À l'impression, ces îlots se détachent, ou s'impriment à côté comme de petites pièces séparées.

<figure class="screenshot" markdown>
![Dans Tinkercad, les intérieurs des lettres o et b apparaissent comme des îlots détachés du reste de la plaque](../assets/rover-s03/26-contreformes-a-traiter.png)
</figure>

Deux façons de s'en sortir :

- **Relier** l'îlot au reste de la pièce par un pont de matière — c'est ce que font les typographies dites « au pochoir »
- **Effacer** l'îlot, en posant une forme en perçage par-dessus

La règle vaut au-delà du texte : **une pièce imprimée est d'un seul tenant, ou elle est plusieurs pièces.** Il n'y a pas d'entre-deux.

### Aligner plutôt que viser

Tinkercad a un outil **Aligner** : tu sélectionnes plusieurs formes, et des poignées apparaissent pour les caler à gauche, au centre, à droite, devant, au milieu, derrière.

<figure class="screenshot" markdown>
![L'outil d'alignement de Tinkercad, avec ses poignées de positionnement](../assets/rover-s03/25-outils-alignement.png)
</figure>

Centrer à la souris donne toujours un décalage d'un demi-millimètre qu'on ne voit qu'une fois la pièce imprimée.

### Vérifier avant d'exporter

Regarde ta pièce **de face**, pas seulement de dessus. C'est la seule vue qui montre les épaisseurs et les reliefs.

<figure class="screenshot" markdown>
![Vue de face d'une plaque dans Tinkercad, montrant le texte en relief sur l'épaisseur](../assets/rover-s03/27-vue-de-face-relief.png)
</figure>

### Exporter

**Exporter** → **La forme sélectionnée** → **.STL**

Le `.STL` est le format que comprennent toutes les imprimantes 3D. Les autres servent à autre chose : `.OBJ` et `.glb` pour l'image de synthèse, `.SVG` pour la découpe laser.

## L'impression

### Le principe : on ajoute, on n'enlève pas

Une imprimante 3D dépose du plastique fondu **couche par couche**, de bas en haut. C'est l'inverse du travail au cutter, où on retire de la matière.

> [!NOTE] Une pièce casse entre ses couches
> Les couches sont collées les unes aux autres, et ce collage est moins solide que le plastique lui-même. Une pièce se rompt donc presque toujours **dans le sens des couches**.
>
> Conséquence directe : on oriente une pièce pour que les efforts qu'elle subira soient **dans le plan des couches**, pas perpendiculaires.

### Le slicer

L'imprimante ne comprend pas ton modèle. Elle comprend des déplacements. Le **slicer** tranche ta pièce en couches et écrit la liste des mouvements à exécuter.

<figure class="screenshot" markdown>
![Le slicer affichant la plaque tranchée, avec l'aperçu des trajets et le réglage de hauteur de couche](../assets/rover-s03/31-slicer-apercu.png)
</figure>

Trois réglages décident de tout :

| Réglage | Ce que ça change |
|---|---|
| **Hauteur de couche** | Plus fin = plus beau et plus long. 0,2 mm est le compromis courant |
| **Remplissage** | Une pièce n'est **pas pleine** : l'intérieur est un maillage. Plus de remplissage = plus solide et plus lent |
| **Adhérence** | Si la première couche ne colle pas au plateau, tout le reste rate |

> [!CAUTION] Un plateau partagé est un risque partagé
> Toutes les plaques du groupe s'impriment ensemble. Si une pièce se décolle, elle peut faire rater ses voisines. C'est pour ça qu'on vérifie la disposition collectivement avant de lancer.

### Concevoir pour la machine

On ne dessine jamais dans le vide. Une pièce se dessine pour **une fonction** et pour **une machine**.

- **Ça doit tenir sur le plateau** — le tien et celui des autres
- **Ça doit tenir à l'usage** — assez de matière autour d'un trou, assez d'épaisseur sous un effort
- **Ça doit s'imprimer** — une forme qui surplombe dans le vide a besoin de supports, ou d'être réorientée

→ [Quand ça ne marche pas](depannage.md)
