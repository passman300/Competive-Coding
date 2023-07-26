n = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = {}

for i in range(len(nums)):
    if nums[i] not in count:
        count[nums[i]] = 1
    else:
        count[nums[i]] += 1
# print(max(count.values()))
ans = (sorted(count.items(), key=lambda x: x[1], reverse=True))
# print(ans)
print(ans[0][0])