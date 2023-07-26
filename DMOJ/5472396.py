import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, s = map(int, input().split())
    d = int(((n*(n+1)) // 2)) - s
    print(min(n, d-1) - ((d//2)+1) + 1)