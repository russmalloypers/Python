#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

wrd=input("Please enter a word \n")
wrd=str(wrd)
rvs=wrd[::-1]
print("\n" +  wrd)
print(rvs + " (reversed)")

if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")