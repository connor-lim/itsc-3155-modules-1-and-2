print("enter a string")
firstWord = input()

firstList = []
secondList = []

for x in firstWord:
    firstList.append(x)

print(firstList)

miniList = []
for x in range(0, len(firstList),3):
    secondList.append(firstList[x:x+3])

print("Second List: ",secondList)