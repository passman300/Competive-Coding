import sys
cords = set()
P = int(input())
for i in range(P):
    cords.add(tuple(map(int, input().split())))
# print(cords)
cords = list(cords)
# the left side would have the smallest x value
leftmost = sys.maxsize
# the right side would have the largest x value
rightmost = -1 * sys.maxsize
# the bottom side would have the smallest y value
bottommost = sys.maxsize
# the top side would have the largest y value
topmost = -1 * sys.maxsize

for i in range(P):
    if cords[i][0] < leftmost:
        leftmost = cords[i][0]
    if int(cords[i][0]) > rightmost:
        rightmost = cords[i][0]
    if int(cords[i][1]) < bottommost:
        bottommost = cords[i][1]
    if int(cords[i][1]) > topmost:
        topmost = cords[i][1]

# print(leftmost)
# print(rightmost)
# print(bottommost)
# print(topmost)

disty = abs(topmost - bottommost)
distx = abs(rightmost - leftmost)
primeter = 2 * (distx + disty)
print(primeter)