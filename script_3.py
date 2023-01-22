def return_dict(word):
    dictionary = {}
    for x in word:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary


print("Enter a word: ")
word = input()
print(return_dict(word))