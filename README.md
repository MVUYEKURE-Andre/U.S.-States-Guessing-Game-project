# U.S.-States-Guessing-Game-project
U.S. States Guessing Game project on a map 
<img width="1911" height="846" alt="image" src="https://github.com/user-attachments/assets/55d7bd08-5136-4f7c-b16f-fa914e05fc47" />

# U.S. States Guessing Game 🗺️ (Python + Turtle + Pandas)

This is an interactive **geography quiz game** where you guess all 50 U.S. states.  
The game uses Python’s `turtle` graphics to display a U.S. map, and `pandas` to manage state data and track your progress.

---

## Features
- Interactive map where players **type in the name of U.S. states**.
- Each correct guess is **written on the map at the correct location**.
- Players can type `Exit` anytime to quit the game:
  - A **CSV file** (`missing_states_after_guess.csv`) is generated listing the states you missed.
- Uses **list comprehension** for a clean way to generate missing states.

---

## How to Play
1. The game will show a blank U.S. map.
2. Enter the name of a state (case-insensitive) when prompted.
3. If your guess is correct, the state name appears on the map.
4. Guess all 50 states to win, or type `Exit` to quit early and see which states you missed.

---

## Controls
- **Type a state name** → Guess a state.
- **Type `Exit`** → End the game and get a CSV file of missed states.

---

## How to Run
1. Make sure you have **Python 3.x** installed.
2. Install the required Python libraries:
   ```bash
   pip install pandas
<img width="1911" height="838" alt="image" src="https://github.com/user-attachments/assets/dae370d5-050a-4122-810f-5b04333f8076" />
