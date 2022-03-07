import datetime
import time
##from datetime import datetime, timedelta

date_time=datetime.datetime.now()   
print(date_time)
Hrs_Min=date_time.strftime("%H:%M:%S")
print(Hrs_Min)
date=date_time.strftime("%d/%m/%Y")
print('date',date)
##mon=date_time.strftime("%m")
##print('mon',mon)
##year=date_time.strfti me("%Y")
##print(year)

week_no=date_time.strftime("%W")
# print('week_no',week_no)
week_day=date_time.strftime("%w")
# print('week_day',week_day)

##a=date_time.date().strftime("%W")
##print(a)
