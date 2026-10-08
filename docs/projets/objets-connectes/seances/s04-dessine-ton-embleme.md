# Séance 4 — Dessine l'emblème de ta lampe

1. **[Dessine ton emblème](#1-dessine-ton-embleme)** : ta forme, ton motif, et un trou pour l'accrocher.
2. **[Vérifie et exporte](#2-verifie-et-exporte)** : ton emblème validé part à l'impression.

## 1. Dessine ton emblème

**Ce que tu vas obtenir :**

<span class="todo-media">[photo : un emblème imprimé accroché à la lampe par un élastique]</span>

| | |
|---|---|
| Taille | **50 × 50 mm** au plus |
| Épaisseur | **3 mm** |
| Trou d'accroche | **5 mm**, avec 3 mm de matière autour |

> [!CAUTION] Les cotes ne se discutent pas
> Tous les emblèmes partent sur un seul plateau. Un emblème hors cotes ne part pas à l'impression.

[tinkercad.com/joinclass](https://www.tinkercad.com/joinclass) → code de classe, identifiant → **Créer** → nomme-la `lampe-<ton prénom>`.

→ [Modéliser et imprimer en 3D](../../../fiches/modeliser-imprimer-3d.md#tinkercad)

### Ta forme

Pars d'une forme simple (**Cylindre**, **Étoile**, **Cœur**, **Boîte**), ou dessine la tienne avec **Scribble**. Hauteur : 3 mm. Tape les cotes dans le panneau, ne les ajuste pas à la souris.

<span class="todo-media">[capture : une forme de base posée et cotée, 50 × 50 × 3 mm au plus]</span>

### Ton motif

Ton nom, un symbole, un motif : en **relief** (posé dessus), ou en **creux** (en **Perçage**, qui traverse). Centre avec l'outil **Aligner**, pas à l'œil.

<span class="todo-media">[capture : un texte et une forme posés sur la base, en relief]</span>

<figure class="screenshot" markdown>
![L'outil d'alignement de Tinkercad, avec ses poignées pour centrer les formes sélectionnées](../../../assets/rover-s03/23-outils-alignement.png)
</figure>

### Le trou d'accroche

Un **Cylindre** en **Perçage**, de 5 mm, près du bord. Au moins 3 mm de matière autour.

## 2. Vérifie et exporte

**Ce que tu vas obtenir :** ton emblème validé, exporté en `.STL`, prêt pour l'imprimante.

**Vue de face** : ce qui doit être en relief est posé sur la base, ce qui doit être en creux la traverse.

**Est-ce que tout tient ?** L'intérieur des lettres fermées (`o`, `b`, `a`, `d`) n'est relié à rien quand le texte est en creux.

<figure class="screenshot" markdown>
![Dans Tinkercad, les intérieurs des lettres o et b apparaissent comme des îlots détachés du reste de la plaque](../../../assets/rover-s03/29-contreformes-a-traiter.png)
<figcaption>Ils tombent, ou ils s'impriment tout seuls à côté.</figcaption>
</figure>

→ [Les îlots détachés](../../../fiches/modeliser-imprimer-3d.md#les-ilots-detaches)

> [!IMPORTANT] Point de contrôle
> Fais valider ton emblème avant d'exporter : cotes, trou, rien de détaché.

Sélectionne tout, **Regroupe** (<kbd>Ctrl</kbd> + <kbd>G</kbd>). Puis **Exporter** → **La forme sélectionnée** → **.STL**. Nomme le fichier `lampe-<ton prénom>.stl` et dépose-le dans le dossier partagé.

## Va plus loin

- **Deux hauteurs.** Un relief à 2 mm et un autre à 4 mm : ton emblème prend du volume.
- **Un emblème qui laisse passer la lumière.** Des motifs en creux qui traversent : posé devant la matrice, il laisse passer la lumière par ses trous.
