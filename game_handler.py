from __future__ import annotations

from typing import TYPE_CHECKING

from entity import Entity
from handler import Handler
from map import Map
from player import Player

if TYPE_CHECKING:
    from engine import Engine


class GameHandler(Handler):

    def __init__(self, engine: Engine):
        engine.game_handler = self

        self.player = Player(char="%", color=(255, 0, 0), coordinates=engine.screen_center)
        self.map = Map(engine)
        self.map.entities.append(
            Entity(x=self.player.x - 5, y=self.player.y - 5,
                   char="#",
                   color=(0, 255, 0)
                   )
        )
        self.map.entities.append(
            Entity(x=self.player.x + 15, y=self.player.y + 5,
                   char="#",
                   color=(0, 255, 255)
                   )
        )
        self.map.entities.append(self.player)
