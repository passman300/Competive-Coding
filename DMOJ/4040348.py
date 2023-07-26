import sys

n = int(input())
boxes = [sorted(list(map(int, input().split()))) for i in range(n)]
# print(boxes)
m = int(input())
packages = [sorted(list(map(int, input().split()))) for i in range(m)]
for package in packages:
    volume = sys.maxsize
    changed = False
    for box in boxes:
        if all(box[i] >= package[i] for i in range(3)):
            temp_volume = box[0] * box[1] * box[2]
            if temp_volume < volume:
                changed = True
                volume = temp_volume
    if changed:
        print(volume)
    else:
        print("Item does not fit.")