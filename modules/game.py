from modules.player import *

def play_game(player_1, player_2):
    if player_1.choice == "rock":
        if player_2.choice == "paper":
            return player_2
        elif player_2.choice == "scissors":
            return player_1
        elif player_2.choice == "rock":
            return None

    if player_1.choice == "paper":
        if player_2.choice == "paper":
            return None
        elif player_2.choice == "scissors":
            return  player_2
        elif player_2.choice == "rock":
            return player_1

    if player_1.choice == "scissors":
        if player_2.choice == "paper":
            return player_1
        elif player_2.choice == "scissors":
            return None
        elif player_2.choice == "rock":
            return player_2

    # if player_1 == "rock":
    #     if player_2 == "paper":
    #         return player_2
    #     elif player_2 == "scissors":
    #         return player_1
    #     elif player_2 == "rock":
    #         return None

    # if player_1 == "paper":
    #     if player_2 == "paper":
    #         return None
    #     elif player_2 == "scissors":
    #         return  player_2
    #     elif player_2 == "rock":
    #         return player_1

    # if player_1 == "scissors":
    #     if player_2 == "paper":
    #         return player_1
    #     elif player_2 == "scissors":
    #         return None
    #     elif player_2 == "rock":
    #         return player_2


