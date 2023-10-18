import datetime

date = datetime.date(2023, 10, 17)

today = datetime.date.today()
# print(date.weekday())
# print(date.day)

#---------- timedelta ----------
# In Python, timedelta is a class within the datetime module that represents a duration of time. 
# It allows you to perform arithmetic with dates and times, such as addition or subtraction of time 
# intervals. timedelta objects are often used for tasks like calculating the difference between two 
# dates or adding/subtracting a specific time duration to a given date or time.
# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)
bday = datetime.date(2000, 7, 14)
# print(today - bday)

#------------time-----------
time = datetime.time()

#-----------date------
date = datetime.date(23, 2, 12).today()

#------pytz-------
import pytz

date = datetime.datetime.now(tz=pytz.UTC)
print(date)

# as_timezone = date.astimezone(tz=pytz.timezone())

# for tz in pytz.all_timezones:
#     print(tz)

# print(date.strftime()) datetime to str

dt_str = "July 26, 1967"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y") # str to datetime
print(dt)
