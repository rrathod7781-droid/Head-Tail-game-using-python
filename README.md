# Head-Tail-game-using-python
# 🪙 Head-Tail Game (Python)

A simple command-line coin toss game where the user guesses **Head** or **Tail** and plays against the system.

---

## 📸 Sample Output

Below is the output of the game:

<p align="center">
  <img src="images/output.png" alt="Head Tail Game Output" width="600"/>
</p>

> ⚠️ Make sure to place your screenshot inside a folder named `images` and name it `output.png`

---

## 📌 How the Game Works

- The user enters the number of rounds.
- For each round:
  - The user chooses **Head** or **Tail**.
  - The system tosses a coin randomly.
  - If the guess is correct → User1 wins.
  - Otherwise → User2 wins.
- Scores are updated after every round.
- Final winner is announced at the end.

---

## 🧠 Output Explanation

### 🔁 Round 1
- User chooses: `head`
- Coin result: `head`
- ✅ Match → **User1 wins**
- Score → User1: 1 | User2: 0

---

### 🔁 Round 2
- User chooses: `tail`
- Coin result: `tail`
- ✅ Match → **User1 wins**
- Score → User1: 2 | User2: 0

---

### 🔁 Round 3
- User enters invalid input: `toil`
- ❌ Program shows error: `Plz enter valid input`
- User re-enters: `tail`
- Coin result: `tail`
- ✅ Match → **User1 wins**
- Score → User1: 3 | User2: 0

---

## 🏆 Final Result

- 🎉 **User1 wins the game!**

---

## 🚀 How to Run

```bash
python head_tail_game.py
