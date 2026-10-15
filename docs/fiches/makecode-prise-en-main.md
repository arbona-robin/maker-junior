# Prendre en main MakeCode

MakeCode est l'éditeur dans lequel tu écris tes programmes. Il s'ouvre dans un navigateur, à [makecode.microbit.org](https://makecode.microbit.org). Rien à installer.

## Créer un projet

Sur la page d'accueil, **Nouveau projet**, puis un nom.

<figure class="screenshot" markdown>
![La page d'accueil de MakeCode, section « Mes projets »](../assets/rover-s01/20-makecode-accueil.png)
<figcaption>Tes projets restent dans le navigateur de l'ordinateur où tu les as créés.</figcaption>
</figure>

> [!TIP] Un projet, plusieurs séances
> Donne un nom clair dès le début, par exemple `rover`, et reviens dans le même projet d'une séance à l'autre plutôt que d'en créer un nouveau à chaque fois.
>
> Les projets sont enregistrés dans le navigateur, pas dans un compte. Sur un autre ordinateur, tu ne les retrouveras pas. Si tu changes de poste, utilise le bouton de partage pour récupérer un lien vers ton projet.

## L'écran

Trois zones, de gauche à droite.

**Le simulateur** : un micro:bit dessiné qui exécute ton programme en direct, avant même de le téléverser. Il affiche l'écran, réagit aux boutons, joue les sons. Pratique pour tester une animation sans brancher la carte.

**La palette** : les catégories de blocs, chacune sa couleur. Base, Entrée, Musique, LED, Radio, Boucles, Logique, Variables, Maths, puis Extensions et Avancé.

**L'espace de travail** : où tu assembles tes blocs.

En bas à gauche, le bouton **Télécharger**. En haut au centre, la bascule **Blocs / JavaScript / Python**.

## Les deux blocs de départ

Un projet neuf contient déjà deux blocs.

`au démarrage` s'exécute **une seule fois**, au moment où la carte s'allume ou redémarre. C'est là qu'on met ce qui se règle au début.

`toujours` s'exécute **en boucle, sans fin**, tant que la carte est alimentée. Arrivé en bas, il repart en haut. C'est là qu'on met ce qui doit se répéter.

> [!NOTE] Pourquoi il faut des pauses
> La carte exécute les instructions bien plus vite que l'œil ne suit. Un `toujours` qui allume puis éteint l'écran sans pause produit une image grise et immobile, pas un clignotement.
>
> Le bloc `pause (ms)` se règle en millisecondes : `1000` ms font une seconde. C'est lui qui rend un programme visible.

## Téléverser

Branche le micro:bit en USB, clique sur **Télécharger**, et suis les instructions.

<figure class="screenshot" markdown>
![La fenêtre « 1. Connectez votre micro:bit à votre ordinateur »](../assets/rover-s01/28-televersement.png)
<figcaption>La première fois, l'éditeur demande l'autorisation d'accéder à la carte.</figcaption>
</figure>

La LED jaune au dos de la carte clignote pendant le transfert. Quand elle s'arrête, le programme démarre.

> [!TIP] Sache que ton programme tourne
> Mets toujours une icône et un son dans `au démarrage`. Quand quelque chose ne marchera pas, tu sauras au premier coup d'œil si c'est bien ton programme qui s'exécute, et tu t'épargneras de chercher dans le code un problème qui est dans les fils.

Une fois téléversé, le programme est **dans la carte**. Débranche l'USB, alimente par les accus : il repart tout seul. L'ordinateur n'est plus nécessaire.

## Les fonctions

Une fonction est un bloc que **tu** fabriques : tu lui donnes un nom, tu mets des blocs dedans, et tu l'appelles ensuite par son nom.

**Fonctions** → **Créer une fonction…** → nomme-la → **Terminé**.

<figure class="screenshot" markdown>
![La catégorie Fonctions dépliée dans MakeCode, avec le bouton « Créer une fonction… »](../assets/rover-s02/20-categorie-fonctions.png)
</figure>

Le nouveau bloc `fonction <nom>` apparaît dans l'espace de travail : glisse tes blocs dedans. Un bloc `appel <nom>` apparaît en même temps dans la catégorie **Fonctions**. C'est lui que tu places dans `toujours` ou dans `au démarrage`.

> [!NOTE] À quoi ça sert
> À écrire une fois ce qu'on utilise dix fois, et à se relire. `appel avancer` se comprend sans lire le détail ; trois blocs moteur avec des chiffres, non.

Deux règles qui évitent des heures perdues :

- **Un nom qui dit ce que ça fait.** `avancer`, pas `fonction2`.
- **On modifie la fonction, jamais ses copies.** Change la vitesse dans `avancer`, et tous les appels suivent.

Pour renommer une fonction ou lui ajouter un paramètre : clique sur la roue dentée du bloc `fonction`.

## Les variables

Une variable est une **boîte nommée** qui retient une valeur. Tu y ranges quelque chose, tu le relis quand tu veux.

**Variables** → **Créer une variable…** → donne-lui un nom qui dit ce qu'elle contient.

<figure class="screenshot" markdown>
![La fenêtre « Nom de la nouvelle variable » dans MakeCode](../assets/rover-s03/41-creer-variable.png)
</figure>

Deux blocs suffisent : `définir <nom> à …` pour y mettre une valeur, et le bloc `<nom>` lui-même pour la relire.

## Un interrupteur : basculer un état

Un même bouton allume puis éteint : à chaque appui, une variable passe de `0` à `1`, ou de `1` à `0`. Elle retient l'**état**, et le reste du programme le lit.

```blocks
input.onButtonPressed(Button.A, function () {
    if (marche == 0) {
        marche = 1
        basic.showIcon(IconNames.Yes)
    } else {
        marche = 0
        basic.showIcon(IconNames.No)
    }
})
let marche = 0
```

Ailleurs dans le programme, `si marche = 1` décide de ce qui se passe en marche. Les bandes de cuivre font aussi un bouton : `lorsque la broche P2 est activée`, dans **Entrée**, se déclenche une fois à chaque toucher, quand le doigt relie `P2` et `GND`.

## Répéter en comptant

`pour index variant de 0 à 4`, dans **Boucles**, répète ce qu'il contient en comptant : `index` vaut 0 au premier tour, 1 au deuxième, et ainsi de suite jusqu'à 4. Glisse `index` dans un bloc, et chaque tour fait un peu autre chose.

```blocks
for (let index = 0; index <= 4; index++) {
    led.plot(index, 2)
    basic.pause(200)
}
```

Les LED du milieu s'allument une à une, de gauche à droite.

## Les capteurs, et la décision

Un capteur ne dit jamais « penche à gauche ». Il dit `-247`. Il faut donc **transformer un nombre en décision**, et c'est le même geste pour un thermostat, un détecteur de présence, un capteur de ligne ou une télécommande.

### 1. Regarde avant de décider

La faute classique est d'écrire le test avant d'avoir vu les chiffres. On se trompe de signe, d'ordre de grandeur, d'axe, et on cherche ensuite dans le code un problème qui n'y est pas.

Affiche les valeurs brutes, dans `toujours` :

```blocks
basic.forever(function () {
    serial.writeValue("x", input.acceleration(Dimension.X))
})
```

Téléverse, puis **Afficher données Appareil**. Bouge la carte et regarde les courbes.

> [!NOTE] La communication série
> `série écrire valeur` n'affiche rien sur la carte : il **envoie** les valeurs à l'ordinateur par la liaison série, dans le câble USB. C'est pour ça qu'il faut rester branché pour voir quelque chose, et c'est aussi pour ça que ces blocs ne servent qu'à la mise au point : une fois le rover autonome, personne ne les lit plus.

<figure class="screenshot" markdown>
![Afficher données Appareil : la courbe de x en haut, celle de y en dessous, qui montent et descendent quand on incline la carte, et la liste des valeurs reçues](../assets/rover-s04/21-afficher-donnees-x-y.png)
</figure>

Trois questions, à chaque fois, et pour n'importe quel capteur :

- **Quelle valeur au repos ?** C'est ton point zéro, et il n'est pas forcément à 0.
- **Ça monte ou ça descend** quand tu fais le geste ?
- **Jusqu'où ça va ?** Un capteur qui varie de 40 et un qui varie de 1000 ne se traitent pas pareil.

### L'accéléromètre du micro:bit

Il mesure une accélération sur trois axes, en **mg** (millièmes de g). À plat, écran vers le haut, la pesanteur donne environ `-1000` sur `z` et environ `0` sur `x` et `y`.

| Axe | Ce qu'il mesure |
|---|---|
| `x` | L'inclinaison gauche / droite, le **roulis** |
| `y` | L'inclinaison avant / arrière, le **tangage** |
| `z` | Le haut et le bas |
| `force` | L'intensité totale, tous axes confondus |

### Le capteur de lumière

Le micro:bit mesure la lumière avec **son écran**. `niveau d'intensité lumineuse`, dans **Entrée**, va de `0` (noir) à `255` (pleine lumière).

Trois conséquences : l'écran doit voir la pièce, il ne doit rien afficher pendant la mesure, et on ne le touche pas. Une icône allumée ou un doigt posé sur la carte fausse la valeur : pour faire de l'ombre, la main passe au-dessus sans toucher, ou un objet se pose devant.

> [!CAUTION] Un objet qui se voit lui-même
> Si la lumière de ta lampe arrive sur l'écran du micro:bit, elle s'allume, se voit, s'éteint, et recommence.

### 2. Choisis un seuil

Un seuil est la valeur à partir de laquelle tu décides que **ça compte**.

> [!NOTE] Pourquoi il en faut un
> Une carte posée à plat n'affiche jamais exactement `0`. Elle oscille, elle vibre, la table n'est pas d'équerre. Sans seuil, ta télécommande part dans tous les sens toute seule.

**Trop bas**, ça se déclenche sans que tu bouges. **Trop haut**, il faut pencher la carte à la verticale pour obtenir quelque chose. Entre les deux, il y a une zone morte confortable.

> [!TIP] Il n'y a pas de bon seuil
> Comme pour les vitesses de tes moteurs : le tien dépend de ta main et de ta façon de tenir la carte. Note-le, ne le recopie pas.

### 3. Écris la décision

Les blocs sont dans **Logique** : `si … alors`, et le `+` du bloc pour ajouter `sinon si` et `sinon`.

<figure class="screenshot" markdown>
![La catégorie Logique de MakeCode, avec les blocs si/alors et les comparaisons](../assets/rover-s03/42-categorie-logique.png)
</figure>

Compare directement la mesure au seuil :

```blocks
basic.forever(function () {
    basic.clearScreen()
    if (input.acceleration(Dimension.Y) < -200) {
        led.plot(2, 0)
    } else if (input.acceleration(Dimension.Y) > 200) {
        led.plot(2, 4)
    } else {
        led.plot(2, 2)
    }
})
```

**`effacer l'écran` est en tête de la boucle.** Chaque tour éteint tout, puis rallume un seul point. Sans lui, les points s'accumulent.

L'ordre compte : le premier test vrai gagne, les suivants ne sont même pas lus. Mets en premier ce qui doit primer.

### 4. Ne réagis qu'au changement

Dans `toujours`, la décision se prend plusieurs fois par seconde. Si l'action ne doit arriver qu'une fois (un son, un message radio), elle se répète à chaque tour.

La parade est une **variable d'état** : elle garde en mémoire ce que l'objet fait déjà.

```blocks
basic.forever(function () {
    if (input.lightLevel() < 50 && allumee == 0) {
        basic.showIcon(IconNames.Heart)
        allumee = 1
    } else if (input.lightLevel() > 50 && allumee == 1) {
        basic.clearScreen()
        allumee = 0
    }
})
let allumee = 0
```

On ne déclenche qu'au **changement** : on s'arme, on se désarme. C'est le même raisonnement pour toutes les alertes.

> [!TIP] Deux seuils
> À la limite, la mesure oscille et l'objet clignote. Un seuil pour allumer, un autre un peu plus haut pour éteindre : entre les deux, rien ne bouge. C'est l'**hystérésis**.

### Afficher vite

> [!CAUTION] `montrer la flèche` bloque 400 ms
> `montrer la flèche`, `montrer l'icône` et `montrer les LED` **attendent après avoir affiché** 400 ms, et en blocs cette durée n'est pas réglable. Dans une boucle qui lit un capteur en continu, le programme ne relit la mesure que deux fois et demie par seconde.
>
> `allumer x y`, dans **LED**, n'attend pas.

<figure markdown>
![Schéma du micro:bit : la grille de 5 sur 5 LED, colonnes numérotées 0 à 4 pour x, lignes numérotées 0 à 4 pour y, avec le repère X vers la droite et Y vers le bas](../assets/rover-s03/34-grille-led-xy.png)
<figcaption>Le coin en haut à gauche est `0,0`.</figcaption>
</figure>

Cinq points suffisent à faire une manette lisible : haut `2,0`, bas `2,4`, gauche `0,2`, droite `4,2`, repos `2,2`.

## La radio

Deux micro:bit communiquent sans fil, sans réseau et sans rien à installer. Les blocs sont dans la catégorie **Radio**.

### La bande de fréquence

Deux cartes ne se parlent que si elles émettent **au même endroit du spectre**. Un seul bloc, dans `au démarrage`, **sur chacune des deux cartes** :

```blocks
radio.setFrequencyBand(15)
```

Le numéro va de `0` à `83`, un mégahertz par pas à partir de 2400 : la bande `15` est à 2415 MHz. Par défaut, une carte neuve est sur la bande `7`. Le réglage ne s'applique qu'à une vraie carte : dans le simulateur du navigateur, le bloc ne fait rien.

> [!NOTE] Bande ou groupe ?
> `radio définir groupe` trie aussi les conversations, mais toutes les cartes restent sur la même fréquence : elles s'entendent et filtrent à l'arrivée. Quand une salle entière émet en continu, les messages se gênent quoi qu'il arrive. La bande sépare vraiment les cartes : c'est elle qu'on utilise ici.
>
> Ni l'une ni l'autre ne rend la liaison plus sûre : n'importe qui peut se régler sur la tienne et écouter.

### La puissance et la portée

La **puissance d'émission** se règle de `0` à `7`, dans `au démarrage`. Par défaut, une carte émet à `6`.

```blocks
radio.setTransmitPower(4)
```

Plus de puissance, c'est plus de portée, mais des accus qui se vident plus vite. Les murs, le métal et les corps affaiblissent le signal.

La carte qui reçoit mesure la **force du signal**, en dBm : autour de `-40` tout près, `-100` à la limite. Sur le tableau de bord, elle s'affiche en haut de chaque carte, en dBm et en barres.

Le bon réglage : la puissance la plus basse qui garde au moins deux barres depuis l'emplacement.

### Envoyer, recevoir

Trois façons d'envoyer un message. En face, trois blocs portent le même nom, `quand une donnée est reçue par radio` : chacun n'entend que son type de message.

**Un nombre.** `envoyer le nombre … par radio`. Le bloc qui reçoit apporte `receivedNumber`.

```blocks
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(7)
})
radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
```

**Un mot.** `envoyer la chaîne … par radio`, 19 caractères au plus. Le bloc qui reçoit apporte `receivedString`.

```blocks
input.onButtonPressed(Button.A, function () {
    radio.sendString("bonjour")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
```

**Une clé et une valeur.** `envoyer la valeur … = …`, un mot et un nombre : une vitesse, une distance, une mesure. Le bloc qui reçoit apporte `nom` (la clé) et `valeur` (le nombre).

```blocks
input.onButtonPressed(Button.A, function () {
    radio.sendValue("temp", input.temperature())
})
radio.onReceivedValue(function (name, value) {
    if (name == "temp") {
        basic.showNumber(value)
    }
})
```

Ici, la carte envoie sa température avec la clé `temp`, et celle qui la reçoit l'affiche.

Avec un mot ou une clé, on teste ce qui est reçu pour savoir quoi faire. Attention au bloc de comparaison : il en existe deux, et celui qui compare des **textes** a deux cases blanches. Celui qui compare des nombres ne marchera pas ici.

> [!CAUTION] La clé fait 8 caractères, pas un de plus
> Avec une clé et une valeur, la carte tronque la clé sans prévenir au-delà de 8 caractères.

| Ce que tu tapes | Ce qui part vraiment |
|---|---|
| `tournerAGauche` | `tournerA` |
| `tournerADroite` | `tournerA` |
| `gauche` | `gauche` |
| `droite` | `droite` |

Deux clés qui commencent pareil deviennent **le même message**. Le programme est juste, il se relit sans qu'on trouve rien, et le rover désobéit : compte les caractères avant de coder.

### Message diffusé, message adressé

Quand toutes les cartes sont sur la même bande, elles entendent **tous** les messages.

- Un message **diffusé** concerne tout le monde : chaque carte qui l'entend réagit.
- Un message **adressé** ne concerne qu'une carte. L'adresse est dans la clé : `inter7` est pour la lampe 7. Toutes l'entendent, et chacune ne réagit qu'à sa propre clé.

```blocks
radio.onReceivedValue(function (name, value) {
    if (name == "inter7") {
        active = value
    }
})
let active = 0
```

### Se mettre d'accord avant de coder

Deux machines qui échangent doivent s'entendre sur **le canal** et sur **le vocabulaire**. Cet accord s'appelle un **protocole**, et il s'écrit avant le programme.

| Mot | Ce que fait le rover |
|---|---|
| `avancer` | Les deux moteurs en avant |
| `reculer` | Les deux moteurs en arrière |
| `gauche` | Tourne à gauche |
| `droite` | Tourne à droite |
| `arreter` | Tout s'arrête |

### Quand rien ne passe

La radio est muette : elle ne signale ni l'échec, ni le succès. **Fais-la parler toi-même** : une flèche, une icône, un son à chaque message envoyé et à chaque message reçu. C'est le seul moyen de voir où la chaîne se coupe.

| Ce que tu vois | Où chercher |
|---|---|
| Rien ne s'affiche, même côté émetteur | Le programme n'envoie pas : seuils, conditions |
| L'émetteur affiche, le récepteur non | Les bandes diffèrent, ou une carte n'est pas alimentée |
| Le récepteur affiche, mais le mauvais ordre | Les mots ne correspondent pas : vérifie l'orthographe, et les 8 caractères pour une clé |
| Ça marche, puis ça s'arrête | Les accus |

> [!TIP] Retire les témoins à la fin
> Un écran qui clignote pendant une mission gêne. Mais tant que tu règles, laisse-les : c'est ce qui te fait gagner du temps.

## S'arrêter quand le signal se perd

Dans un train, le conducteur appuie régulièrement sur une pédale ; s'il ne le fait plus, le train freine seul. C'est le **dispositif de l'homme mort**. Une carte qui obéit à la radio peut faire pareil : sans message depuis un moment, elle revient à un état sûr.

Le programme se partage en deux :

- **le gestionnaire range** : le message reçu, et l'heure à laquelle il est arrivé ;
- **`toujours` agit** : trop longtemps sans message, il passe à l'état sûr ; sinon, il fait ce que dit le dernier message.

`temps d’exécution (ms)`, dans **Entrée**, donne le nombre de millisecondes depuis l'allumage de la carte : c'est son horloge.

```blocks
radio.onReceivedString(function (receivedString) {
    message = receivedString
    dernierMessage = input.runningTime()
})
basic.forever(function () {
    if (input.runningTime() - dernierMessage > 1000) {
        basic.showIcon(IconNames.No)
    } else if (message == "oui") {
        basic.showIcon(IconNames.Yes)
    }
})
let dernierMessage = 0
let message = ""
```

Ici, plus d'une seconde sans message : la croix s'affiche.

> [!NOTE] Pas de pause dans le gestionnaire
> La carte ne garde que quatre messages en attente. Si le gestionnaire attend, les suivants sont perdus.

## Changer de mode

Un même programme peut faire plusieurs choses : écouter une source, puis une autre. Chacune est un **mode**.

**Une variable `mode`, pour tout le programme.** Donne un numéro à chaque mode : `0`, `1`… `au démarrage`, `toujours` et `quand une donnée est reçue` lisent tous la même variable.

**Un geste pour en changer.** Un bouton par mode (`A` pour l'un, `B` pour l'autre), ou le logo : à chaque contact, `mode` passe au suivant et revient à `0` après le dernier. C'est là aussi qu'on règle la radio du nouveau mode, si elle change.

**Un témoin pour le voir.** Chaque mode allume son point, dans un coin que tes autres témoins n'utilisent pas. Rallume-le à chaque tour de `toujours`, juste après `effacer l'écran`.

| Mode | `mode` | Point |
|---|---|---|
| Premier mode | `0` | `0,0` |
| Second mode | `1` | `4,0` |

Dans `toujours`, un `si mode = 0 … sinon si mode = 1 …` choisit ce que fait le programme.

> [!NOTE] Pourquoi un témoin
> Une carte dans le mauvais mode n'obéit plus à ce qu'on attend d'elle. Sans témoin, on croit à une panne.

Autre solution : un projet par mode, téléversé selon le besoin. Plus simple à écrire, plus lent à changer : il faut l'ordinateur.

## Blocs, JavaScript, Python

La bascule en haut de l'écran montre le même programme sous trois formes.

<figure class="screenshot" markdown>
![Un programme affiché en Python dans MakeCode](../assets/rover-s01/24-vue-python.png)
<figcaption>Les blocs sont une façon d'écrire du code.</figcaption>
</figure>

Tu peux regarder, c'est instructif. Attention : en passant en texte puis en revenant aux blocs, une mise en page peut se perdre. Fais l'aller-retour sur un projet dont tu n'as pas peur de perdre l'agencement.

→ [La carte DFR0548 et ses blocs](carte-dfr0548.md) · [Déboguer](deboguer.md)
