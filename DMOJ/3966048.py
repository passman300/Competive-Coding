well = {}

for x in range(-1, -201, -1):
    for y in range(-200, 201):
        well[(x, y)] = False

well[(-1,0)] = True
well[(-2,0)] = True
well[(-3,0)] = True
well[(-3,1)] = True
well[(-3,2)] = True
well[(-3,3)] = True
well[(-4,3)] = True
well[(-5,3)] = True
well[(-5,4)] = True
well[(-5,5)] = True
well[(-4,5)] = True
well[(-3,5)] = True
well[(-3,6)] = True
well[(-3,7)] = True
well[(-4,7)] = True
well[(-5,7)] = True
well[(-6,7)] = True
well[(-7,7)] = True
well[(-7,6)] = True
well[(-7,5)] = True
well[(-7,4)] = True
well[(-7,3)] = True
well[(-7,2)] = True
well[(-7,1)] = True
well[(-7,0)] = True
well[(-7,-1)] = True
well[(-6,-1)] = True
well[(-5,-1)] = True

direc, dist = input().split()
dist = int(dist)

Safe = True
row, col = -5, -1 # starting point


while Safe and direc != "q":
    row_count = 0
    column_count = 0
    if direc == "l":
        row_count = 0
    if direc == "l":
        column_count = -1
    elif direc == "u":
        row_count = 1
    elif direc == "r":
        column_count = 1
    elif direc == "d":
        row_count = -1

    while dist > 0:
        row += row_count
        col += column_count
        if well[(row, col)]:
            Safe = False
        else:
            well[(row, col)] = True
        dist -= 1

    if Safe:
        print(col, row, "safe")
    else:
        print(col, row, "DANGER")

    direc, dist = input().split()
    dist = int(dist)