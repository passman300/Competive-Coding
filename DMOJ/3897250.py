n = int(input())
rivers = []

def split(list1, index, percent):
    index = index - 1
    left = round(list1[index] * percent/100)
    right = list1[index] - left
    list1[index] = left
    list1.insert(index + 1, right)
    return list1

def join(list1, index):
    index = index - 1
    list1[index] = list1[index] + list1[index + 1]
    del list1[index + 1]
    return list1

def printlist(list1):
    for ele in list1:
        print(ele, end=" ")
for i in range(n):
    rivers.append(int(input()))

num = int(input())
while num != 77:
    if num == 99:
        index = int(input())
        percent = int(input())
        rivers = split(rivers, index, percent)
        # print(rivers)
    elif num == 88:
        index = int(input())
        rivers = join(rivers, index)
        # print(rivers)
    num = int(input())

printlist(rivers)