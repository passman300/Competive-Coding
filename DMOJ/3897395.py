import sys

input = sys.stdin.readline

m = int(input())
n = int(input())
k = int(input())

leftright = set()
updown = set()

for _ in range(k):
    line = input()
    line = line.split()
    optype = line[0]
    x = int(line[1])
    if(optype=='R'):
        if x in leftright:
            leftright.remove(x)
        else:
            leftright.add(x)
    else:
        if x in updown:
            updown.remove(x)
        else:
            updown.add(x)

total = 0

total += m * len(updown)
total += n * len(leftright)
total -= 2 * len(updown) * len(leftright)

print(total)