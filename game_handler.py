from player import Player

from typing import TYPE_CHECKING

from handler import Handler


class GameHandler(Handler):

    def __init__(self):
        self.player = Player()
