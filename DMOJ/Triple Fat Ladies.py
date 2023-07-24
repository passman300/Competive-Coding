N = int(input())
# lineNums = list(map(int, input().split()))
for i in range(N):
    Num = int(input())
    if Num < 1000:
        if Num < 192:
            print(192)
            # print(192, end=" ")
        elif Num < 442:
            print(442)
            # print(442, end=" ")
        elif Num < 692:
            print(692)
            # print(692, end=" ")
        elif Num < 942:
            print(942)
            # print(942, end=" ")
    elif 943 < Num < 1000:
        # print(1192, end=" ")
        print(1192)
    else:
        firstDigit = int(str(Num)[ :-3 ])
        lastDigit = int(str(Num)[ -3: ])
        # print(firstDigit)
        if lastDigit < 192:
            print(str(firstDigit) + str(192))
            # print(str(firstDigit) + str(192), end=" ")
        elif lastDigit < 442:
            print(str(firstDigit) + str(442))
            # print(str(firstDigit) + str(442), end=" ")
        elif lastDigit < 692:
            print(str(firstDigit) + str(692))
            # print(str(firstDigit) + str(692), end=" ")
        elif lastDigit < 942:
            print(str(firstDigit) + str(942))
            # print(str(firstDigit) + str(942), end=" ")

# Num = int(input())
# if Num < 1000:
#     if Num < 192:
#         print(192, end="")
#     elif Num < 442:
#         print(442, end="")
#     elif Num < 692:
#         print(692, end="")
#     elif Num < 942:
#         print(942, end="")
# elif 943 < Num < 1000:
#     print(1192, end="")
# else:
#     firstDigit = int(str(Num)[ :-3 ])
#     lastDigit = int(str(Num)[ -3: ])
#     # print(firstDigit)
#     if lastDigit < 192:
#         print(str(firstDigit) + str(192), end="")
#     elif lastDigit < 442:
#         print(str(firstDigit) + str(442), end="")
#     elif lastDigit < 692:
#         print(str(firstDigit) + str(692), end="")
#     elif lastDigit < 942:
#         print(str(firstDigit) + str(942), end="")
