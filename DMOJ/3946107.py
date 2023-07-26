import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

X, Y, Z = list(map(int, input().split()))

output = "NO"
for i in range(1, lcm(X, Y)):
    if X*i % Y == Z:
        output = "YES"
        break
print(output)