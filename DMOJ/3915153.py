J = int(input()) # number of Jerseys
A = int(input()) # numbers of Athletes

Jerseys = []
Taken = [False for i in range(J)]
for i in range(J):
    Jersey_input = input()
    if Jersey_input == "S":
        Jerseys.append(1)
    elif Jersey_input == "M":
        Jerseys.append(2)
    else: Jerseys.append(3)

Request_Size = -1
Request_Num = []
output = 0

for i in range(A):
    Size, Num = input().split(" ")
    Num = int(Num)
    if Size == "S":
        Request_Size = 1
    elif Size == "M":
        Request_Size = 2
    else: Request_Size = 3

    if Taken[Num - 1] or (Jerseys[Num - 1] < Request_Size): continue
    else:
        Taken[Num - 1] = True
        output += 1


print(output)