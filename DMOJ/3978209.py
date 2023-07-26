n, h, p = list(map(int, input().split()))
a = []
sum = 0
line = list(map(int, input().split()))
for i in range(n):
    a.append(line[i])
    sum += a[-1]
ans = sum * p
a.sort()
for i in range(n):
    perm = a[i] * h
    temp = (sum - (n - i) * a[i]) * p
    ans = min(ans, perm + temp)
    sum -= a[i]
print(ans)