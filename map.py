from __future__ import annotations

from random import randint, randrange
from typing import Optional, TYPE_CHECKING, List

from tiles import Tile

if TYPE_CHECKING:
    from entity import Entity
    from engine import Engine


class Map:

    def __init__(self, engine: Optional[Engine] = None):
        self.engine = engine
        self.engine.active_map = self

        self.width = engine.screen_width
        self.height = engine.screen_height

        self.entities: Optional[List[Entity]] = []
        """Contains all entities on a given map"""

        self.tiles: List[List[Tile]] = [
            [Tile(char=chr(randrange(0x2591, 0x2593)), x=x, y=y,
                  color_fg=(randint(50, 150), randint(20, 60), 20),
                  color_bg=(randint(20, 50), randint(10, 15), randint(20, 40)),
                  ) for y in range(self.height)]
            for x in range(self.width)
            ]