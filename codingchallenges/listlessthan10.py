#a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 4, 5, 6, 9, 15]
for i in a:
    if i < 5:
        print(str(i) + " is less than 5")
    else:
        print(str(i) + " is not less than 5")