w, l = int(input()), int(input())
cut_w, cut_l = int(input()), int(input())
steps = int(input())

board = [[False for _ in range(w)] for i in range(l)]

# top left
for i in range(cut_l):
    for j in range(cut_w):
        board[i][j] = True

# bottom left
for i in range(1, cut_l + 1):
    for j in range(cut_w):
        board[-i][j] = True

# top right
for i in range(cut_l):
    for j in range(1, cut_w + 1):
        board[i][-j] = True

# bottom left
for i in range(1, cut_l + 1):
    for j in range(1, cut_w + 1):
        board[-i][-j] = True

# boarder
board.insert(0, [True for i in range(w)])
board.insert(len(board) + 1, [True for i in range(w)])

for i in range(len(board)):
    board[i].insert(0, True)
    board[i].insert(len(board[i]) + 1, True)

place_w = cut_w + 1
place_y = 1
direction = "E"

for i in range(steps):
    blocked = False
    board[place_y][place_w] = True
    if direction == "E":
        # left
        if not board[place_y - 1][place_w]:
            place_y -= 1
            direction = "N"
        # forwards
        elif not board[place_y][place_w + 1]:
            place_w += 1
            direction = "E"
        # right
        elif not board[place_y + 1][place_w]:
            place_y += 1
            direction = "S"
        else:
            blocked = True

    elif direction == "S":
        # left
        if not board[place_y][place_w + 1]:
            place_w += 1
            direction = "E"
        # forwards
        elif not board[place_y + 1][place_w]:
            place_y += 1
            direction = "S"
        # right
        elif not board[place_y][place_w - 1]:
            place_w -= 1
            direction = "W"
        else:
            blocked = True

    elif direction == "W":
        # left
        if not board[place_y + 1][place_w]:
            place_y += 1
            direction = "S"
        # forwards
        elif not board[place_y][place_w - 1]:
            place_w -= 1
            direction = "W"
        # right
        elif not board[place_y - 1][place_w]:
            place_y -= 1
            direction = "N"
            # print("pass")
        else:
            blocked = True

    elif direction == "N":
        # left
        if not board[place_y][place_w - 1]:
            place_w -= 1
            direction = "W"
        # forwards
        elif not board[place_y - 1][place_w]:
            place_y -= 1
            direction = "N"
        # right
        elif not board[place_y][place_w + 1]:
            place_w += 1
            direction = "E"
        else:
            blocked = True
    # board[ place_y ][ place_w ] = "(HERE)"
    # for j in board:
    #     for k in j:
    #         print(k, end="\t")
    #     print()
    #
    # print('-----------', i, direction)
    if blocked:
        break

print(place_w)
print(place_y)