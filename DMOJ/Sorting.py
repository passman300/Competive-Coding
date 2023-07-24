N = int(input())
Nums = []

for i in range(N):
    Nums.append(int(input()))
Nums.sort()
for i in range(N):
    print(Nums[i])