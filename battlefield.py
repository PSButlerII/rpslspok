from human import Human
from automaticplayer import Automaticplayer


class Battlefield:
    def __init__(self):
        self.player_one = Human(input("WHAT IS YOUR NAME"))
        self.player_two = ""
        self.draw = 0

    def run_game(self):
        self.introduction()
        self.choose_game_mode()
        self.game_rounds()

    def introduction(self):
        print(f"Welcome {self.player_one.name},{self.player_two} to RPSLS: Rock Paper Scissor Lizard Spock")
        print('The rules are simple')
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
        print("Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
        print("Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock Spock vaporizes Rock")



    def choose_game_mode(self):
        response = input("How many players?")
        if response == "2":
            self.player_two = Human(input("ENTER SECOND PLAYER NAME"))
        else:
            self.player_two = Automaticplayer(self)

    def game_rounds(self):
        print("Rock Paper Scissor Lizard Spock")
        self.player_one.chosen_gesture = input("chooses gesture")

        self.player_two.chooses_gesture = ""

        # Determine winner of round, winner's score increases
        # Loop to continue gameplay until best of three occurs

        # End Game
        # Display winner of game
        # Prompt to play again? - Not MVP
        pass


    # def draw(self):
    #     if self.player_one.chosen_gesture == self.player_two.chooses_gesture:
    #         print("THAT'S A DRAW!! ")
    #
    # def rock(self):
    #  pass
    #
    #
    # def paper():
    #     pass
    #
    # def scissors():
    #     pass
    #
    # def lizzard():
    #     pass
    #
    # def spock():
    #     pass
