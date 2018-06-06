
x = int(input("Please input a number and I will return a list of all the divisors of that number \n"))

print("You chose " + str(x))

#if(x % 2 ==0):
    #print("Divisible by 2")
    
rangeofnumbers = range(2, x+1)
for y in rangeofnumbers:
    if (x % y == 0):
        print(str(y) + " is a divisor of " + str(x))
    else:
        print(str(y) + " is not a divisor of " + str(x))
