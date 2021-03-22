from os import system, name
from art import logo

values = [' ' for x in range(9)]
turn = 0
game_not_over = True
# All possible winning combinations
soln = [[1, 2, 4], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


# Function to print Tic Tac Toe
def print_tic_tac_toe():
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[1], values[2], values[3]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[4], values[5], values[6]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[7], values[8], values[9]))
    print("\t     |     |")
    print("\n")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def initialise_grid():
    global turn, values
    values = [' ' for x in range(10)]
    turn = 0


def get_input():
    choice = int(input(f"Pick a block. Values 1 to 3 for the top row, 4 to 6 for the middle row and 7 to 9 for the bottom row. 0 to quit: "))
    game_engine(choice)


def game_engine(choice):
    global turn, game_not_over
    if choice == 0:
        game_not_over = False
    if choice > 9:
        print("Please choose a valid number")
    else:
        user = turn % 2
        if values[choice] == ' ':
            turn += + 1
            if user == 0:
                player = 'X'
                values[choice] = player
            else:
                player = 'O'
                values[choice] = player
            for combination in soln:
                if all([values[item] == player for item in combination]):
                    print_tic_tac_toe()
                    print(f"We have a winner, player {player}")
                    game_not_over = False
        else:
            print("Square already taken")


def play_game():
    global game_not_over
    print(logo)
    initialise_grid()
    game_not_over = True
    while game_not_over:
        print_tic_tac_toe()
        get_input()


while input("Do you want to play a game of tic tac toe? Type 'y' or 'n':") == "y":
    clear()
    play_game()
