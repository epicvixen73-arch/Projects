# Integrated App in C#

An **integrated console application** in C# that combines the calculator and minigame projects with a central navigation menu. Features modular architecture, code reusability, and multi-level state management.

## 📋 Table of Contents

- [Main Features](#main-features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Main Menu Flow](#main-menu-flow)
- [Calculator Module](#calculator-module)
- [Minigame Module](#minigame-module)
- [Shared Methods](#shared-methods)
- [Technical Notes](#technical-notes)
- [OOP Concepts](#oop-concepts)
- [Possible Improvements](#possible-improvements)

---

## ✨ Main Features

### Calculator Module (Option 1)
Same as the `Calculatrice.cs` project:
* **5 Operators** — Addition, Subtraction, Multiplication, Division, Remainder
* **5 Functions** — Square, Cube, Square Root, Absolute Value, Inverse
* **Power calculations** — `a^n`
* Object-oriented architecture with abstract classes

### Minigame Module (Option 2)
A **"Juste Prix" guessing game**:
* Guess a number between **0 and 50**
* **5 attempts** to succeed
* Feedback: "The value is higher/lower"
* Win if your guess is within ±1 of the secret number
* Display of remaining attempts

### Main Menu (Option 3)
* **Quit** — Exit the application

---

## 🏗 Global Architecture

```
Program
├── Main() → Main Menu (3 options)
│
├── [1] Calculator
│   ├── abstract class Operation
│   │   ├── Addition, Subtraction, Multiplication, Division, Remainder
│   │   └── Calcul(a, b) & GetName()
│   │
│   ├── abstract class Fonctions
│   │   ├── Square, Cube, Inverse, Sqrt, Absolute
│   │   └── Fonction(a) & GetName()
│   │
│   └── Logic
│       ├── Operator/function menus
│       ├── Parameter input
│       └── Result display
│
├── [2] Juste Prix (Guessing Game)
│   ├── Random.Next(0, 51) → Generate secret number
│   ├── Loop (5 attempts)
│   │   ├── Get user guess
│   │   ├── Compare with ±1
│   │   └── Feedback + decrement attempts
│   └── Final result display
│
└── [3] Quit
    └── return;
```

---

## 📦 Requirements

* .NET Framework or .NET Core/5+
* C# compiler (`csc` or `dotnet`)

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/epicvixen73-arch/Projects.git
   cd Projects/CSharp/Appli
   ```

2. Or download the [`TestAppli.cs`](https://github.com/epicvixen73-arch/Projects/blob/main/CSharp/Appli/TestAppli.cs) file directly

---

## 💻 Usage

### Compile
```bash
csc TestAppli.cs
```

### Run
```bash
./TestAppli.exe
```

Or using dotnet:
```bash
dotnet run
```

### Initial Menu
```
===  Test_App  ===
1: Calculator
2: Guessing Game
3: Quit
Choice: 2
```

### Minigame Example
```
Ton guess: 25
La valeur est inférieur
4 / 5 essai(s) restant(s).
Ton guess: 20
Tu as gagné !
Fin du jeu, merci d'y avoir joué ! La valeur était : 21
```

---

## 🔄 Main Menu Flow

```
┌──────────────────────────────────────┐
│      === Test_App ===                │
│  1: Calculator                       │
│  2: Guessing Game                    │
│  3: Quit                             │
│  Choice:                             │
└──────────────────────────────────────┘
         │
    ┌────┼────┬─────────┐
    ▼    ▼    ▼         ▼
   [1]  [2]  [3]      ...
    │    │    │
    ▼    ▼    ▼
  Calc  Game  Quit
```

---

## 🧮 Calculator Module

Identical to `Calculatrice.cs` but encapsulated in a `case 1` switch statement:

1. Initialize `operations` & `fonctions` (lists)
2. Internal loop with `quitCalc` flag
3. Operator/power/function menu
4. Validate choices with overloaded `Saisir()`
5. Display result
6. Continue or quit to main menu

### Features
✅ Input validation with `TryParse`
✅ Range verification for menu selection
✅ Division by zero handling (implicit with potential Try-Catch)
✅ Infinite loop until quit (case 4)

---

## 🎮 Minigame Module

### Game State Variables

| Variable | Type | Description |
|----------|------|-------------|
| `random` | `Random` | Random number generator |
| `valueToGuess` | `int` | Secret number (0-50) |
| `guess` | `int` | User input |
| `nbGuess` | `int` | Remaining attempts (decrements) |
| `hasWon` | `bool` | Victory flag |

### Game Logic

```csharp
while (nbGuess > 0 && !hasWon) {
    // Request a guess
    if (Saisir(..., out guess, 51)) {

        // Check ±1
        if (guess == valueToGuess - 1 ||
            guess == valueToGuess ||
            guess == valueToGuess + 1) {
            hasWon = true;
            Console.WriteLine("You won!");
        } else {
            // Directive feedback
            Console.WriteLine(
                valueToGuess > guess ?
                "The value is higher" :
                "The value is lower"
            );
        }
    }
    nbGuess--;
    Console.WriteLine($"{nbGuess} / 5 attempt(s) remaining.");
}
```

### Features
* Random generation `Random.Next(0, 51)`
* Attempt counter (decrements each try)
* Directive feedback (higher/lower)
* Victory condition: `±1` around secret number
* Display of secret number at end of game

---

## ✅ Shared Methods

### `bool Saisir(string message, out int userChoice, int borne)`
Retrieves an **integer** with validation in `[1, borne]`

### `bool Saisir(string message, out float userChoice, float borne)`
Retrieves a **float** with validation in `[1, borne]`

### `bool IsInBorne(float choix, float borne)`
Verifies limits: `choix >= 1 && choix <= borne`

---

## ⚙️ Technical Notes

* **Namespace** — `Test_App`
* **Framework** — .NET Console Application
* **Parent class** — All operators/functions inherit from their abstract classes
* **Polymorphism** — Same interface `Calcul()` / `Fonction()`, multiple implementations
* **Overloading** — `Saisir()` in 2 versions (`int`, `float`)
* **Error handling** — TryParse + retry loop

---

## 🎯 OOP Concepts Demonstrated

* **Abstract class** — `Operation`, `Fonctions`
* **Inheritance** — 5 implementations of each
* **Polymorphism** — Uniform calls, diverse behaviors
* **Method overloading** — `Saisir()` for `int` and `float`
* **Collection enumeration** — Implicit `foreach` in menus
* **Flow control** — `while`, `switch`, flags `quitCalc`, `hasWon`

---

## 💡 Possible Improvements

- [ ] Handle division by zero with try-catch
- [ ] Add calculation history
- [ ] Difficulty options for minigame (attempts, range)
- [ ] Cumulative score between sessions
- [ ] File persistence (JSON/CSV)
- [ ] Multi-level navigation menu
- [ ] Sound effects for game events
- [ ] Statistics tracking (games played, win rate)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**epicvixen73-arch** — feel free to contribute or report bugs!

---

*Enjoy the integrated application!* 🚀
