for i in range(10):
    n = int(input())
    train = input().split(" ")
    train.remove("")
    train = [int(i) for i in train]
    count = 0
    for i in range(n - 1, 0, - 1):
        if train.index(i) > train.index(i + 1):
            count += train.index(i)
            train.remove(i)
            train.insert(0, i)
        # print(train)
    print(count)