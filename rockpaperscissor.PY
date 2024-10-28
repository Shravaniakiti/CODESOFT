import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("WELCOME TO ROCK, PAPER, SCISSORS!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("CHOOSE ROCK, PAPER, or SCISSORS (or 'q' to quit): ").lower()

        if user_choice == 'q':
            print("THANKS FOR PLAYING!")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nComputer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
