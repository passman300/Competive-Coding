input()

numbers = input().split(" ")
numbers = [int(i) for i in numbers]
Duke = 0
Alice = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:

        Duke += numbers[i] // 2
    else:
        Alice += (numbers[i] + 1) // 2

if Duke > Alice:
    print("Duke")
else: print("Alice")