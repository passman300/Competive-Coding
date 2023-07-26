dist = list(map(int, input().split()))

ans = [[],[],[],[],[]]
for i in range(5):
    for j in range(5):
        if i == j: ans[i].append(0)
        else:
            # print(dist[j:])
            if i > j:
                ans[ i ].append(sum(dist[j:i]))
            else:
                ans[i].append(sum(dist[i:j]))
for i in range(5):
    for j in range(5):
        print(ans[i][j], end=" ")
    print()
#
# print(ans)