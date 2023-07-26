def next_true (a, N, n):
    for i in range(n, N):
        if a[i]:
            return a[i]
    return False
def check(a, N):
    wild = 0
    i = 0
    for i in range(len(a)):
        if a[i]:
            i += 1
        else:
            break
    wild = next_true(a, N, i)
    if not wild:
        wild = a[i-1]
    for i in range(N):
        if not a[i]:
            a[i] = wild
    for i in range(1, N):
        if a[i] < a[i - 1]:
            return False
    return True


N = int(input())
a = list(map(int, input().split()))

if check(a, N):
    print("YES")
else:
    print("NO")