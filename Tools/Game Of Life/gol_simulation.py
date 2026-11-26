import tkinter
import random as random_module

CELL_SIZE = 20
ROWS = 25
COLS = 25

running = False

root = tkinter.Tk()
root.title("game of life")

canvas = tkinter.Canvas(
    root,
    width=COLS * CELL_SIZE,
    height=ROWS * CELL_SIZE,
    bg="#FFFFFF"
)
canvas.pack()

grid = [
    [random_module.randint(0,1) for _ in range(COLS)]
    for _ in range(ROWS)
]


def draw_gird():
    canvas.delete("all")

    for row in range(ROWS):
        for col in range(COLS):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if grid[row][col] == 1:
                color = "#000000"
            else:
                color = "white"

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=color, outline="gray"
            )


def count_neighbours(row, col):
    count = 0

    for r in range(-1, 2):
        for c in range(-1, 2):
            if r==0 and c==0:
                continue
            nr = row + r
            nc = col + c

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                count += grid[nr][nc]

    return count


def next_generation():
    new_gird = [
        [0 for _ in range(COLS)]
        for _ in range(ROWS)
    ]

    for row in range(ROWS):
        for col in range(COLS):

            neighbours = count_neighbours(row, col)
            if grid[row][col] == 1:
                if neighbours == 2 or neighbours == 3:
                    new_gird[row][col] = 1
                else:
                    new_gird[row][col] = 0

            else:
                if neighbours == 3:
                    new_gird[row][col] = 1
    return new_gird

def update():
    global grid
    if running:
        grid = next_generation()
        draw_gird()
        root.after(200, update)

def start():
    global running
    if not running:
        running = True
        update()


def stop():
    global running
    running = False


def randomize_grid():
    global grid
    grid = [
        [random_module.randint(0,1) for _ in range(COLS)]
        for _ in range(ROWS)
    ]
    draw_gird()

def clear():
    global grid
    grid = [
        [0 for _ in range(COLS)]
        for _ in range(ROWS)
    ]
    draw_gird()


tkinter.Button(root, text="Start", command=start).pack(side="left")
tkinter.Button(root, text="Stop", command=stop).pack(side="left")
tkinter.Button(root, text="Random", command=randomize_grid).pack(side="left")
tkinter.Button(root, text="Clear", command=clear).pack(side="left")

draw_gird()
root.mainloop()

