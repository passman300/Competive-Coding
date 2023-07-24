import sys

input = sys.stdin.readline

def solve(x, y):
    T, W = 0, 0

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] > y[j]:
                W += 1
            elif x[i] == y[j]:
                T += 1
    # print(W, T)
    W = W / 16
    T = T / 16
    # print(W, T)
    if W == 1: return True
    elif T == 1: return False
    else:
        num = W / (1 - T)
        return num > 0.5


N = int(input().strip())

for _ in range(N):
    line = tuple(map(int, input().strip().split()))
    A = line[:4]
    B = line[4:]

    ans = False

    # possbile numbers Brute force Kek
    for i in range(1, 11):
        if ans: break

        for j in range(1, 11):
            if ans: break

            for k in range(1, 11):
                if ans: break

                for l in range(1, 11):
                    if ans: break

                    wins_A, wins_B, wins_C = 0, 0, 0

                    C = [i, j, k, l]
                    # print(C)

                    wins_A += (solve(A, B) + solve(A, C))
                    wins_B += (solve(B, A) + solve(B, C))
                    wins_C += (solve(C, A) + solve(C, B))
                    # print(wins_A, wins_B, wins_C)

                    if wins_A == wins_B and wins_A == wins_C:
                        ans = True
    if ans:
        print("yes")
    else:
        print("no")
