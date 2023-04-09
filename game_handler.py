from __future__ import annotations

from typing import TYPE_CHECKING

from entity import Entity
from handler import Handler
from game_map import Map
from player import Player

if TYPE_CHECKING:
    from engine import Engine


class GameHandler(Handler):

    def __init__(self, engine: Engine):
        engine.game_handler = self
        # Right now, all the tiles and entities and map creation is happening here
        self.map = Map(engine)
        self.player = Player(char="%", color=(255, 0, 0), coordinates=engine.screen_center, game_map=self.map)

        self.map.entities.append(
            Entity(x=0, y=0,
                   char="#",
                   color=(0, 255, 0),
                   game_map=self.map,
                   solid=True
                   )
        )
        self.map.entities.append(
            Entity(x=self.player.x + 15, y=self.player.y + 5,
                   char="#",
                   color=(0, 255, 255),
                   game_map=self.map,
                   solid=True
                   )
        )
        self.map.entities.append(self.player)
