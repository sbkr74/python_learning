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

# String to Time Using strptime
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

#------------------------------------------------------------------
# Using date
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05

# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5

# Difference between date and datetime
today = date(year=2024, month=12, day=5)
new_year = date(year=2025, month=1, day=1)
days_left_for_newyear = new_year - today

print("Time left for new year: ",days_left_for_newyear)

t1 = datetime(year=2024, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2025, month=1, day=1, hour=0, minute=0, second=0)
diff = t2-t1
print('Time left for new year:',diff)

# Using time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

# Difference using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)