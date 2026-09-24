# Séance 8 — Faites piloter votre rover par la table

La table va piloter votre rover. Elle envoie les mêmes messages que votre télécommande : quatre changements dans votre programme suffisent.

## 1. Regardez la table piloter

<span class="todo-media">[photo : la table, un rover dessus, en train de suivre une figure]</span>

La table voit le tag du rover, le mesure, puis le fait suivre une figure. Elle envoie `avancer`, `reculer`, `gauche`, `droite`, `arreter` — les clés de ta télécommande.

## 2. La bande et le groupe

En séance 4, chaque télécommande avait **sa bande** : douze émetteurs en même temps se seraient gênés.

Ici, **un seul émetteur parle à tous les rovers** : la table. Tout le monde est sur la bande `83`, et le **groupe** dit à qui le message s'adresse. Votre groupe, c'est le numéro de votre tag.

<span class="todo-media">[capture : au démarrage → radio régler la bande de fréquence 83, radio définir groupe 12]</span>

## 3. La valeur devient la vitesse

La table envoie une valeur de `0` à `1023`. Ton moteur accepte de `0` à `255`. Et dans tes cinq fonctions, les vitesses sont écrites en chiffres depuis la séance 2.

> [!NOTE] Une variable pour tout le programme
> Créée une fois, une variable se lit partout : dans le gestionnaire radio, dans `toujours`, dans tes fonctions.

### À toi : la vitesse variable

Range la valeur reçue, mise à l'échelle, dans une variable `vitesse`. Puis, dans tes cinq fonctions, remplace les vitesses par `vitesse`.

> [!TIP] Ta compensation et ta vitesse minimale
> Tu as noté en séance 2 un moteur réglé plus haut que l'autre : garde l'écart, par exemple `vitesse + 10`. Et sous ta vitesse minimale, le rover ne démarre pas : mets à l'échelle vers ta vitesse minimale, pas vers `0`.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : vitesse ← mettre à l'échelle valeur de 0–1023 vers vitesse minimale–255]</span>

<span class="todo-media">[capture : la fonction avancer, M1 à vitesse, M2 à vitesse + 10]</span>

Diviser par 4 donne presque le même résultat que la mise à l'échelle vers `0–255`.

</details>

## 4. Le gestionnaire range, la boucle agit

Dans `quand une donnée est reçue par radio`, range seulement l'ordre et la vitesse dans deux variables. C'est `toujours` qui appelle tes fonctions.

<span class="todo-media">[capture : le gestionnaire qui range nom et vitesse dans deux variables, et la boucle toujours qui appelle la fonction correspondante]</span>

> [!NOTE] Pas de pause dans le gestionnaire
> La carte ne garde que quatre messages en attente. Si le gestionnaire attend, les suivants sont perdus.

## 5. Le silence arrête le rover

**À toi.** À chaque message, note l'heure avec `temps écoulé (ms)`. Dans `toujours` : si plus de 1000 ms sont passées depuis, arrête les moteurs.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : dernier message ← temps écoulé ; dans toujours, si temps écoulé − dernier message > 1000 alors arrêter]</span>

</details>

## 6. Changez de mode

Votre rover doit obéir à la télécommande, sur la bande de l'équipe, et à la table, sur la bande `83`. Ce sont deux **modes**.

**Une variable `mode`**, créée une fois, que tout le programme lit : `0` télécommande, `1` table.

**Un geste pour en changer**, par exemple `quand le logo est touché`. Il change `mode` et règle la radio du nouveau mode.

**Un témoin** : un point dans un coin libre de l'écran, un par mode, rallumé à chaque tour de `toujours`.

> [!NOTE] Pourquoi un témoin
> En mode table, le rover n'obéit plus à sa télécommande. Sans témoin, on croit à une panne.

### À toi : les deux modes

Au logo, le rover passe d'un mode à l'autre. En mode `0`, point `0,0` et bande de l'équipe. En mode `1`, point `4,0`, bande `83` et votre groupe.

<details markdown>
<summary>La solution</summary>

<span class="todo-media">[capture : quand le logo est touché → si mode = 0 alors mode ← 1, bande 83, groupe ; sinon mode ← 0, bande de l'équipe]</span>

<span class="todo-media">[capture : toujours → effacer l'écran ; si mode = 0 alors allumer 0,0 sinon allumer 4,0 ; puis l'appel de la fonction]</span>

</details>

Vous préférez deux programmes, un par mode ? C'est permis. Notez votre choix au carnet.

→ [Changer de mode](../../../fiches/makecode-prise-en-main.md#changer-de-mode)

> [!TIP] Tester sans la table
> Mets ta télécommande sur la bande `83` et votre groupe. Si le rover lui obéit, il obéira à la table.

## 7. Passez sur la table

Une équipe à la fois, dans l'ordre du tableau. La table vérifie :

- `avancer` : 5 cm au moins en 1,5 s
- `gauche` et `droite` : deux sens opposés
- la table se tait : le rover s'arrête en 1 s

---

## Ce que vous devez avoir à la fin

- [ ] Bande `83` et votre groupe
- [ ] La vitesse variable dans tes cinq fonctions, compensation gardée
- [ ] Aucune pause dans le gestionnaire
- [ ] L'arrêt après 1 s de silence
- [ ] Deux modes, et le témoin qui dit lequel est actif
- [ ] Votre rover qui suit la figure de la table
- [ ] Ton [carnet de bord](../../../carnet-de-bord/rover-s08.md) rempli

→ [Prendre en main MakeCode](../../../fiches/makecode-prise-en-main.md) · [Déboguer](../../../fiches/deboguer.md)

## Avant de partir

Programme enregistré. Accus en charge.
