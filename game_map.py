from __future__ import annotations

from random import randrange, randint
from typing import Optional, TYPE_CHECKING, List

from tiles import Tile, TileType

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

        # Generating some random background tiles for testing
        self.tiles: List[List[Tile]] = [
            [Tile(char=chr(randrange(0x2591, 0x2593)), x=x, y=y,
                  color_fg=(randint(50, 150), randint(20, 60), 20),
                  color_bg=(randint(20, 50), randint(10, 15), randint(20, 40)),
                  ) for y in range(self.height)]
            for x in range(self.width)
        ]

        # # Define a numpy array of tiles with same shape as map
        # self.tiles = np.full(
        #     shape=(self.width, self.height),
        #     fill_value=0
        # )
        # for x in range(0, self.tiles.shape[0]):
        #     for y in range(0, self.tiles.shape[1]):
        #         self.tiles[x, y] = Tile(char=chr(randrange(0x2591, 0x2593)), x=x, y=y,
        #                                 color_fg=(randint(50, 150), randint(20, 60), 20),
        #                                 color_bg=(randint(20, 50), randint(10, 15), randint(20, 40))
        #                                 )

    def is_in_bounds(self, x: int, y: int):
        """Return true if the target coordinates are in bounds of the map"""
        # return 0 <= x < self.width and 0 <= y < self.height
        if x > self.width or x < 0 or y > self.height or y < 0:
            return False
        return True

    def is_tile_walkable(self, x: int, y: int):
        target_tile = self.tiles[x][y]
        """Return true if the target coordinates are walkable"""
        if target_tile.tile_type == TileType.floor and \
                target_tile.entity is None or target_tile.entity.solid is False:
            return True
        else:
            return False
