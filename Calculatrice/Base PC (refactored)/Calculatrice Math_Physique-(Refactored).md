# Calculatrice Mathématiques & Physique — Version refactorisée

Calculateur interactif en Python (bibliothèque standard uniquement) proposant des dizaines de formules de mathématiques et de physique, organisées par menus hiérarchiques, avec historique des calculs et validation des saisies.

Cette version reprend toutes les fonctionnalités du calculateur original, mais repose sur une architecture **entièrement pilotée par les données** (un arbre de `Menu` / `Action`) plutôt que sur une succession de blocs `if/elif`. Résultat : un seul endroit où chaque calcul est décrit, et plus aucune duplication entre la navigation et la liste de formules.

---

## Fonctionnalités

### Mathématiques

- **Fonctions de base** : carré, cube, inverse, racine carrée, valeur absolue
- **Fonctions spéciales** : factorielle, exponentielle
- **Coordonnées** : milieu, distance entre deux points
- **Théorèmes** : Pythagore (théorème + réciproque/contraposée), Thalès (4 inconnues)
- **Vecteurs** : relation de Chasles (3 inconnues), déterminant
- **Triangles** : somme angulaire, trigonométrie (cos/sin/tan) et fonctions réciproques (`arccos`/`arcsin`/`arctan`)
- **Taux** : taux d'évolution, taux global (composé)

### Physique

- **Matière** : masse volumique (3 inconnues), masse d'un atome, nombre de moles, dilution (2 inconnues)
- **Électricité** : loi d'Ohm (3 inconnues), puissance électrique (3 formules), énergie électrique
- **Optique** : loi de Snell-Descartes, indice de réfraction (2 inconnues)
- **Cinématique** : vitesse moyenne (vitesse / distance / temps)
- **Forces** : force de gravitation, poids

### Formules

- Liste de référence des **35 formules**, **générée automatiquement** à partir de l'arbre de menus — aucune liste à maintenir à la main
- Sélection directe d'une formule depuis cette liste pour l'exécuter immédiatement

### Autres

- **Historique** : chaque calcul est enregistré et récapitulé en fin de session
- **Validation des saisies** : les entiers et les nombres décimaux invalides sont redemandés en boucle, sans faire planter le programme

---

## Architecture (ce qui a changé)

Toute la calculatrice repose sur deux structures de données :

```python
@dataclass
class Action:
    label: str                     # texte affiché dans le menu
    fonction: Callable[[], None]   # le calcul à exécuter
    formule: Optional[str] = None  # texte affiché dans "Formules"

@dataclass
class Menu:
    label: str
    items: list                    # Action ou Menu enfants
    formule: Optional[str] = None
    recapitulatif: bool = False
```

Un moteur générique (`choisir`, `executer_noeud`) parcourt cette structure sans rien connaître de son contenu : il affiche les options de `menu.items`, demande un choix, et descend récursivement jusqu'à une `Action` exécutable.

La section **"Formules"** est calculée à partir de ce même arbre (`collecter_formules`). Elle ne peut donc jamais se désynchroniser des menus de navigation, puisqu'il n'existe plus qu'une seule source de vérité par calcul.

---

## Prérequis

- Python 3.9+ (utilise les `dataclasses` et les annotations `list[str]`)
- Aucune bibliothèque externe : uniquement la bibliothèque standard (`math`, `time`, `dataclasses`, `typing`)

---

## Utilisation

1. Récupérez le fichier `calculatrice.py`.
2. Exécutez-le :
    ```
	python calculatrice.py
    ```
    
3. Suivez les menus :
    - Choisissez **Maths**, **Physique** ou **Formules**.
    - Naviguez dans les sous-catégories jusqu'au calcul souhaité.
    - Renseignez les valeurs demandées.
4. À la fin de chaque calcul, indiquez si vous avez terminé pour afficher l'historique, ou continuez.

---

## Structure du code

|Élément|Rôle|
|---|---|
|`Action` / `Menu`|Modèle de données décrivant un calcul, ou un regroupement de calculs|
|`choisir(menu)`|Affiche les options d'un menu et renvoie l'item choisi|
|`executer_noeud(noeud)`|Descend dans l'arbre jusqu'à une `Action`, puis l'exécute|
|`collecter_formules(menu)`|Génère automatiquement la liste de référence "Formules" depuis l'arbre|
|`calc_xxx()`|Une fonction par calcul : saisie, calcul, affichage, historique|
|`ARBRE`|La racine de l'arbre de menus (Maths / Physique / Formules)|
|`historique` (liste)|Stocke chaque calcul effectué, affiché en fin de session|

Les constantes physiques (`G_UNIVERSELLE`, `G_TERRESTRE`, `NA`, `C_LUMIERE`, masses des particules) sont définies en tête de fichier.

---

## Exemple d'exécution

```
Calculatrice
  1: Maths
  2: Physique
  3: Formules
Choix : 1

Maths
  1: Fonctions
  2: Coordonnées
  3: Théorèmes
  4: Vecteurs
  5: Triangles
  6: Taux
Choix : 1

Fonctions
  1: De base
  2: Spéciales
Choix : 1

De base
  1: Carrée
  2: Cube
  3: Inverse
  4: Racine carrée
  5: Valeur absolue
Choix : 1

x: 5
L'image de 5.0 est 25.0 par la fonction carrée.
```

---

## Ajouter un nouveau calcul

C'est le principal avantage de cette architecture : **un seul endroit à modifier**, contre quatre auparavant (liste de validation, branche `elif` de navigation, branche `elif` d'exécution, tableau de formules).

1. Écrire une fonction qui lit les entrées, calcule, affiche et journalise :
    
    ```python
    def calc_logarithme():    x = saisir_nombre("x: ")    res = arrondi(log(x))    print(f"ln({x}) = {res}")    historique.append(f"Logarithme: ln({x}) = {res}")
    ```
    
2. La déclarer dans le `Menu` concerné :
    
    ```python
    Action("Logarithme", calc_logarithme, "ln(x)"),
    ```
    

Aucune liste à étendre, aucun `elif` à ajouter ailleurs, aucun index à synchroniser : le menu de navigation **et** la liste "Formules" se mettent à jour automatiquement.

---

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le redistribuer.

---

## Auteur

Projet réalisé par **moi** — n'hésitez pas à contribuer ou à signaler des bugs !

---

_Bon calcul !_
