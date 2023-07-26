import datetime

hours = int(input())

hours = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=hours, weeks=0)

date, time = input().split()

date = date.split("/")
for i in range(len(date)): date[i] = int(date[i])

time = time.split(":")
for i in range(len(time)): time[i] = int(time[i])

today = datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[2])

past = today - hours

str_output = (str(past)).replace("-", "/")

print(str_output)