from __future__ import annotations
from typing import Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from entity import Entity
    from engine import Engine


class Map:

    def __init__(self, engine: Optional[Engine] = None):
        self.engine = engine
        self.engine.active_map = self
        self.entities: Optional[List[Entity]] = []
        """Contains all entities on a given map"""
