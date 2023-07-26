import sys
G = int(input())
P = int(input())
Gates = [0 for x in range(G)]
ans = 0
for i in range(P):
    plane = int(input()) - 1

    while plane >= 0 and Gates[plane] > 0:
        save = Gates[plane]
        Gates[plane] += 1
        plane = plane - save

    if plane < 0:
        break
    else:
        Gates[plane] += 1
        ans += 1
print(ans)