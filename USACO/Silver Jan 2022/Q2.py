import sys

input = sys.stdin.readline

N = int(input())
cows = list(map(int, input().split()))

ans = 0


for i in range(len(cows) - 1):
    minn = min(cows[i], cows[i + 1])
    maxx = min(cows[i], cows[i + 1])

    for j in range(i + 1, len(cows)):
        if minn > cows[j]:
            minn = cows[j]
        elif maxx > cows[j]:
            # maxx = cow[j]
            continue
        else:
            ans += j - i + 1
            maxx = cows[j]
            if cows[i] < cows[j]:
                break

        if cows[ i ] < cows[ j ]:
            ans += j - i + 1
            break

print(ans)