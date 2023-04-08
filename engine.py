from __future__ import annotations

import typing

import tcod
from typing import TYPE_CHECKING

import game_handler
from handler import Handler
from event_handler import EventHandler
from game_handler import GameHandler
from input_handler import InputHandler


class Engine:
    def __init__(self, handlers: typing.List, width=80, height=50):
        self.screen_width = width
        self.screen_height = height
        self.fps = 60
        self.console = tcod.Console(width, height, order="F")
        self.tileset = tcod.tileset.load_tilesheet(
            "resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
        )
        # Get handler refs
        for h in handlers:
            if isinstance(h, Handler):
                if isinstance(h, EventHandler):
                    self.event_handler = h
                elif isinstance(h, GameHandler):
                    self.game_handler = h
                elif isinstance(h, InputHandler):
                    self.input_handler = h

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
