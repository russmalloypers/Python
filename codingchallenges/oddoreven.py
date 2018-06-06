#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

num = int(input("Please input an integer \n"))
#print("Your number is " + str(num))
mod = num % 2
if(num % 2 ==0):
    print("Your number is even!")
else:
    print("Your number is odd!")