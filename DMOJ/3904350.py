T = int(input())

for i in range(T):
    n, k = input().split(" ")
    n = int(n)
    k = int(k)
    if n % k == 0:
        print(n//k)
    elif n % k != 0:
        print(n//k + 1)
    else:
        print(1)