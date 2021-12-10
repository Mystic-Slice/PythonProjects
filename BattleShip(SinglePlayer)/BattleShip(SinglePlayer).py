from random import randint


# Intro function
def print_intro():
    print("The Battleship")
    print()
    print(
        "The target of the game is to guess where the enemy's battleship is placed in the 5X5 grid in the ocean and "
        "destroy it.")
    print()
    print("How to play:")
    print()
    print("1.You get 4 chances to guess.")
    print("2.You must choose the row and column within the 5X5 grid.")
    print("3.You win if you guess the position correctly.")
    print("4.You lose if cannot guess the position within 4 chances.")
    print("")


print_intro()
# Board setup

board = []
for x in range(0, 5):
    board.append(["O"] * 5)


# Function for displaying board


def print_board(play_board):
    print("The board")
    for row in play_board:
        print(" ".join(row))
    print()


print_board(board)


# Functions for choosing random no.


def random_row(board_row):
    return randint(0, len(board_row) - 1)


def random_col(board_col):
    return randint(0, len(board_col[0]) - 1)



ship_row = random_row(board)
ship_col = random_col(board)
choice = {}


# The game



for turn in range(1, 5):
    print("Turn", turn)

    # Obtaining Guess from player

    # Row Guess
    guess_row1 = input("Guess Row: ")

    while True:
        if guess_row1.isdigit() and 0 < int(guess_row1) < 6:
            guess_row = int(guess_row1) - 1
            break
        elif guess_row1.isdigit():
            print("That's not even in the ocean")
            print("Please enter a number from 1 to 5")
            guess_row1 = input("Guess Row: ")
        else:
            print("Character invalid")
            print("Please enter a number from 1 to 5")
            guess_row1 = input("Guess Row: ")

    # Column Guess
    guess_col1 = input("Guess Col: ")
    while True:
        if guess_col1.isdigit() and 0 < int(guess_col1) < 6:
            guess_col = int(guess_col1) - 1
            break
        elif guess_col1.isdigit():
            print("That's not even in the ocean")
            print("Please enter a number from 1 to 5")
        else:
            print("Character invalid")
            print("Please enter a number from 1 to 5")
            guess_col1 = input("Guess Col: ")
    choice.update({"Turn {0}".format(str(turn))
                  : (guess_row + 1, guess_col + 1)})

    # Using Guess to determine game status
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:

        if board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 4:
            print("")
            print("GAME OVER")
        else:
            print_board(board)
print("Your Guesses:")
print(choice)
print("My ship was at " + "(" + str(ship_row + 1) + "," + str(ship_col + 1) + ")")
