import random

def getUserSelection():
    selection = input("Enter a choice : (1. Rock, 2. Paper, 3. Scissor) \n")

    while selection.isdigit():
        selection = input("Please Enter a choice (AlphaNumeric!): (1. Rock, 2. Paper, 3. Scissor) \n")

        if selection.isalpha():
            break
    
    return selection


def determineWinner(userAction, computerAction):
    if userAction == computerAction:
        print("Both players selected : " + userAction + ". It's a tie game")
    elif userAction == "Rock" or userAction == "1":
        if computerAction == "Scissor":
            print("Rock smashes Scissors!! You Win!! :)")
        else:
            print("Paper covers Rock!! You lose!! :(")
    elif userAction == "Paper" or userAction == "2":
        if computerAction == "Rock":
            print("Paper covers Rock!! You Win!! :)")
        else:
            print("Scissor cut Paper!! You lose!! :(")
    elif userAction == "Scissor" or userAction == "3":
        if computerAction == "Paper":
            print("Scissor cut Paper!! You Win!! :)")
        else:
            print("Rock smashes Scissor!! You lose!! :(")
    




while True:
    userActionInput = getUserSelection()

    possibleActions = ["Rock", "Paper", "Scissor"]
    computerAction = random.choice(possibleActions)

    print("\n You chose : " + userActionInput + ", Computer chose : " + computerAction)


    determineWinner(userActionInput,computerAction)

    playAgain = input("Play again? \n")
    if playAgain.lower() != "y" or playAgain.lower() != "yes":
        break