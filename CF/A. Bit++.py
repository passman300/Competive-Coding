NumofCases = int(input())
counter = 0
X = 0

while counter < NumofCases:
    Operation = str(input())
    if '+' in Operation:
        X+=1
    elif '-' in Operation:
        X-=1
    counter += 1
print(X)