# Séance 4 — Dessine ton porte-clés pixel

1. **[Ta grille de pixels](#1-ta-grille-de-pixels)** : 64 pixels de 5 mm, en damier.
2. **[Ton dessin](#2-ton-dessin)** : ton personnage pixel, avec sa patte de porte-clés.
3. **[Vérifie et exporte](#3-verifie-et-exporte)** : ton porte-clés part à l'impression.

## 1. Ta grille de pixels

**Ce que tu vas obtenir :**

<span class="todo-media">[photo : le porte-clés pixel imprimé, à côté de la lampe qui affiche le même dessin]</span>

### Rejoins la classe Tinkercad

Va sur [tinkercad.com/joinclass](https://www.tinkercad.com/joinclass), entre le **code de classe** que donne l'animateur, puis ton **identifiant d'élève**.

<figure class="screenshot" markdown>
![La fenêtre « Rejoindre une classe » de Tinkercad, avec le champ pour le code fourni par l'enseignant](../../../assets/rover-s03/20-rejoindre-une-classe.png)
</figure>

### Un pixel

En bas à droite, **Grille d'accrochage** → **5,0 mm** : chaque forme se pose pile sur une case.

<figure class="screenshot" markdown>
![Le menu Grille d'accrochage de Tinkercad, ouvert, avec 5,0 mm sélectionné](../../../assets/objets-connectes-s04/20-grille-5mm.png)
</figure>

Pose une **Boîte**, et règle-la à **5 × 5 × 4 mm** : c'est ton premier pixel.

<figure class="screenshot" markdown>
![Le panneau d'une Boîte : longueur 5, largeur 5, hauteur 4](../../../assets/objets-connectes-s04/21-boite-5-5-4.png)
</figure>

> [!CAUTION] Les cotes ne se discutent pas
> Tous les porte-clés partent sur **un seul plateau d'imprimante** : 8 × 8 pixels au plus. Un porte-clés hors cotes ne part pas à l'impression.

### La grille

Passe en vue **de dessus**. Sélectionne ton pixel, **Dupliquer** (<kbd>Ctrl</kbd> + <kbd>D</kbd>), puis décale la copie d'une case avec une flèche du clavier. Recommence : huit pixels en rangée.

<figure class="screenshot" markdown>
![Une rangée de huit pixels rouges, collés les uns aux autres](../../../assets/objets-connectes-s04/22-rangee-de-8.png)
</figure>

Sélectionne la rangée, duplique-la, décale-la d'une case vers le haut. Huit rangées : ta grille de 8 × 8, la même que ta lampe.

<figure class="screenshot" markdown>
![Une grille de 8 × 8 pixels rouges, vue de dessus](../../../assets/objets-connectes-s04/23-grille-8x8.png)
</figure>

### Le damier

Sélectionne un pixel sur deux, en damier, en maintenant <kbd>Maj</kbd>. Règle leur **hauteur à 3 mm**, et donne-leur une autre couleur pour t'y retrouver. Imprimé d'une seule couleur, ce relief fait ressortir chaque pixel.

<figure class="screenshot" markdown>
![La grille en vue 3D : un pixel sur deux passé en orange et descendu à 3 mm, avec la palette de couleurs ouverte](../../../assets/objets-connectes-s04/24-damier-hauteur-3.png)
</figure>

Ton porte-clés peut prendre deux formes : en silhouette, ou en relief sur une plaque. Dans les deux cas, chaque pixel touche un voisin par un côté.

<figure markdown>
![Vu de dessus : à gauche, le smiley en relief sur une plaque ; au milieu, le smiley en silhouette avec sa patte de porte-clés ; à droite, deux pixels qui ne se touchent que par un coin, puis le pixel ajouté qui les relie par un côté](../../../assets/objets-connectes-s04/25-silhouette-relief-piege.png)
</figure>

## 2. Ton dessin

**Ce que tu vas obtenir :** ton personnage pixel, comme sur ta lampe.

Reprends le dessin de ta lampe, ou invente-le. Supprime les pixels éteints : il ne reste que ton dessin.

<figure class="screenshot" markdown>
![Un smiley en damier rouge et orange : les yeux et la bouche sont des cases vides, une Boîte de 10 × 10 mm attend au-dessus](../../../assets/objets-connectes-s04/26-smiley.png)
</figure>

**Chaque pixel touche un voisin par un côté.** Deux pixels qui ne se touchent que par un coin cassent à la première chute.

### La patte de porte-clés

Une **Boîte** de **10 × 10 × 2 mm**, collée au bord de ton dessin. Un **Cylindre** de **3 mm** de diamètre, centré dedans avec l'outil **Aligner**.

<figure class="screenshot" markdown>
![La patte de 10 × 10 mm posée au-dessus du smiley, le cylindre centré dedans par l'outil Aligner](../../../assets/objets-connectes-s04/27-patte-alignee.png)
</figure>

Passe le cylindre en **Perçage**. En vue **de face**, il doit traverser la patte, dessus et dessous.

<figure class="screenshot" markdown>
![Le cylindre en perçage traverse la patte, et son panneau montre Perçage sélectionné](../../../assets/objets-connectes-s04/28-trou-percage.png)
</figure>

## 3. Vérifie et exporte

**Ce que tu vas obtenir :** ton porte-clés regroupé en une seule pièce, exporté en `.STL`.

Sélectionne tout, puis **Regroupe** (<kbd>Ctrl</kbd> + <kbd>G</kbd>).

<figure class="screenshot" markdown>
![Le porte-clés regroupé en une seule pièce rouge : le smiley en damier, la patte et son trou](../../../assets/objets-connectes-s04/29-porte-cles-regroupe.png)
</figure>

**Est-ce que tout tient ?** Chaque pixel touche un voisin par un côté, et la patte touche ton dessin.

> [!IMPORTANT] Point de contrôle
> Fais valider ton porte-clés avant d'exporter. Après, il part à l'impression tel quel.

**Exporter** → **La forme sélectionnée** → **.STL**

<figure class="screenshot" markdown>
![La fenêtre Exporter de Tinkercad : La forme sélectionnée cochée, le bouton .STL](../../../assets/objets-connectes-s04/30-exporter-stl.png)
</figure>

Nomme le fichier `prenom-pixel.stl` et dépose-le où l'animateur te l'indique.

→ [Modéliser et imprimer en 3D](../../../fiches/modeliser-imprimer-3d.md)

## Va plus loin

- **En relief sur une plaque.** Plutôt qu'une silhouette : une plaque de 40 × 40 × 2 mm, et tes pixels posés dessus, à 2 et 1 mm en damier. Rien ne peut tomber, et les cases vides se lisent en creux.
