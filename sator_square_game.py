import tkinter as tk
from random import shuffle

# Sator Square
sator_square = [
    "S", "A", "T", "O", "R",
    "A", "R", "E", "P", "O",
    "T", "E", "N", "E", "T",
    "O", "P", "E", "R", "A",
    "R", "O", "T", "A", "S"
]

def shuffle_board():
    shuffle(sator_square)
    for i in range(25):
        buttons[i].config(text=sator_square[i])

def check_solution():
    user_input = entry.get()
    if user_input == ''.join(sator_square):
        add_point()  # Tambahkan poin jika benar
        result_label.config(text="Marvelous! You earned 1 point.")
    else:
        result_label.config(text="Nope, Try again!!!")

def restart_game():
    shuffle_board()
    entry.delete(0, "end")
    result_label.config(text="")

def add_point():
    current_points = int(points_label.cget("text"))
    current_points += 1
    points_label.config(text=str(current_points))

root = tk.Tk()
root.title("The Sator Square Game")

title_label = tk.Label(root, text="Sator Square Puzzle")
title_label.pack()

instruction_label = tk.Label(root, text="Get The Mystery Right")
instruction_label.pack()

frame = tk.Frame(root)
frame.pack()

buttons = []
for i in range(25):
    button = tk.Button(frame, text=sator_square[i], padx=10, pady=10)
    buttons.append(button)
    row, col = divmod(i, 5)
    button.grid(row=row, column=col)

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Confirm", command=check_solution)
check_button.pack()

restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

points_label = tk.Label(root, text="0")
points_label.pack()

shuffle_board()  

root.mainloop()
