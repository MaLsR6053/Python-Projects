import pwinput
import time
import sys

ascii_art = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
"""
print(ascii_art)

def clear_previous_line():
    sys.stdout.write('\x1b[1A')  # Move cursor up
    sys.stdout.write('\x1b[2K')  # Clear entire line
    sys.stdout.flush()
print("Welcome to my rock, paper, scissors game.\nv1.5")
time.sleep(1.5)
print("Please enter your choice, and then hit enter.")
time.sleep(1.5)
#Player 1 enters input (asterisks show while typing)
player1 = pwinput.pwinput("Player 1, what is your choice? ", mask="*")

#Short delay, then erase the asterisk line
time.sleep(0.75)
clear_previous_line()

#Continuing the game...
print("-" * 40)
player2 = pwinput.pwinput("Player 2, what is your choice? ", mask="*")
time.sleep(0.2)
clear_previous_line()
print("Calculating....")
time.sleep(2)


#Super inefficient code
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
elif player1 == "scissors" and player2 == "scissors":
    print("It's a tie! You both played scissors.")
else:
        print("One of you must have had a typo in your response. Let's try that again, dummy.")

