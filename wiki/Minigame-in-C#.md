# Minigame in C#

A **simple guessing game** written in C# with input validation and interactive feedback. Guess a number between 0 and 50 in 5 attempts with a ±1 tolerance for winning.

## 📋 Table of Contents

- [Game Rules](#game-rules)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Win Logic](#win-logic)
- [Key Variables](#key-variables)
- [Execution Flow](#execution-flow)
- [Methods](#methods)
- [Technical Notes](#technical-notes)
- [Example Game State](#example-game-state)
- [Possible Improvements](#possible-improvements)
- [User Experience](#user-experience)

---

## 🎮 Game Rules

| Aspect | Detail |
|--------|--------|
| **Objective** | Guess a secret number between **0 and 50** |
| **Attempts** | You have **5 tries** |
| **Win Condition** | Your guess is exact **or within ±1** of the secret number |
| **Feedback** | The game tells you if the secret is higher/lower |
| **End Game** | Displays the secret number after 5 attempts or victory |

---

## 🏗 Architecture

```
Program
├── Main()
│   ├── Initialization
│   │   ├── Random al = new Random()
│   │   ├── int NbGuess = 5
│   │   ├── int valueToGuess = al.Next(0, 51)
│   │   └── int Score = 0 (0=lost, 1=won)
│   │
│   └── Game Loop
│       ├── while (NbGuess > 0 && Score == 0)
│       │   ├── Call Saisir(..., valueToGuess)
│       │   ├── If valid → IsInBorne()
│       │   ├── If win → Score = 1
│       │   ├── Else → Feedback
│       │   └── Decrement NbGuess
│       │
│       └── End Game → Display result
│
├── bool Saisir(string, out int, int)
│   └── User input validation
│
└── bool IsInBorne(float, float)
    └── Verification ±1 of secret number
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
   cd Projects/CSharp/Minigame
   ```

2. Or download the [`Minigame_Juste-Prix.cs`](https://github.com/epicvixen73-arch/Projects/blob/main/CSharp/Minigame/Minigame%20%22Juste_prix%22.cs) file directly

---

## 💻 Usage

### Compile
```bash
csc "Minigame Juste_prix.cs"
```

### Run
```bash
./"Minigame Juste_prix.exe"
```

Or using dotnet:
```bash
dotnet run
```

### Example Session
```
Ton guess: 25
Choix valide !
Choix invalide !    [The number was ≠ 25±1]
4 / 5 essai(s) restant(s).

Ton guess: 30
Choix valide !
0 / 5 essai(s) restant(s).

Fin du jeu, merci d'y avoir joué !
```

---

## 🏆 Win Logic

To **win**, your guess must satisfy one of these conditions:

```csharp
guess == aleatoire - 1   // One below
|| guess == aleatoire    // Exact!
|| guess == aleatoire + 1 // One above
```

This mechanic makes the game **more accessible** without being trivial.

---

## 📊 Key Variables

| Variable | Type | Value/Role |
|----------|------|------------|
| `al` | `Random` | Pseudo-random generator |
| `valueToGuess` | `int` | Secret number (0-50) |
| `UserGuess` | `int` | User input |
| `NbGuess` | `int` | Counter (5 → 0) |
| `Score` | `int` | 0=In progress, 1=Victory |
| `Credit` | `string` | End message |

---

## 🔄 Execution Flow

```
┌─────────────────────────────────┐
│ Initialize Random & Number      │
│ aleatoire ∈ [0, 51[             │
│ NbGuess = 5                     │
│ Score = 0                       │
└──────────────┬──────────────────┘
               │
        ┌──────▼───────────────┐
        │ while (NbGuess>0 &&  │
        │        Score==0)     │
        └──────┬───────────────┘
               │
        ┌──────▼──────────────┐
        │ Request user guess  │
        └──────┬──────────────┘
               │
        ┌──────▼──────────────┐
        │ Validate input      │
        │ IsInBorne()         │
        └──────┬──────────────┘
               │
        ┌──┬───▼────┬──┐
        ▼  ▼        ▼  ▼
      Lost  Exact  ±1  ...
        │     │     │
        ▼     ▼     ▼
      Feedback Victory
        │             │
        └──────┬──────┘
               │
        NbGuess--
        │
        └─────► (back to loop)
```

---

## ✅ Methods

### `bool Saisir(string message, out int UserGuess, int aleatoire)`

**Role** — Retrieves user input and validates it

**Parameters**:
- `message`: Text to display to the user
- `UserGuess`: The entered value (output)
- `aleatoire`: The number to guess (for IsInBorne)

**Logic**:
1. Display the message
2. Infinite loop:
   - Read a line
   - Try to parse as `int`
   - If success → call `IsInBorne()` and return the result
   - If failure → display "Invalide, reboot..." and return `false`

### `bool IsInBorne(float UserGuess, float aleatoire)`

**Role** — Checks if the guess is in the winning zone

**Logic**:
```csharp
if (UserGuess == aleatoire - 1 ||
    UserGuess == aleatoire ||
    UserGuess == aleatoire + 1) {
    Console.WriteLine("Choix valide !");
    return true;
} else {
    Console.WriteLine("Choix invalide !");
    return false;
}
```

---

## ⚙️ Technical Notes

* **Namespace** — `Juste_prix`
* **Framework** — .NET Console Application
* **Random generation** — `Random.Next(0, 51)` → integers from 0 to 50 (51 excluded)
* **Validation** — `int.TryParse()` with retry loop
* **Display** — Console.Write / Console.WriteLine

---

## 📝 Example Game State

| Step | `aleatoire` | `guess` | `NbGuess` | `Score` | Result |
|-------|------------|---------|-----------|---------|----------|
| Initial | 25 | - | 5 | 0 | In progress |
| Attempt 1 | 25 | 20 | 5 | 0 | Invalid (< 24) |
| Attempt 2 | 25 | 26 | 4 | 0 | Valid! ±1 ✓ |
| Final | 25 | 26 | 4 | 1 | **Victory** |

---

## 💡 Possible Improvements

- [ ] **Score by difficulty** — Fewer attempts = more points
- [ ] **Game modes** — Easy (0-20), Normal (0-50), Hard (0-100)
- [ ] **Leaderboard** — Persistence of best scores
- [ ] **Richer feedback** — "You're hot!" vs "Cold"
- [ ] **Sound/Vibration** — Auditory feedback on victory
- [ ] **Replay menu** — Option to restart a game without restarting

---

## 👥 User Experience

### Positives
* Simple and accessible mechanics
* Immediate feedback (higher/lower)
* Motivating attempt counter
* Display of secret number at the end

### To Improve
* No cumulative score
* No progressive difficulty
* End message a bit abrupt
* No "replay" option

---

## 🎯 C# Concepts Used

* **`Random` class** — Random number generation
* **Method overloading** — Single `Saisir()` method
* **Validation with TryParse** — Parsing error handling
* **Loops (`while`)** — Retry on error, main game loop
* **Conditions (`if`/`else`)** — Directive feedback
* **Flags (`NbGuess`, `Score`)** — Flow control

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**epicvixen73-arch** — feel free to contribute or report bugs!

---

*Happy guessing!* 🎲
