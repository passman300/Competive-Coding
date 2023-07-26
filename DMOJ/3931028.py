n = int(input())
elements = []

for _ in range(n):
    num = int(input())
    if num not in elements:
        elements.append(num)
print(len(elements))