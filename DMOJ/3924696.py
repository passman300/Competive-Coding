for m in range(5):
    numCards = int(input())
    ranks = list(map(int, input().split(" ")))

    Indexes = [ ]
    rest = True
    for i in range(len(ranks) - 1, -1, -1):
        if ranks[ i ] < 0 or ranks[ i ] > len(Indexes):
            print("IMPOSSIBLE")
            rest = False
            break
        Indexes.insert(len(Indexes) - ranks[ i ], i)

    if rest:
        cards = [ 0 for i in range(numCards) ]

        for i in range(len(Indexes)):
            cards[ Indexes[ i ] ] = i + 1
        head = True
        for c in cards:
            print(c, end=" ")
        print("")