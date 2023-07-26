def flipRow(Square, Row):
    for i in range(len(Square)):
        if Square[Row][i] == "0":
            Square[Row][i] = "1"
        else: Square[Row][i] = "0"
    return Square

def flipColumn(Square, Column):
    for i in range(len(Square)):
        if Square[i][Column] == "0":
            Square[i][Column] = "1"
        else: Square[i][Column] = "0"
    return Square

N = int(input())

Perfect_Sqaure = [["0" for i in range(N)] for i in range(N)]
Square = []
for i in range(N):
    line = input().split(" ")
    Square.append(line)


count = 0
moves = []

for row in range(len(Square)):
    if Square[row][0] == "1":
        Square = flipRow(Square, row)
        count += 1
        moves.append("R " + str(row + 1))

for column in range(1, len(Square)):
    if Square[0][column] == "1":
        Square = flipColumn(Square, column)
        count += 1
        moves.append("C " + str(column + 1))

Solvable = True

if Square != Perfect_Sqaure:
    Solvable = False

if not Solvable:
    print(-1)
else:
    print(count)
    for i in moves:
        print(i)