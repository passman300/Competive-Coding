key = input()
text = input()
i = 0
for j in range(len(text)):
    if "A" <= text[j] <= "Z":
        l = ord(text[j]) + (ord(key[i]) - ord("A"))
        if l > ord("Z"):
            l = ord("A") + (l - ord("Z") - 1)
        print(chr(l), end="")
        i += 1
        if i > len(key)-1:
            i = 0