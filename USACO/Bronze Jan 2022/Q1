import sys

input = sys.stdin.readline


G = 0
Y = 0

amount = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
          "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

grid = []
for i in range(3):
    line = input().strip()
    grid.append(line)
    for j in range(3):
        amount[line[j]] += 1

guess = []
for i in range(3):
    guess.append(input().strip())

for i in range(3):
    for j in range(3):
        if grid[i][j] == guess[i][j]:
            G += 1
            amount[grid[i][j]] -= 1

for i in range(3):
    for j in range(3):
        if grid[i][j] != guess[i][j] and amount[guess[i][j]] > 0:
            Y += 1
            amount[guess[i][j]] -= 1

print(G)
print(Y)
