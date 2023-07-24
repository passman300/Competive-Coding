N, Q = input().split(" ")
items = input().split()
items.sort(reverse=True)


def maxitems(items, amount_items):
    max = 0
    for i in range(amount_items):
        if int(items[i]) > 0:
            max += int(items[i])
    return max

for i in range(int(Q)):
    amount_items = int(input())
    print(maxitems(items, amount_items))

