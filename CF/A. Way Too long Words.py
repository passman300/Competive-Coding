Numwords = int(input())

counter = 0


while counter < Numwords:
    word = str(input())
    if len(word) > 10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)
    counter += 1