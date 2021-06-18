from human import Human
from automaticplayer import AI


class Battlefield:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.draw = 0

    def run_game(self):
        self.introduction()
        self.choose_game_mode()
        self.play_game()
        # self.display_winner()
        # self.ask_to_play_again()

    @staticmethod
    def introduction():
        print(f"Welcome to R.P.S.L.S: Rock Paper Scissor Lizard Spock")
        print('The rules are simple')
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
        print("Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
        print("Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock \n")

    def choose_game_mode(self):
        response = input("ENTER 1 OR 2 FOR NUMBER OF PLAYERS")
        if response == "2":
            self.player_one = Human(str(input("ENTER FIRST PLAYER NAME")))
            self.player_two = Human(str(input("ENTER SECOND PLAYER NAME")))
        else:
            self.player_one = Human(str(input("ENTER FIRST PLAYER NAME")))
            self.player_two = AI()

    def play_game(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()



        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print(self.player_one.chosen_gesture)
        elif self.player_one.chosen_gesture == self.player_one.gesture:
            if self.player_two.chosen_gesture == self.player_two.gesture or self.player_one.gesture[3]:
                print("you win")
                self.player_one.score += 1
            else:
                print("YOU LOSE")
                self.player_two.score += 1
        elif self.player_one.chosen_gesture == self.player_two.chosen_gesture[1]:
            if self.player_two.chosen_gesture == [0]:
                if self.player_two.chosen_gesture == [4]:
                    print("you win")
                    self.player_one.score += 1
                else:
                    print("YOU LOSE")
                    self.player_two.score += 1
        if self.player_two.score == 3:
            print("YOU LOSE THE GAME PLAY AGAIN?")
        elif self.player_one.score == 3:
            print("YOU WIN THE GAME PLAY AGAIN?")
        else:
            self.play_game()
    # while self.player_one.score or self.player_two.score < 3:
    #     if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
    #         print("IT'S A TIE")

    # self.player_two.chosen_gesture = [i]
    # self.player_one.chosen_gesture = [i]
    # while i > 5:
    #     try:
    #         self.player_two.chosen_gesture = self.player_two.gesture[ii]
    #     except IndexError:
    #         print("Sorry, that is not a list item. Try again")
    #     else:
    #         print("good, good")
    #     finally:
    #         ii = int(input(f"{self.player_two.gesture}  Pick a number!!!"))
    #         self.player_two.chosen_gesture = self.player_two.gesture[ii]

# Determine winner of round, winner's score increases
# Loop to continue gameplay until best of three occurs

# End Game
# Display winner of game
# Prompt to play again? - Not MVP
