#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

def name():
    nameis = input("What is your name? \n")
    return nameis
    
    
def ageto100():
    ageis = input("What is your age? \n")
    ageis = int(ageis)
    yearsleft = str(100 - ageis)
    return yearsleft
    
print("Hello " + name() + ", you we be 100 in " + ageto100() + " years")
