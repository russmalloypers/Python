"""
Convert inches to centimeters
"""

#inches = 2
converttocentimeter = 2.54
#converted = 1


#while loop will run until "break" is reached.
while True:
    try:
        inches = (int(input("Provide a number in inches: \n")))
        converted = (inches * converttocentimeter)
        inches = (str(inches))
        converted = (str(converted))
        print(inches + " inches is " + converted + " cm")
        print("goodbye")
        break
    except ValueError:
        print("This is not a valid number")