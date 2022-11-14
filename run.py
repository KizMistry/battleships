# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# List of lists. 6 lists that contain a list of 6 spaces
Player_Board = [['  '] * 6 for x in range(5)]
Computer_Board = [['  '] * 6 for x in range(5)]
Comp_Ship_Board = [['  '] * 6 for x in range(5)]

# Score Trackers
user_score = 0
comp_score = 0


def welcome():
    """
    Welcome message, game description and name request
    """
    print("Welcome to BattleShips\n"
          "\nThe Objective is to guess the location\n"
          "of each battleship on the computers board\n"
          "before the computer guesses yours.\n"
          "\nA Ship is displayed as: 0\n"
          "A Hit is displayed as: X\n"
          "A Miss is displayed as: -\n")
    name = input("Please enter your name:\n")
    while name == "" or len(name) > 10:
        name = input("Please enter a username (10 characters max)\n")
    return name


def print_board(board, name):
    """
    Creates a board for the player and computer
    """
    print(f"\n   {name}'s Board")
    print('   A   B   C   D   E')
    row_number = 1
    for row in board:
        print(row_number, " |".join(row))
        row_number += 1


def update_board():
    """
    Calls print_board function with updated info
    """
    print_board(Player_Board, name)
    print_board(Computer_Board, "Computer")
    print_board(Comp_Ship_Board, "Hidden")


def generate_ships(board):
    """
    Generate random coordinates for ships to put on player and computer board
    """
    for i in range(5):
        ran_row = random.randint(0, 4)
        ran_col = random.randint(0, 4)
        while board[ran_row][ran_col] == " 0":
            ran_row = random.randint(0, 4)
            ran_col = random.randint(0, 4)
        board[ran_row][ran_col] = " 0"


def user_guess():
    """
    Requests users guess
    """
    enter_column = "Enter a column letter between A-E:\n"
    enter_row = "\nEnter a row number between 1-5:\n"
    invalid_input = "\nYour entered input is invalid\n"
    print("\nYour turn, enter coordinates you'd like to strike")

    column = input(enter_column).upper()
    while column not in "ABCDE" or column == "" or len(column) > 1:
        print(invalid_input)
        column = input(enter_column).upper()
    column = ord(column) - 65

    row = input(enter_row)
    while row not in "12345" or row == "" or len(row) > 1:
        print(invalid_input)
        row = input(enter_row)
    row = int(row)
    row -= 1
    board_check(Comp_Ship_Board, row, column)


def board_check(board, row, column):
    """
    Check the board against the users coordinates input
    """
    global user_score
    if board[row][column] == " 0":
        board[row][column] = " X"
        Computer_Board[row][column] = " X"
        update_board()
        print("\nBang! You hit a ship!\n")
        user_score += 1
    elif board[row][column] == "  ":
        board[row][column] = " -"
        Computer_Board[row][column] = " -"
        update_board()
        print("\nSplash.. unlucky, you missed!\n")
    else:
        print("You have already cleared this area")
        user_guess()
    if user_score < 5:
        print("Computers turn... \n")
        input("Hit Enter to continue\n")
        comp_guess()
    else:
        print("Kaboom! You just destroyed the computers\n"
              "last ship and won the battle!")
        play_on()


def comp_guess():
    """
    Computer will generate a random guess after player has a turn
    """
    global comp_score
    # print("Computers turn... \n")
    # input("Hit Enter to continue\n")
    row, column = random.randint(0, 4), random.randint(0, 4)
    if Player_Board[row][column] == " 0":
        Player_Board[row][column] = " X"
        comp_score += 1
        update_board()
        print("\nBoom! The computer just hit your ship!")
    elif Player_Board[row][column] == "  ":
        Player_Board[row][column] = " -"
        update_board()
        print("\nPlop... The computer missed!")
    else:
        comp_guess()
    if comp_score == 5:
        print("\nKaboom! The Computer just destroyed your\n"
              "last ship and won the battle!")
        play_on()
    else:
        user_guess()


def play_on():
    """
    Asks the user if they would like to continue or exit
    """
    global comp_score, user_score, name
    if input("\nHit enter to play / type 'exit' to quit\n").upper() == "EXIT":
        print("Thanks for playing, the scores this round ended:")
        print(f"{name}: {user_score} | Computer: {comp_score}")
        yesNo = input("\nAre you sure you want to quit? y/n\n").upper()
        while yesNo not in "YN":
            print("\nInvalid input, please enter Y or N")
            yesNo = input("\nAre you sure you want to quit? Y/N\n").upper()
        if yesNo == "N":
            new_game()
        elif yesNo == "Y":
            print("\nGood game, Cya!")
            exit()
    else:
        new_game()

    
def new_game():
    global Player_Board, Computer_Board, Comp_Ship_Board, \
     comp_score, user_score
    Player_Board = [['  '] * 6 for x in range(5)]
    Computer_Board = [['  '] * 6 for x in range(5)]
    Comp_Ship_Board = [['  '] * 6 for x in range(5)]
    user_score = 0
    comp_score = 0
    main()


def main():
    """
    Runs all main functions
    """
    global name
    name = welcome()
    generate_ships(Player_Board)
    generate_ships(Comp_Ship_Board)
    update_board()
    user_guess()


main()