num = int(input())
words = []
for _ in range(num):
    x = input()
    words.append(x)

pwrd = ""
for i in range(len(words)):
    if words[i][::-1] in words or words[i] == words[i][::-1]:
        pwrd = words[i][::-1]
        # print(pwrd)
        break


mid = len(pwrd) // 2

print(len(pwrd), pwrd[mid])