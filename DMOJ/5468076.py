n = int(input())
s = []
s = list(input()[0::])
pair = []
for i in range(0, len(s), 2):
    if s[i] != s[i + 1]:
        if s[i] == 'G' and s[i + 1] == 'H':
            pair.append(1)
        else:
            pair.append(0)

cnt = 1
for i in range(1, len(pair)):
    if pair[i] != pair[i - 1]:
        cnt += 1

if len(pair) > 0 and pair[-1] == 0:
    cnt -= 1

print(cnt)