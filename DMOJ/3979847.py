n, k = list(map(int, input().split()))

first = {}
second = {}

for i in range(n):
    x, y = list(map(int, input().split()))
    first[i + 1] = (x)
    second[i + 1] = (y)

first = dict(sorted(first.items(), key=lambda item: item[1], reverse=True))
second = dict(sorted(second.items(), key=lambda item: item[1], reverse=True))

top3_first = d = dict(list(first.items())[:k])
#
# print(top3_first)

max_value = 0
max_key = 0
for key in top3_first.keys():
    if second[key] > max_value:
        max_value = second[key]
        max_key = key
print(max_key)