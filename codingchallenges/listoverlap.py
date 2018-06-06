#take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes

a = [1,2,3,4,5,6,6]
b = [3,4,5,1,2,6,6]

duplicates = []

#nested for loop that iterates over each item a:1, b:1, b:2, b:3 etc. Then it runs a:2, b:1, b:2, b:3 etc.
for i in range(len(a)):
    for y in range(len(b)):
        if a[i] == b[y]:
            duplicates.append(a[i])


#list(set(listname)) removes all duplicate entries
duplicates = list(set(duplicates))
print(duplicates)