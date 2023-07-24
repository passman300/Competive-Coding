N = int(input())
requestTemp = list(map(int, input().split()))
currentTemp = list(map(int ,input().split()))

temp = []
for i in range(N):
    temp.append(requestTemp[i] - currentTemp[i])

ans = 0
R = 0
L = N - 1

while True:
    Flag = True
    for i in range(N):
        if temp[i] != 0:
            Flag = False
    if Flag == True:
        break

    for i in range(R, N):
        if temp[i] != 0:
            R = i
            break
    for i in range(L, 0, -1):
        if temp[i] != 0:
            L = i
            break

    diffrence = 0

    if abs(temp[R]) < abs(temp[L]):
        diffrence = temp[R]
    else: diffrence = temp[L]

    for i in range(R, L + 1):
        temp[i] -= diffrence

    ans += abs(diffrence)
    print(temp)
print(ans)