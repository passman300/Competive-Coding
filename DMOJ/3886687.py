string = input()
test = string[::-1]
a = string.index("A")
z = len(string) - test.index("Z")

print(z - a)