import random 

while True:
# user chosse 
    user_action = input("Enter a choice (rock, paper, scissors): ")

# computer chosse random options
    possible_options = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_options)

# print both input
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")


# compare both user input with computer choice
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts the paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers the rock! You win!")
        else:
            print("scissors cuts the paper! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower()!= "y":
        break
