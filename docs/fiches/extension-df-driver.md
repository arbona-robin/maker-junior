# L'extension DF-Driver

MakeCode ne connaît pas ta carte moteur. Les blocs qui la pilotent sont fournis à part, dans une extension écrite par DFRobot — le fabricant de la carte.

## L'installer

Dans la palette, ouvre **Extensions**, et colle cette adresse dans la barre de recherche :

```
https://github.com/DFRobot/pxt-motor
```

<figure class="screenshot" markdown>
![La fenêtre Extensions, l'URL collée, la carte « motor » dans les résultats](../assets/rover-s01/25-extension-url-collee.png)
<figcaption>Clique sur la carte « motor » pour l'ajouter au projet.</figcaption>
</figure>

> [!NOTE] Ce qu'est une extension
> Une extension est une bibliothèque de blocs écrite par quelqu'un d'autre, que tu ajoutes à ton éditeur. Personne ne réécrit depuis zéro le code qui pilote un composant : on part de ce que le fabricant a publié.
>
> MakeCode prévient que l'extension est « fournie par l'utilisateur, non approuvée par Microsoft ». C'est normal — Microsoft ne vérifie que ses propres extensions. Celle-ci vient de DFRobot, qui fabrique la carte.
>
> L'extension est attachée **au projet**, pas à l'ordinateur. Un nouveau projet repartira sans elle.

Une catégorie orange, **DF-Driver**, apparaît alors dans la palette.

<figure class="screenshot" markdown>
![La catégorie DF-Driver dépliée, blocs Servo, Motor et Stepper](../assets/rover-s01/26-categorie-df-driver.png)
<figcaption>Les blocs de l'extension sont en anglais : elle n'est pas traduite en français.</figcaption>
</figure>

## Les blocs qu'on utilise

### Faire tourner un moteur

```
Motor  M1 ▾  dir  CW ▾  speed  100
```

| Champ | Valeurs | Ce que c'est |
|---|---|---|
| Premier menu | `M1` `M2` `M3` `M4` | Quel bornier de la carte. Sur le rover : `M1` et `M2`. |
| `dir` | `CW` `CCW` | Le sens. `CW` pour *clockwise*, dans le sens des aiguilles d'une montre ; `CCW` dans l'autre. |
| `speed` | `0` à `255` | La vitesse. `0` arrête, `255` est le maximum. |

Le bloc **lance** le moteur et rend la main aussitôt. Le moteur continue de tourner jusqu'à ce qu'on lui dise d'arrêter : c'est pour ça qu'un programme moteur a toujours une pause puis un arrêt derrière.

### Arrêter

```
Motor stop  M1 ▾        ← un seul moteur
Motor Stop All          ← tous les moteurs
```

Sur le rover, `Motor Stop All` est presque toujours le bon choix : il ne laisse rien tourner par oubli.

> [!TIP] Un moteur qui tourne à l'envers
> Ce n'est pas une erreur, c'est l'ordre des deux fils dans le bornier. Deux solutions, aussi valables l'une que l'autre : inverse les fils dans le bornier, ou change `CW` en `CCW` dans le bloc.
>
> Note ce que tu as choisi dans ton carnet de bord — dans deux séances, tu ne t'en souviendras plus.

### Les autres blocs

La catégorie contient aussi `Servo` et plusieurs blocs `Stepper`, pour d'autres types de moteurs. On ne s'en sert pas encore.

## Ce que veut dire `speed`

`speed` n'est pas une vitesse en tours par minute, c'est une **puissance envoyée au moteur**. La vitesse réelle dépend de ce que le rover a à pousser.

> [!NOTE] Le seuil de démarrage
> En dessous d'une certaine valeur, le moteur ne démarre pas du tout : il bourdonne sans tourner. Il faut plus de puissance pour vaincre le frottement de départ que pour entretenir le mouvement une fois lancé.
>
> Et ce seuil n'est pas fixe : un rover chargé démarre plus tard qu'un rover à vide. C'est une chose que tu constateras toi-même en équipant ton rover.

→ La carte et ses branchements : [La carte DFR0548](carte-dfr0548.md)
