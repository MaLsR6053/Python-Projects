import getpass

print("Hello! This is my first interactive game.")
print(".....rock.....")
print(".....paper.....")
print(".....scissors.....")

#player1 = input("Player 1, what is your choice? ")
#player2 = input("Player 2, what is your choice? ")
player1 = getpass.getpass("Player 1, what is your choice? ")
player2 = getpass.getpass("Player 2, what is your choice? ")

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