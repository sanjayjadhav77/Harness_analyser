import time, pprint, cups
import os
from datetime import date, timedelta, datetime
conn = cups.Connection()
printers = conn.getPrinters ()
pprint.pprint(printers)
printer = conn.getDefault()
print("Default1:", printer)
     
if printer == None:
    printer = list(printers.keys())[0]
    print("Default2:", printer)
     
myfile ="/home/pi/Desktop/Akash/garbage/test.lbl"
pid = conn.printFile(printer, myfile, "test", {})
print("label printed sucessfully")


time.sleep(5)


howmanydaysago=-1
today=date.today()
daysago=today-timedelta(days=howmanydaysago)
epoch_today=time.mktime(today.timetuple())
##print("epoch_today",epoch_today,daysago)
epoch_daysago=time.mktime(daysago.timetuple())
date_difference=epoch_today-epoch_daysago
for line in os.popen('/usr/bin/lpstat -o').readlines():
    
    data = line.strip().split()
##    print("data",data)
    job=data[0].split('-')
##    print("job",job)
    #15 Apr 2008 12:00:00
    month = data[5].split(data[5][3])
    date_time=data[4]+"-"+month[0]+"-"+data[6]+"."+"12:49:00"
##    print("date_time",date_time)
    pattern = '%d-%b-%Y.%H:%M:%S'
    epoch_job = int(time.mktime(time.strptime(date_time, pattern)))
    difference=epoch_today - epoch_job
##    print("difference",difference,date_difference)
##    print("epoch_job",epoch_job)
    if difference > date_difference:
        print ("Canceling pending job: "+str(job[-1]))
        os.popen('/usr/bin/cancel '+str(job[-1]))

