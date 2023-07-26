n = int(input())
ans = 0
i = 1
while i <= n:
    if i * 10 >= n:
        ans += n - i + 1
    else:
        ans += 9 * i
    i *= 100
print(ans)