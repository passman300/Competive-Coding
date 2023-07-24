N, L, S = map(int, input().split())
Houses = [0 for i in range(L)]

count = 0
for i in range(N):
    a, b, s = map(int, input().split())
    for j in range(a - 1, b):
        Houses[j] += s
for i in range(L):
    if Houses[i] < S:
        count += 1

# print(Houses)
# print(len(Houses))
print(count)