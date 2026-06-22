# 🗂️ Projects

Welcome to my personal projects repository!  
Here you'll find tools I built to automate, calculate, and customize my setup.

---
- [1st Project -   Math & Physics Calculator (PC)](https://github.com/epicvixen73-arch/Projects/tree/main#1--math--physics-calculator-pc)
- [2nd Project -   NumWorks Calculator](https://github.com/epicvixen73-arch/Projects/tree/main#2--numworks-calculator)
- [3rd Project -   Spicetify Setup on Windows & Linux](https://github.com/epicvixen73-arch/Projects/tree/main#3--spicetify-setup-on-windows--linux)
- [4th Project -   Calculator in C#](https://github.com/epicvixen73-arch/Projects/blob/main/README.md#4---calculator-in-c)
- [5th Project -   Minigame in C#](https://github.com/epicvixen73-arch/Projects/blob/main/README.md#5---minigame-in-c)
- [6th Project -   App in C#](https://github.com/epicvixen73-arch/Projects/blob/main/README.md#6---app-in-c)
--- 

## 📦 Available Projects

### 1 - [Math & Physics Calculator (PC)](https://github.com/epicvixen73-arch/Projects/blob/main/Calculatrice/Full%20Calculator%20(FinalV2).md)
An interactive **Python 3** calculator covering math and physics formulas at the 10th grade level.  
Hierarchical menus, calculation history, input validation, 33+ available formulas.  
→ Main file: [`FinalV2.py`](FinalV2.py)

---

### 2 - [NumWorks Calculator](https://github.com/epicvixen73-arch/Projects/blob/main/Calculatrice/Numworks%20Calculator.md)
The same calculator, adapted for the **NumWorks N0110/N0120** in **MicroPython**.  
35 formulas, compact menus, built-in physical constants.  
→ Main file: [`calculatrice_numworks.py`](calculatrice_numworks.py)

---

### 3 - [Spicetify Setup on Windows & Linux](https://github.com/epicvixen73-arch/Projects/blob/main/Spicetify/Spicetify_setup.md)
A step-by-step guide to install **Spicetify + Marketplace** on standalone Spotify.  
Includes automatic update blocking and troubleshooting.  
Available on **Windows** and **Linux** (Ubuntu, Arch, Fedora).

**Automated installation scripts:**

| Platform | Script | Usage |
|---|---|---|
| Windows | [`install-spicetify.ps1`](https://github.com/epicvixen73-arch/Projects/blob/main/Spicetify/install-spicetify.ps1) | PowerShell (without admin) |
| Linux | [`install-spicetify.sh`](https://github.com/epicvixen73-arch/Projects/blob/main/Spicetify/install-spicetify.sh) | `bash install-spicetify.sh` |

---
## 🚧 In Construction 🚧
### 4 - Calculator in C#
An **interactive console calculator** with object-oriented architecture using abstract classes and inheritance.

**Operators** — Addition, Subtraction, Multiplication, Division, Remainder  
**Functions** — Square, Cube, Square Root, Absolute Value, Inverse  
**Powers** — Computes `a^n` for any exponent  

**Architecture** — Abstract classes `Operation` and `Fonctions` with polymorphic implementations, overloaded input validation in 2 versions (`int`, `float`)

→ Detailed documentation: [`Calculatrice_CSharp.md`](https://github.com/epicvixen73-arch/Projects/blob/main/CSharp/Calculatrice/Calculatrice_CSharp.md)

---

### 5 - Minigame in C#
A **simple guessing game** — Guess a number between 0 and 50 in 5 attempts.

**Mechanics** — You win if your guess is exactly **or within ±1** of the secret number  
**Feedback** — The game indicates whether the value is higher or lower  
**Validation** — Robust error handling with retry on invalid input

**Key points** — Random generation with `Random.Next()`, attempt counter, display of the secret number at the end of the game

→ Detailed documentation: [`Minigame_Juste_Prix.md`](https://github.com/epicvixen73-arch/Projects/blob/main/CSharp/Minigame/Minigame_Juste_Prix.md)

---

### 6 - App in C#
Testing the Creation of an App that for the moment contain the calculator and the minigame in it.
An **integrated application** that combines the two previous projects with a **central navigation menu**.

**Main Menu**:
1. **Calculator** — All the power of the calculator module as an option
2. **Juste Prix** — Play the minigame at any time
3. **Exit** — Close the application

**Architecture** — Reuses the abstract classes (`Operation`, `Fonctions`), overloaded validation methods (`Saisir()`), and the minigame logic in an optional switch

**Concepts demonstrated** — Multi-level polymorphism, state management with flags, nested flow control, code reusability

→ Detailed documentation: [`TestAppli_CSharp.md`](https://github.com/epicvixen73-arch/Projects/blob/main/CSharp/TestAppli_CSharp.md)

## Technologies Used

- Python 3 / MicroPython
- PowerShell / Bash (Windows / Linux & macOS scripting)
- C#

---

## Author

**epicvixen73-arch** — feel free to open an issue or fork!
