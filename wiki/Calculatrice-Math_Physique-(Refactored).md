# Calculatrice Math_Physique (Refactored)

An interactive **Python 3** calculator covering math and physics formulas at the 10th grade level, refactored into a fully **data-driven menu architecture** (`Menu`/`Action` tree). Adding a new formula now takes one function + one line, with zero duplicated logic. Features 35 available formulas, calculation history, and input validation.

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Available Formulas](#available-formulas)
- [Adding New Calculations](#adding-new-calculations)
- [Example Run](#example-run)

---

## ✨ Features

### Mathematics

* **Basic functions**: square, cube, inverse, square root, absolute value
* **Special functions**: factorial, exponential
* **Coordinates**: midpoint, distance between two points
* **Theorems**: Pythagorean theorem (direct & converse), Thales' theorem (4 unknowns)
* **Vectors**: Chasles' relation (3 unknowns), determinant
* **Triangles**: angle sum, trigonometry (cos/sin/tan) and inverse functions (arccos/arcsin/arctan)
* **Rates**: rate of change, compound rate

### Physics

* **Matter**: density (3 unknowns), atomic mass, number of moles, dilution (2 unknowns)
* **Electricity**: Ohm's law (3 unknowns), electric power (3 formulas), electric energy
* **Optics**: Snell-Descartes law, refractive index (2 unknowns)
* **Kinematics**: average speed (speed/distance/time)
* **Forces**: gravitational force, weight

### General Features

* **Formula List**: Reference list of **35 formulas**, **automatically generated** from the menu tree — no manual maintenance needed
* **Direct Selection**: Execute any formula directly from the formula list
* **History**: Every calculation is recorded and summarized at the end of the session
* **Input Validation**: Invalid integers and decimals are re-requested in a loop without crashing the program

---

## 🏗 Architecture

This version maintains all features of the original calculator but relies on a **fully data-driven architecture** (a tree of `Menu` / `Action`) rather than a succession of `if/elif` blocks. Result: a single place where each calculation is described, with no duplication between navigation and formula lists.

The entire calculator is built on two data structures:

```python
@dataclass
class Action:
    label: str                     # text displayed in the menu
    fonction: Callable[[], None]   # the calculation to execute
    formule: Optional[str] = None  # text displayed in "Formulas"

@dataclass
class Menu:
    label: str
    items: list                    # child Action or Menu items
    formule: Optional[str] = None
    recapitulatif: bool = False
```

A generic engine (`choisir`, `executer_noeud`) traverses this structure without knowing its content: it displays options from `menu.items`, requests a choice, and recursively descends until reaching an executable `Action`.

The **"Formulas"** section is calculated from this same tree (`collecter_formules`). It can never become desynchronized from the navigation menus because there is now only one source of truth per calculation.

---

## 📦 Requirements

* Python 3.9+ (uses `dataclasses` and `list[str]` annotations)
* No external libraries: standard library only (`math`, `time`, `dataclasses`, `typing`)

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/epicvixen73-arch/Projects.git
   cd Projects/Calculatrice/Base\ PC\ \(refactored\)
   ```

2. Or download the [`Calc.py`](https://github.com/epicvixen73-arch/Projects/blob/main/Calculatrice/Base%20PC%20(refactored)/Calc.py) file directly

---

## 💻 Usage

1. Run the script:
   ```bash
   python Calc.py
   ```

2. Follow the menus:
   * Choose **Maths**, **Physics**, or **Formulas**
   * Navigate through sub-categories to the desired calculation
   * Enter the requested values

3. At the end of each calculation, indicate if you're done to display the history, or continue

---

## 🏗 Code Structure

| Element | Role |
| --- | --- |
| `Action` / `Menu` | Data model describing a calculation or grouping of calculations |
| `choisir(menu)` | Displays menu options and returns the selected item |
| `executer_noeud(noeud)` | Descends through the tree to an `Action`, then executes it |
| `collecter_formules(menu)` | Automatically generates the "Formulas" reference list from the tree |
| `calc_xxx()` | One function per calculation: input, calculation, display, history |
| `ARBRE` | Root of the menu tree (Maths / Physics / Formulas) |
| `historique` (list) | Stores each calculation performed, displayed at end of session |

Physical constants (`G_UNIVERSELLE`, `G_TERRESTRE`, `NA`, `C_LUMIERE`, particle masses) are defined at the top of the file.

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

### Physics (17 formulas)
1. Density - ρ = m/V (3 unknowns)
2. Atomic Mass
3. Number of Moles - n = m/M
4. Dilution - C₁V₁ = C₂V₂ (2 unknowns)
5. Ohm's Law - U = R×I (3 unknowns)
6. Electric Power - P = U×I
7. Electric Power - P = R×I²
8. Electric Power - P = U²/R
9. Electric Energy - E = P×t
10. Snell-Descartes Law - n₁×sin(i₁) = n₂×sin(i₂)
11. Refractive Index - n = c/v (2 unknowns)
12. Speed - v = d/t
13. Distance - d = v×t
14. Time - t = d/v
15. Gravitational Force - F = G×(m₁×m₂)/d²
16. Weight - P = m×g
17. Physical Constants Reference

---

## ➕ Adding New Calculations

This is the main advantage of this architecture: **only one place to modify**, compared to four before (validation list, navigation `elif` branch, execution `elif` branch, formula table).

### Step 1: Write a calculation function

Create a function that reads inputs, calculates, displays, and logs:

```python
def calc_logarithme():
    x = saisir_nombre("x: ")
    res = arrondi(log(x))
    print(f"ln({x}) = {res}")
    historique.append(f"Logarithm: ln({x}) = {res}")
```

### Step 2: Declare it in the relevant Menu

Add it as an `Action` in the appropriate menu:

```python
Action("Logarithm", calc_logarithme, "ln(x)"),
```

That's it! No list to extend, no `elif` to add elsewhere, no index to synchronize: the navigation menu **and** the "Formulas" list update automatically.

---

## 📝 Example Run

```
Calculatrice
  1: Maths
  2: Physics
  3: Formulas
Choice: 1

Maths
  1: Functions
  2: Coordinates
  3: Theorems
  4: Vectors
  5: Triangles
  6: Rates
Choice: 1

Functions
  1: Basic
  2: Special
Choice: 1

Basic
  1: Square
  2: Cube
  3: Inverse
  4: Square root
  5: Absolute value
Choice: 1

x: 5
L'image de 5.0 est 25.0 par la fonction carrée.
```

---

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and redistribute it.

---

## 👤 Author

**epicvixen73-arch** — feel free to contribute or report bugs!

---

*Happy calculating!* 🧮
