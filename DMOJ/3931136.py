import sys

N, M = list(map(int, input().split()))

count = 0
Haves = []
for i in range(N):
    element = sys.stdin.readline()[:-1]
    Haves.append(element)

for _ in range(M):
    num = int(input())
    needs = []
    haveall = True
    for i in range(num):
        element = sys.stdin.readline()[:-1]
        needs.append(element)
    for i in range(len(needs)):
        if needs[i] not in Haves:
            haveall = False
            break
    if haveall:
        count += 1

print(count)