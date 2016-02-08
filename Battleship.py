#Battleship game!!!#
from random import randint


# JUI for the ship
player_Board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], [
    'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
bot_Board = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], [
    'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]


def printBoard(board):
    counterx = 0
    countery = 0
    while counterx < 5:
        countery = 0
        print("")
        while countery < 5:
            print(board[counterx][countery], end=" ")
            countery += 1
        counterx += 1


def placePiece(board, x, y, piece):
    int(x)
    int(y)
    x -= 1
    y -= 1
    board[x][y] = piece


def bot_locations():  # Gets bot's ships' locations#
    global bot_ship_1
    global bot_ship_2
    global bot_ship_3
    bot_ship_1 = {"row": randint(1, 5), "col": randint(1, 5)}
    bot_ship_2 = {"row": randint(1, 5), "col": randint(1, 5)}
    bot_ship_3 = {"row": randint(1, 5), "col": randint(1, 5)}
    #Following lines check if ships overlap#
    if bot_ship_1["row"] == bot_ship_2[
            "row"] and bot_ship_1["col"] == bot_ship_2["col"]:
        bot_locations()
    if bot_ship_1["row"] == bot_ship_3[
            "row"] and bot_ship_1["col"] == bot_ship_3["col"]:
        bot_locations()
    if bot_ship_2["row"] == bot_ship_3[
            "row"] and bot_ship_2["col"] == bot_ship_3["col"]:
        bot_locations()


def player_auto():  # automatically gives player's ships' locations#
    global player_ship_1
    global player_ship_2
    global player_ship_3
    player_ship_1 = {"row": randint(1, 5), "col": randint(1, 5)}
    player_ship_2 = {"row": randint(1, 5), "col": randint(1, 5)}
    player_ship_3 = {"row": randint(1, 5), "col": randint(1, 5)}
    if player_ship_1["row"] == player_ship_2[
            "row"] and player_ship_1["col"] == player_ship_2["col"]:
        player_auto()
    if player_ship_1["row"] == player_ship_3[
            "row"] and player_ship_1["col"] == player_ship_3["col"]:
        player_auto()
    if player_ship_2["row"] == player_ship_3[
            "row"] and player_ship_2["col"] == player_ship_3["col"]:
        player_auto()

    ship_1x = player_ship_1["row"]
    ship_2x = player_ship_2["row"]
    ship_3x = player_ship_3["row"]

    ship_1y = player_ship_1["col"]
    ship_2y = player_ship_2["col"]
    ship_3y = player_ship_3["col"]

    placePiece(player_Board, ship_1x, ship_1y, "S")
    placePiece(player_Board, ship_2x, ship_2y, "S")
    placePiece(player_Board, ship_3x, ship_3y, "S")


def player_manual():
    global player_ship_1
    global player_ship_2
    global player_ship_3

    player_ship_1 = {
        "row": int(
            input("Choose a row for your first ship(1-5)")),
        "col": int(
            input("Choose a coloum for your first ship: "))}
    if player_ship_1["row"] not in range(1, 6):
        print("Invalid input. Please input location again: ")
        player_manual()

    player_ship_2 = {
        "row": int(
            input("Choose a row for your second ship(1-5)")),
        "col": int(
            input("Choose a coloum for your second ship: "))}
    if player_ship_2["row"] not in range(1, 6):
        print("Invalid input. Please input location again: ")
        player_manual()

    if player_ship_1["row"] == player_ship_2[
            "row"] and player_ship_1["col"] == player_ship_2["col"]:
        print("Invalid input. Ships can't overlap.")
        player_manual()

    player_ship_3 = {
        "row": int(
            input("Choose a row for your third ship(1-5)")),
        "col": int(
            input("Choose a coloum for your third ship: "))}
    if player_ship_3["row"] not in range(1, 6):
        print("Invalid input. Please input location again: ")
        player_manual()

    if (player_ship_1["row"] == player_ship_3["row"]) and (
            player_ship_1["col"] == player_ship_3["col"]):
        print("Invalid input. Ships can't overlap.")
        player_manual()

    if (player_ship_2["row"] == player_ship_3["row"]) and (
            player_ship_2["col"] == player_ship_3["col"]):
        print("Invalid input. Ships can't overlap.")
        player_manual()

    ship_1x = player_ship_1["row"]
    ship_2x = player_ship_2["row"]
    ship_3x = player_ship_3["row"]

    ship_1y = player_ship_1["col"]
    ship_2y = player_ship_2["col"]
    ship_3y = player_ship_3["col"]

    placePiece(player_Board, ship_1x, ship_1y, "S")
    placePiece(player_Board, ship_2x, ship_2y, "S")
    placePiece(player_Board, ship_3x, ship_3y, "S")


"""
def check_int(x):
	try:
		int(x)
	except ValueError:
		print("Invalid Input. Only numbers.")
		x=input("Input again")
		check_int(x)
	if x not in range(1,6):
		print("Invalid Input. Only numbers from 1 to 5")
		x=input("Input again")
		check_int(x)
"""


# Whenever player has to input an integer, this should be used. Catches errors.
def input_int():
    x = input("")
    try:
        int(x)
    except ValueError:
        print("Invalid. Only integer numbers are accepted!")
        print("Try again: ")
        x = input_int()
    x = int(x)
    return x


def player_fire():
    global player_fired_cols
    global player_fired_rows
    global player_fired_no
    global fire_col
    global fire_row

    print("Choose a row to fire upon: ")
    fire_row = input_int()
    if fire_row in range(1, 6):
        print("Choose a coloum to fire upon: ")
        fire_col = input_int()
        if fire_col in range(1, 6):
            check = 1
            #Checks if player has already fired there#
            for i in range(0, len(player_fired_rows)):
                if (player_fired_rows[i] == fire_row) and (
                        player_fired_cols[i] == fire_col):
                    check = 0
                    break
            if check == 1:
                player_fired_cols.append(fire_col)
                player_fired_rows.append(fire_row)
            else:
                print("You have already fired there! Try again")
                player_fire()

        else:
            print("Invalid Input. Only numbers from 1 to 5 are accepted!")
            player_fire()
    else:
        print("Invalid Input. Only numbers from 1 to 5 are accepted!")
        player_fire()


def bot_fire():
    global bot_fired_rows
    global bot_fired_cols
    global bot_fired_no
    global fire_row
    global fire_col
    fire_row = randint(1, 5)
    fire_col = randint(1, 5)
    #Checks if bot has already fired there#
    for i in range(0, len(bot_fired_rows)):
        if (bot_fired_rows[i] == fire_row) and (bot_fired_cols[i] == fire_col):
            bot_fire()
    bot_fired_cols.append(fire_col)
    bot_fired_rows.append(fire_row)


def battleship():
    global bot_fired_rows
    global bot_fired_cols
    global player_fired_cols
    global player_fired_rows
    #Stores places already fired upon#
    bot_fired_rows = []
    bot_fired_cols = []
    player_fired_rows = []
    player_fired_cols = []

    winner = ""
    player_ship_1_status = 1
    player_ship_2_status = 1
    player_ship_3_status = 1
    bot_ship_1_status = 1
    bot_ship_2_status = 1
    bot_ship_3_status = 1
    print("Welcome to Battleship. ")
    print("Rules:\nYou and the bot have a 5 by 5 board.\nYou can choose to place your ships yourself or let the computer do it."
          "\nYou will then choose a place to fire(Between 1-5).\nThe bot will randomly fire ont your board.\nFirst to destroy all ships wins\nGood luck")
    print("Here's your board: ")
    printBoard(player_Board)
    print("")
    print("\nHere's the bot's board: ")
    printBoard(bot_Board)
    bot_locations()
    #Print's bot's ship locations. It's not cheating, it's debugging!!!#

    choice = input(
        "\n\nWould you like to choose your ship location yourself?(Y/N)")
    choice = choice[0].lower()
    if choice != "y" and choice != "n":
        print("Invalid input. Try again")
        battleship()
    else:
        if choice == "y":
            player_manual()
        elif choice == "n":
            player_auto()
        printBoard(player_Board)
        #Code to see player's ships' locations#
        print("\nThese are your ships' locations: ")
        print(player_ship_1)
        print(player_ship_2)
        print(player_ship_3)

        while winner == "":
            player_fire()
            if fire_row == bot_ship_1["row"] and fire_col == bot_ship_1["col"]:
                bot_ship_1_status = 0
                print("You hit the bot's first ship!!!")
                placePiece(bot_Board, fire_row, fire_col, "X")

            elif fire_row == bot_ship_2["row"] and fire_col == bot_ship_2["col"]:
                bot_ship_2_status = 0
                print("You hit the bot's second ship!!!")
                placePiece(bot_Board, fire_row, fire_col, "X")

            elif fire_row == bot_ship_3["row"] and fire_col == bot_ship_3["col"]:
                bot_ship_3_status = 0
                print("You hit the bot's third ship!!!")
                placePiece(bot_Board, fire_row, fire_col, "X")
            else:
                print("You missed!!!")
                placePiece(bot_Board, fire_row, fire_col, "M")

            if bot_ship_1_status == 0 and bot_ship_2_status == 0 and bot_ship_3_status == 0:
                winner = "Player"
            print("Here's the bot's board: ")
            printBoard(bot_Board)
            bot_fire()
            """
			print("\nThis is where the bot fired: ")
			print(bot_fired_rows,bot_fired_cols)
			"""
            if fire_row == player_ship_1[
                    "row"] and fire_col == player_ship_1["col"]:
                player_ship_1_status = 0
                print("\nThe bot hit your first ship!")
                placePiece(player_Board, fire_row, fire_col, "X")
            elif fire_row == player_ship_2["row"] and fire_col == player_ship_2["col"]:
                player_ship_2_status = 0
                print("\nThe bot hit your second ship!")
                placePiece(player_Board, fire_row, fire_col, "X")
            elif fire_row == player_ship_3["row"] and fire_col == player_ship_3["col"]:
                player_ship_3_status = 0
                print("\nThe bot hit your third ship!")
                placePiece(player_Board, fire_row, fire_col, "X")
            else:
                print("\nThe bot missed!!!")
                placePiece(player_Board, fire_row, fire_col, "M")

            if player_ship_1_status == 0 and player_ship_2_status == 0 and player_ship_3_status == 0:
                winner = "Bot"
            print("Here's the player's board: ")
            printBoard(player_Board)
        print("\nThe " + winner + " wins!!!")
        again = input("Want to play again?(Y/N)")
        again = again[0].lower()
        if again == "y":
            battleship()
        else:
            print("Okay. Thanks for playing!!!")
battleship()
