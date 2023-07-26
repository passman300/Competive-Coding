num_input = int(input())
counter = 0
largestbid = 0
largestname = ''


while counter < num_input:
    name = input()
    bid = int(input())
    if bid > largestbid:
        largestbid = bid
        largestname = name
    counter +=1

print(largestname)