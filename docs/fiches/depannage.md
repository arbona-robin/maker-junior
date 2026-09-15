# Quand ça ne marche pas

Une panne se cherche, elle ne se devine pas. Le réflexe qui fait la différence n'est pas de connaître la réponse : c'est de **séparer ce qui marche de ce qui ne marche pas**, pour ne chercher que dans la moitié qui reste.

## Le principe

> [!NOTE] Diviser pour trouver
> Ton rover est une chaîne : l'ordinateur écrit le programme, l'USB le transmet, la carte l'exécute, les accus alimentent, les fils transportent, les moteurs tournent.
>
> Quand rien ne bouge, la question n'est pas « qu'est-ce qui ne va pas », mais **« jusqu'où ça marche ? »**. Chaque témoin visible — une icône, un son, une LED — te dit qu'un maillon est franchi.
>
> C'est pour ça qu'on met une icône et un son dans `au démarrage`, et qu'on affiche une flèche pendant que les moteurs tournent. Ce ne sont pas des décorations, ce sont des points de mesure.

## L'arbre de décision

**L'écran du micro:bit reste éteint au démarrage.**
La carte n'est pas alimentée, ou le programme n'a pas été téléversé. Rebranche l'USB : si l'écran s'allume, c'est l'alimentation. Sinon, retéléverse.

**L'icône de démarrage s'affiche, mais pas la suite.**
Le programme a démarré et s'est arrêté ou bloqué. Regarde ce qui suit dans ton code, et vérifie que tes actions répétées sont bien dans `toujours` et non dans `au démarrage`.

**La flèche s'affiche, mais aucun moteur ne tourne.**
Le programme se déroule — **le problème n'est pas dans le code.** Dans l'ordre :

1. L'interrupteur de la carte est-il sur *on* ?
2. Le pack d'accus est-il branché, et les accus chargés ?
3. Les fils des moteurs sont-ils bien serrés dans les borniers `M1` et `M2` ? Tire doucement dessus : un fil qui sort n'était pas serré.
4. Les numéros des blocs correspondent-ils aux borniers utilisés ?

**Un seul moteur tourne.**
Le problème est du côté qui ne tourne pas, et il est presque toujours mécanique ou électrique. Échange les deux fiches des moteurs dans les borniers : si la panne suit le moteur, c'est le moteur ou ses fils ; si elle reste sur le même bornier, c'est la carte ou le code.

**Les moteurs tournent en sens opposés.**
Normal, et attendu : les deux moteurs sont montés tête-bêche sur le châssis. Inverse les deux fils de l'un dans son bornier, ou passe son bloc de `CW` à `CCW`.

**Les moteurs bourdonnent sans tourner.**
La vitesse est trop basse pour vaincre le frottement de départ, ou les accus sont faibles. Monte la valeur de `speed`, ou change de pack.

**Le rover tourne au lieu d'avancer droit.**
Ce n'est pas une panne. Deux moteurs identiques ne tournent jamais exactement à la même vitesse, et le châssis n'est jamais parfaitement symétrique. On s'en occupe.

**Le rover roulait, il ne roule plus.**
Regarde d'abord les accus : c'est la cause la plus fréquente, et la plus vite écartée. Puis les élastiques : un moteur qui a glissé dans son logement débranche souvent un fil au passage.

## Avant d'appeler à l'aide

Trois questions à te poser. Elles résolvent la moitié des pannes, et rendent l'autre moitié beaucoup plus rapide à traiter.

1. **Jusqu'où ça marche ?** Quel est le dernier témoin que tu as vu s'allumer ?
2. **Qu'est-ce qui a changé ?** Ça marchait il y a cinq minutes — qu'as-tu touché entre-temps ?
3. **Est-ce que ça marche sur le rover d'à côté ?** Échange une pièce avec un binôme : c'est le moyen le plus rapide de savoir si le problème est dans la pièce ou dans le montage.

> [!TIP] Note ta panne
> Quand tu as trouvé, écris-la dans ton carnet de bord : le symptôme, la cause, la solution. Tu la retrouveras — et quelqu'un d'autre l'aura aussi.
