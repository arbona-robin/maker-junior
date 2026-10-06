# Le catalogue des produits

Des idées d'objets connectés qui servent à tout le monde. Votre équipe en choisit un, ou invente le sien.

Le catalogue dépend de ce qu'il y a au magasin : l'animateur vous dira lesquels sont possibles cette fois.

## La langue commune

Tous les produits parlent la même langue. Le tableau de bord les reconnaît et choisit seul comment afficher leurs mesures.

| | |
|---|---|
| Bande | `40`, la même que les lampes |
| Numéro de série | `radio émettre le numéro de série` **vrai**, dans `au démarrage` : c'est à lui que le tableau de bord reconnaît ton micro:bit |
| Clé | Ce que tu mesures, **8 caractères au plus**, sans accent. Son début choisit l'affichage |
| Valeur | Un nombre |
| Rythme | Toutes les 5 à 10 secondes, et tout de suite quand quelque chose change |

> [!NOTE] Pourquoi pas en continu
> Un micro:bit qui émet sans arrêt vide ses accus en quelques jours, et gêne les messages des autres.

### Les clés que le tableau de bord connaît

| La clé commence par | Le tableau de bord affiche | Valeur |
|---|---|---|
| `temp` | Une jauge, en °C | La température |
| `lum` | Une jauge | La lumière, de 0 à 255 |
| `son` | Une jauge | Le niveau sonore, de 0 à 255 |
| `hum` | Une jauge, en % | L'humidité, de 0 à 100 |
| `incl` | Une jauge, en degrés | L'inclinaison, de −90 à 90, avec `rotation (°)` |
| `accel` | Une courbe, en mg | L'accélération, avec `accélération (mg)` : 1000 mg = 1 g |
| `dist` | Un nombre, en cm | Une distance |
| `compte` | Un compteur | Un nombre qui augmente |
| `bouton`, `etat`, `presence` | Un voyant allumé ou éteint | `0` ou `1` |
| Autre chose | Une courbe | N'importe quel nombre |

Deux mesures du même genre : `temp` et `tempext`. Les deux s'affichent en jauge.

Un micro:bit qui n'a rien envoyé depuis 30 secondes apparaît **hors ligne**.

Les clés `tous` et `tour` appartiennent aux lampes : le tableau de bord les ignore.

<details markdown>
<summary>Pour aller plus loin : un interrupteur sur le tableau de bord</summary>

Une clé qui commence par `inter`, suivie de la lettre de votre équipe (`interA`), s'affiche comme un interrupteur. Quand on le bascule sur le tableau de bord, le pont envoie la même clé avec la nouvelle valeur, `0` ou `1`.

Votre produit l'écoute avec `quand une donnée est reçue`. Il doit fonctionner sans : l'ordre du tableau de bord ne fait que forcer un état.

</details>

## Les produits

| Produit | Ce qu'il fait | Il mesure | Il agit | Clés |
|---|---|---|---|---|
| Panneau occupé ou libre | Dit de loin si une salle est prise | Un interrupteur, ou la présence | Matrice RGB | `etat` |
| Lampe à gestes | On l'allume et on change sa couleur d'un geste | Inclinaison d'une carte tenue en main | Matrice RGB | `etat` |
| Sémaphore du bruit | Vert, orange, rouge selon le bruit de la salle | Niveau sonore (micro de la carte) | Matrice RGB ou servomoteur en aiguille | `son` |
| Surveillance des plantes | Prévient quand une plante a soif | Humidité du sol (sonde) | LED, son | `hum` |
| Sonnette à messages | Prévient l'accueil qu'on attend à une porte | Un bouton | Son, voyant sur le tableau de bord | `bouton` |
| Moniteur d'imprimante 3D | Dit si l'imprimante tourne ou s'est arrêtée | Vibrations (accéléromètre) | Voyant sur le tableau de bord | `accel`, `etat` |
| Station météo de fenêtre | Affiche la température et la lumière dehors | Température, lumière (capteurs de la carte) | Écran de la carte | `temp`, `lum` |
| Compteur de passages | Compte les passages à une porte | Présence, ou un faisceau de lumière coupé | Compteur sur le tableau de bord | `presence`, `compte` |
| Poubelle mains-libres | Le couvercle s'ouvre quand on approche | Présence (capteur PIR) | Servomoteur | `presence`, `compte` |
| Coffre à code | S'ouvre avec la bonne suite de boutons | Boutons `A` et `B` | Servomoteur en verrou | `etat` |

## Inventez le vôtre

Votre idée n'est pas dans la liste ? Elle est bienvenue, à quatre conditions :

1. Il sert à quelqu'un d'autre que vous.
2. Il mesure quelque chose, et il agit ou il prévient.
3. Il se construit avec ce qu'il y a au magasin : vérifiez-le avec l'animateur.
4. Il parle la langue commune.

> [!TIP] Une idée trop grande ?
> Gardez une mesure et une action. Le reste viendra si vous avez le temps.

## Les composants du magasin

**Le servomoteur** va à un angle et le tient. Pour un couvercle, un verrou, une aiguille.

**Le moteur à courant continu** tourne, sans savoir où il en est. Il demande une carte de puissance, la DFR0548.

→ [La carte DFR0548 et ses blocs](../../fiches/carte-dfr0548.md)

Aucun n'est obligatoire. On choisit un composant parce que le produit le demande.
