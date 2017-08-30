class Game:
    def __init__(type, difficulty, dimension):
        self.graph = self.create_graph(type, dimension, dimension)
        self.cell_count = dimension * dimension
        self.mine_count = difficulty * cell_count
        self.mines = self.add_mines(dimension, dimension, mine_count)
        self.button_numbers = self.calc_mines(self.graph)
    

    def create_graph(type, width, height):
        """ Function to create the graph for a board of n * n size """
        graph = {}
        for i in range(h):
            for j in range(w):
                neighbors = []
                # Top left
                if i - 1 >= 0 and j - 1 >= 0:
                    neighbors.append((i - 1, j - 1))
                # Top
                if i - 1 >= 0:
                    neighbors.append((i - 1, j))
                # Top Right
                if i - 1 >= 0 and j + 1 < w:
                    neighbors.append((i - 1, j + 1))
                # Right
                if j + 1 < w:
                    neighbors.append((i, j + 1))
                # Bottom Right
                if i + 1 < h and j + 1 < w:
                    neighbors.append((i + 1, j + 1))
                # Bottom
                if i + 1 < h:
                    neighbors.append((i + 1, j))
                # Bottom Left
                if i + 1 < h and j - 1 >= 0:
                    neighbors.append((i + 1, j - 1))
                # Left
                if j - 1 >= 0:
                    neighbors.append((i, j - 1))
                graph[(i,j)] = neighbors
        return graph


    def add_mines(w, h, mineCount):
        mines = [[0 for col in range(w)] for row in range(h)]
        count = mineCount
        done = False
        while not done:
            for i in range(h):
                for j in range(w):
                    if mines[i][j] != 1 and rand.random() > 0.91:
                        if count < 0:
                            done = True
                            break
                        mines[i][j] = 1
                        count = count - 1
        return mines

    
    