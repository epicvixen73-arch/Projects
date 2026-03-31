# 🧮 Calculatrice Scientifique — NumWorks

> Application de calcul scientifique développée en **MicroPython** pour la calculatrice graphique **NumWorks N0110/N0120**, couvrant les formules de **Maths** et de **Physique-Chimie** niveau **Seconde**.

---

## 📋 Description

Ce projet est une calculatrice scientifique interactive qui permet d'effectuer rapidement des calculs courants, organisés en menus hiérarchiques. L'application enregistre un **historique des calculs** effectués pendant la session et propose également un mode **Formules** pour consulter et appliquer directement n'importe quelle formule du programme.

---

## ✨ Fonctionnalités

### 📐 Mathématiques
| Catégorie | Formules disponibles |
|-----------|---------------------|
| **Fonctions** | Carrée, Cube, Inverse, Racine carrée, Valeur absolue, Factorielle, Exponentielle |
| **Coordonnées** | Milieu, Distance entre deux points |
| **Théorèmes** | Pythagore (théorème + réciproque/contraposée), Thalès |
| **Vecteurs** | Relation de Chasles, Déterminant |
| **Triangles** | Somme angulaire, Trigonométrie (cos, sin, tan, arccos, arcsin, arctan) |
| **Taux** | Taux d'évolution, Taux global (taux composés) |

### ⚗️ Physique-Chimie
| Catégorie | Formules disponibles |
|-----------|---------------------|
| **Matière** | Masse volumique, Masse d'un atome, Quantité de matière (mol), Dilution |
| **Électricité** | Loi d'Ohm, Puissance électrique, Énergie électrique |
| **Optique** | Loi de Snell-Descartes, Indice de réfraction |
| **Vitesse moyenne** | Calcul de v, d ou t |
| **Forces** | Force de gravitation universelle, Poids |

### 📖 Mode Formules
- Affichage de toutes les **35 formules** du programme
- Sélection directe d'une formule par son numéro pour effectuer le calcul

### 🕓 Historique
- Enregistrement automatique de chaque calcul effectué
- Affichage complet de l'historique en fin de session

---

## 🚀 Installation & Utilisation

### Prérequis
- Calculatrice **NumWorks N0110 ou N0120**
- Accès à l'éditeur de scripts NumWorks (via la calculatrice ou [numworks.com/simulator](https://my.numworks.com))

### Installation
1. Connecte ta NumWorks à ton ordinateur via USB ou ouvre le simulateur en ligne
2. Accède à l'onglet **Scripts** de la calculatrice
3. Crée un nouveau script et copie-colle le contenu
4. Sauvegarde le script

### Lancement
Dans l'interface NumWorks :
```
from calculatrice import *
run()
```
Ou directement depuis l'onglet Scripts en exécutant le fichier.

---

## 🗂️ Structure du code

```
calculatrice.py
├── Constantes physiques (G, NA, c, mp, mn, me, g)
├── Menus hiérarchiques (listes d'options)
├── formules[]          → liste des 35 formules
├── historique[]        → liste des calculs effectués
├── arrondi()           → arrondit à 4 décimales
├── saisir()            → saisie sécurisée avec validation
├── executer_formule()  → calcul par index (mode Formules)
├── run()               → menu principal et navigation
└── Boucle principale   → gestion de session et affichage historique
```

---

## 📌 Constantes intégrées

| Constante | Valeur | Description |
|-----------|--------|-------------|
| `G` | `6.674e-11` | Constante gravitationnelle (N·m²/kg²) |
| `NA` | `6.02e23` | Nombre d'Avogadro (mol⁻¹) |
| `c` | `3e8` | Vitesse de la lumière (m/s) |
| `g` | `9.81` | Accélération gravitationnelle (m/s²) |
| `MP` | `1.673e-27` | Masse d'un proton (kg) |
| `MN` | `1.675e-27` | Masse d'un neutron (kg) |
| `ME` | `9.110e-31` | Masse d'un électron (kg) |

---

## 💡 Exemple d'utilisation

```
1: Maths, 2: Physique, 3: Formules
Choix: 1

1: Fonctions, 2: Coordonnées
3: Théorèmes, 4: Vecteurs
5: Triangles, 6: Taux
Choix: 3

1: Pythagore, 2: Thalès
Choix: 1

1: Théorème
2: Réciproque/Contraposée
Choix: 1

Le Théorème est: a²+b²=c² (c est l'hypoténuse inconnu)
a: 3
b: 4
c = 5.0
```

---

## 🛠️ Technologies

- **Langage** : Python 3 / MicroPython
- **Plateforme** : NumWorks N0110 / N0120
- **Modules** : `math`, `time`

---

## 👤 Auteur

Projet développé par **epicvixen73-arch**

---

## 📄 Licence

Ce projet est libre d'utilisation à des fins éducatives.
