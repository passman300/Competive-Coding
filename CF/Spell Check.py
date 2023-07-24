import sys

# input = sys.stdin.readline
#Timur

def check(s, name):
    if len(s) != 5:
        return False
    temp = set()
    for i in range(len(s)):
        temp.add(s[i])
    if temp == name:
        return True
    else: return False

name = {'T', 'i', 'm', 'u', 'r'}
# test = {'T', 'm', 'i', 'u', 'r'}
# if name == test:
#     print('TES')
T = int(input())
for qwert in range(T):
    n = int(input())
    s = input()

    flag = check(s, name)
    if flag: print('YES')
    else: print('NO')
