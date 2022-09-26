from random import randint
import rockPaperScissorsChoices

yourChoice = input('What would you like to play with?\n[Rock, Paper, Scissors]\n').lower()

# Gets the computers selection
computerChoice = rockPaperScissorsChoices.computerSelection()     
print("\u0332".join('Your Selection\n'))

#Gets the numeric value of your selection
yourChoiceNumeric = rockPaperScissorsChoices.yourSelection(yourChoice)     
print("\u0332".join('Computer Selection\n'))

#Compares your selection with the computers to determine the winner
rockPaperScissorsChoices.winLoseeTable(yourChoiceNumeric, computerChoice)