from _collections import deque
M, N, K = list(map(int, input().split()))
line = list(map(int, input().split()))

heights = deque(sorted(line))
total = 0
while K > 1:
  K -= 1
  i = 1
  h = heights.pop()
  while i < M and K > 0:
    h += 1
    total += h - heights.popleft()
    i += 1
    K -= 1

print(total)