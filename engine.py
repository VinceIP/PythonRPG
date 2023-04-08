from __future__ import annotations

import tcod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from event_handler import EventHandler


class Engine:
    def __init__(self, event_handler: EventHandler, width=80, height=50):
        self.screen_width = width
        self.screen_height = height
        self.fps = 20
        self.console = tcod.Console(width, height, order="F")
        self.tileset = tcod.tileset.load_tilesheet(
            "resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
        )
        self.event_handler = event_handler

    def render(self):
        with tcod.context.new(
                columns=self.console.width, rows=self.console.height, tileset=self.tileset,
        ) as self.context:
            while True:
                self.console.clear()
                self.console.print(x=10, y=10, string="Hello world!")
                self.context.present(self.console)
                self.event_handler.wait_for_event(self)
