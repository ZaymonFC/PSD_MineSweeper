#####   ---------------------------------------------------------------   #####
##                               Board Class                                 ##
##                Contains Model Representation of a Game Board              ##
#####   ---------------------------------------------------------------   #####

class Board:
    def __init__(board_type, difficulty, dimension):
        self.type = board_type
        self.graph = self.create_graph(type, dimension, dimension)
        self.cell_count = dimension * dimension
        self.mine_count = difficulty * cell_count
        self.mines = self.add_mines(dimension, dimension, mine_count)
        self.button_numbers = self.calc_mines(self.graph, self.mines)

        self.toggles = [[False] * dimension for _ in range(dimension)]
        self.game_over = False


#
# ─── SETUP FUNCTIONS ────────────────────────────────────────────────────────────
#
    def create_graph(self, type, width, height):
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


    def add_mines(self, w, h, mineCount):
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


    def calc_mines(self, graph, mines, w, h):
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


    def count_surrounds(self, graph, i, j, mines):
        count = 0
        for neighbor in graph[i,j]:
            if mines[neighbor[0]][neighbor[1]] == 1:
                count += 1
        return count
    
    
#
# ─── STATE MODIFICATION FUNCTIONS ───────────────────────────────────────────────
#
    def recursive_reveal(self, i, j):
        neighbors = self.graph[i,j]
        grow_list = []
        for neighbor in neighbors:
            n_i = neighbor[0]
            n_j = neighbor[1]
            if self.button_numbers[n_i][n_j] == 0:
                # Toggle the button
                self.toggles[n_i][n_j] = True
                # Add the button to the grow list
                grow_list.append([n_i,n_j])
                # Set to English 'zero' to prevent endless recursion
                self.button_numbers[n_i][n_j] = 'zero'
            elif button_numbers[n_i][n_j] == 1:
                # Toggle the 'button'
                self.toggles[n_i][n_j] = True
        if grow_list:
            for neighbor in grow_list:
            recursive_reveal(neighbor[0], neighbor[1])


    def toggle_button(self, i, j):
        if self.toggles[i][j]:
            return 0
        self.toggles[i][j] = True
        button_value = self.button_numbers[i][j]
        if button_value == 0:
            self.recursive_reveal(i,j)
            return 0
        elif button_value == -1:
            self.game_over = True
            return -1


#
# ─── GETTERS ────────────────────────────────────────────────────────────────────
#
    def get_state_toggles(self):
        return self.toggles


    def get_state_button_numbers(self):
        return self.button_numbers

    
    def get_state_board_type(self):
        return self.board_type