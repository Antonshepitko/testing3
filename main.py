from random import randint

# initializing board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

# starting the game and printing the board
print("Let's play Battleship!")
print_board(board)

# defining where the ship is
def random_cell(board):
    return randint(0, len(board) - 1)

ship_row = random_cell(board)
ship_col = random_cell(board)

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))
# if the user's right, the game ends
if guess_row == ship_row + 1 and guess_col == ship_col + 1:
    print("Congratulations! You sunk my battleship!")