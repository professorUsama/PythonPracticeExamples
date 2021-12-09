import datetime

# string_date = '21 june, 2018'
# print(f"String Date: {string_date}")

# obj_date = datetime.datetime.strptime(string_date,'%d %B, %Y')
# print(f"Oject date: {obj_date}")

current_time = datetime.datetime.now()
time = current_time.astimezone().strftime('%H:%M:%S %z') # print the time with time zone
print(current_time)
print(time)