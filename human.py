from player import Player


class Human(Player):
    def __init__(self, name):
        self.name = name
        self.gesture = ["rock", "paper", "scissors", "lizard", "spock"]
        self.score = 0
        self.chosen_gesture = ""
        super().__init__(name)




