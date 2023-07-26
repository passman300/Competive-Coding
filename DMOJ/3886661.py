inputline = input().split(" ")
n = int(inputline[0])
k = int(inputline[1])
letters = []


for i in range(n):
    letters.append(input())


for i in range(k + 2):
    print("#", end="")
print("")
for i in range(n):
    print("#" + letters[i] + "#")

for i in range(k + 2):
    print("#", end="")