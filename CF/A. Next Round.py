n, k = input().split(' ')
n = int(n)
k = int(k)
counter = 0

Answerslist = input().split(' ')
Totalpassed = 0

if sorted(Answerslist) == Answerslist:
    if int(Answerslist[0]) > 0:
        Totalpassed = n


else:
    for i in range(0, k):
        if Answerslist[i] == Answerslist[i+1]:
            Totalpassed += 2
        else:
            Totalpassed += 1






print(Totalpassed)

# 5 1
# 1 1 1 1 1