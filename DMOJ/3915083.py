for i in range(5):
    M = int(input())
    perfect_sum = 0
    real_sum = 0
    for j in range(1, M + 2):
        perfect_sum += j
    for j in range(M):
        real_sum += int(input())
    print(perfect_sum - real_sum)