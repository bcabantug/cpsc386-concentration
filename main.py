import sys
from player_ai import Player_vs_AI
from player_player import Player_vs_Player


def main():
    print("\t**************************")
    print("\t*   Choose a game mode   *")
    print("\t*+----------------------+*")
    print("\t*|  1. Single Player    |*")
    print("\t*|  2. Multiple Player  |*")
    print("\t*+----------------------+*")
    print("\t**************************")
    mode = input("\t-> ")
    if mode == '1':
        print("mode 1")
        Player_vs_AI()
    if mode == '2':
        print("mode 2")
        Player_vs_Player()


if __name__ == "__main__":
    main()
    sys.exit(0)




