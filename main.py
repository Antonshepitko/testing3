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

def shoot(row, col, guess_row, guess_col):
    if guess_row == row + 1 and guess_col == col + 1:
        print("Congratulations! You sunk my battleship!")
        return ("Victory!")
    else:
        print("You missed my battleship!")
        board[guess_row - 1][guess_col - 1] = 'X'
        print_board(board)
        return ("Miss")

def main_game():
    row = 1
    col = 1
    for i in range(4):
        guess_row = input("Enter row: ")
        guess_col = input("Enter column: ")
        result = shoot(row, col, guess_row, guess_col)
        if result == "Victory!":
            return (0)
    print ("Defeat")