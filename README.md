# 🐢🏁 Turtle Race Game in Python

Welcome to **Turtle GUI Racing Challenge**, a fun and interactive project that uses Python's `turtle` module to simulate a colorful turtle race with random outcomes and user interaction! 🎨🐢

This project allows users to place bets, watch animated turtles race across the screen, and find out if their chosen turtle wins!

---

## ✨ What This Project Does

- 🏁 **Turtle Race Simulation**
- 🎨 **Six Colorful Turtle Racers**
- 🎲 **Random Movement Logic**
- 👤 **User Betting Interaction**
- 🐢 Built entirely with Python's built-in `turtle` module

---

## 🖼️ Visual Output

Below is an example of what the race might look like:

### 🐢 Turtle Race in Action
<img width="329" alt="turtal_race" src="https://github.com/user-attachments/assets/8c125680-331e-4de2-ab46-0a04638ac9bc" />


## 🧠 How It Works

### 1. `user_bet`
- Prompts the user to enter a color to bet on.
- The race only starts after the user makes a valid bet.

### 2. `winning_line`
- A vertical dashed finish line is drawn at the right edge of the race track.
- The first turtle to cross this line wins the race.

### 3. `all_turtles`
- Initializes six turtle objects, each with a unique color and position.
- Each turtle moves forward by a random number of pixels (0–10) in each iteration.

### 4. `Race Logic`
- A loop checks each turtle’s position.
- When a turtle crosses the finish line, the race stops and the result is printed in the console.

---

## 🧰 Project Structure

```text
📁 turtle-race-game/
│
├── main.py                 # Main race logic with turtle movement and user interaction
└── README.md               # Project documentation
