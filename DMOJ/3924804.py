full_info = [0 for i in range(1000000)]

for i in range(len(full_info)):
    full_info[i] = i + 1

n = int(input())
t = list(map(int, input().split(" ")))
k = t[0]
l = True
for i in range(n):
    if t[i] != k:
        l = False
        break

if not l:
    for i in range(n):
        if t[i] == full_info[i]:
            index = 0
            while t[i] == full_info[index] or t[index] == full_info[i]:
                index += 1
            temp = full_info[i]
            full_info[i] = full_info[index]
            full_info[index] = temp
    for i in range(n):
        print(full_info[i], end=" ")
else:
    print(-1)