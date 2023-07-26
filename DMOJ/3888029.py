'''
• If their sum is odd, then the direction to turn is left.
• If their sum is even and not zero, then the direction to turn is right.
• If their sum is zero, then the direction to turn is the same as the previous instruction.
'''

intnumber = (input())
numberlist = []
for i in intnumber:
    numberlist.append(i)
direction = ''


while intnumber != '99999':
    last3 = ''
    if (int(numberlist[0]) + int(numberlist[1])) % 2 != 0:
        direction = 'left'
    elif (int(numberlist[0]) + int(numberlist[1])) % 2 == 0 and (int(numberlist[0]) + int(numberlist[1])) != 0:
        direction = 'right'
    for i in (numberlist[2:]):
        last3 = last3 + i
    print(direction, last3)


    intnumber = (input())
    numberlist = [ ]
    for i in intnumber:
        numberlist.append(i)