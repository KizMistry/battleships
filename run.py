# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# List of lists. 6 lists that contain a list of 6 spaces
Player_Board = [['  '] * 6 for x in range(5)]
Computer_Board = [['  '] * 6 for x in range(5)]
Comp_Ship_Board = [['  '] * 6 for x in range(5)]

# 
user_score = 0
comp_score = 0


def welcome():
    """
    Welcome message and name request
    """
    print("Welcome to BattleShips")
    name = input("Please enter your name: ")
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
        # col_num.append(ran_col)
        # row_num.append(ran_row)
    # return row_num, col_num


def user_guess():
    """
    Requests users guess
    """
    print("\nYour turn, enter coordinates you'd like to strike")
    column = input("Enter a column letter between A-E:\n").upper()
    while column not in "ABCDE":
        print("You input an invalid column letter")
        column = input("Enter a column letter between A-E:\n").upper()
    column = ord(column) - 65
    
    row = input("\nEnter a row number between 1-5:\n")
    while row not in "12345":
        print("You input an invalid row number")
        row = input("Enter a row number between 1-5:\n")
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
        print_board(Player_Board, name)
        print_board(Computer_Board, "Computer")
        print_board(Comp_Ship_Board, "Hidden")
        print("\nBang! You hit a ship!")
        user_score += 1
        if input("Hit enter to play or type 'exit' to quit").upper() == "Exit":
            print("quiter")
    else:
        board[row][column] = " -"
        Computer_Board[row][column] = " -"
        print_board(Player_Board, name)
        print_board(Computer_Board, "Computer")
        print_board(Comp_Ship_Board, "Hidden")
        print("\nSplash.. unlucky, you missed!")
    if user_score < 5:
        comp_guess()
        user_guess()


def comp_guess():
    """
    Computer will generate a random guess after player has a turn
    """
    global comp_score
    print("\nComputer's turn... \n")
    row, column = random.randint(0, 4), random.randint(0, 4)
    if Player_Board[row][column] == " 0":
        Player_Board[row][column] = " X"
        comp_score += 1
        print("Boom! The computer just hit your ship!\n")
        print_board(Player_Board, name)
        print_board(Computer_Board, "Computer")
        print_board(Comp_Ship_Board, "Hidden")
    else:
        Player_Board[row][column] = " -"
        print("Plop... The computer missed!\n")
        print_board(Player_Board, name)
        print_board(Computer_Board, "Computer")
        print_board(Comp_Ship_Board, "Hidden")


name = welcome()
generate_ships(Player_Board)
generate_ships(Comp_Ship_Board)
print_board(Player_Board, name)
print_board(Computer_Board, "Computer")
print_board(Comp_Ship_Board, "Hidden")
user_guess()
# row, column = user_guess()
# print(column)
# print(row)
# print(user_guess)
# board_check(Comp_Ship_Board, row, column)
