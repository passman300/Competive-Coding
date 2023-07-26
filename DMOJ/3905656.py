alphabet = []
alphabet[:0] = input()

word = []
word[:0] = input().lower()

count = 0
while len(word) > 0:
    count += 1
    for letter in alphabet:
        if len(word) > 0:
            if letter == word[0]:
                word.pop(0)


print(count)