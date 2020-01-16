#!/usr/bin/python
import time
import arrow
utc = arrow.utcnow()
print(f"UTC time is = {utc}")
pacific = utc.to('US/Pacific')
print(f"Pacific time is = {pacific}")
birth_date = arrow.get('You were born in February 21, 1990', 'MMMM D, YYYY')
print(f"Your birth date is {birth_date}")
print(f"You were born {birth_date.humanize()}")
