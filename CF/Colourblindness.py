import sys

# input = sys.stdin.readline

'''
Vasya has a grid with 2 rows and n columns.
 He colours each cell red, green, or blue.

Vasya is colourblind and can't distinguish 
green from blue. Determine if Vasya will 
consider the two rows of the grid to be coloured the same.
'''

def check(top, bottom, n):
    for i in range(n):
        if (top[i] == 'R' and bottom[i] != 'R') or (top[i] != 'R' and bottom[i] == 'R'):
            return False
    return True
T = int(input())

for qwer in range(T):
    col = int(input())
    top = input()

    bottom = input()

    if check(top, bottom, col): print("YES")
    else: print("NO")