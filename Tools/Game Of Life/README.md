
# Conway's Game of Life (Tkinter)

A lightweight, interactive desktop implementation of John Conway's **Game of Life** built entirely with Python's standard library (`tkinter` and `random`).

## Overview

Conway's Game of Life is a zero-player cellular automaton where cells on a 2D grid live, die, or multiply based on a few simple mathematical rules. This application renders a 25 \times 25 grid on a Tkinter canvas and updates every 200\text{ ms} when running.

### Rules of the Simulation
Every cell interacts with its eight horizontal, vertical, and diagonal neighbors:
1. **Underpopulation:** Any live cell with fewer than 2 live neighbors dies.
2. **Survival:** Any live cell with 2 or 3 live neighbors lives on to the next generation.
3. **Overpopulation:** Any live cell with more than 3 live neighbors dies.
4. **Reproduction:** Any dead cell with exactly 3 live neighbors becomes a live cell.

---

## Features

- **Zero External Dependencies:** Uses only built-in Python modules (`tkinter` and `random`).
- **Interactive Controls:**
  - **Start:** Begins the simulation loop (5 generations per second).
  - **Stop:** Pauses the current simulation state.
  - **Random:** Populates the grid with a new random distribution of live and dead cells.
  - **Clear:** Resets all cells on the board to dead (`0`).
- **Configurable Grid:** Easily adjust `CELL_SIZE`, `ROWS`, and `COLS` directly in the script to customize board dimensions.

---

## Prerequisites

- **Python 3.x** installed on your system.
- **Tkinter** (included by default with standard Python installations on Windows and macOS; on some Linux distributions, install via `sudo apt-get install python3-tk`).

---

## Getting Started

1. **Save the script** as `game_of_life.py` (or clone the repository containing the file).
2. **Run the application** from your terminal or command prompt:

```bash
python game_of_life.py
```

---

## Customization

You can modify the constants at the top of `game_of_life.py` to change the grid size and simulation speed:

```python
CELL_SIZE = 20  # Pixel width/height of each cell
ROWS = 25       # Number of vertical rows
COLS = 25       # Number of horizontal columns
```

To adjust the simulation speed, change the delay (in milliseconds) inside the `update()` function:

```python
root.after(200, update)  # Lower values = faster simulation
```

---

## License

This project is open-source and available for personal and educational use.
