import sys

input = sys.stdin.readline

line1 = input().strip().replace(" ", "")
line2 = input().strip().replace(" ", "")


A = []
A[:0] = line1
B = []
B[:0] = line2

A.sort()
B.sort()

ACount = {}
BCount = {}
# print(A)
# print(B)
ans = 'Is not an anagram.'
if len(A) == len(B):
    for i in range(len(A)):
        if A[i] not in ACount:
            ACount[A[i]] = 1
        else:
            ACount[A[i]] += 1

        if B[i] not in BCount:
            BCount[B[i]] = 1
        else:
            BCount[B[i]] += 1
    if ACount == BCount:
        ans = 'Is an anagram.'

# print(ACount)
# print(BCount)

print(ans)