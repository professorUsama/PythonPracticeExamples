from datetime import datetime, timedelta
import datetime

current_time = datetime.now()

print(f"Current Date & Time: {str(current_time)}")

# calculating future date and time for next two years
future_date_next_two_year = current_time + timedelta(days=730)
future_date_next_two_days = current_time + timedelta(days=25)
future_date = datetime.datetime.strftime('')
print(f"Future Date for next two year: {future_date_next_two_year}")
print(f"Future Date for next two days: {future_date_next_two_days}")