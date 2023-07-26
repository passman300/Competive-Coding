N = int(input())
cords = []

for i in range(N):
    XY = list(map(int, input().split()))
    cords.append(XY)
# print(cords)

ans = 0

for i in range(len(cords)):
    for j in range(len(cords)):
        for k in range(len(cords)):
            if cords[i][1] == cords[j][1] and cords[j][0] == cords[k][0] \
                    and cords[i] != cords[j] and cords[j] != cords[k] and cords[i] != cords[k]:
                distx = abs(cords[i][0] - cords[j][0])
                disty = abs(cords[j][1] - cords[k][1])
                area = distx * disty
                # print(distx, disty)
                if area > ans:
                    # print(cords[ i ], cords[ j ], cords[ k ])
                    ans = area
print(ans)