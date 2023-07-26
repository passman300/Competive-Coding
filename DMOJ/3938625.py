N = int(input())
cows = []
for i in range(N):
    pos, sick = map(int, input().strip().split())
    cows.append((pos, sick))

cows.sort(key=lambda cow: cow[0])

R = N
for i in range(N):
    if cows[i][1] == 0:
        if i != 0:
            if cows[i-1][1] == 1:
                R = min(R, cows[i][0]-cows[i-1][0])
        if i != N-1:
            if cows[i+1][1] == 1:
                R = min(R, cows[i+1][0]-cows[i][0])
R -= 1

count = 0
cows.insert(0, (0, 0))
for i in range(N):
    if cows[i][1] == cows[i+1][1] == 1:
        if cows[i+1][0]-R > cows[i][0]:
            count += 1
    elif cows[i][1] == 0 and cows[i+1][1] == 1:
        count += 1

print(count)