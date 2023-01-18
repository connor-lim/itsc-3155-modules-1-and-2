listLength = int(input("enter number: "))
floatList = []
for x in range(listLength):
    print("enter number " + str(x+1) + ": ")
    tempFloat = float(input())
    floatList.append(tempFloat)

print(floatList)

