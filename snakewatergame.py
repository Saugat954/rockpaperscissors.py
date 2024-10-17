 #rock paper and scissors
import random

def winPattern(userScore, computerScore):
    userInput = input("Select rock, paper, or scissors to play with the computer (or type 'exit' to quit): ").lower()
    computer = random.choice(("rock", "paper", "scissors"))
    validChoice = ['rock', 'paper', 'scissors']
    
    if userInput == 'exit':
        return userScore, computerScore, False  # Exit the game loop
    if userInput not in validChoice:
        print("Select a valid choice, the choices are 'rock', 'paper', or 'scissors'.")
        return userScore, computerScore, True  # Continue the loop for another game

    print(f"The user input is {userInput}")
    print(f"The computer input is {computer}")

    result = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if userInput == computer:
        print("It's a tie!")
    elif result[userInput] == computer:
        userScore += 1
        print("You win!")
    else:
        computerScore += 1
        print("You lose!")

    print(f"Scores -> User: {userScore}, Computer: {computerScore}")
    
    return userScore, computerScore, True  # Continue the loop for another game

def main():
    userScore = 0
    computerScore = 0

    while True:
        userScore, computerScore, continue_game = winPattern(userScore, computerScore)
        if not continue_game:
            break  

 


