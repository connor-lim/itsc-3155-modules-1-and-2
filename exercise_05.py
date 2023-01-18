firstList = []
secondList = []
matchList = []
for x in range(5):
    print("enter number for the first list: ")
    temp = int(input())
    firstList.append(temp)

for y in range(5):
    print("enter number for the second list: ")
    temp = int(input())
    secondList.append(temp)

print("first list: " , firstList)
print("second list: " , secondList)

for a in range(5):
    for b in range(5):
        if firstList[a] == secondList[b]:
            matchList.append(firstList[a])

print("common list: ", matchList)