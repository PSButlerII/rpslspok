from automaticplayer import AI
from battlefield import Battlefield
from human import Human

if __name__ == "__main__":
    obj = Battlefield(Human, AI)
    obj.run_game()
