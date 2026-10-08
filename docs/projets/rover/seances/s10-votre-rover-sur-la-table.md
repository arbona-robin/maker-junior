# Séance 10 — Votre rover sur la table

> [!NOTE] Nouveau concept : la bande et le groupe
> La table parle à tous les rovers sur la même bande, la `83`. Le **groupe**, votre numéro, dit à qui le message s'adresse. L'animateur le montre en début de séance.
>
> → [La bande de fréquence](../../../fiches/makecode-prise-en-main.md#la-bande-de-frequence)

1. **[Préparez le passage sur la table](#1-preparez-le-passage-sur-la-table)** : un bouton pour la table, un pour la télécommande.
2. **[Passez sur la table](#2-passez-sur-la-table)** : la table pilote votre rover le long d'une figure.

## 1. Préparez le passage sur la table

**Ce que vous allez obtenir :** `A`, votre rover écoute la table ; `B`, il écoute la télécommande. Un point dans un coin dit lequel.

<video controls playsinline preload="metadata" src="../../../../assets/rover-s08/video-table-pilote.mp4"></video>

`radio définir groupe` est dans **Radio**.

Un bouton par source : `A` pour la table, `B` pour la télécommande. Ici, l'équipe 10 :

```blocks
input.onButtonPressed(Button.A, function () {
    radio.setFrequencyBand(83)
    radio.setGroup(10)
})
input.onButtonPressed(Button.B, function () {
    radio.setFrequencyBand(10)
    radio.setGroup(0)
})
```

Une variable `mode` : `1` avec `A`, `0` avec `B`. Dans `toujours`, juste après `effacer l'écran`, un point témoin par mode : `0,0` et `4,0`. Deux programmes, un par mode, c'est permis aussi.

> [!TIP] Tester sans la table
> Mets ta télécommande sur la bande `83` et votre groupe. Si le rover lui obéit, il obéira à la table.

→ [Changer de mode](../../../fiches/makecode-prise-en-main.md#changer-de-mode)

## 2. Passez sur la table

**Ce que vous allez obtenir :** votre rover suit la figure de la table, et s'arrête quand elle se tait.

Une équipe à la fois, dans l'ordre du tableau. En attendant votre tour, avancez votre rover. La table vérifie :

- `avancer` : 5 cm au moins en 1,5 s
- `gauche` et `droite` : deux sens opposés
- la table se tait : le rover s'arrête en 1 s

Cochez ce qui passe sur votre feuille d'équipe.

## Va plus loin

- **Le parcours.** Entraînez-vous : slalom et pente, chronométrés. Notez votre temps.
