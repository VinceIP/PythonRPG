from engine import Engine
from event_handler import EventHandler
from game_handler import GameHandler


def main():
    game_handler = GameHandler()
    event_handler = EventHandler()
    handlers = (game_handler, event_handler)
    engine = Engine(handlers)
    engine.render()


if __name__ == "__main__":
    main()
