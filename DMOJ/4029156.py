import sys
n = int(input())
tree_keys = {}
heights = []
for i in range(n):
    x, y = list(map(int, input().split()))
    tree_keys[x] = y
    heights.append(x)
years = 0
ans = -1
# print(heights)
# print(list(tree_keys.keys()))

if len(set(heights)) != n:
    print(0)
    flag = False
    sys.exit()

flag = True
while years < 10000 and flag:
    years += 1
    for i in range(len(heights)):
        heights[i] += tree_keys[list(tree_keys.keys())[i]]
    for i in range(len(heights)):
        if heights.count(heights[i]) > 1:
            ans = years
            flag = False
            break

print(ans)