# This is the python implementation of minesweeper
import random as rand

def create_graph(w, h):
    graph = {}

    for i in range(h):
        for j in range(w):
            neighbors = []
            # Top left
            if (i - 1 >= 0 and j - 1 >= 0):
                neighbors.append((i - 1, j - 1))
            # Top
            if (i - 1 >= 0):
                neighbors.append((i - 1, j))
            # Top Right
            if (i - 1 >= 0 and j + 1 < w):
                neighbors.append((i - 1, j + 1))
            # Right
            if (j + 1 < w):
                neighbors.append((i, j + 1))
            # Bottom Right
            if (i + 1 < h and j + 1 < w):
                neighbors.append((i + 1, j + 1))
            # Bottom
            if (i + 1 < h):
                neighbors.append((i + 1, j))
            # Bottom Left
            if (i + 1 < h and j - 1 >= 0):
                neighbors.append((i + 1, j - 1))
            # Left
            if (j - 1 >= 0):
                neighbors.append((i, j - 1))
            graph[(i,j)] = neighbors
    return graph

def add_mines(w, h, mineCount):
    mines = [[0 for col in range(w)] for row in range(h)]
    count = mineCount
    done = False
    while(not done):
        for i in range(h):
            for j in range(w):
                if mines[i][j] != 1 and rand.random() > 0.91:
                    if(count < 0):
                        done = True
                        break
                    mines[i][j] = 1
                    count = count - 1
    return mines

def count_surrounds(graph, i, j, mines):
    count = 0
    for neighbor in graph[i,j]:
        if mines[neighbor[0]][neighbor[1]] == 1:
            count += 1
    return count


def calc_mines(graph, mines, w, h):
    button_numbers = [[0 for col in range(w)] for row in range(h)]
    for i in range (h):
        for j in range(w):
            # add -1 if the button is over a bomb
            if mines[i][j] == 1:
                button_numbers[i][j] = -1
            # Else calculate the buttons value
            else:
                button_numbers[i][j] = count_surrounds(graph, i, j, mines)
    return button_numbers


height = 10
width = 10

# Create the graph
graph = create_graph(width, height)
mines = add_mines(width, height, 10)
button_numbers = calc_mines(graph, mines, width, height)

for i in range(height):
    for j in range(width):
        print(button_numbers[i][j], end='\t')
    print()

from tkinter import *

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

#example values
for i in range(10):
    for j in range(10):
        btn_value = button_numbers[i][j]
        btn = Button(frame, text=btn_value)
        if btn_value == 1:
            btn.configure(bg='blue')
        elif btn_value == 2:
            btn.configure(bg='green')
        elif btn_value == 3:
            btn.configure(bg='red')
        elif btn_value == -1:
            btn.configure(bg='black')
        btn.grid(column=j, row=i, sticky=N+S+E+W)

for i in range(10):
  Grid.columnconfigure(frame, i, weight=1)

for j in range(10):
  Grid.rowconfigure(frame, j, weight=1)

root.mainloop()
