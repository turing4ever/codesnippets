#!python3

from datetime import datetime, timedelta
from datetime import date

today = datetime.today()


print(today, type(today))

todaydate = date.today()

print(todaydate, type(todaydate))
#<class 'datetime.date'>

print(todaydate.month, todaydate.year, todaydate.day)

christmas = date(2018, 12, 25)

if christmas is not todaydate:
    print(f"Sorry there are still {(christmas - todaydate).days} until Christmas!")
else:
    print("Yay it's Christmas!")

eta = timedelta(days=1, hours=3, minutes=39)
print(eta.days, eta.total_seconds())

