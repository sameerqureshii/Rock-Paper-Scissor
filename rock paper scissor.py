import random

# Define options
options = ["rock", "paper", "scissor"]

# Initialize score and rounds
player_wins, computer_wins, draws = 0, 0, 0
rounds_remaining = 5

# Game loop
while rounds_remaining > 0:
    # Get user choice
    player_choice = input("Choose rock, paper or scissor: ").lower()

    # Check for invalid input
    if player_choice not in options:
        print("Enter a valid option: rock, paper or scissor.")
        continue

    # Generate computer choice
    computer_choice = random.choice(options)

    # Determine winner & update score
    if player_choice == computer_choice:
        draws += 1
        print(f"It's a tie! You both choose {player_choice}.")
    elif (player_choice == "rock" and computer_choice == "scissor") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissor" and computer_choice == "paper"):
        player_wins += 1
        print(f"You win!  You choose {player_choice} and the computer choose {computer_choice}.")
    else:
        computer_wins += 1
        print(f"Computer wins!  You choose {player_choice} and the computer choose {computer_choice}.")

    # Display remaining rounds
    rounds_remaining -= 1
    print(f"{rounds_remaining} rounds remaining.")

# Show final results
print(f"\nFinal Score:")
print(f"Me: {player_wins}")
print(f"Computer: {computer_wins}")
print(f"Draws: {draws}")

# Determine overall winner
if player_wins > computer_wins:
    print("You won the game! ")
elif player_wins < computer_wins:
    print("Computer won the game!")
else:
    print("It's a draw! Play again!")