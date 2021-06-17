class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = ["rock [0]", "paper [1]", "scissors [2]", "lizard [3]", "spock [4]"]
        self.score = 0
        self.chosen_gesture = ""

    def choose_gesture(self):
        input("Which gesture would you like to use?")
        self.chosen_gesture = input
        return self.chosen_gesture

