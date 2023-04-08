from entity import Entity


class Player(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
