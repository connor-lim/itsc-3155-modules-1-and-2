print("enter a string")
word = input()

upperCase = ""
lowerCase = ""

for x in word:
    if x.isupper():
        upperCase += x
    elif x.islower():
        lowerCase += x

finalWord = lowerCase + upperCase
print(finalWord)