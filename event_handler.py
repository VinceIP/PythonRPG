from __future__ import annotations

import tcod.event
from typing import TYPE_CHECKING

from handler import Handler

if TYPE_CHECKING:
    from engine import Engine


class EventHandler(Handler):

    def wait_for_event(self, engine: Engine):
        for event in tcod.event.wait():
            engine.context.convert_event(event)
            print(event)

            if isinstance(event, tcod.event.Quit):
                raise SystemExit()
