import sys
# input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
total = 0
L, R = 0, K - 1

while (R < N):



    if abs(L - R) >= K:
        print('GOOD')
        total += 1
        if R == N:
            L += 1
        else: R += 1

    else: L += 1
    print(nums[L: R], L, R)
    print(total)