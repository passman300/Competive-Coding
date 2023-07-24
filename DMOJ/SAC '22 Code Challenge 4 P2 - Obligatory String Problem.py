import sys
from itertools import permutations
alpha = "abcdefghijklmnopqrstuvwxyz"


N = int(input())
anskey = input()
ans = [anskey]

for i in range(4):
    if N > 26:
        N = 26
    letter = alpha.index(anskey[i])
    alpha1 = alpha[letter: ] + alpha[: letter]
    alpha2 = alpha[letter + 1: ] + alpha[: letter + 1]
    # print(alpha1)
    # print(alpha2)
    for j in range(1, N + 1):
        word = anskey
        # print(word[i], alpha1[j])
        word = word.replace(word[i], alpha1[j])
        ans.append(word)
        word = anskey
        # print(word[ i ], alpha2[-(j + 1)])
        word = word.replace(word[ i ], alpha2[-(j + 1)])
        # print(word)
        ans.append(word)
ans.sort()
for i in ans:
    print(i)
# print(ans)

        # alpha1 = alpha[]
        # print(alpha2)
        # word = anskey.copy()
        # # del word[i]
        # first = alpha1[ord("word[i]") + j]

