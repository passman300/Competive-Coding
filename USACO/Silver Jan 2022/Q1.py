import sys

input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    A, B = map(int, input().strip().split())
    if A == B:
        print(0)
    elif A > B:
        ans = 0

        while A > B:
            if A == B:
                break
            if A % 2 == 0:
                A /= 2
                ans += 1
            else:
                A += 1
                ans += 1
        ans += abs(A - B)
        print(int(ans))
    else:
        temp = A
        A = B
        B = temp
        ans = 0

        while A > B:
            # print(A, B)
            if A == B:
                break
            if A % 2 == 0 and A / 2 > B:
                A /= 2
                ans += 1
            else:
                A -= 1
                ans += 1

        ans += abs(A - B)
        print(int(ans))

#just for partical
