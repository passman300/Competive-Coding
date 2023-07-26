B = int(input())
P = (5 * B) - 400
N = 0
if P == 100:
    N = 0
elif P < 100:
    N = 1
elif P > 100:
    N = -1
print(P)
print(N)