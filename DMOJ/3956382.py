N, K = list(map(int, input().split()))
paper = 1
counter = 0
# before stack
while paper < K and paper < N:
    paper += paper
    counter += 1
# after stack
# dividing the N, by the stack
counter += (N - paper + K - 1) // K

print(counter)