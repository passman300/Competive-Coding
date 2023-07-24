import sys

input = sys.stdin.readline

limit = int(input())

M = int(input())

chores = []

for i in range(M):
    chores.append(int(input()))

chores.sort()
time = 0

cnt = 0
while time <= limit:
    if time + chores[cnt] > limit:
        break
    else:
        time += chores[cnt]
        cnt += 1

# print(time)
print(cnt)
