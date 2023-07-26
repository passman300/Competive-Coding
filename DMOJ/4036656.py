N, T = list(map(int, input().split()))
cards = {}
cards_list = []
for i in range(N):
    s, c = input().split()
    cards_list.append(s)
    cards[s] = int(c)
final = []
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if cards[cards_list[i]] + cards[cards_list[j]] + cards[cards_list[k]] <= T:
                ans = []
                ans.append(cards_list[i])
                ans.append(cards_list[j])
                ans.append(cards_list[k])
                ans.sort()
                final.append(ans)
final.sort()
for i in range(len(final)):
    for j in range(len(final[i])):
        print(final[i][j], end=" ")
    print()