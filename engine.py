from __future__ import annotations
from typing import Optional
import tcod
from event_handler import EventHandler
from game_handler import GameHandler
from game_map import Map


class Engine:
    def __init__(self, width=60, height=60):
        self.screen_width = width
        self.screen_height = height
        self.screen_center = (
            int((width / 2)),
            int((height / 2))
        )
        self.fps = 60
        self.console = tcod.Console(width, height, order="F")
        self.tileset = tcod.tileset.load_tilesheet(
            "resources/fonts/cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437,
        )
        # These get set by their respective handlers on their creation
        self.game_handler: Optional[GameHandler] = None
        self.event_handler: Optional[EventHandler] = None
        # self.input_handler: InputHandler
        self.active_map: Optional[Map] = None

    def render_game(self):
        with tcod.context.new(
                columns=self.console.width,
                rows=self.console.height,
                tileset=self.tileset,
                vsync=True,
                title="Python RPG"
        ) as self.context:
            while True:
                self.console.clear()
                self.render_map()
                self.context.present(self.console)
                self.event_handler.wait_for_event(self)

    def render_map(self):
        tile_layers = self.active_map.tile_layers
        transparent_color = (255, 0, 255)
        # For each tile layer
        for layer in range(len(tile_layers)):
            # For each x/y coordinate
            for i in range(len(tile_layers[layer].data)):
                for j in range(len(tile_layers[layer].data)):
                    # Point to an individual tile
                    tile = tile_layers[layer].data[i, j]
                    # Only render tiles that aren't flagged as transparent
                    # Layer != 3 - do not render tiles on layer 4, which signifies solid tiles
                    if tile.color_bg != transparent_color\
                            and layer != 3:
                        self.console.print(
                            x=tile.x, y=tile.y, string=tile.char,
                            fg=tile.color_fg, bg=tile.color_bg
                        )
        # Render entities
        for entity in self.active_map.entities:
            self.console.print(x=entity.x, y=entity.y,
                               string=entity.char,
                               fg=entity.color,
                               )
