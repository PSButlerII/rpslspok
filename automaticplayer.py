import random
from player import Player


class AI(Player):
    def __init__(self):
        super().__init__("Computer")

    def choose_gesture(self):
        self.chosen_gesture = random.choice(list(self.gesture))



