# La carte DFR0548 et ses blocs

C'est la carte sur laquelle s'enfiche ton micro:bit. Son nom complet est *Micro:bit Driver Expansion Board*. Elle fait le lien entre un micro:bit qui décide et des moteurs qui consomment.

<figure markdown>
![Schéma de la carte DFR0548 vue de dessus, avec ses zones encadrées et nommées : Motor Interface en haut, Power Input et Power Switch à droite, IIC Interface, Micro:bit IO Interface et Servo Interface à gauche, Micro:bit Adapter en bas](../assets/rover-s01/29-carte-dfr0548-reperes.png)
<figcaption>Les repères sont ceux du fabricant, en anglais.</figcaption>
</figure>

| Sur le schéma | Ce que c'est |
|---|---|
| **Motor Interface** | Les borniers `M1` à `M4` |
| **Power Input** | L'entrée des accus, `3.5~5.5V` |
| **Power Switch** | L'interrupteur `ON` / `OFF` des moteurs |
| **Micro:bit Adapter** | Le connecteur du micro:bit |
| **Servo Interface** | Les broches à servomoteurs `S1` à `S8` |
| **IIC Interface** | Le bus entre la carte et le micro:bit |
| **Micro:bit IO Interface** | Les broches `P0` à `P16` ressorties |

## Pourquoi elle existe

> [!NOTE] Trois choses qu'une broche ne peut pas faire
> **Fournir assez de courant.** Une broche de micro:bit délivre quelques milliampères — de quoi allumer une LED. Un moteur à courant continu en réclame plusieurs centaines. Branché en direct, le moteur ne tourne pas, et la broche risque de lâcher.
>
> **Inverser le sens.** Une broche envoie du courant ou n'en envoie pas. Pour faire tourner un moteur dans l'autre sens, il faut inverser la polarité à ses bornes — ce qu'aucune broche ne peut faire seule.
>
> **Doser la vitesse.** Il faut découper l'alimentation en impulsions très rapides et régler leur durée. La carte s'en charge, en continu, sans que le micro:bit ait à s'en occuper.

Le partage des rôles est donc :

| Qui | Fait quoi |
|---|---|
| **Le micro:bit** | décide : quel moteur, quel sens, quelle vitesse |
| **La carte** | exécute : elle commute la puissance et découpe le courant |
| **Les accus** | fournissent l'énergie |

## Deux sources d'énergie, séparées

C'est le point qui surprend le plus au début.

Le micro:bit est alimenté par l'USB ou par sa propre pile. Les moteurs sont alimentés par le pack d'accus branché sur la carte. **Ce ne sont pas les mêmes circuits.**

Conséquence pratique : ton programme peut tourner parfaitement — écran allumé, animations, sons — pendant que les moteurs restent immobiles, simplement parce que le pack est débranché ou l'interrupteur sur *off*. C'est même la panne numéro un.

→ [Déboguer](deboguer.md)

## Les branchements

Avant de câbler quoi que ce soit : **interrupteur de la carte sur *off***. On ne visse jamais un fil sur un circuit sous tension.

**Le micro:bit** s'enfiche dans le connecteur de la carte, **écran vers l'extérieur**, boutons A et B accessibles. Le connecteur est détrompé : il ne rentre que dans un sens. S'il résiste, il est à l'envers — ne force pas, retourne-le.

<figure markdown>
![Le micro:bit en train d'être enfiché dans le connecteur de la carte d'extension, écran vers l'extérieur](../assets/rover-s01/17-microbit-sur-carte.jpg)
<figcaption>Le connecteur est détrompé. S'il résiste, retourne le micro:bit.</figcaption>
</figure>

**Les moteurs** se vissent sur les borniers verts repérés `M1`, `M2`, `M3`, `M4`. Sur le rover, on utilise `M1` et `M2`.

Chaque moteur sort deux fils : desserre la vis, glisse la partie dénudée, resserre. Puis **tire doucement sur le fil** : s'il ressort, il n'était pas serré, et il ressortira tout seul à la première secousse.

<figure markdown>
![Un fil de moteur glissé dans le bornier, tournevis sur la vis](../assets/rover-s01/18-fil-dans-bornier.jpg)
<figcaption>Desserrer, glisser le fil dénudé, resserrer — puis tirer dessus pour vérifier.</figcaption>
</figure>

L'ordre des deux fils d'un moteur détermine son sens de rotation. Il n'y a pas de bon ou de mauvais branchement : si un moteur tourne à l'envers, tu peux soit inverser ses deux fils, soit changer `CW` en `CCW` dans le code.

**Les servomoteurs** s'enfichent sur les broches `S1` à `S8`, trois broches par servomoteur. Le connecteur a un sens : **fil orange côté rangée verte, rouge sur la rouge, marron côté rangée noire.** Le bloc `Servo` de DF-Driver prend le même numéro de broche.

<figure markdown>
![Deux connecteurs de servomoteur enfichés sur S8 et S7, fil orange sur la rangée verte, fil marron sur la rangée noire](../assets/rover-s07/02-branchement-s7-s8.jpg)
</figure>

**Le pack d'accus** se visse sur le bornier d'alimentation — le petit connecteur vert à deux vis, marqué `3.5~5.5V`, à l'écart du bornier des moteurs. Fil rouge sur `+`, fil noir sur `−`. La carte accepte de 3,5 à 5,5 V ; un pack de quatre accus NiMH fournit environ 4,8 V.

> [!CAUTION] La polarité ne se rattrape pas
> Inverser le `+` et le `−` peut détruire la carte. C'est le seul geste du montage qui abîme du matériel pour de bon. Vérifie deux fois avant de basculer l'interrupteur, et fais contrôler si tu as le moindre doute.

**L'interrupteur** de la carte coupe l'alimentation des moteurs. Prends l'habitude de le laisser sur *off* pendant que tu manipules le rover.

## Les dangers

> [!CAUTION] Un moteur alimenté part tout seul
> Un moteur branché part à pleine vitesse, entraîne ce à quoi il est fixé, et le fait tomber de la table. Avec une roue montée, un rover traverse un bureau en une seconde.
>
> **Tout essai de moteur se fait dans la boîte en carton de test.** Le rover y reste tant qu'il n'est pas sur la piste.

Attention aussi aux cheveux longs, aux cordons de sweat et aux manches larges près d'un axe qui tourne : ça s'enroule très vite. Et avant de brancher, vérifie qu'aucun doigt n'est entre une roue et le châssis.

> [!CAUTION] Les accus
> Les accus NiMH ne prennent pas feu, mais ils délivrent beaucoup de courant d'un coup si on les met en court-circuit.
>
> - Respecte le `+` et le `−` en vissant les fils au bornier.
> - Ne laisse pas deux fils dénudés se toucher.
> - Si un pack chauffe, débranche-le et préviens.
> - En fin de séance, les packs vont en charge, pas dans le bac.

## Comment le micro:bit lui parle

Le micro:bit et la carte communiquent sur deux fils seulement, par un dialogue qu'on appelle **I2C**. Chaque appareil branché sur ces deux fils possède une adresse ; quand le micro:bit envoie un ordre, il commence par dire à qui il s'adresse, et seul l'appareil concerné répond.

C'est la même idée que d'appeler quelqu'un par son prénom dans une pièce où tout le monde entend — et c'est exactement ce que fait la radio quand plusieurs rovers partagent le même groupe.

Tu n'as rien à programmer de tout ça : les blocs de l'extension s'en occupent.

→ [La radio](makecode-prise-en-main.md#la-radio)

MakeCode ne fournit pas les blocs de cette carte. Ils sont publiés à part, dans une extension écrite par DFRobot.

## L'extension DF-Driver

### L'installer

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

### Les blocs

#### Faire tourner un moteur

```
Motor  M1 ▾  dir  CW ▾  speed  100
```

| Champ | Valeurs | Ce que c'est |
|---|---|---|
| Premier menu | `M1` `M2` `M3` `M4` | Quel bornier de la carte. Sur le rover : `M1` et `M2`. |
| `dir` | `CW` `CCW` | Le sens. `CW` pour *clockwise*, dans le sens des aiguilles d'une montre ; `CCW` dans l'autre. |
| `speed` | `0` à `255` | La vitesse. `0` arrête, `255` est le maximum. |

Le bloc **lance** le moteur et rend la main aussitôt. Le moteur continue de tourner jusqu'à ce qu'on lui dise d'arrêter : c'est pour ça qu'un programme moteur a toujours une pause puis un arrêt derrière.

#### Arrêter

```
Motor stop  M1 ▾        ← un seul moteur
Motor Stop All          ← tous les moteurs
```

Sur le rover, `Motor Stop All` est presque toujours le bon choix : il ne laisse rien tourner par oubli.

> [!TIP] Un moteur qui tourne à l'envers
> Ce n'est pas une erreur, c'est l'ordre des deux fils dans le bornier. Deux solutions, aussi valables l'une que l'autre : inverse les fils dans le bornier, ou change `CW` en `CCW` dans le bloc.
>
> Note ce que tu as choisi dans ton carnet de bord — dans deux séances, tu ne t'en souviendras plus.

#### Les autres blocs

La catégorie contient aussi `Servo S1 degree 0`, pour un servomoteur — la broche, puis l'angle de 0 à 180° —, et plusieurs blocs `Stepper`, pour les moteurs pas à pas.

### Ce que veut dire `speed`

`speed` n'est pas une vitesse en tours par minute, c'est une **puissance envoyée au moteur**. La vitesse réelle dépend de ce que le rover a à pousser.

> [!NOTE] Le seuil de démarrage
> En dessous d'une certaine valeur, le moteur ne démarre pas du tout : il bourdonne sans tourner. Il faut plus de puissance pour vaincre le frottement de départ que pour entretenir le mouvement une fois lancé.
>
> Et ce seuil n'est pas fixe : un rover chargé démarre plus tard qu'un rover à vide. C'est une chose que tu constateras toi-même en équipant ton rover.

→ [Rouler droit et tourner](rouler-droit.md) · [Déboguer](deboguer.md)
