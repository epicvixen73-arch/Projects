# Calculateur Mathématiques & Physique

Ce projet est un calculateur interactif en Python proposant de nombreuses formules mathématiques et physiques.  
Il permet de calculer rapidement des fonctions, des théorèmes, des grandeurs physiques et bien plus encore, le tout avec un historique des calculs effectués.

---

## Fonctionnalités

### Mathématiques
- **Fonctions de base** : carré, cube, inverse, racine carrée, valeur absolue, factorielle, exponentielle.
- **Coordonnées** : calcul du milieu et de la distance entre deux points.
- **Théorèmes** : Pythagore (direct et réciproque), Thalès.
- **Vecteurs** : relation de Chasles, déterminant.
- **Triangles** : somme angulaire, trigonométrie (cos, sin, tan) et leurs réciproques (arccos, arcsin, arctan).
- **Taux** : taux d’évolution, taux global.

### Physique
- **Matière** : masse volumique, masse d’un atome, nombre de moles, dilution.
- **Électricité** : loi d’Ohm, puissance électrique, énergie électrique.
- **Optique** : loi de Snell-Descartes, indice de réfraction.
- **Cinématique** : vitesse, distance, temps.
- **Forces** : force de gravitation, poids.

### Formules
- Liste complète de toutes les formules disponibles avec possibilité d’exécution directe.

### Autres
- **Historique** : toutes les opérations sont enregistrées et affichées en fin de session.
- **Validation des entrées** : gestion des erreurs de saisie (valeurs non numériques, choix hors limites).

---

## Prérequis

- Python 3.x (testé avec Python 3.7+)
- Aucune bibliothèque externe requise (seulement la bibliothèque standard).

---

## Utilisation

1. Clonez le dépôt ou téléchargez le fichier `FinalV2.py`.
2. Exécutez le script :
   ```bash
   python FinalV2.py
   ```
3. Suivez les menus :
   - Choisissez entre **Maths**, **Physique** ou **Formules**.
   - Naviguez dans les sous‑catégories pour sélectionner le calcul souhaité.
   - Saisissez les valeurs demandées.
4. À la fin de chaque session, vous pouvez consulter l’historique ou continuer.

---

## Structure du code

| Fichier / Élément            | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `FinalV2.py`                 | Script principal contenant toute l’application.                             |
| `arrondi(valeur)`            | Arrondit un nombre à 4 décimales.                                           |
| `saisir(message, valeurs)`   | Gère les saisies utilisateur avec validation.                               |
| `executer_formule(choix)`    | Exécute une formule à partir de son index dans la liste `formules`.         |
| `run()`                      | Affiche le menu principal et dirige vers les sous‑menus.                    |
| `historique` (liste)         | Stocke chaque calcul effectué pour les afficher à la fin.                   |

Les constantes physiques (G, NA, c, masses, etc.) sont définies en début de fichier.

---

## Exemple d’exécution

```
1: Maths, 2: Physique, 3: Formules
Choix: 1

1: Fonctions, 2: Coordonnées
3: Théorèmes, 4: Vecteurs
5: Triangles, 6: Taux
Choix: 1

1: De bases, 2: Spécialées
Choix: 1

1: Carrée, 2: Cube
3: Inverse, 4: Racine carrée
5: Valeur absolue
Choix: 1

x: 5
L'image de 5.0 est 25.0 par la fonction carrée.
```

---

## Personnalisation

Vous pouvez facilement ajouter de nouvelles formules :
- Définissez la formule dans la liste `formules` (avec son index).
- Ajoutez une branche `elif` dans `executer_formule` avec le code de calcul correspondant.
- Si la formule doit apparaître dans les menus classiques, ajoutez‑la également dans les structures de données (ex: `maths_H1`, `math_fn`, etc.).

---

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l’utiliser, de le modifier et de le redistribuer.

---

## Auteur

Projet réalisé par **epicvixen73-arch** – n’hésitez pas à contribuer ou à signaler des bugs !

---

*Bon calcul !*
