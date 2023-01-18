stringList = []
finalString = ""
for x in range(5):
    print("Enter a word: ")
    word = input()
    stringList.append(word)

for y in range(5):
    finalString += stringList[y]
    finalString += " "

print("Words: ", stringList)
print("One String: ", finalString)