
N = int(input())
requestTemps = list(map(int, input().split()))
currentTemps = list(map(int, input().split()))
complet = [False for i in range(N)]

cnt = 0
while True:
    if requestTemps == currentTemps:
        break
    for i in range(N):
        if requestTemps[i] == currentTemps[i]:
            complet[i] = True
        if complet[i] == False:
            currentTemps[i] += 1

    if complet[0] == False and complet[1] == True:
        cnt += 1
    for i in range(1, N):
        if complet[i] == False and complet[i] != complet[i - 1]:
            cnt += 1

    print(currentTemps)
    print(complet)

print(cnt)