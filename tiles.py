from __future__ import annotations
from typing import Tuple, TYPE_CHECKING

import numpy

if TYPE_CHECKING:
    from entity import Entity

# A tile graphic
graphic_dt = numpy.dtype(
    [
        ("ch", numpy.int32),  # Unicode codepoint
        ("fg", "3B"),  # 3 unsigned bytes for RGB colors
        ("bg", "3B"),
    ]
)

# A tile
tile_dt = numpy.dtype(
    [
        ("walkable", bool),
        ("transparent", bool),  # See through FOV
        ("dark", graphic_dt)  # Alt graphic for when hidden by FOV
    ]
)


def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> numpy.ndarray:
    """Helper function for definining tile types"""
    return numpy.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150))
)

wall = new_tile(
    walkable=False, transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100))
)


class Tile:
    def __init__(self, entity: Entity = None, x=0, y=0,
                 char: str = " ",
                 color_fg: tuple = (255, 255, 255),
                 color_bg: tuple = (0, 0, 0),
                 properties: tile_dt = (True, True, None)):
        self.entity = entity  # Entity contained on this tile
        self.char = char
        self.color_fg = color_fg
        self.color_bg = color_bg
        self.properties: tile_dt = None
        self.x = x
        self.y = y
