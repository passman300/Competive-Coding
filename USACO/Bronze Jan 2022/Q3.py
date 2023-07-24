import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    cows = list(map(int, input().strip().split()))
    # print(cows)
    ans = -1

    minn = 0
    maxx = min(cows)
    # print(minn, maxx)
    # if N == 1 or (N == 2 and cows[0] == cows[1]):
    #     ans = 0
    #     print(minn, maxx)
    if N == 1:
        ans = 0
    elif N == 2:
        if cows[0] == cows[1]:
            ans = 0
    else:
        while minn <= maxx:
            temp_farm = cows.copy()
            cnt = 0

            mid = (maxx + minn) // 2
            for i in range(N - 1):
                diff = min(temp_farm[i] - mid, temp_farm[i + 1] - mid)
                cnt += diff * 2
                temp_farm[i] -= diff
                temp_farm[i + 1] -= diff

            flag = True
            for i in range(N - 1):
                if temp_farm[i] != mid:
                    flag = False
                    break

            # if flag and ans == -1:
            #     ans = cnt
            if flag:
                if ans == -1:
                    ans = cnt
                else:
                    ans = min(ans, cnt)
                minn = mid + 1
            else: maxx = mid - 1
            # print(cnt)
    print(ans)
