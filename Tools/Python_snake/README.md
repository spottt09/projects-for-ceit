
# 🐍 Python Snake Game

A classic Snake arcade game built using Python's built-in `tkinter` GUI library. Guide the snake around the board, eat the red food pellets to grow longer, and rack up your high score!

---

## ✨ Features

* **Classic Grid-Based Gameplay:** Smooth movement across a customizable game board.
* **Dynamic Scoring:** Real-time score tracking displayed at the top of the window.
* **Responsive Controls:** Instant directional changes using your keyboard's arrow keys (with built-in prevention against 180-degree self-reversals).
* **Centered Window Launch:** Automatically calculates screen dimensions to launch the game window right in the center of your display.
* **Zero External Dependencies:** Runs completely on Python's standard library (`tkinter` and `random`).

---

## 🛠️ Prerequisites

Make sure you have **Python 3.x** installed on your system. Since `tkinter` comes pre-installed with most standard Python distributions, no additional `pip` packages are required.

> **Linux Users:** If `tkinter` is not installed by default on your distribution, you can install it via your package manager (e.g., `sudo apt-get install python3-tk` on Ubuntu/Debian).

---

## 🚀 How to Run

1. **Clone or download** this repository to your local machine.
2. **Save the script** (e.g., as `snake_game.py`).
3. **Open your terminal or command prompt**, navigate to the project directory, and run:

```bash
python snake_game.py
```

---

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| **Up Arrow (`↑`)** | Move Up |
| **Down Arrow (`↓`)** | Move Down |
| **Left Arrow (`←`)** | Move Left |
| **Right Arrow (`→`)** | Move Right |

---

## ⚙️ Customization

You can easily tweak the game's difficulty, size, and appearance by modifying the constants at the top of the Python script:

```python
GAME_WIDTH = 500          # Width of the game canvas in pixels
GAME_HEIGHT = 500         # Height of the game canvas in pixels
SPEED = 70                # Game tick speed in milliseconds (lower = faster)
SPACE_SIZE = 30           # Size of each grid cell/snake segment
BODY_PART = 3             # Initial body part configuration
SNAKE_COLOR = "#00FF00"   # Hex color for the snake (Neon Green)
FOOD_COLOR = "#FF0000"    # Hex color for the food (Red)
BACKGROUND_COLOR = "#000000" # Hex color for the canvas background (Black)
```

---

## 🚧 Roadmap & Known Limitations

This project is currently in active development. Upcoming features and fixes include:
* [ ] **Collision Detection:** Implementing `check_collision()` to detect when the snake hits the wall boundaries or its own body.
* [ ] **Game Over Screen:** Implementing `game_over()` to stop the game loop and display a "Game Over" message/restart option.
* [ ] **Grid Alignment:** Ensuring `GAME_WIDTH` and `GAME_HEIGHT` are exact multiples of `SPACE_SIZE` so food never spawns partially off-edge.

---

## 📄 License

This project is open-source and free to use for learning and personal projects.
