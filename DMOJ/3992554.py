import statistics

N = int(input()) # taking n

factory = list(map(int, input().split()))
pref = list(map(int, input().split()))

real = []

for i in range(N):
    real.append(factory[i] - pref[i])

mode = statistics.mode(real)
print(real.count(mode))