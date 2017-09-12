class PositionService:
    def __init__(self, mode, tile_dimension):
        self.mode == mode
        self.tile_dimension = tile_dimension
        self.grid_height = tile_dimension * 0.75
    
    def calculate_coordinates(self, x, y):
        if self.mode == "SQUARE":
            return self.calculate_coordinates_square(x, y)
        elif self.mode == "HEX":
            return self.calculate_coordinates_hex(x, y)
    
    def calculate_coordinates_square(self, x, y):
        return (x // self.tile_dimension, y // self.tile_dimension)

    def calculate_coordinates_hex(self, x, y):
        row = y / (self.grid_height)
        odd_row = r & 1
        if odd_row:
            column = (x - self.tile_dimension / 2) / self.tile_dimension
        else:
            column = x / self.tile_dimension
        #
        # ─── DETERMINE RELATIVE POSITION ─────────────────────────────────
        rel_y = y - row * grid_height
        if odd_row:
            rel_x = x - column * (self.tile_dimension) - self.tile_dimension / 2
        else:
            rel_x = x - column * self.tile_dimension
        
        #
        # ─── CALCULATE THE GRADIENT OF THE TOP EDGES ─────────────────────
        #
        gradient = (self.tile_dimension * 0.25) / (self.tile_dimension / 2)

        #
        # ─── DETERMINE IF POINT IS ABOVE HEXAGONS TOP EDGES ──────────────
        if rel_y < (-m * rel_x + c):
            row -= 1
            if odd_row:
                column -= 1
        elif rel_y < (m * rel_x - c)
            row -= 1
            if odd_row:
                column += 1
        
        return [row, column]


            
            
