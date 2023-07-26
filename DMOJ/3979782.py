import sys
def shift(index, s):
    alpha_backwards = 'zyxwvutsrqponmlkjihgfedcba'
    ans = (index + s) % 26
    return alpha_backwards[ans]


# k = int(input())
alpha_backwards = 'zyxwvutsrqponmlkjihgfedcba'
k = int(input())
string = (sys.stdin.readline()[:-1]).lower()
word = ''
for i in range(len(string)):
    # print(i)
    # print(string[i])
    s = 3 * (i + 1) + k
    word += shift(alpha_backwards.index(string[i]), s)
print(word.upper())