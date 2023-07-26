num_l = 0
num_m = 0
num_s = 0

bookself = input()

for i in range(len(bookself)):
    if bookself[i] == "L":
        num_l += 1
    elif bookself[i] == "M":
        num_m += 1
    else:
        num_s += 1


non_l_in_l = 0
non_m_in_m = 0

for i in range(num_l, num_m + num_l):
    if bookself[i] != "M":
        non_m_in_m += 1
#num of Ms in Ls

for i in range(num_l):
    if bookself[i] != "L":
        non_l_in_l += 1


num_l_in_m = 0
num_m_in_l = 0
#num of Ls in Ms
for i in range(num_l, num_m + num_l):
    if bookself[i] == "L":
        num_l_in_m += 1
#num of Ms in Ls
for i in range(num_l):
    if bookself[i] == "M":
        num_m_in_l += 1


print(non_m_in_m + non_l_in_l - min(num_m_in_l, num_l_in_m))