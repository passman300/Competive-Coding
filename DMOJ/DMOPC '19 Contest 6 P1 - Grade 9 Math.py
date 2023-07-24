import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


A1 =  y1 - y2
B1 = x2 - x1
C1 =  -(A1 * x1 + B1 * y1)


A2 = y3 - y4
B2 = x4 - x3
C2 = -(A2 * x3 + B2 * y3)

if A1 * B2 == A2 * B1:
    if B1 * C2 == B2 * C1:
        print("coincident")
    else: print("parallel")
else:
    x = (B1 * C2 - B2 * C1) / (B2 * A1 - B1 * A2)
    y = (A1 * C2 - A2 * C1) / (A2 * B1 - A1 * B2)

    if x == -0.0:
        x = 0.0
    if y == -0.0:
        y = 0.0
    print(x, y)