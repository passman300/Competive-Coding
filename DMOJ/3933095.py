S = int(input())
phone_book_counter = {}
phone_book_names = {}

for _ in range(S):
    name, number = input().split()
    phone_book_names[number] = name
    phone_book_counter[number] = 0

T = int(input())
for _ in range(T):
    num = input()
    phone_book_counter[num] += 1

max = 0
prev_len = 0



for number, count in phone_book_counter.items():
    number = int(number)
    count = int(count)
    if count > max:
        max = count
        prev_len = number
    if count >= max:
        if number < prev_len:

            max = count
            prev_len = number


print(phone_book_names[str(prev_len)])