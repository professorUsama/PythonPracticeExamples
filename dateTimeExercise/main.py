import calendar
import datetime

# Global variables
current_time = datetime.datetime.now()

if __name__ == '__main__':
    print(f"press 1 for find future date time and day\n"
          "press 2 for find past date time and day")
    try:
        user_choice = int(input("Enter choice: "))
        days = int(input("Enter the number of days: "))
        if user_choice == 1:
            t = current_time + datetime.timedelta(days)
            print(f"Future time given below...\n")
        else:
            t = current_time - datetime.timedelta(days)
        date = int(t.strftime('%d'))
        month = int(t.strftime('%m'))
        year = int(t.strftime('%Y'))
        day_name = calendar.day_name[calendar.weekday(year, month, date)]
        time = t.strftime('%I:%M:%S %p')
        d = t.strftime('%m/%d/%Y')
        print(f"Time: {time}\nDate: {d}\nDay: {day_name} at {d}")
    except ValueError as e:
        print(f"Please enter valid choice {e}")
