from random import randint

#initializing board
def create_board():
    board = []
    for x in range(5):
        board.append(["0"] * 5)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def get_cords(board):
    return randint(0, len(board) - 1)

# starting the game and printing the board
print("Let's play Battleship!")
board = create_board()
print_board(board)