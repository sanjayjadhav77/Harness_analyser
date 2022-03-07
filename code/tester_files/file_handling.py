import time, pprint, cups
def file_handl():
    read_data= open("/home/pi/Downloads/Harness-lbl.LBL","r")
    file_read=read_data.read()
    read_data.close()
    
    file_read=file_read.replace("@1","abc")
    file_read=file_read.replace("@2","xyz")
    print(file_read)

    conn = cups.Connection()
    printers = conn.getPrinters ()
    pprint.pprint(printers)
 
    printer = conn.getDefault()
    print("Default1:", printer)
     
    if printer == None:
        printer = list(printers.keys())[0]
        print("Default2:", printer)
     
##    myfile = '/home/pi/Desktop/AWHT/DB/1.LBL'
    pid = conn.printFile(printer, file_read, "test", {})
    while conn.getJobs().get(pid, None) is not None:
        time.sleep(1)

file_handl()
