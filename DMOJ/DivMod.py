import math
Q = int(input())
for i in range(Q):
    A, B, C = map(int, input().split())
    x, y = (A * B // C) * C, C % A
    for N in range(C, 1000000000000, A):
        # print(N)
        if N // A == B:
            print(N)
            # print(N // A, N % A, C % A)
            break