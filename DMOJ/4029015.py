N, A, B = list(map(int, input().split()))
sum = A + B
whole = N % 2
multi = N // 2


print(multi * sum + whole * A)