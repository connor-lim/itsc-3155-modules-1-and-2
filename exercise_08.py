firstList = []
secondList = []
for x in range(10):
    print("Enter number ", x)
    number = int(input())
    firstList.append(number)

for x in range(10):
    count = 0
    for y in range(10):
        if firstList[x] == firstList[y]:
            count += 1
    if count <= 1:
        secondList.append(firstList[x])
    count = 0
print(firstList)
print(secondList)
       
        