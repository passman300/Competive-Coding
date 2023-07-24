N, Q = map(int, input().split())
nums = list(map(int, input().split()))

PMA = [1]

for i in range(N):
    PMA.append(PMA[-1] * nums[i])
print(nums)
print(PMA)
for _ in range(Q):
    l, r, product = map(int, input().split())
    sub = nums[l-1:r]
    flag = False
    for i in range(len(sub)):
        if flag: break
        for j in range(i, len(sub)):
            if sub[i] * sub[j] == product:
                print(sub[i], sub[j])
                flag = True
                print('Yes')
                break
    if flag == False:
        print('No')