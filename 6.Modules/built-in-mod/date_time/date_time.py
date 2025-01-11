from datetime import datetime

# Date Information
now = datetime.now()
print(now)          # 2025-01-11 23:00:39.717741

day = now.day                   # 11
month = now.month               # 01
year = now.year                 # 2025
hour = now.hour                 # 23
minute = now.minute             # 00
second = now.second             # 39
timestamp = now.timestamp()
print(day, month, year, hour, minute)            # 11 1 2025 23 0
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 11/1/2025, 23:0

# formatting Date output Using strftime
from datetime import datetime
new_year = datetime(2025, 1, 1)
print(new_year)      # 2025-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)            #1 1 2025 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2025, 0:0
#------------------------------------------------------------------
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)