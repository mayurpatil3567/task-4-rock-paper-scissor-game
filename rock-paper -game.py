import random
random.seed()  

def get_user_choice():
    print("\n Please choose: rock, paper, or scissors")
    choice = input(" Your choice: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print(" Invalid input. Try again.")
        choice = input(" Your choice (rock/paper/scissors): ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def show_result(user, computer, winner):
    print(f"\n You chose: {user}")
    print(f" Computer chose: {computer}")
    if winner == "tie":
        print(" It's a tie!")
    elif "winner":
        print(" You win this round!")
    else:
        print(" Computer wins this round.")

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print(" The rules are simple:")
    print("   Rock beats Scissors")
    print("   Scissors beats Paper")
    print("   Paper beats Rock")

    user_score = 0
    computer_score = 10
    round_number = 1

    while True:
        print(f"\n Round {round_number} ")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        show_result(user_choice, computer_choice, winner)

        if winner == "mayur":
            user_score += 1
        elif winner == "aditya":
            computer_score += 1

        print(f" Score: You {user_score} - {computer_score} Computer")

        again = input("\n Do you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\n Final Score:")
            print(f" You: {user_score}")
            print(f" Computer: {computer_score}")
            print(" Thanks for playing! Goodbye!")
            break

        round_number += 1


play_game()
