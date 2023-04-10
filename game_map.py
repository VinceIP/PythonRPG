from __future__ import annotations

from random import randrange, randint
from typing import Optional, TYPE_CHECKING, List

import numpy as np
import tcod.console

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

        self.create_map_from_xp()

        def make_test_map():
            # Generating some random background tiles for testing
            self.tiles: List[List[Tile]] = [
                [Tile(char=chr(randrange(0x2591, 0x2593)), x=x, y=y,
                      color_fg=(randint(50, 150), randint(20, 60), 20),
                      color_bg=(randint(20, 50), randint(10, 15), randint(20, 40)),
                      ) for y in range(self.height)]
                for x in range(self.width)
            ]

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

    def create_map_from_xp(self):
        path = "resources/maps/"
        file = "mockup.xp"
        console = self.load_map_from_xp(path + file)
        self.tiles = self.create_map_from_console(console)

    @staticmethod
    def load_map_from_xp(absolute_path: str) -> tcod.Console:

        console, = tcod.console.load_xp(absolute_path, order="F")
        CP437_TO_UNICODE = np.asarray(tcod.tileset.CHARMAP_CP437)
        console.ch[:] = CP437_TO_UNICODE[console.ch]

        KEY_COLOR = (255, 0, 255)
        is_transparent = (console.rgb["bg"] == KEY_COLOR).all(axis=-1)
        console.rgba[is_transparent] = (ord(" "), (0,), (0,))
        return console

    def create_map_from_console(self, console: tcod.Console):
        # Return DEC CODE POINT - or a char code
        print(console.rgb[1, 1][0])
        get_chr = 0
        # FG color
        print(console.rgb[1, 1][1])
        get_fg = 1
        # BG Color
        print(console.rgb[1, 1][2])
        get_bg = 2

        width = console.rgb.shape[0]
        height = console.rgb.shape[1]
        tiles = np.zeros((width, height), dtype=Tile, order="F")

        for x in range(width):
            for y in range(height):
                fg_color = tuple(console.rgb[x, y][get_fg])
                bg_color = tuple(console.rgb[x, y][get_bg])
                chr = console.rgb[x, y][get_chr]
                tiles[x, y] = Tile(
                    x=x, y=y,
                    color_fg=fg_color, color_bg=bg_color,
                    char=chr,
                    tile_type=TileType.floor
                )
        return tiles
