#memory_game.py
import random
import time

def initialize_board(size):
    numbers = list(range(1, (size ** 2) // 2 + 1)) * 2
    random.shuffle(numbers)
    board = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = numbers.pop()
    return board

def display_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('*', end=' ')
        print()

def get_card(card_no):
    while True:
        try:
            row = int(input(f"Enter row for card {card_no} : "))
            col = int(input(f"Enter column for card {card_no} : "))
            if 0 <= row < 4 and 0 <= col < 4:
                return row, col
            else:
                print("Invalid input. Please enter values between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def play_game(size):
    board = initialize_board(size)
    revealed = [[False] * size for _ in range(size)]
    attempts = 0

    while True:
        display_board(board, revealed)
        
        card_no = 1
        row1, col1 = get_card(card_no)
        revealed[row1][col1] = True


        display_board(board, revealed)

        card_no = 2
        row2, col2 = get_card(card_no)
        revealed[row2][col2] = True

        display_board(board, revealed)

        attempts += 1

        if board[row1][col1] == board[row2][col2]:
            print("Match found!")
        else:
            print("Try again!")
            time.sleep(1)
            revealed[row1][col1] = False
            revealed[row2][col2] = False

        if all(all(revealed[i][j] for j in range(size)) for i in range(size)):
            print(f"Congratulations! You completed the game in {attempts} attempts.")
            break
        
def correct_board_size(board_size):
    if board_size % 2 != 0:
        print("Please enter an even number for the board size.")
        enter_board_size()
    else:
        play_game(board_size)

def enter_board_size():
    board_size = int(input("Enter the size of the board (even number): "))
    correct_board_size(board_size)


if __name__ == "__main__":
    print("Welcome to memory game !!!!!!!!!!")
    enter_board_size()
