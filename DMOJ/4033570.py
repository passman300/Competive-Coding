n = int(input())
a = []
ans = 0
for i in range(n):
    a.append(int(input()))

a.sort()

i, j = 0, -1
while i < n//2 - 1:
    ans += a[j]*2 - a[i] * 2
    i += 1
    j -= 1

if n % 2 == 0:
    ans += a[n//2] - a[n//2-1]
else:
    x = a[n//2-1]
    y = a[n//2]
    z = a[n//2+1]
    ans += max(2*z - x - y, z + y - x*2)
print(ans)