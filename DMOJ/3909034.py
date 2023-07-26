input()
number = input().split(" ")
number = [int(i) for i in number]
even = 0
odd = 0
for i in range(len(number)):
    if number[i] % 2 == 0:
        even += 1
    else: odd += 1

while odd > even:
    odd -= 2
    even += 1
if even > (odd + 1):
    even = odd + 1

print(odd + even)