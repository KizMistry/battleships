# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# List of lists. 6 lists that contain a list of 6 spaces
Player_Board = [['  '] * 6 for x in range(5)]
Computer_Board = [['  '] * 6 for x in range(5)]
Comp_Ship_Board = [['  '] * 6 for x in range(5)]


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
    answer = input("Enter a column letter between A-E:\n").upper()
    while answer not in "ABCDE":
        print("You input an invalid column letter")
        answer = input("Enter a column letter between A-E:\n").upper()
    print(answer) 
    

name = welcome()
generate_ships(Player_Board)
generate_ships(Comp_Ship_Board)
print_board(Player_Board, name)
print_board(Computer_Board, "Computer")
print_board(Comp_Ship_Board, "Hidden")
user_guess()