# Prendre en main MakeCode

MakeCode est l'éditeur dans lequel tu écris tes programmes. Il s'ouvre dans un navigateur, à [makecode.microbit.org](https://makecode.microbit.org). Rien à installer.

## Créer un projet

Sur la page d'accueil, **Nouveau projet**, puis un nom.

<figure class="screenshot" markdown>
![La page d'accueil de MakeCode, section « Mes projets »](../assets/rover-s01/20-makecode-accueil.png)
<figcaption>Tes projets restent dans le navigateur de l'ordinateur où tu les as créés.</figcaption>
</figure>

> [!TIP] Un projet, plusieurs séances
> Donne un nom clair dès le début — `rover` — et reviens dans le même projet d'une séance à l'autre plutôt que d'en créer un nouveau à chaque fois.
>
> Les projets sont enregistrés dans le navigateur, pas dans un compte. Sur un autre ordinateur, tu ne les retrouveras pas. Si tu changes de poste, utilise le bouton de partage pour récupérer un lien vers ton projet.

## L'écran

Trois zones, de gauche à droite.

**Le simulateur** — un micro:bit dessiné qui exécute ton programme en direct, avant même de le téléverser. Il affiche l'écran, réagit aux boutons, joue les sons. Pratique pour tester une animation sans brancher la carte.

**La palette** — les catégories de blocs, chacune sa couleur. Base, Entrée, Musique, LED, Radio, Boucles, Logique, Variables, Maths, puis Extensions et Avancé.

**L'espace de travail** — où tu assembles tes blocs.

En bas à gauche, le bouton **Télécharger**. En haut au centre, la bascule **Blocs / JavaScript / Python**.

## Les deux blocs de départ

Un projet neuf contient déjà deux blocs, et la différence entre eux est la première chose à comprendre.

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
> Mets toujours une icône et un son dans `au démarrage`. Quand quelque chose ne marchera pas, tu sauras au premier coup d'œil si c'est bien ton programme qui s'exécute — et tu t'épargneras de chercher dans le code un problème qui est dans les fils.

Une fois téléversé, le programme est **dans la carte**. Débranche l'USB, alimente par les accus : il repart tout seul. L'ordinateur n'est plus nécessaire.

## Les fonctions

Une fonction est un bloc que **tu** fabriques : tu lui donnes un nom, tu mets des blocs dedans, et tu l'appelles ensuite par son nom.

**Fonctions** → **Créer une fonction…** → nomme-la → **Terminé**.

<figure class="screenshot" markdown>
![La catégorie Fonctions dépliée dans MakeCode, avec le bouton « Créer une fonction… »](../assets/rover-s02/20-categorie-fonctions.png)
</figure>

Le nouveau bloc `fonction <nom>` apparaît dans l'espace de travail : glisse tes blocs dedans. Un bloc `appel <nom>` apparaît en même temps dans la catégorie **Fonctions** — c'est lui que tu places dans `toujours` ou dans `au démarrage`.

> [!NOTE] À quoi ça sert
> À écrire une fois ce qu'on utilise dix fois, et à se relire. `appel avancer` se comprend sans lire le détail ; trois blocs moteur avec des chiffres, non.

Deux règles qui évitent des heures perdues :

- **Un nom qui dit ce que ça fait.** `avancer`, pas `fonction2`.
- **On modifie la fonction, jamais ses copies.** Change la vitesse dans `avancer`, et tous les appels suivent. C'est tout l'intérêt.

Pour renommer une fonction ou lui ajouter un paramètre : clique sur la roue dentée du bloc `fonction`.

## Les variables

Une variable est une **boîte nommée** qui retient une valeur. Tu y ranges quelque chose, tu le relis quand tu veux.

**Variables** → **Créer une variable…** → donne-lui un nom qui dit ce qu'elle contient.

<figure class="screenshot" markdown>
![La fenêtre « Nom de la nouvelle variable » dans MakeCode](../assets/rover-s03/35-creer-variable.png)
</figure>

Deux blocs suffisent : `définir <nom> à …` pour y mettre une valeur, et le bloc `<nom>` lui-même pour la relire.

> [!NOTE] À quoi ça sert avec un capteur
> Lire un capteur deux fois de suite donne deux valeurs différentes — il bouge entre les deux lectures. Range la mesure dans une variable, et tous tes tests parleront bien du **même** instant.

→ [D'une mesure à une décision](mesure-vers-decision.md)

## Blocs, JavaScript, Python

La bascule en haut de l'écran montre le même programme sous trois formes.

<figure class="screenshot" markdown>
![Un programme affiché en Python dans MakeCode](../assets/rover-s01/24-vue-python.png)
<figcaption>Les blocs sont une façon d'écrire du code, pas une chose différente du code.</figcaption>
</figure>

Tu peux regarder, c'est instructif. Attention : en passant en texte puis en revenant aux blocs, une mise en page peut se perdre. Fais l'aller-retour sur un projet dont tu n'as pas peur de perdre l'agencement.
