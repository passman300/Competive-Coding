import sys
# input = sys.stdin.readline

T = int(input())

for qwre in range(T):
    n = int(input())
    mid = n//2
    temp = input()

    line = []
    for i in range(n):
        line.append(temp[i])

    values = []
    fliped = []
    diffrence = []
    for i in range(n):
        if line[i] == 'R':
            values.append(n - i - 1)
            fliped.append(i)

        else:
            values.append(i)
            fliped.append(n - i - 1)

        diffrence.append(fliped[-1] - values[-1])

    total = sum(values)
    for i in range(n):
        if i < mid and line[i] == 'L':
            line[i] = 'R'
            total += diffrence[i]
        else: total += abs(diffrence[i])
        print(total, end=" ")
    print()
