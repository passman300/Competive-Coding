import sys
import bisect

# input = sys.stdin.readline

total = 0
N, Money = map(int, input().split())
stands = list(map(int, input().split()))

stands.sort()



flag = True
while flag:
    point = bisect.bisect_right(stands, Money)
    for i in range(point):
        Money -= stands[i]

        if Money > 0:
            total += 1
        print(Money, i + 1)
print(total)