from entity import Entity


class Character(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solid = True

    def move(self, dx: int, dy: int):
        # If the move target is a solid entity
        if self.map.tiles[self.x + dx][self.y + dy].entity:
            if self.map.tiles[self.x + dx][self.y + dy].entity.solid:
                return
        else:
            self.map.tiles[self.x][self.y].entity = None
            self.x += dx
            self.y += dy
            self.map.tiles[self.x][self.y].entity = self
