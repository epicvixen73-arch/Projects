# Math & Physics Calculator

This project is an interactive Python calculator offering a wide range of mathematical and physics formulas.
It lets you quickly compute functions, theorems, physical quantities, and much more — with a full history of every calculation performed.

---

## Features

### Mathematics

* **Basic functions**: square, cube, inverse, square root, absolute value, factorial, exponential.
* **Coordinates**: midpoint and distance between two points.
* **Theorems**: Pythagorean theorem (direct and converse), Thales' theorem.
* **Vectors**: Chasles' relation, determinant.
* **Triangles**: angle sum, trigonometry (cos, sin, tan) and their inverses (arccos, arcsin, arctan).
* **Rates**: rate of change, compound rate.

### Physics

* **Matter**: density, atomic mass, number of moles, dilution.
* **Electricity**: Ohm's law, electric power, electric energy.
* **Optics**: Snell-Descartes law, refractive index.
* **Kinematics**: speed, distance, time.
* **Forces**: gravitational force, weight.

### Formulas

* A complete list of all available formulas with the option to run them directly.

### Other

* **History**: every operation is recorded and displayed at the end of the session.
* **Input validation**: handles invalid inputs (non-numeric values, out-of-range choices).

---

## Requirements

* Python 3.x (tested with Python 3.7+)
* No external libraries required (standard library only).

---

## Usage

1. Clone the repository or download the `FinalV2.py` file.
2. Run the script:

   ```
   python FinalV2.py
   ```
3. Follow the menus:
   * Choose between **Maths**, **Physics**, or **Formulas**.
   * Navigate through sub-categories to select the desired calculation.
   * Enter the requested values.
4. At the end of each session, you can view the history or continue.

---

## Code Structure

| File / Element | Description |
| --- | --- |
| `FinalV2.py` | Main script containing the entire application. |
| `arrondi(valeur)` | Rounds a number to 4 decimal places. |
| `saisir(message, valeurs)` | Handles user input with validation. |
| `executer_formule(choix)` | Runs a formula by its index in the `formules` list. |
| `run()` | Displays the main menu and routes to sub-menus. |
| `historique` (list) | Stores each calculation performed, displayed at the end. |

Physical constants (G, NA, c, masses, etc.) are defined at the top of the file.

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

## Customization

You can easily add new formulas:

* Define the formula in the `formules` list (with its index).
* Add an `elif` branch in `executer_formule` with the corresponding calculation code.
* If the formula should also appear in the classic menus, add it to the relevant data structures (e.g. `maths_H1`, `math_fn`, etc.).

---

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and redistribute it.

---

## 👤 Author

Project by **epicvixen73-arch** — feel free to contribute or report bugs!

---

*Happy calculating!*
