Numquestions = int(input())

counter = 0
Anwseredquestions = 0
while counter < Numquestions:
    question = (input().split(' '))
    Ones = 0
    Zeros = 0
    for i in range(0, len(question)):
        if question[i] == '0':
            Zeros += 1
        elif question[i] == '1':
            Ones += 1
    if Ones > Zeros:
        Anwseredquestions += 1
    counter +=1

print(Anwseredquestions)