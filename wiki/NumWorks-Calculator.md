# NumWorks Calculator

A scientific calculator application developed in **MicroPython** for the **NumWorks N0110/N0120** graphing calculator, covering **Math** and **Physics & Chemistry** formulas at the **Seconde** (10th grade) level with 35 formulas, compact menus, and built-in physical constants.

## 📋 Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Built-in Constants](#built-in-constants)
- [Available Formulas](#available-formulas)
- [Example Usage](#example-usage)

---

## 📖 Description

This project is an interactive scientific calculator that lets you quickly perform common calculations, organized through hierarchical menus. The app keeps a **history of calculations** made during the session and also offers a **Formulas** mode to browse and directly apply any formula from the curriculum.

---

## ✨ Features

### Mathematics

| Category | Available Formulas |
| --- | --- |
| **Functions** | Square, Cube, Inverse, Square root, Absolute value, Factorial, Exponential |
| **Coordinates** | Midpoint, Distance between two points |
| **Theorems** | Pythagorean theorem (theorem + converse/contrapositive), Thales' theorem |
| **Vectors** | Chasles' relation, Determinant |
| **Triangles** | Angle sum, Trigonometry (cos, sin, tan, arccos, arcsin, arctan) |
| **Rates** | Rate of change, Compound rate |

### Physics & Chemistry

| Category | Available Formulas |
| --- | --- |
| **Matter** | Density, Atomic mass, Amount of substance (mol), Dilution |
| **Electricity** | Ohm's law, Electric power, Electric energy |
| **Optics** | Snell-Descartes law, Refractive index |
| **Average Speed** | Calculate v, d, or t |
| **Forces** | Universal gravitational force, Weight |

### Formulas Mode

* Browse all **35 formulas** from the curriculum
* Select a formula directly by number to run the calculation

### History

* Automatic recording of every calculation performed
* Full history displayed at the end of the session

---

## 📦 Requirements

* **NumWorks N0110 or N0120** calculator
* Access to the NumWorks script editor (via the calculator or [numworks.com/simulator](https://my.numworks.com))

---

## 🚀 Installation

1. Connect your NumWorks to your computer via USB, or open the online simulator
2. Go to the **Scripts** tab on the calculator
3. Create a new script and paste the file contents
4. Save the script

---

## 💻 Usage

From the NumWorks interface:

```python
from calculatrice import *
run()
```

Or directly from the Scripts tab by running the file.

### Navigation

1. Choose between **Maths**, **Physics**, or **Formulas**
2. Navigate through sub-categories to select the desired calculation
3. Enter the requested values
4. View history at the end of the session

---

## 🏗 Code Structure

```
calculatrice.py
├── Physical constants (G, NA, c, mp, mn, me, g)
├── Hierarchical menus (option lists)
├── formulas[]          → list of 35 formulas
├── history[]           → list of calculations performed
├── round()             → rounds to 4 decimal places
├── input_safe()        → validated input with error handling
├── run_formula()       → calculation by index (Formulas mode)
├── run()               → main menu and navigation
└── Main loop           → session management and history display
```

| Element | Description |
| --- | --- |
| `calculatrice.py` | Main script containing the entire application |
| `round(valeur)` | Rounds a number to 4 decimal places |
| `input_safe(message, valeurs)` | Handles user input with validation |
| `run_formula(choix)` | Runs a formula by its index in the `formulas` list |
| `run()` | Displays the main menu and routes to sub-menus |
| `history` (list) | Stores each calculation performed, displayed at the end |

---

## 🔬 Built-in Constants

| Constant | Value | Description |
| --- | --- | --- |
| `G` | `6.674e-11` | Gravitational constant (N·m²/kg²) |
| `NA` | `6.02e23` | Avogadro's number (mol⁻¹) |
| `c` | `3e8` | Speed of light (m/s) |
| `g` | `9.81` | Gravitational acceleration (m/s²) |
| `MP` | `1.673e-27` | Proton mass (kg) |
| `MN` | `1.675e-27` | Neutron mass (kg) |
| `ME` | `9.110e-31` | Electron mass (kg) |

---

## 📐 Available Formulas

### Mathematics (18 formulas)
1. Square - x²
2. Cube - x³
3. Inverse - 1/x
4. Square Root - √x
5. Absolute Value - |x|
6. Factorial - n!
7. Exponential - e^x
8. Midpoint Coordinates
9. Distance Between Two Points
10. Pythagorean Theorem (Direct)
11. Pythagorean Theorem (Converse)
12. Thales' Theorem
13. Chasles' Relation (Vectors)
14. Vector Determinant
15. Triangle Angle Sum
16. Trigonometric Ratios (cos, sin, tan)
17. Inverse Trigonometric Functions (arccos, arcsin, arctan)
18. Rate of Change & Compound Rate

### Physics & Chemistry (17 formulas)
1. Density - ρ = m/V
2. Atomic Mass
3. Number of Moles - n = m/M
4. Dilution - C₁V₁ = C₂V₂
5. Ohm's Law - U = R×I
6. Electric Power - P = U×I
7. Electric Energy - E = P×t
8. Snell-Descartes Law - n₁×sin(i₁) = n₂×sin(i₂)
9. Refractive Index - n = c/v
10. Speed - v = d/t
11. Distance - d = v×t
12. Time - t = d/v
13. Gravitational Force - F = G×(m₁×m₂)/d²
14. Weight - P = m×g
15. Physical Constants Reference

---

## 📝 Example Usage

```
1: Maths, 2: Physics, 3: Formulas
Choice: 1

1: Functions, 2: Coordinates
3: Theorems, 4: Vectors
5: Triangles, 6: Rates
Choice: 3

1: Pythagorean, 2: Thales
Choice: 1

1: Theorem
2: Converse/Contrapositive
Choice: 1

The theorem is: a²+b²=c² (c is the unknown hypotenuse)
a: 3
b: 4
c = 5.0
```

---

## 🛠 Technologies

* **Language**: Python 3 / MicroPython
* **Platform**: NumWorks N0110 / N0120
* **Modules**: `math`, `time`

---

## 📄 License

This project is free to use for educational purposes.

---

## 👤 Author

**epicvixen73-arch** — feel free to contribute or report bugs!

---

*Happy calculating!* 🧮
