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

    def introduction_two(self):
        print(f"Welcome {self.player_one.name},and {self.player_two.name} to RPSLS: Rock Paper Scissor Lizard Spock")
        print('The rules are simple')
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
        print("Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
        print("Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock Spock vaporizes Rock \n")

    def introduction_one(self):
        print(f"Welcome {self.player_one.name},and {self.player_two.name} to RPSLS: Rock Paper Scissor "
              f"Lizard Spock"
              )
        print('The rules are simple')
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
        print("Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
        print("Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock Spock vaporizes Rock \n")

    def choose_game_mode(self):
        response = input("How many players?")
        if response == "2":
            self.player_two = Human(str(input("ENTER SECOND PLAYER NAME")))
            self.introduction_two()
            self.multiplayer()
        else:
            automaticplayer.player_two = "Neumann"
            self.introduction_one()
            self.single_player()

    def multiplayer(self):
        for x in range(3):
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

            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("It's a tie!")
            elif self.player_one.chosen_gesture == "rock":
                if self.player_two.chosen_gesture == "scissors":
                    print("You win!")
                    self.player_one.score += 1
                elif self.player_two.chosen_gesture == "lizard":
                    print("You win!")
                    self.player_one.score += 1
                else:
                    print("You lose.")
                    self.player_two.score += 1
            elif self.player_one.chosen_gesture == "paper":
                if self.player_two.chosen_gesture == "rock":
                    print("You win!")
                    self.player_one.score += 1
                elif self.player_two.chosen_gesture == "spock":
                    print("You win!")
                    self.player_one.score += 1
                else:
                    print("You lose.")
                    self.player_two.score += 1
            elif self.player_one.chosen_gesture == "scissors":
                if self.player_two.chosen_gesture == "paper":
                    print("You win!")
                    self.player_one.score += 1
                elif self.player_two.chosen_gesture == "lizard":
                    print("You win!")
                    self.player_one.score += 1
                else:
                    print("You lose.")
                    self.player_two.score += 1
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
            AI.choose_gesture(self.player_two.chosen_gesture)
            print(f"\nYou picked {self.player_one.chosen_gesture}, Neumann picked {self.player_two.chosen_gesture}")

    # def rules(self):
    #     self.player_two.gesture = ["rock [0]", "paper [1]", "scissors [2]", "lizard [3]", "spock [4]"]
    #     AI.choose_gesture(self.player_two.chosen_gesture)
    #     print(f"\nYou chose {self.player_one.chosen_gesture}, Neumann chose {self.player_two.chosen_gesture}.\n")
    #     #
    # if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
    #     print("It's a tie!")
    # elif self.player_one.chosen_gesture == "rock":
    #     if self.player_two.chosen_gesture == "scissors" or "lizard":
    #         print("You win!")
    #         self.player_one.score += 1
    #     else:
    #         print("Paper covers rock! You lose.")
    #         self.player_two.score += 1
    # elif self.player_one.chosen_gesture == "paper":
    #     if self.player_two.chosen_gesture == "rock" or "spock":
    #         print("You win!")
    #         self.player_one.score += 1
    #     else:
    #         print("Scissors cuts paper! You lose.")
    #         self.player_two.score += 1
    # elif self.player_one.chosen_gesture == "scissors":
    #     if self.player_two.chosen_gesture == "paper" or "lizard":
    #         print("You win!")
    #         self.player_one.score += 1
    #     else:
    #         print("You lose.")
    #         self.player_two.score += 1
    # while ii > 5:
    #     try:
    #         self.player_two.chosen_gesture = self.player_two.gesture[ii]
    #     except IndexError:
    #         print("Sorry, that is not a list item. Try again")
    #     else:
    #         print("good, good")
    #     finally:
    #         ii = int(input(f"{self.player_two.gesture}  Pick a number!!!"))
    # self.player_two.chosen_gesture = self.player_two.gesture[ii]

# Determine winner of round, winner's score increases
# Loop to continue gameplay until best of three occurs

# End Game
# Display winner of game
# Prompt to play again? - Not MVP
