import pwinput
import time
import sys
import random

ascii_art = r"""
    _______
---'   ____)
      (_____)
      (_____)   ROCK
      (____)
---.__(___)
""" 
ascii_art_2 = r"""
   _______
---'   ____)____
          ______)
          _______)    PAPER
          _______)
---.__________)
""" 
ascii_art_3 = r"""	
   _______
---'   ____)____
          ______)
        __________)   SCISSORS
      (____)
---.__(___)
"""
try:	
	print(ascii_art)
	time.sleep(1.5)
	print(ascii_art_2)
	time.sleep(1.5)
	print(ascii_art_3)
	time.sleep(1.5)
	def clear_previous_line():
    		sys.stdout.write('\x1b[1A')  # Move cursor up
    		sys.stdout.write('\x1b[2K')  # Clear entire line
    		sys.stdout.flush()


	print("Welcome to my rock, paper, scissors game where you are now playing against a computer opponent!\nv1.5")
	time.sleep(1.5)
	print("Please enter your choice, and then hit enter.")
	time.sleep(1.5)
#Player enters input (asterisks show while typing)
	player = input("Player, what is your choice? ").lower()

rand_num = random.randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer plays {computer}")



#Super inefficient code
	if player == "rock" and compputer == "scissors":
    		print("You win! You played rock and the Computer played scissors.")
	elif player == "paper" and computer == "rock":
    		print("You win! You played paper and the Computer played rock.")
	elif player == "scissors" and computer == "paper":
    		print("You win! You played scissors and the Computer played paper.")
	elif player == "rock" and computer == "paper":
    		print("Computer wins! You played rock and the Computer played paper.")
	elif player == "rock" and computer == "rock":
    		print("It's a tie! You both played rock.")
	elif player == "paper" and computer == "paper":
    		print("It's a tie! You both played paper.")
	elif player == "paper" and computer == "scissors":
    		print("Computer wins! You played paper and the Computer played scissors.")
	elif player == "scissors" and computer == "rock":
    		print("Computer wins! You played scissors and the Computer played rock.")
	elif player == "scissors" and computer == "scissors":
    		print("It's a tie! You both played scissors.")
	else:
        	print("One of you must have had a typo in your response. Let's try that again, dummy.")

except KeyboardInterrupt:
    print("\n[!] User interrupted. What...you don't want to play my game? :*(")
    sys.exit(0)
