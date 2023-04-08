from __future__ import annotations

from typing import TYPE_CHECKING

from handler import Handler
from player import Player

if TYPE_CHECKING:
    from engine import Engine


class GameHandler(Handler):

    def __init__(self, engine: Engine):
        engine.game_handler = self

        self.player = Player(char="%", color=(255, 0, 0), coordinates=engine.screen_center)
