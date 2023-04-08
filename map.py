from __future__ import annotations

from random import randint
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

        self.tiles: Optional[List[Tile]] = []
        for x in range(self.width):
            for y in range(self.height):
                self.tiles.append(
                    Tile(x=x, y=y, color_fg=(0, 0, 0), color_bg=(randint(20, 50), randint(20, 40), 20),
                         )
                )
