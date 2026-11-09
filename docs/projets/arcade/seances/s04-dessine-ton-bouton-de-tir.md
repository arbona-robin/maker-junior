# Séance 4 — Dessine ton bouton de tir

1. **[Ton capuchon à la bonne taille](#1-ton-capuchon-a-la-bonne-taille)** : le bouton d'arcade, importé dans Tinkercad, fait 40 mm.
2. **[Ton capuchon à toi](#2-ton-capuchon-a-toi)** : ta forme, ton texte, et le fichier parti à l'impression.
3. **[Ton bouton en carton](#3-ton-bouton-en-carton)** : il fait contact quand tu appuies.

## 1. Ton capuchon à la bonne taille

**Ce que tu vas obtenir :** un capuchon de bouton d'arcade, importé dans Tinkercad et ramené à 40 mm de diamètre, sans être déformé.

### Rejoins la classe Tinkercad

Va sur [tinkercad.com/joinclass](https://www.tinkercad.com/joinclass), entre le **code de classe** que donne l'animateur, puis ton **identifiant d'élève**. Crée un nouveau design.

### Importe le capuchon

Télécharge **[capuchon-52mm.stl](../../../assets/arcade-s04/capuchon-52mm.stl)**. Dans Tinkercad, **Importer**, en haut à droite, puis choisis ce fichier.

<figure class="screenshot" markdown>
![La fenêtre Importer une forme 3D de Tinkercad : capuchon-52mm.stl, unités en millimètres, échelle 100 %, cotes 51,98 × 52 × 14,05 mm](../../../assets/arcade-s04/20-importer-le-capuchon.png)
</figure>

Il fait 52 mm. Le plan de ton bouton prévoit 40 mm : il est trop grand.

### Mets-le à l'échelle

Dans **Échelle (%)**, écris le rapport entre la taille voulue et la taille actuelle : 40 ÷ 52 × 100 ≈ **77**. Puis **Importer**.

> [!NOTE] Un modèle trouvé en ligne
> Il arrive rarement à la bonne taille. On le mesure, on calcule l'échelle, et on change toutes les cotes ensemble : la forme reste la même.

> [!TIP] Ça marche si…
> La règle de Tinkercad mesure 40 mm de diamètre.

## 2. Ton capuchon à toi

**Ce que tu vas obtenir :** ton capuchon personnalisé, regroupé en une seule pièce, exporté en `.STL`.

La forme et le texte sont à toi. Deux contraintes : **40 mm de diamètre au plus**, sinon il dépasse de ton bouton, et **le dessous plat**, pour le coller.

Un exemple : aplatir le sommet du dôme pour y poser un texte.

<div class="photo-row" markdown>
<figure class="screenshot" markdown>
![Vue de face : une boîte en mode Perçage, hachurée en gris, posée sur le sommet du dôme rose](../../../assets/arcade-s04/21-boite-percage.png)
<figcaption>Une boîte en **Perçage** sur le sommet…</figcaption>
</figure>
<figure class="screenshot" markdown>
![Vue de face : le capuchon au sommet plat, après le regroupement](../../../assets/arcade-s04/22-dessus-aplati.png)
<figcaption>… puis **Regrouper** : le sommet est plat.</figcaption>
</figure>
</div>

<div class="photo-row" markdown>
<figure class="screenshot" markdown>
![Vue de dessus : la forme Texte, le mot TEXT en rouge, posée au centre du capuchon](../../../assets/arcade-s04/23-le-texte.png)
<figcaption>La forme **Texte**, posée sur le sommet…</figcaption>
</figure>
<figure class="screenshot" markdown>
![Le capuchon terminé, en perspective : le mot FEU ! en relief rouge sur le sommet plat](../../../assets/arcade-s04/24-capuchon-feu.png)
<figcaption>… en relief, ou en Perçage pour la creuser.</figcaption>
</figure>
</div>

→ [Modéliser et imprimer en 3D](../../../fiches/modeliser-imprimer-3d.md#importer-et-modifier-une-piece)

> [!IMPORTANT] Point de contrôle
> Fais valider ton capuchon avant d'exporter. Après, il part à l'impression tel quel.

Sélectionne tout, **Regroupe**, puis **Exporter** → **La forme sélectionnée** → **.STL**. Nomme le fichier `prenom-capuchon.stl` et dépose-le où l'animateur te l'indique.

## 3. Ton bouton en carton

**Ce que tu vas obtenir :** un bouton plié, avec deux bandes de cuivre face à face qui se touchent quand tu appuies.

<figure markdown>
![Le plan du bouton de tir, quatre par page : une pièce de 55 × 89 mm, deux plis rapprochés au milieu qui forment la charnière, une bande de cuivre de 40 mm sur chaque face, l'une depuis le bord gauche, l'autre depuis le bord droit, une encoche en face du bout de chaque bande, et le cercle du capuchon de 40 mm sur la face du haut](../../../assets/plans/bouton-de-tir-v1.png)
<figcaption>[Le plan à imprimer](../../../assets/plans/bouton-de-tir-v1.pdf), en A4 à 100 %, quatre boutons par page.</figcaption>
</figure>

> [!CAUTION] L'outil de découpe
> - Règle métallique **à rebord**, toujours.
> - Doigts **posés sur la règle, derrière le rebord**.
> - **Plusieurs passes légères**, sans forcer.
> - **Protection de lame remise** dès que tu poses l'outil.

1. Découpe le contour, et marque les deux plis. → [Tracer, découper, plier le carton](../../../fiches/carton-tracer-decouper-plier.md)
2. Colle le ruban de cuivre côté imprimé, sur les deux bandes orange.
3. Plie à la charnière, côté imprimé dedans, et tiens le bouton fermé avec deux élastiques.

<div class="photo-row" markdown>
<figure markdown>
![Le bouton déplié : la pièce de carton, une bande de cuivre sur chaque face, une encoche sur chaque face en face du bout de l'autre bande, les plis de la charnière au milieu](../../../assets/arcade-s04/01-bouton-deplie.jpg)
</figure>
<figure markdown>
![Le bouton plié : à travers l'encoche, on voit le bout de la bande de cuivre de la face d'en dessous](../../../assets/arcade-s04/02-bouton-plie.jpg)
</figure>
<figure markdown>
![Le bouton fermé par deux élastiques, le bout de chaque bande visible dans son encoche](../../../assets/arcade-s04/03-bouton-ferme.jpg)
</figure>
</div>

### Teste-le

Une pince dans chaque encoche : elle y mord le bout d'une seule bande. Le multimètre, en continuité, bipe quand les deux bandes se touchent.

<video controls playsinline preload="metadata" src="../../../../assets/arcade-s04/video-test-multimetre.mp4"></video>

> [!TIP] Ça marche si…
> Le multimètre affiche OL au repos, et bipe quand tu appuies. Il bipe sans que tu appuies ? Desserre les élastiques, ou vérifie qu'une pince ne mord pas les deux faces.

Ton capuchon s'imprime pendant la semaine : tu le colles sur ton bouton à la séance 5.

## Va plus loin

Un second capuchon, d'une autre forme (étoile, cœur, flèche), pour un second bouton : ta manette en aura besoin si ton jeu utilise B.
