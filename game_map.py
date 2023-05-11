from __future__ import annotations

from typing import Optional, TYPE_CHECKING, List

import numpy as np
import pyrexpaint

from tiles import Tile, TileLayer

if TYPE_CHECKING:
    from entity import Entity
    from engine import Engine


class NoFileNameError(BaseException):
    pass


class Map:

    def __init__(self, engine: Optional[Engine] = None, filename: str = "mockup.xp"):
        self.engine = engine
        self.engine.active_map = self
        self.entities: Optional[List[Entity]] = []
        """Contains all entities on a given map"""
        self.width = 0
        """Map width in tiles"""
        self.height = 0
        """Map height in tiles"""
        self.tile_layers = None
        self.map_data = self.init_map_data(filename)
        self.populate_tile_layers(self.map_data)

        """Array of tile layers"""

    def init_map_data(self, filename: str) -> list[pyrexpaint.ImageLayer]:
        """Initialize needed arrays for game_map"""
        try:
            if filename == "":
                raise NoFileNameError
            map_data = pyrexpaint.load("resources/maps/" + filename)
            num_layers = len(map_data)
            self.width = map_data[0].width  # get width and height of base layer
            self.height = map_data[0].height

            # Init empty tile layers
            tile_layers = np.zeros(num_layers, dtype=TileLayer, order="F")

            # Populate with tile layer objects
            for i in range(len(tile_layers)):
                tile_layers[i] = TileLayer(self.width, self.height)

            self.tile_layers = tile_layers
            return map_data

        except FileNotFoundError:
            print("Invalid map file name.")
        except NoFileNameError:
            print("No map filename given.")

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

    def populate_tile_layers(self, image_layers: list[pyrexpaint.ImageLayer]):
        """Fill a map's tile layers with new tiles from raw xp map data"""
        # Return DEC CODE POINT - or a char code
        # print(console.rgb[1, 1][0])
        # get_chr = 0
        # # FG color
        # print(console.rgb[1, 1][1])
        # get_fg = 1
        # # BG Color
        # print(console.rgb[1, 1][2])
        # get_bg = 2
        #
        # width = console.rgb.shape[0]
        # height = console.rgb.shape[1]
        # tiles = np.zeros((width, height), dtype=Tile, order="F")
        #
        # for x in range(width):
        #     for y in range(height):
        #         fg_color = tuple(console.rgb[x, y][get_fg])
        #         bg_color = tuple(console.rgb[x, y][get_bg])
        #         chr = console.rgb[x, y][get_chr]
        #         if chr == 0:
        #             chr = 32
        #         tiles[x, y] = Tile(
        #             x=x, y=y,
        #             color_fg=fg_color, color_bg=bg_color,
        #             char=chr,
        #             tile_type=TileType.floor
        #         )
        # return tiles
        width = self.width
        height = self.height
        tile_layers = self.tile_layers
        # For each layer given in xp map data
        for layer in range(len(tile_layers)):

            # Lambda function to split map data layers into x and y
            pos = lambda x, y: x + y * height
            for i in range(width):
                for j in range(height):
                    # Point to a particular raw tile data
                    t = image_layers[layer].tiles[pos(j, i)]

                    # Get first char from 4 byte string
                    char = image_layers[layer].tiles[pos(j, i)].ascii_code.decode(encoding="cp437")[0]

                    # If this char is a blank/null character, set it to keycode 32 (spacebar)
                    if char == "\x00" or ord(char) == 0:
                        char = chr(32)

                    # Get tile properties from xp data
                    color_fg = tuple(
                        [t.fg_r, t.fg_g, t.fg_b]
                    )
                    color_bg = tuple(
                        [t.bg_r, t.bg_g, t.bg_b]
                    )
                    # Create new tile object
                    tile_layers[layer].data[i, j] = Tile(
                        x=i, y=j, char=char, color_fg=color_fg, color_bg=color_bg,
                    )
        return tile_layers
