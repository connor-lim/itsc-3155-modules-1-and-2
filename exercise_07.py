numbers = []
evenNumbers = []
quitAnswer = True

while quitAnswer:
    print("enter a number or type QUIT to quit")
    answer = input()
    if answer == "QUIT":
        quitAnswer = False
    else:
        numbers.append(answer)

for x in range(len(numbers)):
    temp = int(numbers[x])
    if temp % 2 == 0:
        evenNumbers.append(temp)

print("All nums", numbers)
print("Even nums", evenNumbers)