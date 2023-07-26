n = int(input())
line = input().split()
line2 = input().split()
ans = True
for i in range(n):
    if line[i] != line2[i]:
        if line2.index(line[i]) == line.index(line2[i]):
            continue
        else:
            ans = False
            break
    else:
        ans = False
        break


if ans:
    print("good")
else: print("bad")