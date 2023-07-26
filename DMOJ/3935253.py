words = {}
counter = {}
alphabet_keyboard = 'qwertyuiopasdfghjklzxcvbnm'

for c in alphabet_keyboard:
    words[c] = []

n, m = map(int, input().split())
for i in range(n):
    word = input()
    words[word[0]].append(word)

for c in alphabet_keyboard:
    words[c].sort()
    counter[c] = 0

for i in range(m):
    letter = input()[0]
    print(words[letter][counter[letter]])
    counter[letter] += 1
    if counter[letter] == len(words[letter]):
        counter[letter] = 0