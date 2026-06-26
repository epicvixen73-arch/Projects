# Math & Physics Calculator (PC)

An interactive **Python 3** calculator covering math and physics formulas at the 10th grade level with hierarchical menus, calculation history, input validation, and 33+ available formulas.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Available Formulas](#available-formulas)
- [Example Run](#example-run)
- [Customization](#customization)

---

## ✨ Features

### Mathematics

* **Basic functions**: square, cube, inverse, square root, absolute value, factorial, exponential
* **Coordinates**: midpoint and distance between two points
* **Theorems**: Pythagorean theorem (direct and converse), Thales' theorem
* **Vectors**: Chasles' relation, determinant
* **Triangles**: angle sum, trigonometry (cos, sin, tan) and their inverses (arccos, arcsin, arctan)
* **Rates**: rate of change, compound rate

### Physics

* **Matter**: density, atomic mass, number of moles, dilution
* **Electricity**: Ohm's law, electric power, electric energy
* **Optics**: Snell-Descartes law, refractive index
* **Kinematics**: speed, distance, time
* **Forces**: gravitational force, weight

### General Features

* **Formula List**: Complete list of all available formulas with the option to run them directly
* **History**: Every operation is recorded and displayed at the end of the session
* **Input Validation**: Handles invalid inputs (non-numeric values, out-of-range choices)

---

## 📦 Requirements

* Python 3.x (tested with Python 3.7+)
* No external libraries required (standard library only)

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/epicvixen73-arch/Projects.git
   cd Projects/Calculatrice/Base PC
   ```

2. Or download the [`FinalV2.py`](https://github.com/epicvixen73-arch/Projects/blob/main/Calculatrice/Base%20PC/FinalV2.py) file directly

---

## 💻 Usage

1. Run the script:
   ```bash
   python FinalV2.py
   ```

2. Follow the menus:
   * Choose between **Maths**, **Physics**, or **Formulas**
   * Navigate through sub-categories to select the desired calculation
   * Enter the requested values

3. At the end of each session, you can view the history or continue

---

## 🏗 Code Structure

| File / Element | Description |
| --- | --- |
| `FinalV2.py` | Main script containing the entire application |
| `arrondi(valeur)` | Rounds a number to 4 decimal places |
| `saisir(message, valeurs)` | Handles user input with validation |
| `executer_formule(choix)` | Runs a formula by its index in the `formules` list |
| `run()` | Displays the main menu and routes to sub-menus |
| `historique` (list) | Stores each calculation performed, displayed at the end |

Physical constants (G, NA, c, masses, etc.) are defined at the top of the file.

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

### Physics (15 formulas)
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

## 📝 Example Run

```
1: Maths, 2: Physics, 3: Formulas
Choice: 1

1: Functions, 2: Coordinates
3: Theorems, 4: Vectors
5: Triangles, 6: Rates
Choice: 1

1: Basic, 2: Special
Choice: 1

1: Square, 2: Cube
3: Inverse, 4: Square root
5: Absolute value
Choice: 1

x: 5
The image of 5.0 is 25.0 by the square function.
```

---

## 🔧 Customization

You can easily add new formulas:

1. Define the formula in the `formules` list (with its index)
2. Add an `elif` branch in `executer_formule` with the corresponding calculation code
3. If the formula should also appear in the classic menus, add it to the relevant data structures (e.g. `maths_H1`, `math_fn`, etc.)

---

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and redistribute it.

---

## 👤 Author

**epicvixen73-arch** — feel free to contribute or report bugs!

---

*Happy calculating!* 🧮
