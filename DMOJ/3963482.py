P = int(input())
x_cords_list = [0 for i in range(P)]
y_cords_list = [0 for i in range(P)]

real_cords = [(0, 0)]

for i in range(1, P):
    index, x, y = list(map(int, input().split()))
    index -= 1
    x_cords_list[i] = x_cords_list[index] + x
    y_cords_list[i] = y_cords_list[index] + y
    xy = x_cords_list[i], y_cords_list[i]
    if xy not in real_cords:
        real_cords.append(xy)
# print(x_cords_list)
# print(y_cords_list)
# print(real_cords)
print(len(real_cords))