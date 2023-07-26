t = int(input())
s = int(input())
h = int(input())


conector = 2*s + 3
spaces = conector//2
for m in range(t):
    print("*", end="")
    for j in range(2):
        for i in range(s):
            print(" ", end="")
        print('*', end="")
    print("")
for i in range(conector):
    print("*", end="")
print("")

for i in range(h):
    for j in range(spaces):
        print(' ', end= "")
    print("*")

'''
*   *   *
*   *   *
*   *   *
*   *   *
*********
    *
    *
'''