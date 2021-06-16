import random

from player import Player


class Automaticplayer(Player):
    def __init__(self, name):
        self.name = "Neumann"
        self.gesture = ["rock", "paper", "scissors", "lizard", "Spock"]
        self.score = 0
        self.chosen_gesture = ""
        super().__init__(self)

    def choose_gesture(self):
        random.choice(self.gesture)
