from random import randint

# Used to print Rock Paper Scissors on the screen
def rockPaperScissorsChoices():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''
    
    return rock,paper,scissors

rock, paper, scissors = rockPaperScissorsChoices()

#Used to calculate who is the winner and loser
def winLoseeTable(yourChoiceNumeric, computerChoice):
    if yourChoiceNumeric == computerChoice:
        print('You have tied!')
    
    if (yourChoiceNumeric == 1) and (computerChoice == 2):
        print('You Lose!')

    if (yourChoiceNumeric == 2) and (computerChoice == 1):
        print('You Win!')
    
    if (yourChoiceNumeric == 2) and (computerChoice == 3):
        print('You Lose!')

    if (yourChoiceNumeric == 3) and (computerChoice == 2):
        print('You Win!')

    if (yourChoiceNumeric == 1) and (computerChoice == 3):
        print('You Win!')

    if (yourChoiceNumeric == 3) and (computerChoice == 1):
        print('You Lose!')

#Used to determine what choice the computer will choose        
def computerSelection():        
    computerChoice = randint(1,3)
    match computerChoice:
        case 1:
            print(rock)

        case 2:
            print(paper)

        case 3:
            print(scissors)
    return computerChoice

# Gets your number assignment from your choice
def yourSelection(yourChoice):
    yourChoiceNumeric = 0
    match yourChoice:
        case 'rock':
            print(rock)
            yourChoiceNumeric = 1

        case 'paper':
            print(paper)
            yourChoiceNumeric = 2

        case 'scissors':
            print(scissors)
            yourChoiceNumeric = 3
    return yourChoiceNumeric