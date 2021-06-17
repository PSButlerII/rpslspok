import random
import automaticplayer
import human
import random
import player
from human import Human
from automaticplayer import AI


class Battlefield:
    def __init__(self):
        self.player_one = Human(input("WHAT IS YOUR NAME"))
        self.player_two = AI()
        self.draw = 0

    def run_game(self):
        self.choose_game_mode()
        self.game_rounds()

    def introduction_two(self):
        print(f"Welcome {self.player_one.name},and {self.player_two.name} to RPSLS: Rock Paper Scissor Lizard Spock")
        print('The rules are simple')
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
        print("Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
        print("Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock Spock vaporizes Rock \n")

    def introduction_one(self):
        print(f"Welcome {self.player_one.name},and {self.player_two} to RPSLS: Rock Paper Scissor "
              f"Lizard Spock"
              )
        print('The rules are simple')
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
        print("Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
        print("Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock Spock vaporizes Rock \n")

    def choose_game_mode(self):
        response = input("How many players?")
        if response == "2":
            player.player_two = Human(str(input("ENTER SECOND PLAYER NAME")))
            self.introduction_two()
            self.multiplayer()
        else:
            self.player_two = "Neumann"
            self.introduction_one()
            self.single_player()

    # def round_rules(self):
    #     self.rock
    #     self.paper
    #     self.scissors
    #     self.lizard
    #     self.spock

    def multiplayer(self):
        i = int(input(f"{self.player_one.gesture}  Pick a number!!!"))
        while i > 5:
            try:
                self.player_one.chosen_gesture = self.player_one.gesture[i]
            except IndexError:
                print("Sorry, that is not a list item. Try again")
            else:
                print("good, good")
            finally:
                i = int(input(f"{self.player_one.gesture}  Pick a number!!!"))
        self.player_one.chosen_gesture = self.player_one.gesture[i]
        print(self.player_one.chosen_gesture)

        ii = int(input(f"{self.player_two.gesture} Pick a number Player two"))
        while ii > 5:
            try:
                self.player_two.chosen_gesture = self.player_two.gesture[ii]
            except IndexError:
                print("Sorry, that is not a list item. Try again")
            else:
                print("good, good")
            finally:
                ii = int(input(f"{self.player_two.gesture}  Pick a number!!!"))
        self.player_two.chosen_gesture = self.player_two.gesture[ii]

    def single_player(self):
        i = int(input(f"{self.player_one.gesture}  Pick a number!!!"))
        while i > 5:
            try:
                self.player_one.chosen_gesture = self.player_one.gesture[i]
            except IndexError:
                print("Sorry, that is not a list item. Try again")
            else:
                print("good, good")
            finally:
                i = int(input(f"{self.player_one.gesture}  Pick a number!!!"))
                self.player_one.chosen_gesture = self.player_one.gesture
                print(self.player_one.chosen_gesture)

        self.player_two.chosen_gesture = random.choice(self.player_two.gesture)
        print(f"\nYou picked {self.player_one.chosen_gesture}, Neumann picked {self.player_two.chosen_gesture}")

    def game_rounds(self):
        pass
    # Determine winner of round, winner's score increases
    # Loop to continue gameplay until best of three occurs

    # End Game
    # Display winner of game
    # Prompt to play again? - Not MVP

    # def draw(self):
    #     if self.player_one.chosen_gesture == self.player_one.chosen_gesture:
    #         pass
    # def rock(self):
    #  if self.player_one.chosen_gesture == rock:
    #      if self.player_two.chosen_gesture = scissor:
    #          print("Rock beats Scissors")
    #          elif self.player_two.chosen_gesture ==
    #
    # def paper():
    #     if self.player_one.chosen_gesture == paper:
    #         if self.player_two.chosen_gesture = scissor:
    #             print("Rock beats Scissors")
    #
    # def scissors():
    #     if self.player_one.chosen_gesture == rock:
    #         if self.player_two.chosen_gesture = scissor:
    #             print("Rock beats Scissors")
    #
    # def lizard():
    #     if self.player_one.chosen_gesture == rock:
    #         if self.player_two.chosen_gesture = scissor:
    #             print("Rock beats Scissors")
    #
    # def spock():
    #     if self.player_one.chosen_gesture == rock:
    #         if self.player_two.chosen_gesture = scissor:
    #             print("Rock beats Scissors")
