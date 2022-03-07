import serial
import time
import global_test_var as GV
import datetime
from datetime import datetime
from weekno import*


#'/dev/ttyAMA0'
#'/dev/ttyUSB0'
def Serial_Init():
    try:
        GV.serialobj=serial.Serial('/dev/ttyAMA0', baudrate=9600, bytesize=8, parity='N', stopbits=1,timeout=0.009,xonxoff=0)
    except(IOError, ValueError, TypeError):
        print("serial comm error")

    
##def serial_receive():
##    global serial_data
##    global ser
##    while True:
##            GV.serial_data=GV.serialobj.read()
##            print(type(serial_data),serial_data)


       
def send():
        global ser
        hi="WELCOME TO DCTGEN2.0"
        GV.serialobj.write(hi.encode())

def filehandle(path):
    try:
        f=open(path,"rb")
        x=f.read()
        print("lable data......................")
        #x=bytes(GV.Local_Label_Data,'utf-8')
        GV.Local_Label_Data=x
        print(GV.Local_Label_Data)
        #print(GV.Local_Label_Data[3])
    except (IOError,ValueError,EOFError):
        print("file openning error")


    
		
		
def Serial_Printing():
  
    GV.code_1=str(GV.code_1)
    GV.code_2=str(GV.code_2)
    # GV.DMY=str(GV.DMY)
    currentDate=datetime.now()   
    Hrs_Min=currentDate.strftime("%H:%M")
    GV.mon_yr=currentDate.strftime("%d %b %Y")
    #print(GV.mon_yr)
    day=currentDate.strftime("%A")
    GV.day=currentDate.strftime("%A")
    GV.HMS=currentDate.strftime("%H:%M:%S")
    #print(GV.HMS)
    GV.hrs=currentDate.strftime("%H")
    GV.mint=currentDate.strftime("%M")
    GV.sec=currentDate.strftime("%S")
    GV.DMY=currentDate.strftime("%d/%m/%Y")
    
   
    GV.date=currentDate.strftime("%d")
    GV.mon=currentDate.strftime("%m")
    GV.year=currentDate.strftime("%Y")
    GV.week_no=currentDate.strftime("%W")
    GV.week_day=currentDate.strftime("%w")

    localtime = time.localtime(time.time())
    my_calendar = CustomizedCalendar(start_weekday=WEEKDAY.SUN)
    week_no = my_calendar.calculate(datetime(localtime[0],localtime[1],localtime[2]))[1]
    ##print(my_calendar.calculate(datetime(localtime[0],localtime[1],localtime[2]))[1])    
    #print("week_no",week_no)
    if(week_no<=9):
        GV.week_no = '0'+ str(week_no)
        #print(week_number,"week_number")
    else:
        GV.week_no = str(week_no)

    if(int(GV.Pass_Count)<=9):
        PC='0'+'0'+'0'+'0'+'0'+str(GV.Pass_Count)
    elif(int(GV.Pass_Count)<=99):
        PC='0'+'0'+'0'+'0'+str(GV.Pass_Count)
    elif(int(GV.Pass_Count)<=999):
        PC='0'+'0'+'0'+str(GV.Pass_Count)
    elif(int(GV.Pass_Count)<=9999):
        PC='0'+'0'+str(GV.Pass_Count)    
    elif(int(GV.Pass_Count)<=99999):
        PC='0'+str(GV.Pass_Count)
    elif(int(GV.Pass_Count)<=999999):
        PC=str(GV.Pass_Count)
    else:
        PC=GV.Pass_Count
    #daycount-------------------------------------------------------------------------------
    date=GV.DMY
    d = list(map(int,date.split("/")))
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if d[2] % 400 == 0:
        days[2]+=1
    elif d[2]%4 == 0 and d[2]%100!=0:
        days[2]+=1
    for i in range(1,len(days)):
        days[i]+=days[i-1]
    GV.daycount=str(days[d[1]-1]+d[0])
    if(int(GV.daycount) <=  99):
        GV.daycount='0'+GV.daycount
        
    #week day-----------------------------------------------------------------------
    
    if(int(localtime[6]==6)):#for sunday localtime 6=6....so to start week from sunday minus 5 is added
        GV.week_day = (str(localtime[6]-5))
    else:
        GV.week_day = (str(localtime[6]+2)) #from monday localtime 6 = 0 (to 5)so plus 2 is added
        ##print(Week_day,"Week_day")
    #week no-------------------------------------------------------------------------------------------------
    if((GV.HMS>='06:00:00')&(GV.HMS<='13:59:59')): # 06AM to 02PM(shift A)
        GV.shift = 'A'
    elif((GV.HMS>='14:00:00')&(GV.HMS<='21:59:59')): # 02PM to 10PM(shift B)
        GV.shift = 'B'
    elif((GV.HMS>='22:00:00')&(GV.HMS<='23:59:59')): # 10PM to 12AM(shift C)
        GV.shift = 'C'
    elif((GV.HMS>='00:00:00')&(GV.HMS<='05:59:59')): # 12AM to 06AM(shift C)
        GV.shift = 'C'
    else:
        print('no shift')
    
    year=GV.year[2:]
   # print('GV.year',year)
    file_read=" "      
    file_read=GV.Local_Label_Data
    file_read=file_read.replace("@1",(GV.DMY))
    file_read=file_read.replace("@2",(GV.HMS))
    file_read=file_read.replace("@4",(GV.mon))
    file_read=file_read.replace("@5",(year))
    file_read=file_read.replace("@6",str(PC))
    file_read=file_read.replace("@8",(GV.date))
    file_read=file_read.replace("@C",str(GV.code_1))
    file_read=file_read.replace("@B",str(GV.code_2))
    file_read=file_read.replace("@X",(GV.week_day))
    file_read=file_read.replace("@Y",(GV.daycount))
    file_read=file_read.replace("@N",(GV.week_no))
    file_read=file_read.replace("@D",(GV.shift))
    file_read=file_read.replace("@H",(GV.hrs))
    file_read=file_read.replace("@M",(GV.mint))
    file_read=file_read.replace("@S",(GV.sec))
    GV.serialobj.write(file_read.encode())
    # GV.DMY=bytes(GV.DMY,'utf-8')
    # GV.HMS=bytes(GV.HMS,'utf-8')
    # GV.mon=bytes(GV.mon,'utf-8')
    # year=bytes(year,'utf-8')
    # PC=bytes(PC,'utf-8')
    # GV.date=bytes(GV.date,'utf-8')
    # GV.code_1=bytes(GV.code_1,'utf-8')
    # GV.code_2=bytes(GV.code_2,'utf-8')
    # GV.week_day=bytes(GV.week_day,'utf-8')
    # GV.daycount=bytes(GV.daycount,'utf-8')
    # GV.week_no=bytes(GV.week_no,'utf-8')
    # GV.shift=bytes(GV.shift,'utf-8')
    # GV.hrs=bytes(GV.hrs,'utf-8')
    # GV.mint=bytes(GV.mint,'utf-8')
    # GV.sec=bytes(GV.sec,'utf-8')
    # file_read=" "      
    # file_read=GV.Local_Label_Data
    # file_read=file_read.replace(b'@1',bytes(GV.DMY))
    # file_read=file_read.replace(b'@2',bytes(GV.HMS))
    # file_read=file_read.replace(b'@4',bytes(GV.mon))
    # file_read=file_read.replace(b'@5',bytes(year))
    # file_read=file_read.replace(b'@6',bytes(PC))
    # file_read=file_read.replace(b'@8',bytes(GV.date))
    # file_read=file_read.replace(b'@C',bytes(GV.code_1))
    # file_read=file_read.replace(b'@B',bytes(GV.code_2))
    # file_read=file_read.replace(b'@X',bytes(GV.week_day))
    # file_read=file_read.replace(b'@Y',bytes(GV.daycount))
    # file_read=file_read.replace(b'@N',bytes(GV.week_no))
    # file_read=file_read.replace(b'@D',bytes(GV.shift))
    # file_read=file_read.replace(b'@H',bytes(GV.hrs))
    # file_read=file_read.replace(b'@M',bytes(GV.mint))
    # file_read=file_read.replace(b'@S',bytes(GV.sec))
    # GV.serialobj.write(file_read)
    # GV.code_1=str(GV.code_1)
    # GV.code_2=str(GV.code_2)
    # GV.HMS=str(GV.HMS)
    # GV.mon=str(GV.mon)
    # year=str(year)
    # PC=str(PC)
    # GV.date=str(GV.date)
    # GV.week_day=str(GV.week_day)
    # GV.daycount=str(GV.daycount)
    # GV.week_no=str(GV.week_no)
    # GV.shift=str(GV.shift)
    # GV.hrs=str(GV.hrs)
    # GV.mint=str(GV.mint)
    # GV.sec=str(GV.sec)
    # GV.DMY=str(GV.DMY)
    
    # print(file_read)


if __name__ == '__main__':
    Serial_Init()
    filehandle("/home/pi/Desktop/HCCPL.prn")
    #filehandle("/home/pi/Desktop/New.txt")
    
    Serial_Printing()
   
##    send()
