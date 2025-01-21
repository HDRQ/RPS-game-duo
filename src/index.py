import random

aiScore = 0
p1Score = 0

def lost():
    global aiScore  
    aiScore += 1
    return "Oh no! The computer beat you!"

def win():
    global p1Score  
    p1Score += 1
    return "Congrats! You beat the computer!"

def system(a, b):
    if a == "rock" and b == "paper":
        return lost()
    elif a == "scissor" and b == "rock":
        return lost()
    elif a == "paper" and b == "scissor":
        return lost()
    elif a == "paper" and b == "rock":
        return win()
    elif a == "scissor" and b == "paper":
        return win()
    elif a == "rock" and b == "scissor":
        return win()
    else:
        return "Oh nooo! It's a draw!"

def ai():
    choice = random.randint(0, 2)
    if choice == 0:
        choice = "rock"
    elif choice == 1:
        choice = "paper"
    else:
        choice = "scissor"
    return choice

def check(p1):
    if p1 == "rock" or p1 == "paper" or p1 == "scissor":
        return True
    else:
        return False

# Main game loop
while True:
    p1 = input("Choose your move! rock, paper or scissors: ")
    while not check(p1):
        p1 = input("You can't choose that! Choose your move again! rock, paper or scissors: ")

    p2 = ai()
    print(f"The computer chose: {p2}")
    print(system(p1, p2))
    print(f"The current score is {aiScore} to the Computer and {p1Score} to you.")
    
    # Ask for rematch
    rematch = input("Would you like a rematch? Y/N: ").strip().upper()
    if rematch == "N":
        print(f"Final score: Computer {aiScore}, You {p1Score}. Thanks for playing!")
        break
    elif rematch != "Y":
        print("Invalid input! Exiting the game.")
        break