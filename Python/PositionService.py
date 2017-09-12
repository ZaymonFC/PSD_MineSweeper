class PositionService:
    def __init__(self, mode, tile_dimension):
        self.mode == mode
        self.tile_dimension = tile_dimension
    
    def calculate_coordinates(self, x, y):
        if self.mode == "SQUARE":
            return self.calculate_coordinates_square(x, y)
        elif self.mode == "HEX":
            return self.calculate_coordinates_hex(x, y)
    
    def calculate_coordinates_square(self, x, y):
        return (x // self.tile_dimension, y // self.tile_dimension)

    def calculate_coordinates_hex(self, x, y):
        