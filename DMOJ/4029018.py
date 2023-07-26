row, colum  = list(map(int, input().split()))
maxtrix = []

for i in range(row):
    maxtrix.append(list(map(int, input().split())))

ans = [[maxtrix[j][i] for j in range(len(maxtrix))] for i in range(len(maxtrix[0])-1,-1,-1)]

for i in range(colum):
    for j in range(row):
        print((ans[i][j]), end= " ")
    print("")