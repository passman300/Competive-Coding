import statistics
import math
n = int(input())
histo = list(map(int, input().split()))

mid = int(round(statistics.mean(histo)))
ans = 0
# print(mid)
for i in range(len(histo)):
    ans += (histo[i] - mid) ** 2
print((ans))