import random
import math
import datetime
import calendar
import os

courses = ['history', 'geo', 'math']
rad = math.radians(90)
print(rad)

print(random.choice(courses))

date = datetime.date.today()
print(date)

print(calendar.isleap(2017))

print(os.__file__)