#one-player Rock Paper Scissors game vs CPU

#I'm going to try and make a 1 player and use random library for second player

import random



print("Welcome to rock paper scissors versus the computer!")

def cpumove():
    roll = random.randint(0,2)
    if roll == 0:
        return 'cpurock'
    elif roll == 1:
        return 'cpupaper'
    else:
        return 'cpuscissors'
        
def usermove():
    choice = ''
    while (choice != 'rock') and (choice != 'paper') and (choice != 'scissors'):
        choice = input("Choose your move by inputting rock, paper, or scissors \n")
    return choice
done = ''

while done != 'no':
    cpuchoice = cpumove()
    playerchoice = usermove()
    
    
    #cpuchoice[3:] ignores the first 3 characters in the string cpuchoice so that the strings match when comparing for draw    
    if (cpuchoice[3:]) == (playerchoice):
        print("Draw! CPU's " + cpuchoice[3:] + " is the same as Players " + playerchoice)
        
    if cpuchoice == 'cpurock' and playerchoice == 'paper':
        print("Players paper beats CPU's rock!")
    if cpuchoice == 'cpurock' and playerchoice == 'scissors':
        print("CPU's rock beats Players scissors!")
    if cpuchoice == 'cpupaper' and playerchoice == 'rock':
        print("CPU's paper beats Players rock!")
    if cpuchoice == 'cpupaper' and playerchoice == 'scissors':
        print("Players scissors beat CPU's paper!")
    if cpuchoice == 'cpuscissors' and playerchoice == 'rock':
        print("Players rock beats CPU's scissors!")
    if cpuchoice == 'cpuscissors' and playerchoice == 'paper':
        print("CPU's scissors beat Players paper!")
    done = ''
    while done != 'no' and done != 'yes':
        done = input("Would you like to play again? (yes/no) \n")
        
