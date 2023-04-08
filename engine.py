from __future__ import annotations

from typing import Optional
import tcod

from event_handler import EventHandler
from game_handler import GameHandler
from handler import Handler
from input_handler import InputHandler


class Engine:
    def __init__(self, width=80, height=50):
        self.screen_width = width
        self.screen_height = height
        self.screen_center = (
            int((width / 2)),
            int((height / 2))
        )
        self.fps = 60
        self.console = tcod.Console(width, height, order="F")
        self.tileset = tcod.tileset.load_tilesheet(
            "resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
        )

        # These get set by their respective handlers on their creation
        self.game_handler: Optional[GameHandler] = None
        self.event_handler: Optional[EventHandler] = None
        # self.input_handler: InputHandler

    def render(self):
        with tcod.context.new(
                columns=self.console.width,
                rows=self.console.height,
                tileset=self.tileset,
                vsync=True,
                title="Python RPG"
        ) as self.context:
            while True:
                self.console.clear()
                self.console.print(self.game_handler.player.x, self.game_handler.player.y,
                                   self.game_handler.player.char)
                self.context.present(self.console)
                self.event_handler.wait_for_event(self)
