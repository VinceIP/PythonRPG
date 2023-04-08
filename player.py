from entity import Entity


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.x = 15
        self.y = 15
        self.char = "@"