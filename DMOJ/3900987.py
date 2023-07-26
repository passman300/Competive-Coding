import sys
max = -sys.maxsize - 1

n = int(input())

for i in range(n):
    sum = 0
    num = input()
    for ele in num: sum += int(ele)
    if sum > max: max = sum

print(max)