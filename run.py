# Write your code to expect a terminal of 80 characters wide and 24 rows high

Player_Board = [[''] * 6 for x in range(6)]
Computer_Board = [[''] * 6 for x in range(6)]


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
        print(row_number, "   |".join(row))
        row_number += 1


def generate_ships():
    """
    Generate random coordinates for ships to put on player and computer board
    """
    pass


name = welcome()
print_board(Player_Board, name)
print_board(Player_Board, "Computer")