s = input()
t = input()

count = len(s)
if s == t:
    print(0)
else:
    if len(s) < len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                count = i
                break
    else:
        if len(s) >= len(t):
            for i in range(len(t)):
                if s[i] != t[i]:
                    count = i
                    break

    print(abs(len(s) + len(t) - 2*count))