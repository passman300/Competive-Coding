import sys
# input = sys.stdin.readline




def check(a, b, c, n):
    points = {'A': 0, 'B': 0, 'C': 0}
    words = {}
    owner = {}
    for i in range(n):
        if a[i] in owner:
            # words[a[i]] += 1
            owner[a[i]].append('A')
        else:
            # words[a[i]] = 1
            owner[a[i]] = ['A']

        if b[i] in owner:
            # words[b[i]] += 1
            owner[b[i]].append('B')
        else:
            # words[b[i]] = 1
            owner[b[i]] = ['B']

        if c[i] in owner:
            # words[c[i]] += 1
            owner[c[i]].append('C')
        else:
            # words[c[i]] = 1
            owner[c[i]] = ['C']

    # print(words)
    # print(owner)

    for key, value in owner.items():
        if len(value) == 1:
            points[value[0]] += 3
        elif len(value) == 2:
            points[value[0]] += 1
            points[value[1]] += 1

    for i in points:
        print(points[i], end=" ")
    print()


T = int(input())

for qwer in range(T):


    n = int(input())
    a = list(input().split(" "))
    b = list(input().split(" "))
    c = list(input().split(" "))

    check(a, b, c, n)

