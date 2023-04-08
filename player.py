from character import Character

class Player(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solid = True

