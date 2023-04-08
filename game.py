from engine import Engine
from event_handler import EventHandler
from game_handler import GameHandler


def main():
    engine = Engine()
    game_handler = GameHandler(engine)
    event_handler = EventHandler(engine)
    #input_handler = InputHandler(engine)
    engine.render_game()


if __name__ == "__main__":
    main()
