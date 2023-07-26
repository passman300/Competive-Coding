import sys
N = int(input())
A = sys.stdin.readline()[:-1]
B = sys.stdin.readline()[:-1]
ans = 0
nextEqual = False


for i in range(N):
    if A[i] != B[i]:
        if not nextEqual:
            nextEqual = True
            ans += 1
    else:
        nextEqual = False
print(ans)