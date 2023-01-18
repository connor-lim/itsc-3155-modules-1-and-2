firstString = input("Enter first word")
secondString = input("Enter second word")
if (firstString in secondString):
    print("True")
elif (secondString in firstString):
    print("True")
else:
    print("False")
