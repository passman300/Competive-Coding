import sys

input = sys.stdin.readline


n, t = map(int, input().split())

adj = [[] for i in range(n + 1)]

last = [0 for i in range(n + 1)]


line = list(map(int, input().split()))
for i in range(1, n + 1):
    adj[i].append(line[i - 1])



for _ in range(t):
    add = [[] for i in range(n + 1)]
    for i in range(1, n + 1):
        # print(adj)
        # print(i, adj[3])
        if len(adj[i]) == 0:
            continue
        cur = adj[i][0]
        adj[i].pop(0)
        last[i] = cur
        add[cur].append(i)

    for i in range(1, n + 1):
        if len(add[i]) > 0:
            for x in add[i]:
                adj[i].append(x)


for i in range(1, n):
    print(last[i], end= " ")
print(last[n])