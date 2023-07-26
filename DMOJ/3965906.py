N, P = list(map(int, input().split()))
Names = []
Score = {}
Ranks = []
for i in range(N):
    Ranks.append(i + 3)

for i in range(N):
    user = input()
    Names.append(user)
    Score[user] = 0
for i in range(P):
    line = list(map(int, input().split()))
    for j in range(N):
        Score[Names[j]] += line[j]
# print(Ranks)
# print(Names)
# print(Score)
Sorted_Score = list(sorted(Score.items(), key=lambda item: item[1], reverse=True))
# print(Sorted_Score)
for i in range(N):
    print(str(Ranks[i]) + '. ' + Sorted_Score[i][0])