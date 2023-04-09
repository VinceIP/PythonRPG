from __future__ import annotations

import tcod.event
from typing import TYPE_CHECKING, Optional

from handler import Handler
from actions import Action, EscapeAction, MoveAction

if TYPE_CHECKING:
    from engine import Engine


class EventHandler(Handler, tcod.event.EventDispatch[Action]):
    """Listens for and handles all events"""

    def __init__(self, engine: Engine):
        engine.event_handler = self
        self.last_action: Optional[Action] = None
        self.engine = engine

    def wait_for_event(self, engine: Engine):
        """Waits for an event to occur"""
        for event in tcod.event.wait():
            engine.context.convert_event(event)

            self.last_action = self.dispatch(event)

            if isinstance(self.last_action, EscapeAction):
                raise SystemExit()

            elif isinstance(self.last_action, MoveAction):
                self.last_action.perform(self.engine, self.engine.game_handler.player)

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        """To be run on application exit"""
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        """Get a keydown event and assign it the appropriate Action"""

        key = event.sym

        # Handle arrow keys
        if key == tcod.event.K_UP:
            self.last_action = MoveAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            self.last_action = MoveAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            self.last_action = MoveAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            self.last_action = MoveAction(dx=1, dy=0)

        # Handle ESC
        elif key == tcod.event.K_ESCAPE:
            self.last_action = EscapeAction()

        # Returns None if no key was pressed
        return self.last_action
