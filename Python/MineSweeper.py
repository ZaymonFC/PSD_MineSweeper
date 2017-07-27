# This is the python implementation of minesweeper

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

height = 10
width = 10

# Create the graph
graph = create_graph(width, height)


# Add the mines


# Calculate the neighborhood table
