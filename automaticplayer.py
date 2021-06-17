import random
from player import Player


class AI(Player):
    def __init__(self):
        self.name = "Neumann"
        self.gesture = ["rock", "paper", "scissors", "lizard", "spock"]
        self.score = 0
        self.chosen_gesture = []
        super().__init__(self)

    def choose_gesture(self):
        choose_gesture = random.choice(self.gesture)
        return choose_gesture
