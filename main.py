# SHREE GANESHAY NAMAH
# GURUKRIPA HI KEVALAM
#main.py
import memory_game
import s_w_g
import tic_tac_toe

print("********************** Welcome to QUESTCRAFT **********************")
print("Contains the following games:")
print("1) Memory game")
print("2) Tic-Tac-Toe")
print("3) Snake-Water-Gun")
print("4) EXIT")

while True:
    choice = int(input("Enter your choice here: "))

    def switch_case(choice):
        if choice == 1:
            memory_game.enter_board_size()
        elif choice == 2:
            s_w_g.play_game()
        elif choice == 3:
            tic_tac_toe.play_tic_tac_toe()
        elif choice == 4:
            print("Exiting the game. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

    switch_case(choice)
