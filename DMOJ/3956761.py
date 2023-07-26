N = int(input())
cords = set()

for i in range(N):
    XY = tuple(map(int, input().split()))
    cords.add(XY)
ans = 0

for i in cords:
    for j in cords:
        A = (i[0], j[1])
        B = (j[0], i[1])
        if A in cords and B in cords:
            distx = abs(i[0] - j[0])
            disty = abs(i[1] - j[1])
            area = distx * disty
            if area > ans:
                ans = area
print(ans)