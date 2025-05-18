import pwinput
import time
import sys

def clear_previous_line():
    sys.stdout.write('\x1b[1A')  # Move cursor up
    sys.stdout.write('\x1b[2K')  # Clear entire line
    sys.stdout.flush()

# Player 1 enters input (asterisks show while typing)
player1 = pwinput.pwinput("Player 1, what is your choice? ", mask="*")

# Short delay, then erase the asterisk line
time.sleep(0.75)
clear_previous_line()

# Continue with your game...
print("-" * 40)
player2 = getpass.getpass("Player 2, what is your choice? ")
time.sleep(0.75)
clear_previous_line()

if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins! Player 1 played rock and Player 2 played scissors.")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins! Player 1 played paper and Player 2 played rock.")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins! Player 1 played scissors and Player2 played paper.")
elif player1 == "rock" and player2 == "paper":
    print("Player2 wins! Player 1 played rock and Player 2 played paper.")
elif player1 == "rock" and player2 == "rock":
    print("It's a tie! You both played rock.")
elif player1 == "paper" and player2 == "paper":
    print("It's a tie! You both played paper.")
elif player1 == "paper" and player2 == "scissors":
    print("Player2 wins! Player 1 played paper and Player 2 played scissors.")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins! Player 1 played scissors and Player 2 played rock.")
else:
    print("It's a tie! You both played scissors.")
