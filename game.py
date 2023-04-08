from engine import Engine
from event_handler import EventHandler


def main():
    event_handler = EventHandler()
    engine = Engine(event_handler)
    engine.render()


if __name__ == "__main__":
    main()
