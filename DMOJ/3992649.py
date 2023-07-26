h, v = list(map(int, input().split()))
y = list(map(int, input().split()))
x = list(map(int, input().split()))
dct1 = {}
dct2 = {}
list1 = []
ans = 0
for i in range(h):
    for j in range(i + 1, h):
        temp = y[j] - y[i]
        if temp in dct1.keys():
            dct1[temp] += 1
        else:
            dct1[temp] = 1
            list1.append(temp)
for i in range(v):
    for j in range(i + 1, v):
        temp = x[j] - x[i]
        if temp in dct2.keys():
            dct2[temp] += 1
        else:
            dct2[temp] = 1
for i in list1:
    if i in dct2.keys():
        ans += dct1[i] * dct2[i]
print(ans)