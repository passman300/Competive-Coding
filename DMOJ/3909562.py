import sys

H, M, S = input().split(":")
H = int(H)
M = int(M)
S = int(S)

nums = input()

T = S + 60 * M + 3600 * H

working = [ False for i in range(10) ]

for i in range(len(nums)):
    working[ int(nums[ i ]) ] = True

best_H = 0
best_M = 0
best_S = 0
best_T = sys.maxsize
for i in range(0, 100):
    for j in range(0, 100):
        for k in range(0, 100):
            if working[i // 10] and working[i - (i // 10 * 10)] \
                    and working[j // 10] and working[j - (j // 10 * 10)] \
                    and working[k // 10] and working[k - (k // 10 * 10)]:
                if abs((i * 3600 + j * 60 + k) - T) < best_T:
                    best_H = i
                    best_M = j
                    best_S = k
                    best_T = abs((i * 3600 + j * 60 + k) - T)

placement_best_H = ''
placement_best_M = ''
placement_best_S = ''
if best_H <= 9: placement_best_H = '0'
if best_M <= 9: placement_best_M = '0'
if best_S <= 9: placement_best_S = '0'

print(placement_best_H + str(best_H) + ":" + placement_best_M + str(best_M) + ":" + placement_best_S + str(best_S))