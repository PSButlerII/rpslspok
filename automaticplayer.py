import random
from player import Player


class AI(Player):
    def __init__(self):
        self.name = "Neumann"
        self.gesture = ["rock [0]", "paper [1]", "scissors [2]", "lizard [3]", "spock [4]"]
        self.score = 0
        self.chosen_gesture = []
        super().__init__(self)

    def choose_gesture(self):
        choose_gesture = random.choice(self.gesture)
        return choose_gesture
