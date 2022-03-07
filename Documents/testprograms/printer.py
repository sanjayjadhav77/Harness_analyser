import time, pprint, cups
import os 
import subprocess
conn = cups.Connection()
printers = conn.getPrinters ()
pprint.pprint(printers)
printer = conn.getDefault()
print("Default1:", printer)
     
if printer == None:
    printer = list(printers.keys())[1]
    print("Default2:", printer)
     
    myfile ="/home/pi/Desktop/HCCPL.prn"
    pid = conn.printFile(printer, myfile, "test", {})
    status=subprocess.getoutput("lpstat -t")
    # print(status)
    string="Waiting for printer to become available."
    if(string in status):
        print("printer not available")
    else:    
        print("label printed sucessfully")
else:
    print("printer not available")


##status=os.system("lpstat -t")

