import sys

N = int(sys.stdin.readline())
temp = sys.stdin.readline()
cows = []
for i in range(N):
    cows.append(temp[i])
ans = 0

for i in range(0, N - 2):
    for j in range(i + 3, N + 1):
        if cows[i:N + 1].count("G") == 0 or cows[i:N + 1].count("H") == 0:
            break

        photo = cows[i:j]

        if photo.count("G") > 1:
            if photo.count("H") > 1:
                break

        if photo.count("G") == 1 or photo.count("H") == 1:
            ans += 1

print(ans)
