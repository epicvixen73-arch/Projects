# Calculator in C#

An **interactive console calculator** in C# with object-oriented architecture using abstract classes and inheritance. Features operators, mathematical functions, and power calculations with robust input validation.

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Main Variables](#main-variables)
- [Validation Methods](#validation-methods)
- [Main Loop Flow](#main-loop-flow)
- [OOP Concepts](#oop-concepts)
- [Example Interaction](#example-interaction)

---

## ✨ Features

### Arithmetic Operators
* **Addition** — `a + b`
* **Subtraction** — `a - b`
* **Multiplication** — `a × b`
* **Division** — `a ÷ b`
* **Remainder (modulo)** — `a % b`

### Mathematical Functions
* **Square** — `x²` (uses `Math.Pow`)
* **Cube** — `x³`
* **Square Root** — `√x`
* **Absolute Value** — `|x|`
* **Inverse** — `1/x`

### Powers
* Computes **`a^n`** for any integer exponent

---

## 🏗 Architecture

```
Program
├── abstract class Operation
│   ├── Addition
│   ├── Soustraction
│   ├── Multiplication
│   ├── Division
│   └── Reste
│
├── abstract class Fonctions
│   ├── Carre
│   ├── Cube
│   ├── Racine
│   ├── Absolue
│   └── Inverse
│
└── Helper Methods
    ├── Saisir(string, out int, int)
    ├── Saisir(string, out float, float)
    └── IsInBorne(float, float)
```

### Key Points
* **Abstract classes** — `Operation` and `Fonctions` define contracts
* **Polymorphism** — Each operation/function implements `Calcul()` / `Fonction()`
* **Input validation** — Overloaded `Saisir()` method for `int` and `float`
* **Range management** — Verifies user input is within valid range

---

## 📦 Requirements

* .NET Framework or .NET Core/5+
* C# compiler (`csc` or `dotnet`)

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/epicvixen73-arch/Projects.git
   cd Projects/CSharp/Calculatrice
   ```

2. Or download the [`calculatrice.cs`](https://github.com/epicvixen73-arch/Projects/blob/main/CSharp/Calculatrice/calculatrice.cs) file directly

---

## 💻 Usage

### Compile
```bash
csc calculatrice.cs
```

### Run
```bash
./calculatrice.exe
```

Or using dotnet:
```bash
dotnet run
```

---

## 🏗 Code Structure

| File | Description |
| --- | --- |
| `calculatrice.cs` | Main script containing the entire application |

### Class Hierarchy

| Class | Type | Purpose |
| --- | --- | --- |
| `Operation` | Abstract | Base class for arithmetic operations |
| `Addition` | Concrete | Implements `a + b` |
| `Soustraction` | Concrete | Implements `a - b` |
| `Multiplication` | Concrete | Implements `a × b` |
| `Division` | Concrete | Implements `a ÷ b` |
| `Reste` | Concrete | Implements `a % b` |
| `Fonctions` | Abstract | Base class for mathematical functions |
| `Carre` | Concrete | Implements `x²` |
| `Cube` | Concrete | Implements `x³` |
| `Racine` | Concrete | Implements `√x` |
| `Absolue` | Concrete | Implements `|x|` |
| `Inverse` | Concrete | Implements `1/x` |

---

## 📊 Main Variables

| Variable | Type | Description |
|----------|------|-------------|
| `operations` | `List<Operation>` | List of 5 available operators |
| `fonctions` | `List<Fonctions>` | List of 5 available functions |
| `choix` | `int` | Main menu choice (1-4) |
| `a_ope`, `b` | `float` | Operands for calculations |
| `x` | `float` | Argument for a function |

---

## ✅ Validation Methods

### `bool Saisir(string message, out int choix, int borne)`
Retrieves an **integer** with validation in the range `[1, borne]`

### `bool Saisir(string message, out float choix, float borne)`
Retrieves a **float** with validation in the range `[1, borne]`

### `bool IsInBorne(float choix, float borne)`
Verifies that the choice respects the limits

---

## 🔄 Main Loop Flow

```
┌─────────────────────────────────────┐
│  Main Menu                          │
│  [1] Operator  [2] Powers           │
│  [3] Functions [4] Quit             │
└─────────────────────────────────────┘
         │
    ┌────┴────┬────────┬──────────┐
    ▼         ▼        ▼          ▼
 Select    Enter    Choose      Quit
 operator  a & b   function
    │         │        │
    └─────────┴────────┘
         ▼
    Calculate & Display
    the result
```

1. Display main menu
2. Get user choice (validated)
3. Based on choice:
   - **Case 1**: Select an operation, request `a` and `b`, display result
   - **Case 2**: Request `a` and `n`, calculate `a^n`
   - **Case 3**: Select a function, request `x`, display result
   - **Case 4**: Exit loop
4. Loop until quit

---

## 🎯 OOP Concepts Used

* **Abstract classes** — Define common interface
* **Inheritance** — Each operation/function inherits from its abstract class
* **Polymorphism** — Same call `Calcul()` / `Fonction()`, different implementations
* **Collection enumeration** — Iterating through lists of operations/functions
* **Method overloading** — `Saisir()` exists in 2 versions (`int`, `float`)

---

## 📝 Example Interaction

```
#######################
-----[1]: Opérateur----
-----[2]: Puissances---
-----[3]: Fonctions----
-----[4]: Quit---------
Choix: 1

-------Opérateur-------
[1] Addition
[2] Soustraction
[3] Multiplication
[4] Division
[5] Reste
Choix: 1
-----------------------
a: 10
b: 5
Result: 15
```

---

## ⚙️ Technical Notes

* **Namespace** — `Calculatrice`
* **Framework** — .NET (Console Application)
* **Numeric type** — `float` for calculations (can be changed to `double` for more precision)
* **Error handling** — TryParse with retry loop on invalid input

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**epicvixen73-arch** — feel free to contribute or report bugs!

---

*Happy calculating!* 🧮
