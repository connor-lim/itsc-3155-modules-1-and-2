print("enter a row num from 1 to 5: ")
xCoordinate = int(input())
print("enter a col num from 1 to 5: ")
yCoordinate = int(input())

for x in range(5):
    for y in range(5):
        if x == xCoordinate-1 and y == yCoordinate-1:
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()
        