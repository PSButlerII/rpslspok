class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = {'0': 'Rock', '1': 'paper', '2': 'scissors', '3': 'lizard', '4': 'spock'}
        self.score = 0
        self.chosen_gesture = []

    def choose_gesture(self):
        print(self.gesture)
        self.chosen_gesture = input("Enter A Number")
