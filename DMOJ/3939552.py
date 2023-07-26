n = int(input())
a = [0 for i in range(10**6 + 10)]
line = list(map(int, input().split()))
for i in range(n):
    a[i] = line[i]
sol = 0
lo = 0
hi = n - 1
while lo < hi:
    if a[lo] == a[hi]:
        lo += 1
        hi -= 1
        continue
    if a[lo] < a[hi]:
        a[lo + 1] += a[lo]
        lo += 1
    else:
        a[hi - 1] += a[hi]
        hi -= 1
    sol += 1

print(sol)