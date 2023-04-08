from map import Map


class Entity:

    def __init__(self, coordinates: tuple = None, x: int = 0, y: int = 0, e_id: int = 0, char: str = "",
                 color: tuple = (255, 255, 255), solid: bool = False, game_map: Map = None):
        # Allows entity to take a tuple for coordinates instead of separate ints. Might be handy
        self.map = game_map
        if coordinates is not None and isinstance(coordinates, tuple) and len(coordinates) == 2:
            self.x = coordinates[0]
            self.y = coordinates[1]
        else:
            self.x = x
            self.y = y
        self.e_id = e_id
        """Unique id of all entities, just in case"""
        self.char = char
        self.color = color
        self.solid = solid

        self.map.tiles[self.x][self.y].entity = self
