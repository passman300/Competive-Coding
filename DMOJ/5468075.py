n = int(input())

G = []
L = []

for i in range(n):
    ary, num = input().split()
    num = int(num)
    if ary == 'G':
        G.append(num)
    else:
        L.append(num)
G.sort()
L.sort()


cnt = 0
for i in range(len(G)):
    j = 0
    while j < len(L) and G[i] > L[j]:
        j += 1
    cnt = max(cnt, i + 1 + len(L) - j)
print(n - cnt)