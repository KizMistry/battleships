# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# List of lists. 6 lists that contain a list of 6 spaces
Player_Board = [['  '] * 6 for x in range(5)]
Computer_Board = [['  '] * 6 for x in range(5)]
Comp_Ship_Board = [['  '] * 6 for x in range(5)]

# Changes letters to numbers for the users input


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
        while board[ran_col][ran_row] == " 0":
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
    return column, row


def board_check(board, column, row):
    """
    Check the board against the users coordinates input
    """
    if board[row][column] == " 0":
        board[row][column] = " X"
    else:
        board[row][column] = " -"


name = welcome()
generate_ships(Player_Board)
generate_ships(Comp_Ship_Board)
print_board(Player_Board, name)
print_board(Computer_Board, "Computer")
print_board(Comp_Ship_Board, "Hidden")
column, row = user_guess()
# print(column)
# print(row)
# print(user_guess)
board_check(Comp_Ship_Board, column, row)
print_board(Player_Board, name)
print_board(Computer_Board, "Computer")
print_board(Comp_Ship_Board, "Hidden")