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

    def wait_for_event(self, engine: Engine):
        """Waits for an event to occur"""
        for event in tcod.event.wait():
            engine.context.convert_event(event)

            action = self.dispatch(event)

            if isinstance(action, EscapeAction):
                raise SystemExit()

            elif isinstance(action, MoveAction):
                engine.game_handler.player.move(action.dx, action.dy)

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        """To be run on application exit"""
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        """Get a keydown event and assign it the appropriate Action"""
        action: Optional[Action] = None

        key = event.sym

        # Handle arrow keys
        if key == tcod.event.K_UP:
            action = MoveAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MoveAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MoveAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MoveAction(dx=1, dy=0)

        # Handle ESC
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # Returns None if no key was pressed
        return action
