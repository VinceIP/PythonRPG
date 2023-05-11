from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

import numpy as np

if TYPE_CHECKING:
    from entity import Entity

# # Tile graphics structured type compatible with Console.tiles_rgb.
# graphic_dt = np.dtype(
#     [
#         ("ch", np.int32),  # Unicode codepoint.
#         ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
#         ("bg", "3B"),
#     ]
# )
#
# # Tile struct used for statically defined tile data.
# tile_dt = np.dtype(
#     [
#         ("walkable", np.bool),  # True if this tile can be walked over.
#         ("transparent", np.bool),  # True if this tile doesn't block FOV.
#         ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
#         ("light", graphic_dt)  # When tile is in view
#     ]
# )
#
#
# def new_tile_data(
#         *,  # Enforce the use of keywords, so that parameter order doesn't matter.
#         walkable: int,
#         transparent: int,
#         dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
#         light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
# ) -> np.ndarray:
#     """Helper function for defining individual tile types """
#     return np.array((walkable, transparent, dark, light), dtype=tile_dt)
#
#
# class TileType:
#     def __init__(self, char: str, color_fg: Tuple[int, int, int], color_bg: Tuple[int, int, int]):
#         self.data = new_tile_data(
#             walkable=False,
#             transparent=False,
#             dark=(ord(char), (50, 50, 50), (0, 0, 0)),
#             light=(ord(char), color_fg, color_bg)
#         )
#
#
# class Floor(TileType):
#     def __init__(self, char: str, color_fg: Tuple[int, int, int], color_bg: Tuple[int, int, int]):
#         super().__init__(char, color_fg, color_bg)
#         self.data = new_tile_data(
#             walkable=True,
#             transparent=True,
#             dark=(ord(char), (50, 50, 50), (0, 0, 0)),
#             light=(ord(char), color_fg, color_bg)
#         )
#
#
# class Wall(TileType):
#     def __init__(self, char: str, color_fg: Tuple[int, int, int], color_bg: Tuple[int, int, int]):
#         super().__init__(char, color_fg, color_bg)
#         self.data = new_tile_data(
#             walkable=False,
#             transparent=False,
#             dark=(ord(char), (50, 50, 50), (0, 0, 0)),
#             light=(ord(char), color_fg, color_bg)
#         )


class Tile:
    def __init__(self, entity: Entity = None, x=0, y=0,
                 char: str = " ",
                 color_fg: tuple = (255, 255, 255),
                 color_bg: tuple = (0, 0, 0),
                 # properties: tile_dt = (True, True, None)
                 ):
        self.entity = entity  # Entity contained on this tile
        self.char = char
        self.color_fg = color_fg
        self.color_bg = color_bg
        self.x = x
        self.y = y


class TileLayer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = np.zeros(
            (self.width, self.height),
            dtype=Tile,
            order="F"
        )
