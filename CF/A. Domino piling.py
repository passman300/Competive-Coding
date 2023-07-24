M, N = input().split(' ')
M = int(M)
N = int(N)
Area = M*N

print(int((Area - (Area%2)) /2))