from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:

    def perform(self, engine: Engine, entity: Entity) -> None:
        """Perform an action.

        'engine' is needed for scope.

        'entity' is the target of the action.
        """

    pass


class EscapeAction(Action):

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

    pass


class MoveAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        target_x = entity.x + self.dx
        target_y = entity.y + self.dy
        map = engine.active_map
        # If the target is in index range, set a valid target tile
        if target_x in range(len(map.tile_layers[entity.layer].data)) and target_y in range(len(map.tile_layers[entity.layer].data)):
            target_tile = map.tile_layers[entity.layer].data[target_x, target_y]
        else:
            # Action will fail to perform, no need to continue
            return

        # print("Moving to: " +
        #       str(target_x) + " " + str(target_y))
        # If target tile is in map bounds and walkable
        # May not need in bounds method now??
        if engine.active_map.is_in_bounds(target_x, target_y) \
                and engine.active_map.is_tile_walkable(target_x, target_y):
            # Clear this entity from this tile
            map.tile_layers[entity.layer].data[entity.x, entity.y].entity = None
            entity.x += self.dx
            entity.y += self.dy
            # Set target entity to new target tile
            target_tile.entity = entity
