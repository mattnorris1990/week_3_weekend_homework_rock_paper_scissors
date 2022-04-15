from flask import render_template, request
from app import app
from modules.game import *
from modules.player import *


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/startgame")
def player_1():
    return render_template("play-game.html")

@app.route("/playgame", methods=["POST"])
def input_player_2():
    print(request.form)

    player_1_name = request.form["player1name"]
    player_1_choice = request.form["player1choice"]
    player_2_name = request.form["player2name"]
    player_2_choice = request.form["player2choice"]

    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)

    print(player_1.name)
    print(player_1.choice)
    print(player_2.name)
    print(player_2.choice)

    winner = play_game(player_1, player_2)

    if winner != None:
        return render_template("result.html", player_1 = player_1, player_2 = player_2, winner = winner.name, choice = winner.choice)
    else:
        return render_template("result.html", player_1 = player_1, player_2 = player_2)

# @app.route("/<player_1_choice>/<player_2_choice>")
# def RPS(player_1_choice, player_2_choice):
#     winner = play_game(player_1_choice, player_2_choice)
#     return render_template("result.html", winner = winner )

