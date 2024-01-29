#SNAKE WATER GUN
import random

def get_user_choice():
    user_choice = input("Enter your choice (snake, water, gun): ").lower()
    while user_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice. Please enter snake, water, or gun.")
        user_choice = input("Enter your choice (snake, water, gun): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'snake' and computer_choice == 'water') or
        (user_choice == 'water' and computer_choice == 'gun') or
        (user_choice == 'gun' and computer_choice == 'snake')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Snake-Water-Gun Game!")
    num_rounds = int(input("Enter the number of rounds: "))


    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()
