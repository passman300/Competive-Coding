N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] in A and A.index(A[i] + A[j] + A[k]) > k:
                count += 1
print(count)