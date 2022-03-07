import sqlite3
from datetime import datetime
import sys
import xlrd
import xlsxwriter
from xlutils.copy import copy
import global_var
from os.path import isfile, join
import os.path
import global_test_var as GV
sys.path.insert(1, GV.DBpath)


# =============================================================================
# 
# =============================================================================
def sql_connection():##establish connection with database and return class
    try:
        GV.conn  = sqlite3.connect(GV.DBpath)
        print("Connection is established: Database is created in memory")
    except:
        print("error in conn")
    
def sql_Close():## close connection with dbLocal_Cable_Info [(53, 63, 0, 0, 0, 0)]

    GV.conn.close()
# =============================================================================
#  
# =============================================================================
def DownLoadCableId_boot(): ##dowload  data in Hlist Location_No PartName from db
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement ="SELECT max(LastUsed) from tblCable_Id"
    my_database.execute(sql_statement)
    output = my_database.fetchall()
     
    sql_statement = "SELECT Location,PartName from tblCable_Id where LastUsed = '"+output[0][0]+"'"
    my_database.execute(sql_statement)
    hlist = my_database.fetchall()
   # print("output",hlist)
    return(hlist)

def DownLoadCableId_change(Location_No):##update data in Hlist PartName frm db
    conn  = sqlite3.connect(GV.DBpath)
    Location=Location_No
    my_database = conn.cursor()

    try:
      sql_statement= "SELECT PartName from tblCable_Id where Location = "+str(Location)
      my_database.execute(sql_statement)
      hlist = my_database.fetchall()
##      print("DownLoadCableId_change",hlist[0][0])
      return(hlist)
    except:
      print('name not found please insert')

def UpLoadCableId(Location_No,Part_Name):##update Location Part_Name
    print ('Location_No,Part_Name',Location_No,Part_Name)
    Location = Location_No
    PartName = Part_Name
    LastUsed=datetime.now()
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT count(PartName) from tblCable_Id where Location="+str(Location)
    my_database.execute(sql_statement)
    n = my_database.fetchone()[0]
##    print('my_database',n)
    if(n == 0):
        print("check point",Location,PartName,LastUsed)
        my_database.execute('INSERT  into tblCable_Id(Location,PartName,LastUsed) values(?,?,?)',(Location,PartName,LastUsed))
        conn.commit()
    else:    
        my_database.execute('update tblCable_Id set PartName = ?, LastUsed = ? where Location = ?',(PartName,LastUsed,Location))
        conn.commit()
    conn.close()
    
def DownloadCableId_All():##update Location Part_Name
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Location,PartName from tblCable_Id"
    #sql_statement = "SELECT * from tblCable_Id"
    my_database.execute(sql_statement)
    n =my_database.fetchall()
##    print(n)
    return(n)
# =============================================================================
# 
# =============================================================================
def UploadCable_Info(Location_No,x):##upload (CableInfo_Location,PassCount,FailCount,Stage1,Stage1Points,Stage2,Stage2Points) in db
    Local_Cable_Info=x
    # print("X value ",x)
    CableInfo_Location=Location_No;
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT count(CableInfo_Location) from tblCable_Info where CableInfo_Location="+str(CableInfo_Location)
    my_database = conn.execute(sql_statement)
    n = my_database.fetchone()[0]
    #print('n',n)
    if(n == 0):
        my_database.execute('insert into tblCable_Info(CableInfo_Location,PassCount,FailCount,\
                            Stage1,Stage1Points,Stage2,Stage2Points) values(?,?,?,?,?,?,?)\
                            ',(CableInfo_Location,Local_Cable_Info[0][0],Local_Cable_Info[0][1],Local_Cable_Info[0][2],
                               Local_Cable_Info[0][3],Local_Cable_Info[0][4],Local_Cable_Info[0][5]))
    else:    
        my_database.execute('update tblCable_Info set PassCount = ?, FailCount = ?,Stage1 = ?, \
                            Stage1Points = ?,Stage2 = ?, Stage2Points = ? where CableInfo_Location = ?\
                            ',(Local_Cable_Info[0][0],Local_Cable_Info[0][1],Local_Cable_Info[0][2],Local_Cable_Info[0][3]
                               ,Local_Cable_Info[0][4],Local_Cable_Info[0][5],CableInfo_Location))
    conn.commit()
  
def DownloadCable_Info(Location_No):##download (CableInfo_Location,PassCount,FailCount,Stage1,Stage1Points,Stage2,Stage2Points) in ram
    CableInfo_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    try:
        sql_statement = "SELECT PassCount,FailCount,Stage1,Stage1Points,Stage2,Stage2Points from tblCable_Info where CableInfo_Location="+str(CableInfo_Location)
        my_database = conn.execute(sql_statement)
        x = my_database.fetchall()
        #print("Local_Cable_Info",x)
        return(x)
    except :
        print('Record not found please create...')
        
def DownloadCable_Info_all():##update Location Part_Name
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Stage1Points,Stage2Points from tblCable_Info"
    #sql_statement = "SELECT * from tblCable_Id"
    my_database.execute(sql_statement)
    n =my_database.fetchall()
##    print("Downloaded cable two stage",n)
    return(n)
# =============================================================================
# 
# =============================================================================
def DownloadConfiguration(Id):

    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT AssetCodeScan,CableNos,LeakageChannel,LeakageTestTime,LeakIterations,ConnectorVisual,\
                    TesterNetwork,Traceability,ProductionMonitoring,DeviceInterface,Reports from tblConfiguration \
                    where Id ="+str(Id)
    my_database.execute(sql_statement)
    output = my_database.fetchall()
##    print('output',output)
    return(output)

def uploadConfiguration(Id):
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    my_database.execute('update tblConfiguration set DateTime = ?,AssetCodeScan = ?,CableNos = ?,LeakageChannel = ?,LeakageTestTime = ?,LeakIterations = ?,ConnectorVisual = ?\
                        ,TesterNetwork = ?,Traceability = ?,ProductionMonitoring = ?,DeviceInterface = ?,Reports = ? where Id =?'\
                        ,(datetime.now(),GV.AssetCodeScan,GV.CableNos,GV.LeakageChannel,GV.LeakageTestTime,GV.LeakIterations,GV.ConectorVisual,GV.TesterNetwork,GV.Tracebility,GV.ProductionMonitoring,GV.DeviceInterface,GV.Report,Id))
    conn.commit()

def DownloadUserConfiguration(Id):
    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT AutoPartLoad,PartNoLoc,PartNo_Length,UserVar1_Loc,Var1_Length,UserVar2_Loc,Var2_Length,\
                    UserVar3_Loc,Var3_Length,UserVar4_Loc,Var4_Length,Weekday_STD,Shift_A,A_timing,Shift_B,B_timing,Shift_C,C_timing from tblUser_config \
                    where Id ="+str(Id)
    my_database.execute(sql_statement)
    output = my_database.fetchall()
##    print('output',output)
    return(output)
def uploadUserConfiguration(Id):
    
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    if(GV.user_config_flag==0):
        my_database.execute('update tblUser_config set DateTime = ?,AutoPartLoad = ?,PartNoLoc = ?,PartNo_Length = ?,UserVar1_Loc = ?,Var1_Length = ?,UserVar2_Loc = ?\
                        ,Var2_Length = ?,UserVar3_Loc = ?,Var3_Length = ?,UserVar4_Loc = ?,Var4_Length = ? where Id =?'\
                        ,(datetime.now(),GV.AutoPartLoad,GV.PartNoLoc,GV.PartNO_Length, GV.UserVar1_Loc,GV.Var1_Length,GV.UserVar2_Loc,GV.Var2_Length,GV.UserVar3_Loc,GV.Var3_Length,GV.UserVar4_Loc,GV.Var4_Length,Id))

    else:
        my_database.execute('update tblUser_config set DateTime = ?,AutoPartLoad = ?,Weekday_STD = ?,Shift_A = ?,A_timing = ?,Shift_B = ?\
                        ,B_timing = ?,Shift_C = ?,C_timing = ? where Id =?'\
                        ,(datetime.now(),GV.AutoPartLoad,GV.Weekday_STD,GV.Shift_A,GV.A_timing,GV.Shift_B,GV.B_timing,GV.Shift_C,GV.C_timing,Id))

    conn.commit()

# =============================================================================.
# 
# =============================================================================
def DownloadGlobal_Grp1():
    conn  = sqlite3.connect(GV.DBpath)#/home/pi/Desktop/AWHT/code/tester_files/HAG1DB_V2.0.3.db
    my_database = conn.cursor()
    sql_statement = "SELECT Id,LeakageTestStatus,FixturePosition,ConnectorPartName,FixtureType,NoOfCavities,NavigationStatus,ConnectorPresense,SecondaryLock,SensorInput,EjectorStatus,FixtureActuation from tblGlob_Grp1"
    
    my_database.execute(sql_statement)
    output = my_database.fetchall()
    for x in range (len(output)):
        if None in output[x]:
            hlist=list(output[x])
            hlist.remove(None)
            output[x]=tuple(hlist)
##    print('output',output)
    
    maxnum=0
    for y in range(len(output)):
        key=output[y][0]
        maxnum=max(maxnum,key)
##        print("maxnum",maxnum)
    tp=[[] for i in range(maxnum)]
   
    key=0
    for y in range(len(output)):
        key=output[y][0]
        for x in range(1,len(output[y])):
            tp[key-1].append(output[y][x])
##    print("tp",len(tp),tp)
    GV.Leakage_Test_status=[]
    for x in range (len(tp)):
        if len(tp[x])>0:
            
            GV.Fixture_Position.append(tp[x][1])
            GV.Connector_Part_Name.append(tp[x][2])
            if tp[x][0]==None:
##                GV.Leakage_Test_status[x]=0
                GV.Leakage_Test_status.append(0)
            else:
                GV.Leakage_Test_status.append(int(tp[x][0]))

    Leakage_status=[]
    Fixture_Posi=[]
    for x in output:

        Leakage_status.append(x[1])
        Fixture_Posi.append(x[2])


    conn.close()

    return(output)

def Delete_Database_Table():
    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor
    sql_statement = "DELETE from tblGlob_Grp1" 
    my_database = conn.execute(sql_statement)
    sql_statement1 = "DELETE from tblGlob_Grp2" 
    my_database = conn.execute(sql_statement1)
    conn.commit()
    print("delete tblGlob_Grp1 & tblGlob_Grp2 info")

    
def UploadGlobal_Grp1(lsfp):##Local_Group1_File = [(1,2,3,None,1,10)]
    tuple_Data = lsfp
##    tuple_Data2 = cavity
    
##    print('tuple_Data',tuple_Data)
    print("Check..Successfully Uploaded ")
    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor
    for x in range(len(tuple_Data)):
##        for y in range(len(tuple_Data[x])):
##            print('UploadGlobal_Grp1',y+1,tuple_Data[x][y])
        try:
            Id=tuple_Data[x][0]
            LeakageTestStatus=tuple_Data[x][1]
            FixturePosition=tuple_Data[x][2]
            ConnectorPartName=tuple_Data[x][3]
            FixtureType=tuple_Data[x][4]
            NoOfCavities=tuple_Data[x][5]
            NavigationStatus=tuple_Data[x][6]
            ConnectorPresence=tuple_Data[x][7]
            SecondaryLock=tuple_Data[x][8]
            SensorInput=tuple_Data[x][9]
            EjectorStatus=tuple_Data[x][10]
            FixtureActuation=tuple_Data[x][11]
            
            
        except IndexError:
            pass
        sql_statement = "SELECT count(Id) from tblGlob_Grp1 where Id="+str(Id)
        my_database = conn.execute(sql_statement)
        n = my_database.fetchone()[0]
##        print("n",n)
        if(n == 0):
            my_database.execute('insert into tblGlob_Grp1 (LeakageTestStatus,FixturePosition,ConnectorPartName,FixtureType,NoOfCavities,NavigationStatus,\
                                ConnectorPresense,SecondaryLock,SensorInput,EjectorStatus,FixtureActuation) values(?,?,?,?,?,?,?,?,?,?,?)',
                                (LeakageTestStatus,FixturePosition,ConnectorPartName,FixtureType,NoOfCavities,NavigationStatus,ConnectorPresence,SecondaryLock,SensorInput,EjectorStatus,FixtureActuation))
            
        else:
            my_database.execute('UPDATE tblGlob_Grp1 SET LeakageTestStatus= ?,FixturePosition= ?,ConnectorPartName= ?,FixtureType= ?,NoOfCavities= ?,\
                                NavigationStatus= ?,ConnectorPresense= ?,SecondaryLock= ?,SensorInput= ?,EjectorStatus= ?,FixtureActuation= ?  WHERE Id =?',
                                (LeakageTestStatus,FixturePosition,ConnectorPartName,FixtureType,NoOfCavities,NavigationStatus,ConnectorPresence,SecondaryLock,SensorInput,EjectorStatus,FixtureActuation,Id))
        conn.commit()
# =============================================================================
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# =============================================================================

def UploadGlobal_Grp2(n_tuple_Data):
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement='DELETE FROM tblGlob_Grp2 where GroupNo = '+str(n_tuple_Data[0][0])
    my_database.execute(sql_statement)

    for i in range(len(n_tuple_Data)):
        myTuple=n_tuple_Data[i]
        for j in range(len(myTuple)):
            GrpNo=myTuple[0]
            Cavity=myTuple[1]
            HWpin=myTuple[2]
            point=myTuple[3]
            pinfunction=myTuple[4]

        my_database.execute('insert into tblGlob_Grp2(GroupNo,CavityNo,HW_Pin,\
                            PointNo,PinFunction) values(?,?,?,?,?)',
                            (GrpNo,Cavity,HWpin,point,pinfunction))
    conn.commit() 
def UploadLibMap(n_tuple_Data):
##    print('n_tuple_Data_now',n_tuple_Data)
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    GrpNo=n_tuple_Data[0]
    sql_statement='DELETE FROM tblLibMap where GroupNo = '+str(GrpNo)
    my_database.execute(sql_statement)
    ConnName=n_tuple_Data[1]
    LibName=n_tuple_Data[2]
    my_database.execute('insert into tblLibMap(GroupNo,Library_Name,Part_Name) values(?,?,?)',(GrpNo,LibName,ConnName))
##        my_datab
    conn.commit()
def DownloadGlobal_Grp2_forlocalgrp(z):
    temp_w=[]
    HWCTPin=[]
    tempGrp_data=[]
    GV.Local_Group_data=[]
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    for i in range (len(z)):
        sql_statement = "SELECT GroupNo,CavityNo,HW_Pin,PointNo,PinFunction from tblGlob_Grp2 where GroupNo = "+str(z[i])
        my_database.execute(sql_statement)
        x = my_database.fetchall()
        x.sort(key=lambda y: int(y[0]))
        temp_w.append(x)
    tuple_pass=[]
    for i in range (len(temp_w)):
        tuple_data=temp_w[i]
        tuple_pass.append(tuple_data)
        
        for j in range (len(tuple_data)):
                if ('CT' in tuple_data[j]):
                        HWCTPin.append(tuple_data[j])
##    print("tuple_pass",tuple_pass)
    UploadLocal_Grp2(GV.Location_No,tuple_pass)
##    print("HWCTPin",HWCTPin)
    GV.Local_Group_data= [[] for i in range(128)]
    # grpdata=[]
    for i in range (len(HWCTPin)):
        GV.Local_Group_data[HWCTPin[i][0]-1].append(HWCTPin[i][2])
    # for i in range (len(HWCTPin)):
    #     temp=HWCTPin[i][0]
    #     if(i==0):
    #         tempGrp_data.append(HWCTPin[i][2])
    #     else:
    #         if(temp==HWCTPin[i-1][0]):
    #             tempGrp_data.append(HWCTPin[i][2])
    #         else:
    #             GV.Local_Group_data.append(tempGrp_data)
    #             tempGrp_data=[]
    #             tempGrp_data.append(HWCTPin[i][2])
    #     if((i+1)==len(HWCTPin)):
    #         GV.Local_Group_data.append(tempGrp_data)

    # print("GV.Local_Group_data",GV.Local_Group_data)

def get_lastCTpin():
    print("last ct pin")
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT PointNo from tblGlob_Grp2"
    my_database.execute(sql_statement)
    x = my_database.fetchall()
    if(len(x)==0):
        GV.lstCTP=0
    else:
        y=max(x)
        GV.lstCTP=y[0]
        print(GV.lstCTP)

def DownloadGlobal_Grp2():
    GV.special_pins=[]
    GV.virtual_pins=[]
    GV.Actual_pins=[]
    GV.leakage_gbl=[]
    GV.switch_gbl=[]
    GV.led_gbl=[]
    GV.unused_pin=[]
    GV.led1=[]
    pin_array=[]
    for i in range(1,GV.total_point+1):
        pin_array.append(i)

    HWCTPin=[]
    tempGrp_data=[]
    GV.Group_data=[]
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT GroupNo,CavityNo,HW_Pin,PointNo,PinFunction from tblGlob_Grp2"
    my_database.execute(sql_statement)
    x = my_database.fetchall()

    x.sort(key=lambda y: int(y[0]))
##    print("sorted op.........",x)
    
    for i in range(len(x)):

        GV.Actual_pins.append(x[i][2])
        GV.virtual_pins.append(x[i][3])
        if ('LT' in x[i]):
            t=[x[i][0],x[i][2]]
            GV.leakage_gbl.append(t)
            l=[x[i+1][0],x[i+1][2]]
            GV.led1.append(l)
        if ('NV' in x[i]):
            t=[x[i][0],x[i][2]]
            GV.led_gbl.append(t)
        if ('SW' in x[i]):
            t=[x[i][0],x[i][2]]
            GV.switch_gbl.append(t)

        if ('CT' not in x[i]):
            GV.unused_pin.append(x[i][2])
            
        if ('CT' in x[i]):
            HWCTPin.append(x[i])
        
            
    ##=============================================================
    GV.Group_data= [[] for i in range(128)]
    # grpdata=[]
    for i in range (len(HWCTPin)):
        grpno=HWCTPin[i][0]
        GV.Group_data[HWCTPin[i][0]-1].append(HWCTPin[i][2])
    # for i in range (len(HWCTPin)):
    #     temp=HWCTPin[i][0]
    #     if(i==0):
    #         tempGrp_data.append(HWCTPin[i][2])
    #     else:
    #         if(temp==HWCTPin[i-1][0]):
    #             tempGrp_data.append(HWCTPin[i][2])
    #         else:
    #             GV.Group_data.append(tempGrp_data)
    #             tempGrp_data=[]
    #             tempGrp_data.append(HWCTPin[i][2])
    #     if((i+1)==len(HWCTPin)):
    #         GV.Group_data.append(tempGrp_data)        
##=============================================================
    sortgrp=[]
    for i in range(len(GV.Group_data)):
        for j in range(len(GV.Group_data[i])):
            sortgrp.append(GV.Group_data[i][j])

    for a in range(1,GV.total_point+1):
        if(a in sortgrp ):
            pin_array.remove(a)
    GV.special_pins=pin_array
    GV.leakage=GV.leakage_gbl
    GV.led=GV.led_gbl
    GV.switch=GV.switch_gbl
    
    # print("GV.special_pins",GV.special_pins)        
    return(x)
# =============================================================================
def DownloadGlobal_Grp2_Cavity():
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT GroupNo,CavityNo,PointNo from tblGlob_Grp2 order by GroupNo"
    my_database.execute(sql_statement)
    output = my_database.fetchall()
##    print('output',output)
    return(output)
# =============================================================================
def DownloadGLobal_Cable_Settings():
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT AutoManual,ReleaseTime,QMarkTime,failTime,BuzzerStatus,ExtraPointTest,CutterStatus\
                    ,OpenPointTime,ShortPointTime,InterChangeTime,ExtraPointTime,LablePrint\
                    ,LableNos,BarCodeMatch,BarcodeNos,TestingMode,CompTest,Stages,Operation1\
                    ,Operation2,Operation3,Operation4,Operation5,Operation6\
                    ,Operation7,Operation8,Operation9,Operation10,Operation11\
                    ,Operation12,Operation13,Operation14,Operation15\
                     from tblGlob_Settings "
                   
    my_database.execute(sql_statement)
    x = my_database.fetchall()
##    print('x',x)
    if(len(x)==0):
        print('Record not found please create')
    else:
        return(x)
# =============================================================================
# 
# =============================================================================
def DownloadHarnessData(Location_No,stage):##dowload circuits data of pass  location no from db
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
   
    sql_statement = "SELECT NetNo,Point1,Point2 from tblHarness_Data where HarnessData_Location=? AND stage=?"
    my_database.execute(sql_statement,(str(Location_No),str(stage)))
    output = my_database.fetchall()

    for x in range (len(output)):
        if None in output[x]:
            hlist=list(output[x])
            hlist.remove(None)
            output[x]=tuple(hlist)
    
##    print('output1.....',output)
    
    maxnum=0
    for y in range(len(output)):
        key=output[y][0]
        maxnum=max(maxnum,key)
    tp=[[] for i in range(maxnum)]
   
    key=0
    for y in range(len(output)):
        key=output[y][0]
        for x in range(1,len(output[y])):
            tp[key-1].append(output[y][x])
##    print("tp.......................",tp)
    
    GV.circuits=tp
    print("GV.circuits",GV.circuits)
    

        
    sql_statement = "SELECT NetNo,Wire_Type,Point1,Point2,Wire_color1,Wire_color2,Wire_Gauge from tblHarness_Data where HarnessData_Location=? AND stage=?"
    
    my_database.execute(sql_statement,(str(Location_No),str(stage)))
    output1 = my_database.fetchall()
##    print('output',output)
    for x in range (len(output1)):
        if None in output1[x]:
            hlist=list(output1[x])
            hlist.remove(None)
            output1[x]=tuple(hlist)

    
    maxnum=0
    for y in range(len(output1)):
        key=output1[y][0]
        maxnum=max(maxnum,key)
    tp=[[] for i in range(maxnum)]
   
    key=0
    for y in range(len(output1)):
        key=output1[y][0]
        for x in range(1,len(output1[y])):
            tp[key-1].append(output1[y][x])
##    print("tp",tp)
    
   
    GV.Wire_Type=[]
    GV.Wire_color1=[]
    GV.Wire_color2=[]
    GV.Wire_Gauge = []
    for x in range (len(tp)):
        GV.Wire_Type.append(tp[x][0])
        GV.Wire_color1.append(tp[x][3])
        GV.Wire_color2.append(tp[x][4])
        GV.Wire_Gauge.append(tp[x][5])

    return(output)

def UploadHarnessData(Location_No,stage,Type,value,Tolerence,circuits,Wire_Type,Wire_color1,Wire_color2,Wire_Gauge):##upload  circuits data of pass  location no ram to db
##    print("harness save",Wire_Type[0],Wire_color1[0],Wire_color2[0],Wire_Gauge[0])
    print(circuits)
    conn  = sqlite3.connect(GV.DBpath)
    Data=[]
    HarnessData_Location=Location_No
    my_database =conn.cursor()
    sql_statement ='DELETE FROM tblHarness_Data WHERE HarnessData_Location ='+str(HarnessData_Location)+' AND '+'stage='+str(stage)
    my_database.execute(sql_statement)
    if(len(circuits)>0): 
        for x in range(len(circuits)):
            Data.append(())
            if not((len(circuits[x]) % 2) == 0):
                circuits[x].append(None)
            Data[x]=tuple(circuits[x])

        for NetNo in range(len(Data)):

            for sub_point in range(round(len(Data[NetNo])/2.0)):

                
                my_database.execute('insert into tblHarness_Data(HarnessData_Location,Stage,NetNo,Type,Value,Tolerance,Point1\
                                                                ,Point2,Wire_Type,Wire_color1,Wire_color2,Wire_Gauge) values(?,?,?,?,?,?,?,?,?,?,?,?)',
                                    (HarnessData_Location,stage,NetNo+1,Type,value,Tolerence,Data[NetNo][sub_point*2],Data[NetNo][(sub_point*2)+1],Wire_Type[NetNo],Wire_color1[NetNo],Wire_color2[NetNo],Wire_Gauge[NetNo]))
    conn.commit()          
    conn.close()

def DownloadComp_data(Location_No,stage):
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Type,Value,Tolerance,Point1,Point2 from tblHarness_Data where HarnessData_Location=? AND stage=?"
    my_database.execute(sql_statement,(str(Location_No),str(stage)))
    x = my_database.fetchall()
##    print("x......",x)
##    GV.comp_display=[]
    for i in range (len(x)):
        if ('cnt' not in x[i]):
            GV.component_test.append(x[i])
##    print("GV.component_test",GV.component_test)
def Uploadcomponent_data(Location_No,Type,value,Tole,pt1,pt2):
    conn  = sqlite3.connect(GV.DBpath)
    HarnessData_Location=Location_No
    my_database =conn.cursor()
    my_database.execute('update tblHarness_Data set Type = ?,Value=?,Tolerance=? where Point1 =? and Point2=? and \
                        HarnessData_Location=?',(Type,value,Tole,pt1,pt2,HarnessData_Location))
    conn.commit()
#-------------------------------------------Export harness data--------------------------------------------------------------------------------------------------#
def Export_HarnessData(Location_No):
    print("Export data")
    Get_num_stages(Location_No)
    path = '/home/pi/Desktop/.HA_Editor'  
    GV.source= path + '/' + str(Location_No) + ''+'Hrn.xlsx'
    workbook = xlsxwriter.Workbook(GV.source)   
    for i in range(GV.Num_Stages):
        worksheet = workbook.add_worksheet("Stage"''+str(i+1)+'')
        # print(worksheet)
        output=DownloadHarnessData(Location_No,i+1)
        # print(output)
        maxnum=0
        for y in range(len(output)):
            key=output[y][0]
            maxnum=max(maxnum,key)
        tp=[[] for i in range(maxnum)]
        key=0
        for y in range(len(output)):
            key=output[y][0]
            for x in range(1,len(output[y])):
                tp[key-1].append(output[y][x])
        # print("tp.......................",tp)
        GV.circuits=tp
        GV.ckt_net=[]
    
        circuits=GV.circuits
 
        try:
            for i in range(len(circuits)):
                read=(circuits[i])
                ckt=[]
                
                for j in range(len(read)):
                    if (read[j] in GV.Actual_pins):
                        ind=GV.Actual_pins.index(read[j])
                        ckt.append(GV.virtual_pins[ind])
                        # ckt.append(GV.virtual_pins[read[j]-1])
                    
                GV.ckt_net.append(ckt)
            print("check....",GV.ckt_net)
        except(IndexError):
            print("No data  in circuit")
        num_pt=map(len,GV.ckt_net)
        total_ckt_pt=sum(num_pt)       
        for i in range(len(GV.ckt_net)):
            read_1=(GV.ckt_net[i])
            for j in range(len(read_1)):
                points=read_1[j]    
                worksheet.write(i+1,j,str(points))
        worksheet.write(0,0,str(total_ckt_pt))
               
    workbook.close()   

#----------------------------------------------Export Groub Data----------------------------------------#
def Export_Group_data(Location_No):
    # storage_path = '/home/pi/Desktop/.HA_Editor/' + str(Location_No) + ''+'Grp_data.xlsx'
    # try:
    #     os.makedirs(storage_path)
    # except FileExistsError:
    #     print('folder exist')
    # print(GV.Local_Group_data)
    path = '/home/pi/Desktop/.HA_Editor'  
    GV.GRP_source= path + '/' + str(Location_No) + ''+'Grp_data.xlsx'
    workbook = xlsxwriter.Workbook(GV.GRP_source)
    worksheet = workbook.add_worksheet("Group_data") 
    ckt_net=[]
    try:
        for i in range(len(GV.Local_Group_data)):
            read=(GV.Local_Group_data[i])
            ckt=[]
            
            for j in range(len(read)):
                if (read[j] in GV.Actual_pins):
                    ind=GV.Actual_pins.index(read[j])
                    ckt.append(GV.virtual_pins[ind])
                    
            ckt_net.append(ckt)
            print("check....",ckt_net)
    except(IndexError):
        print("No data  in circuit")
    for i in range(len(ckt_net)):
            read_1=(ckt_net[i])
            for j in range(len(read_1)):
                points=read_1[j]    
                worksheet.write(i,j,str(points))
    workbook.close()
#-------------------------------------------------------------------------------------------------------#  

# =============================================================================
def Download_Help():
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT IsActive from tblHelp Where Id=1"
    my_database.execute(sql_statement)
    n =my_database.fetchall()
##    print(n[0][0])
    return(n[0][0])

def Upload_Help(lt):
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    my_database.execute('update tblHelp set IsActive = ? where Id =?',(lt,1))
    conn.commit()
# =============================================================================
# 
# =============================================================================
def DownloadLocal_Grp1(Location_No):
    print('Location_No',Location_No)
    LocalGrp1_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Group_No,ContunityPointNos from tblLocal_Grp1 \
                    where LocalGrp1_Location ="+str(LocalGrp1_Location)

    my_database.execute(sql_statement)
    output = my_database.fetchall()
    #print('output',output)
    
    tp=[[] for i in range(128)]
    key=0
    for y in range(len(output)):
        key=output[y][0]
        for x in range(1,len(output[y])):
            tp[key-1].append(output[y][x])
##    print("tp",tp)
    GV.Local_Group1_File=tp
    return(output)

def UploadLocal_Grp1(grp_data,Location_No):##Local_Group1_File = [(1,2,3,None,1,10)]
    tuple_Data = grp_data
    print("Check...........Successfully Uploaded.... ")
  
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()    
    
    for x in range(len(tuple_Data)):

        try:
            Id=tuple_Data[x][0]
            LeakageTestStatus=tuple_Data[x][1]
            FixturePosition=tuple_Data[x][2]
            ConnectorPartName=tuple_Data[x][3]
            FixtureType=tuple_Data[x][4]
            NoOfCavities=tuple_Data[x][5]
            NavigationStatus=tuple_Data[x][6]
            ConnectorPresence=tuple_Data[x][7]
            SecondaryLock=tuple_Data[x][8]
            SensorInput=tuple_Data[x][9]
            EjectorStatus=tuple_Data[x][10]
            FixtureActuation=tuple_Data[x][11]
            
            
        except IndexError:
            print("Data not present")
        sql_statement = 'SELECT count(Group_No) from tblLocal_Grp1 where Group_No='+str(Id)+' and LocalGrp1_Location='+str(Location_No)
        my_database = conn.execute(sql_statement)
        n = my_database.fetchone()[0]
##        print("n",n)
        if(n == 0):
            my_database.execute('insert into tblLocal_Grp1 (LocalGrp1_Location,Group_No,FixtureType,ConnectorPartName,\
                                NoOfContunityPoints,FixturePosition,LeakageTestStatus,NavigationStatus,\
                                ConnectorPresense,SecondaryLock,SensorInput,EjectorStatus,FixtureActuation) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                                (Location_No,Id,FixtureType,ConnectorPartName,NoOfCavities,FixturePosition,LeakageTestStatus,NavigationStatus,ConnectorPresence,
                                 SecondaryLock,SensorInput,EjectorStatus,FixtureActuation))
            
        else:
            my_database.execute('UPDATE tblLocal_Grp1 SET FixtureType= ?,ConnectorPartName= ?, NoOfContunityPoints= ?,FixturePosition= ?,LeakageTestStatus= ?,\
                               NavigationStatus= ?,ConnectorPresense= ?,SecondaryLock= ?,SensorInput= ?,\
                                EjectorStatus= ?,FixtureActuation= ?  WHERE Group_No =? and LocalGrp1_Location=?',
                                (FixtureType,ConnectorPartName,NoOfCavities,FixturePosition,LeakageTestStatus,
                                 NavigationStatus,ConnectorPresence,SecondaryLock,
                                 SensorInput,EjectorStatus,FixtureActuation,Id,Location_No))
        conn.commit()
        

##    tuple_Data = lgrp1
##    LocalGrp1_Location=Location_No
##    
##    conn  = sqlite3.connect(GV.DBpath)
##    my_database=conn.cursor()    
##    sql_statement ='DELETE FROM tblLocal_Grp1 WHERE LocalGrp1_Location ='+str(Location_No)
##    my_database.execute(sql_statement)
##
##    for x in range(len(tuple_Data)):
##        for y in range(len(tuple_Data[x])):
##            print(Location_No,y+1,tuple_Data[x][y])
##            my_database.execute('insert into tblLocal_Grp1(LocalGrp1_Location,Group_No,NoOfContunityPoints) values(?,?,?)',(LocalGrp1_Location,y+1,tuple_Data[x][y]))
##            conn.commit()
# =============================================================================
# 
# =============================================================================
def DownloadLocal_Grp2(Location_No):
    LocalGrp2_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()

    sql_statement = "SELECT GroupNo,CavityNo,HW_Pin,PointNo,PinFunction from tblLocal_Grp2 \
                    where LocalGrp2_Location="+str(LocalGrp2_Location)
    my_database.execute(sql_statement)
    x = my_database.fetchall()
    # print("check1",x)
    conn.commit()
    x.sort(key=lambda y: int(y[0]))
    # print("print",x)
    GV.Local_Group2_File=[]
    GV.Local_Group3_File=[]
    GV.LocalGrpNo=[]
    GV.leakage=[]
    GV.switch=[]
    GV.led=[]
    GV.led1=[]
    HWCTPin=[]
    tempGrp_data=[]
    GV.Local_Group_data=[]
    for i in range(len(x)):

        if ('LT' in x[i]):
            t=[x[i][0],x[i][2]]
            # print("t...",t)
            GV.leakage.append(t)
            l=[x[i+1][0],x[i+1][2]]
            GV.led1.append(l)
        if ('NV' in x[i]):
            t=[x[i][0],x[i][2]]
            GV.led.append(t)
        if ('SW' in x[i]):
            t=[x[i][0],x[i][2]]
            GV.switch.append(t)
        if ('CT' in x[i]):
            HWCTPin.append(x[i])
    ##=============================================================
##    print("HWCTPin",HWCTPin)
       
    
    for i in range (len(HWCTPin)):
        temp=HWCTPin[i][0]
        if(i==0):
            
            tempGrp_data.append(HWCTPin[i][2])
        else:
            if(temp==HWCTPin[i-1][0]):
                tempGrp_data.append(HWCTPin[i][2])
            else:
                GV.Local_Group_data.append(tempGrp_data)
                tempGrp_data=[]
                
                tempGrp_data.append(HWCTPin[i][2])
        if((i+1)==len(HWCTPin)):
            GV.Local_Group_data.append(tempGrp_data)


    
    for i in range(len(GV.Local_Group_data)):
        r=GV.Local_Group_data[i][0]
        for j in range(len(HWCTPin)):
            if(r == HWCTPin[j][2]):
                GV.LocalGrpNo.append(HWCTPin[j][0])
            
    # print("GV.leakage",GV.leakage)
    # print("GV.led",GV.led)
    # print("GV.switch",GV.switch)  
    ##======================Connector image data=======================================
    output=[]
    output2=[]
    
    for i in range(len(HWCTPin)):
        x=tuple([HWCTPin[i][0],HWCTPin[i][2]])
        output.append(x)      

    for i in range(len(HWCTPin)):
        x=tuple([HWCTPin[i][0],HWCTPin[i][1]])
        output2.append(x)

    tp=[[] for i in range(128)]
    key=0
    for y in range(len(output)):
        key=output[y][0]
        for x in range(1,len(output[y])):
            tp[key-1].append(output[y][x])
    GV.Local_Group2_File=tp
    tx=[[] for i in range(128)]
    key=0
    for y in range(len(output2)):
        key=output2[y][0]
        for x in range(1,len(output2[y])):
            tx[key-1].append(output2[y][x])
    GV.Local_Group3_File=tx


    # print("GV.LocalGrpNo",GV.LocalGrpNo)
    # print("GV.Local_Group_data",GV.Local_Group_data)
##    print("GV.Local_Group2_File",GV.Local_Group2_File)
##    print("GV.Local_Group3_File",GV.Local_Group3_File)
##=====================================================================================
	
def UploadLocal_Grp2(Location_No,n_tuple_Data):


    print("n_tuple_Data",n_tuple_Data)
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()    
    
    
##    print('Uploaded Successfully.......')
    LocalGrp2_Location=Location_No
    sql_statement ='DELETE FROM tblLocal_Grp2 WHERE LocalGrp2_Location ='+str(LocalGrp2_Location)##+'and GroupNo='+str(n_tuple_Data[0][0])
    my_database.execute(sql_statement)
    
    for i in range(len(n_tuple_Data)):
        tp_pass=n_tuple_Data[i]
        for k in range(len(tp_pass)):
            
            myTuple=tp_pass[k]
            for j in range(len(myTuple)):
                GrpNo=myTuple[0]
                Cavity=myTuple[1]
                HWpin=myTuple[2]
                point=myTuple[3]
                pinfunction=myTuple[4]

            my_database.execute('insert into tblLocal_Grp2(LocalGrp2_Location,GroupNo,CavityNo,HW_Pin,\
                                PointNo,PinFunction) values(?,?,?,?,?,?)',
                                (LocalGrp2_Location,GrpNo,Cavity,HWpin,point,pinfunction))

    conn.commit() 


#========================================
def DownloadCable_Settings(Location_No):
##    print("Location_No....",Location_No)
    
    LocalSettings_Location=Location_No;
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    
    sql_statement = "SELECT AutoManual,ReleaseTime,failTime,QMarkTime,BuzzerStatus,ExtraPointTest,CutterStatus,OpenPointTime,ShortPointTime\
                    ,InterChangeTime,ExtraPointTime,LablePrint,LableNos,BarCodeMatch\
                    ,BarcodeNos,Testing_Mode,CompTest,Stages,Operation1,Operation2,Operation3,Operation4\
                    ,Operation5,Operation6,Operation7,Operation8,Operation9\
                    ,Operation10,Operation11,Operation12,Operation13,Operation14,Operation15 from \
                    tblLocal_Settings where LocalSettings_Location="+str(LocalSettings_Location)
    my_database.execute(sql_statement)
    x = my_database.fetchall()
   
    
##    print("test",x)
    if(len(x)==0):
        print('Record not found please create')
    else:
        GV.Auto_Mode=x[0][0]
        GV.Release_Time=x[0][1]
        GV.Fail_Time=x[0][2]
        GV.Q_Mark_Time=x[0][3]
        
        GV.Buzzer_Status=x[0][4]
        GV.ExtraPointTest=x[0][5]
        GV.Cutter_status=x[0][6]
        GV.Open_point_Timeout=x[0][7]
        GV.Short_point_Timeout=x[0][8]
        GV.Interchange_point_Timeout=x[0][9]
        GV.Extra_point_Timeout=x[0][10]
        GV.LabelPrint=x[0][11]
        GV.LableNos=x[0][12]
        GV.Barcode_Match=x[0][13]
        GV.No_Of_Barcodes=x[0][14]
        GV.All_Error=x[0][15]
        GV.Component_status=x[0][16]
        GV.NoofStages=x[0][17]

    
def UploadCable_Settings(Location_No):
    LocalSettings_Location=Location_No;
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT count(LocalSettings_Location) from tblLocal_Settings where LocalSettings_Location="+str(LocalSettings_Location)
    my_database = conn.execute(sql_statement)
    n = my_database.fetchone()[0]
##    print("n",n)
    if(n == 0):
        print(n)
       
        my_database.execute('insert into tblLocal_Settings(LocalSettings_Location,AutoManual,ReleaseTime,failTime,QMarkTime\
                            ,BuzzerStatus,ExtraPointTest,CutterStatus,OpenPointTime,ShortPointTime\
                            ,InterChangeTime,ExtraPointTime,LablePrint,LableNos,BarCodeMatch\
                            ,BarcodeNos,Testing_Mode,CompTest,Stages,Operation1,Operation2,Operation3,Operation4\
                            ,Operation5,Operation6,Operation7,Operation8,Operation9\
                            ,Operation10,Operation11,Operation12,Operation13,Operation14,Operation15) \
                            values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                            (LocalSettings_Location,GV.Auto_Mode,GV.Release_Time,GV.Fail_Time,GV.Q_Mark_Time,GV.Buzzer_Status\
                            ,GV.ExtraPointTest,GV.Cutter_status,GV.Open_point_Timeout,GV.Short_point_Timeout\
                            ,GV.Interchange_point_Timeout,GV.Extra_point_Timeout,GV.LabelPrint,GV.LabelNos\
                            ,GV.Barcode_Match,GV.No_Of_Barcodes,GV.All_Error,GV.Component_status,GV.NoofStages,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
)
    else:
        print(n)
        
        my_database.execute('update tblLocal_Settings set AutoManual=?,ReleaseTime=?,failTime=?,QMarkTime=?\
                            ,BuzzerStatus=?,ExtraPointTest=?,CutterStatus=?,OpenPointTime=?,ShortPointTime=?\
                            ,InterChangeTime=?,ExtraPointTime=?,LablePrint=?,LableNos=?,BarCodeMatch=?\
                            ,BarcodeNos=?,Testing_Mode=?,CompTest = ?,Stages= ? where LocalSettings_Location = ?',
                            (GV.Auto_Mode,GV.Release_Time,GV.Fail_Time,GV.Q_Mark_Time,GV.Buzzer_Status\
                            ,GV.ExtraPointTest,GV.Cutter_status,GV.Open_point_Timeout,GV.Short_point_Timeout\
                            ,GV.Interchange_point_Timeout,GV.Extra_point_Timeout,GV.LabelPrint,GV.LabelNos\
                            ,GV.Barcode_Match,GV.No_Of_Barcodes,GV.All_Error,GV.Component_status,GV.NoofStages,LocalSettings_Location))                                                  

    conn.commit()

def UploadCable_OP_Settings(Location_No,pref):

    
    LocalSettings_Location=Location_No;
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    my_database.execute('update tblLocal_Settings set Operation1=?,Operation2=?,Operation3=?,Operation4=?\
                            ,Operation5=?,Operation6=?,Operation7=?,Operation8=?,Operation9=?\
                            ,Operation10=?,Operation11=?,Operation12=?,Operation13=?,Operation14=?\
                            ,Operation14=? where LocalSettings_Location = ?',
                        (pref[0],pref[1],pref[2],pref[3],pref[4],pref[5],pref[6],pref[7],pref[8],pref[9]
                         ,pref[10],pref[11],pref[12],pref[13],pref[14],LocalSettings_Location))
                        
                        
    conn.commit()
# =============================================================================
 
# =============================================================================  
def UploadQC1_Data(Location_No,Local_Lable_Data,Local_Barcode1_Data,Local_Barcode2_Data): 
    QCData_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT count(QCData_Location) from tblQC_Data where QCData_Location="+str(QCData_Location)
    my_database = conn.execute(sql_statement)
    n = my_database.fetchone()[0]
    if(n == 0):
        my_database.execute('insert into tblQC_Data(QCData_Location,Lable1Data,BarCode1Data,BarCode2Data) values(?,?,?,?)',(QCData_Location,Local_Lable_Data,Local_Barcode1_Data,Local_Barcode2_Data))
    else:    
        my_database.execute('update tblQC_Data set Lable1Data = ?, BarCode1Data = ?,BarCode2Data = ? where QCData_Location = ?',(Local_Lable_Data,Local_Barcode1_Data,Local_Barcode2_Data,QCData_Location))
    conn.commit()
def UploadQC2_Data(Location_No,Local_Lable2_Data,Local_Barcode1_Data,Local_Barcode2_Data): 
    QCData_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database=conn.cursor()
    sql_statement = "SELECT count(QCData_Location) from tblQC_Data where QCData_Location="+str(QCData_Location)
    my_database = conn.execute(sql_statement)
    n = my_database.fetchone()[0]
    if(n == 0):
        my_database.execute('insert into tblQC_Data(QCData_Location,Lable2Data,BarCode1Data,BarCode2Data) values(?,?,?,?,?)',(QCData_Location,Local_Lable2_Data,Local_Barcode1_Data,Local_Barcode2_Data))
    else:    
        my_database.execute('update tblQC_Data set Lable2Data = ?, BarCode1Data = ?,BarCode2Data = ? where QCData_Location = ?',(Local_Lable2_Data,Local_Barcode1_Data,Local_Barcode2_Data,QCData_Location))
    conn.commit()
def DownloadQC_Data(Location_No):
    conn  = sqlite3.connect(GV.DBpath)
    QCData_Location=Location_No
    my_database=conn.cursor()  
 
    sql_statement = "SELECT Lable1Data,Lable2Data,BarCode1Data,BarCode2Data from tblQC_Data where QCData_Location="+str(QCData_Location)
    my_database.execute(sql_statement)
    hlist = my_database.fetchall()
    #print(hlist[0][0])
    #print(hlist)
    if(len(hlist)==0):
        print('Record not found p,), (2,), (3,), (3,), (4,), (3,), (3,), (3,), (3lease create')
    else:
        return(hlist)
        
# =============================================================================
# 
# =============================================================================
def DownloadSystemInfo(Location_No):
    #print('Location_No',Location_No)
    LocalGrp1_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Key,Value from tblSystem_info \
                    where Id ="+str(LocalGrp1_Location)
    my_database.execute(sql_statement)
    output = my_database.fetchall()
    #print('output',output)
    return(output)

def UploadSystemInfo(val,loc):
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    my_database.execute('update tblSystem_info set Value = ? where Id =?',(val,loc))
    conn.commit()

# =============================================================================
# 
# ==========================production log===================================================
def UploadProdLog_Data(Location_No,Part_Name,Event,Description):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    Location = Location_No
    PartName = Part_Name
    Description=Description
    my_database.execute('insert into tblProduction_logs(Date_Time,LocationNo,PartName,Event,Description) values(?,?,?,?,?)',(datetime.now(),Location,PartName,Event,Description))
    conn.commit() 
def display_prodlogfile(FromDate,ToDate):
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Date_Time,LocationNo,PartName,Event,Description from tblProduction_logs \
                    where Date_Time >='"+ FromDate +"' AND Date_Time <='"+ ToDate +"'"

    my_database.execute(sql_statement)
    output = my_database.fetchall()
    return (output)
    
def DownloadProdLog(FromDate,ToDate):
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Date_Time,LocationNo,PartName,Event,Description from tblProduction_logs \
                    where Date_Time >='"+ FromDate +"' AND Date_Time <='"+ ToDate +"'"

    my_database.execute(sql_statement)
    output = my_database.fetchall()
    cnt=1
##    print('output',output)
    file_name='/home/pi/Desktop/ExportData.xls'
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()

    worksheet.write(0,0,'Date_Time')
    worksheet.write(0,1,'LocationNo')
    worksheet.write(0,2,'PartName')
    worksheet.write(0,3,'Event')
    worksheet.write(0,4,'Description')
    for myOutput in output:
        worksheet.write(cnt,0,myOutput[0])
        worksheet.write(cnt,1,myOutput[1])
        worksheet.write(cnt,2,myOutput[2])
        worksheet.write(cnt,3,myOutput[3])
        worksheet.write(cnt,4,myOutput[4])
        cnt +=1
    workbook.close()
    conn.close()
# ==========================System log===================================================
def UploadSysLog_Data(Location_No,Part_Name,Event,Description):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    Location = Location_No
    PartName = Part_Name
    Description=Description
    my_database.execute('insert into tblSystem_logs(Date_Time,LocationNo,PartName,Event,Description) values(?,?,?,?,?)',(datetime.now(),Location,PartName,Event,Description))
    conn.commit() 
def display_Syslogfile(FromDate,ToDate):
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Date_Time,LocationNo,PartName,Event,Description from tblSystem_logs \
                    where Date_Time >='"+ FromDate +"' AND Date_Time <='"+ ToDate +"'"

    my_database.execute(sql_statement)
    output = my_database.fetchall()
    return (output)
    
def DownloadSysLog(FromDate,ToDate):
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Date_Time,Event,Description from tblSystem_logs \
                    where Date_Time >='"+ FromDate +"' AND Date_Time <='"+ ToDate +"'"

    my_database.execute(sql_statement)
    output = my_database.fetchall()
    cnt=1
##    print('output',output)
    file_name='/home/pi/Desktop/SysExportData.xls'
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()

    worksheet.write(0,0,'Date_Time')
    worksheet.write(0,1,'Event')
    worksheet.write(0,2,'Description') 
    
    for myOutput in output:
        worksheet.write(cnt,0,myOutput[0])
        worksheet.write(cnt,1,myOutput[1])
        worksheet.write(cnt,2,myOutput[2])
        worksheet.write(cnt,3,myOutput[3])
        worksheet.write(cnt,4,myOutput[4])
        cnt +=1
    workbook.close()
    conn.close()
# =============================================================================
def Uploadwirecolor(ColorName,ColorShade):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    Name = str(ColorName)
    Shade = str(ColorShade)
    my_database.execute('insert into tblColorLibrary(ColorName,ColorValue) values (?,?)',(Name,Shade))
    conn.commit()
def Downloadwirecolor():
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()                 
    my_database.execute( "select ColorName,ColorValue from tblColorLibrary")
    output = my_database.fetchall()
##    print("output",output)
    return (output)
def Downloadwirecolor1(ColorName):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()                 
    my_database.execute( "select ColorValue from tblColorLibrary where ColorName = "+'\''+str(ColorName)+'\'')
    output = my_database.fetchall()
##    print("output",output)
    return (output)


def get_Cavity_Map(ConnName):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT CavityNo, X, Y, Shape, Size from tblConn_Lib2 WHERE ConnectorName = "+'\''+str(ConnName)+'\''      #"+'\''+ConnName+'%\''
    my_database = conn.execute(sql_statement)
    output = my_database.fetchall()
    conn.commit()
    return(output)
def get_conn_Image(ConnName):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT Image from tblConn_Lib1 WHERE ConnectorName = "+'\''+str(ConnName)+'\''       #"+'\''+ConnName+'%\''
    my_database = conn.execute(sql_statement)
    output = my_database.fetchall()
    conn.commit()
    return(output)

def get_conn_Cavity(ConnName):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT * from tblConn_Lib2 WHERE ConnectorName ="+'\''+str(ConnName)+'\''       # "+'\''+ConnName+'%\''
    my_database = conn.execute(sql_statement)
    output = my_database.fetchall()
    conn.commit()
    return(output)
def get_LibMap():
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()                 
    my_database.execute( "SELECT GroupNo,Library_Name,Part_Name from tblLibMap ")
    output = my_database.fetchall()
    return(output)
def get_LibMap1(ref):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()                 
    my_database.execute( "SELECT GroupNo,Library_Name,Part_Name from tblLibMap where Part_Name="+'\''+ref+'\'')
    output = my_database.fetchall()
    return(output)        
def get_Points(gr):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()  
    my_database.execute( "SELECT HW_Pin from tblGlob_Grp2 where GroupNo ="+'\''+str(gr)+'\'' " and PinFunction="+'\''+'CT'+'\'')
#    print("SELECT Point from tblGlob_Grp2 where GroupNo ="+str(gr))ConnectorName = '+'\''+connname+'\''
    output = my_database.fetchall()
##    print("output11",output)
    return(output)
def get_allConLib():
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT ConnectorName from tblConn_Lib1"
    my_database = conn.execute(sql_statement)
    output = my_database.fetchall()
    conn.commit()
    return(output)
def get_SpliceLib(SpliceName):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT NetSpliceName from tblSplice1 WHERE NetSpliceName ="+'\''+str(SpliceName)+'\''     # "+'\''+ConnName+'%\''
    my_database = conn.execute(sql_statement)
    output = my_database.fetchall()
    return(output)
def get_ConLib(ConnName):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = "SELECT ConnectorName from tblConn_Lib1 WHERE ConnectorName ="+'\''+str(ConnName)+'\''     # "+'\''+ConnName+'%\''
    my_database = conn.execute(sql_statement)
    output = my_database.fetchall()
    return(output)
def DownloadCavityMap():
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()                 
    my_database.execute( "SELECT ConnectorName,CavityNo,X,Y,Shape,Size from tblConn_Lib2")
    output = my_database.fetchall()
##    print("output",output)
    return (output)
def UploadConnectorImages(Images):
    tuple_Data = Images
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    try:
        ConnectorPartName=tuple_Data[0]
        Image=tuple_Data[1]
    except IndexError:
        pass
    if(len(ConnectorPartName)>0):
        try:
            sql_statement = "SELECT ConnectorName from tblConn_Lib1 WHERE ConnectorName = "+'\''+tuple_Data[0]+'\''
            my_database = conn.execute(sql_statement) 
        except:
            pass
        n = my_database.fetchone()
        if(n==None):
            my_database.execute('insert into tblConn_Lib1(ConnectorName,Image) values (?,?)',(ConnectorPartName,Image))
            
        else:
            my_database.execute("update tblConn_Lib1 set Image = ? WHERE ConnectorName =?",(Image,ConnectorPartName))
            
    else:
        pass
    conn.commit()
def UploadCavityMap(CavityMap):
    try:
        tuple_Data = CavityMap
        connname=tuple_Data[0][0]
        conn = sqlite3.connect(GV.DBpath)
        my_database =conn.cursor()
        sql_statement='DELETE FROM tblConn_Lib2 where ConnectorName = '+'\''+connname+'\''
        my_database.execute(sql_statement)
        for x in range(len(tuple_Data)):
            try:
                ConnectorPartName=tuple_Data[x][0]
                CavityNo=tuple_Data[x][1]
                XCoordinate=tuple_Data[x][2]
                YCordinate=tuple_Data[x][3]
                Shape=tuple_Data[x][4]
                Size=tuple_Data[x][5]
                my_database.execute('insert into tblConn_Lib2(ConnectorName,CavityNo,X,Y,Shape,Size) values (?,?,?,?,?,?)',
                                    (ConnectorPartName,CavityNo,XCoordinate,YCordinate,Shape,Size))

            except IndexError:
                pass
        conn.commit()
    except(IndexError):
        print("Data not filled")
def DownloadConnectorImages():
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Id,ConnectorName,Image from tblConn_Lib1"
    
    my_database.execute(sql_statement)
    output = my_database.fetchall()
    for x in range (len(output)):
        if None in output[x]:
            hlist=list(output[x])
            hlist.remove(None)
            output[x]=tuple(hlist)
##    print('output',output)
    conn.commit()
    return(output)
def UploadFixtureType(Fixture_Setting):
    tuple_Data = Fixture_Setting
##    print("tuple_Data",tuple_Data)
    conn = sqlite3.connect(GV.DBpath)
    
    my_database =conn.cursor()
    for x in range(len(tuple_Data)):
        try:
            Id=tuple_Data[x][0]
            FixtureType=tuple_Data[x][1]
            LeakageStatus=tuple_Data[x][2]
            NavigationStatus=tuple_Data[x][3]
            ConnectorPresence=tuple_Data[x][4]
            SecondaryLock=tuple_Data[x][5]
            SensorInput=tuple_Data[x][6]
            EjectorStatus=tuple_Data[x][7]
            FixtureActuation=tuple_Data[x][8]
            
           
        
        except IndexError:
            pass
        sql_statement = "SELECT count(GroupNo) from tblFixtureType where GroupNo="+str(Id)
        my_database = conn.execute(sql_statement)
        n = my_database.fetchone()[0]
##        print("n",n)
        if(n==0):
            my_database.execute('insert into tblFixtureType(GroupNo,FixtureType,LeakageStatus,NavigationStatus,ConnectorPresence,SecondaryLock,SensorInput,\
                                EjectorStatus,FixtureActuation) values (?,?,?,?,?,?,?,?,?)',
                                (Id,FixtureType,LeakageStatus,NavigationStatus,ConnectorPresence,SecondaryLock,SensorInput,EjectorStatus,FixtureActuation))
        else:
            my_database.execute('update tblFixtureType set FixtureType = ?,LeakageStatus = ?,NavigationStatus= ?,ConnectorPresence= ?,\
                                SecondaryLock = ?,SensorInput= ?,EjectorStatus= ?,FixtureActuation= ? where GroupNo =?',
                                (FixtureType,LeakageStatus,NavigationStatus,ConnectorPresence,SecondaryLock,SensorInput,EjectorStatus,FixtureActuation,Id))
    conn.commit()
def DownloadFixtureType():
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT GroupNo,FixtureType from tblFixtureType"
    
    my_database.execute(sql_statement)
    output = my_database.fetchall()
##    print("output",output)
    conn.commit()
    return(output)
def UploadCutting_ChartData(Location,Type,Name,From,To,Color):
    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    Type=Type
    Name=Name
    From=From
    To=To
    Color=Color
    sql_statement ='DELETE FROM tblCutting_Chart WHERE Location ='+str(Location)
    my_database.execute(sql_statement)
    for i in range(len(From)):
        my_database.execute('insert into tblCutting_Chart(Location,Type,Name,From_Temp,To_Temp,Color) values(?,?,?,?,?,?)',(Location,Type,Name[i],From[i],To[i],Color[i]))
    conn.commit()
def DownloadCutting_ChartData(Location):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement="select Type,Name,From_Temp,To_Temp,Color from tblCutting_Chart where Location ="+str(Location)
    my_database.execute(sql_statement)
    output = my_database.fetchall()
    return (output)

#------------------------------------------------------------------------------------------------------------#
def UploadSplice1(img,CavityMap):
 
    tuple_Data = img
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    try:
        Location=tuple_Data[0]
        Stage=tuple_Data[1]
        NetSpliceNumber=tuple_Data[2]
        SliceName=tuple_Data[3]
        Image=tuple_Data[4]
    except IndexError:
        pass
    if(len(SliceName)>0):
        try:
            sql_statement = "SELECT NetSpliceName from tblSplice1 WHERE NetSpliceName = "+'\''+tuple_Data[3]+'\''
            my_database = conn.execute(sql_statement) 
        except:
            pass
        n = my_database.fetchone()
        if(n==None):
            my_database.execute('insert into tblSplice1(Location,Stage,NetSpliceNumber,NetSpliceName,Image) \
                        values(?,?,?,?,?)',(Location,Stage,NetSpliceNumber,SliceName,Image))
            UploadSplice2(CavityMap,'insert',conn,Location,Stage,NetSpliceNumber)
        else:
            print("CavityMap",CavityMap)
            my_database.execute("update tblSplice1 set Location=?,Stage=?,NetSpliceNumber=?,Image = ? \
            WHERE NetSpliceName =?",(Location,Stage,NetSpliceNumber,Image,SliceName))
            UploadSplice2(CavityMap,'update',conn,Location,Stage,NetSpliceNumber)
    else:
        pass
    conn.commit()

#=======================================================================================================================#

def DownloadSplice1(location,Netnumber):
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement = 'select Image from tblSplice1 where Location='+str(location)+' and NetSpliceNumber='+str(Netnumber)
    my_database = conn.execute(sql_statement)
    output = my_database.fetchall()
    conn.commit()
    return(output)
#===========================================================================================================================#
def UploadSplice2(CavityMap,mode,conn,Location,Stage,NetSpliceNumber):

    my_database = conn.cursor()
    tuple_Data = CavityMap
    sql_statement ='DELETE FROM tblSplice2 WHERE Location ='+str(Location)+' and NetSpliceNumber='+str(NetSpliceNumber)
    
    my_database.execute(sql_statement)
    for x in range(len(tuple_Data)):
        try:
            Splicename=tuple_Data[x][0]
            junctionname=tuple_Data[x][1]
            XCoordinate=tuple_Data[x][2]
            YCordinate=tuple_Data[x][3]
        
            
            my_database.execute('insert into tblSplice2(Location,Stage,NetSpliceNumber,NetSpliceName,Junction_Name,X_Coordinate,Y_Coordinate) \
            values (?,?,?,?,?,?,?)',(Location,Stage,NetSpliceNumber,Splicename,junctionname,XCoordinate,YCordinate))
##            elif(mode == 'update'):
##                print(Splicename,junctionname,XCoordinate,YCordinate,NetSpliceNumber,mode)
##                my_database.execute("update tblSplice2 set Location=?,Stage=?,NetSpliceNumber=?,Junction_Name=?,X_Coordinate = ?,Y_Coordinate=? WHERE NetSpliceName = ? \
##                ",(Location,Stage,NetSpliceNumber,junctionname,XCoordinate,YCordinate,Splicename))
####                                    (+'\''+str(Location)+'\'',+'\''+str(Stage)+'\'',+'\''+str(NetSpliceNumber)+'\'',+'\''+str(junctionname)+'\'',+'\''+str(XCoordinate)+'\'',+'\''+str(YCordinate)+'\'',+'\''+str(Splicename) ))
        except IndexError:
            pass
    conn.commit()
    
        

def DownloadSplice2():
    conn = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()                 
    my_database.execute( "select Location,Stage,NetSpliceNumber,Junction_No,Junction_Name,X_Coordinate,Y_Coordinate from tblSplice2")
    output = my_database.fetchall()
##    print("output",output)
    return (output)    
# =============================================================================

def DownloadAssetcode1(location):
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    my_database.execute("select FOQty,Mode,BarcodeNos,OpenSample,opSampleNos,ShortSample,shSampleNos,\
                        IntrchgSample,inSampleNos,ExtraSample,exSampleNos from tblAsset_code1 where location="+str(location))
    output = my_database.fetchall()
##    print("output",output)
    return (output)
def UploadFO_QTY(Location_No,FOQTY):
    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    my_database.execute('update tblAsset_code1 set FOQty = ? where location =?',(FOQTY,Location_No))
    conn.commit()
def UploadAssetcode1(Location_No,n_tuple_Data):
    print("harness save")
    Prod_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    for i in range(len(n_tuple_Data)):

        FoQuantity=n_tuple_Data[0]
        flow=n_tuple_Data[1]
        NoofBarcode=n_tuple_Data[2]
        OpenPoint=n_tuple_Data[3]
        OpCount=n_tuple_Data[4]
        Shortpoint=n_tuple_Data[5]
        Shcount=n_tuple_Data[6]
        Interchange=n_tuple_Data[7]
        Intercount=n_tuple_Data[8]
        ExtraPoint=n_tuple_Data[9]
        Extracount=n_tuple_Data[10]
        
        sql_statement = "SELECT count(Id) from tblAsset_code1 where location="+str(Prod_Location)
        my_database.execute(sql_statement)
        n = my_database.fetchone()[0]
##        print('my_database',n)
        if(n == 0):
            my_database.execute('INSERT  into tblAsset_code1(location,FOQty,Mode,BarcodeNos,OpenSample,opSampleNos,ShortSample,\
                                shSampleNos,IntrchgSample,inSampleNos,ExtraSample,exSampleNos) values(?,?,?,?,?,?,?,?,?,?,?,?)\
                                ',(Prod_Location,FoQuantity,flow,NoofBarcode,OpenPoint,OpCount,Shortpoint,Shcount,Interchange,Intercount,ExtraPoint,Extracount))
            conn.commit()
        else:    
            my_database.execute('update tblAsset_code1 set FOQty = ?, Mode = ?, BarcodeNos = ?, OpenSample = ?, \
                                opSampleNos = ?, ShortSample = ?, shSampleNos = ?, IntrchgSample = ?,inSampleNos = ?,ExtraSample = ?,exSampleNos = ? where location = ?\
                                ',(FoQuantity,flow,NoofBarcode,OpenPoint,OpCount,Shortpoint,Shcount,Interchange,Intercount,ExtraPoint,Extracount,Prod_Location))
            conn.commit()
    conn.close()
def UploadAssetcode2(Location_No,n_tuple_Data):
    print("harness save")
    Prod_Location=Location_No
    conn  = sqlite3.connect(GV.DBpath)
    my_database =conn.cursor()
    sql_statement ='DELETE FROM tblAsset_code2 WHERE Location ='+str(Prod_Location)
    my_database.execute(sql_statement)
    for i in range(len(n_tuple_Data)):
        myTuple=n_tuple_Data[i]
        Srno=myTuple[0]
        Bar_data=myTuple[1]
        custom_message=myTuple[2]

 
        my_database.execute('insert into tblAsset_code2(Location,Asset_no,Asset_code,DispMsg) values(?,?,?,?)',(Prod_Location,Srno,Bar_data,custom_message))
        
        conn.commit()          
    conn.close()   

def DownloadAssetcode2(location):
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    my_database.execute("select Asset_no,Asset_code,DispMsg from tblAsset_code2 where Location="+str(location))
    output = my_database.fetchall()
    ##    print("output",output)
    return (output)

def Uploadmsg_lib(custom_msg):
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    for i in range(len(custom_msg)):
        sql_statement="""update tblMsg_lib set MsgNo = ?, Message=? where id = ?"""
        my_database.execute(sql_statement,(custom_msg[i][0],custom_msg[i][1],(i+1)))
#        print(i)
        
    conn.commit()
    

def Downloadmsg_lib():
    conn = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    my_database.execute("select MsgNo,Message from tblMsg_lib")
    output = my_database.fetchall()
    ##    print("output",output)
    return (output)    
# ============================Find number of stages=================================================
def Get_num_stages(Location_No):
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    sql_statement = "SELECT Stage,NetNo,Point1,Point2 from tblHarness_Data where HarnessData_Location= '"+str(Location_No)+"'"
    # print(sql_statement)
    my_database.execute(sql_statement)
    output = my_database.fetchall()
    #print('output',output)
    No_ofstages=[]
    for i in range(len(output)):
        No_ofstages.append(output[i][0])
    try:
        #print(max(No_ofstages))
        GV.Num_Stages=max(No_ofstages)
        if(GV.Num_Stages>0):
            for i in range(GV.Num_Stages):
                GV.stage_list.append(i+1)
            print("GV. stage_list",GV.stage_list)
        else:
            GV.stage_list=[]

    except(ValueError):
        print("harness data not present location-"+str(Location_No))
        GV.Num_Stages=0
        GV.stage_list=[]
# ============================Delete HRN data=================================================

def DeleteHarnessData(Location_No):    
    conn  = sqlite3.connect(GV.DBpath)
    my_database = conn.cursor()
    HarnessData_Location=Location_No
    for i in range(GV.Num_Stages):
        sql_statement ='DELETE FROM tblHarness_Data WHERE HarnessData_Location ='+str(HarnessData_Location)+' AND '+'stage='+str(i+1)
        #print(sql_statement)
        my_database.execute(sql_statement)
    conn.commit()          
    conn.close()
# -----------------------------------------------------------------------------------------------------------


def Database_save():
    #print("GV.Location_No",GV.Location_No)
    UpLoadCableId(GV.Location_No,GV.Part_Name)
    x=[(GV.Pass_Count,GV.Fail_Count,GV.Stage1_status,GV.Stage1_Points_No,GV.Stage2_status,GV.Stage2_Points_No)]
    UploadCable_Info(GV.Location_No,x)
    
    UploadCable_Settings(GV.Location_No)
    Type="cnt"
    value= 0
    Tolerence=0
    Wire_Type=[]
    Wire_color1=[]
    Wire_color2=[]
    Wire_Gauge=[]

    if(GV.First_stage==1):
        circuits=GV.circuits
        stage=1
        for i in range(len(circuits)):
            Type="cnt"
            value= 0
            Tolerence=0
            Wire_Type.append('W')
            Wire_color1.append('BLU')
            Wire_color2.append('BLU')
            Wire_Gauge.append(0.5)
        UploadHarnessData(GV.Location_No,stage,Type,value,Tolerence,circuits,Wire_Type,Wire_color1,Wire_color2,Wire_Gauge)

    
    if(GV.Second_stage==1):
        
        circuits=GV.circuits1
##        print("second stage save",circuits)
        stage=2
        for i in range(len(circuits)):
            Type="cnt"
            value= 0
            Tolerence=0
            Wire_Type.append('W')
            Wire_color1.append('BLU')
            Wire_color2.append('BLU')
            Wire_Gauge.append(0.5)
        UploadHarnessData(GV.Location_No,stage,Type,value,Tolerence,circuits,Wire_Type,Wire_color1,Wire_color2,Wire_Gauge)

   
        
    
# =============================================================================

def Sqdb_to_Ram(state):
    # Get_num_stages(GV.Location_No)
    if(state==1):
        Get_num_stages(1)
        x=DownLoadCableId_boot()
        GV.Location_No=x[0][0]
        GV.Part_Name=x[0][1]
    elif(state==2):
        Get_num_stages(GV.Location_No)
        x=DownLoadCableId_change(GV.Location_No)
        GV.Part_Name=x[0][0]
    print("Location_No ....",GV.Location_No)
    GV.Open_points=[]
    GV.OpenPoint_count_temp=0
##    GV.FixtureInfo=DownloadFixtureType()
    GV.part_name_list=[]
    GV.part_name_list=DownloadCableId_All()
    GV.Local_Group2_File=DownloadLocal_Grp2(GV.Location_No)
    x=DownloadGlobal_Grp2()
    DownloadLocal_Grp2(GV.Location_No)
#========================Assetcode2===========================================
    GV.prod_data=[]
    GV.prod_data=DownloadAssetcode2(GV.Location_No)
    DownloadGlobal_Grp1()
##    print("GV.prod_data",GV.prod_data)
#==========================Assetcode1=========================================
    ast=DownloadAssetcode1(GV.Location_No)
    GV.sample_counter=0
    try:
        GV.FoQty=str(ast[0][0])
        GV.flow=str(ast[0][1])
        GV.Noofbar=str(ast[0][2])
        GV.OpenPoint=str(ast[0][3])
        GV.Opcount=str(ast[0][4])
        GV.ShortPoint=str(ast[0][5])
        GV.Shcount=str(ast[0][6])
        GV.Interchange=str(ast[0][7])
        GV.Intercount=str(ast[0][8])
        GV.ExtraPoint=str(ast[0][9])
        GV.Extracount=str(ast[0][10])
        if(GV.OpenPoint=='1'):
            GV.temp_openflag=GV.OpenPoint
            for i in range(int(GV.Opcount)):
                GV.sample_counter=GV.sample_counter+1
        if(GV.ShortPoint=='1'):
            GV.temp_shortflag=GV.ShortPoint
            GV.sample_counter=GV.sample_counter+1
        if(GV.Interchange=='1'):
            GV.temp_interchangeflag=GV.Interchange
            GV.sample_counter=GV.sample_counter+1
        if(GV.ExtraPoint=='1'):
            GV.temp_extraflag= GV.ExtraPoint
            GV.sample_counter=GV.sample_counter+1    
        print("GV.sample_counter",GV.sample_counter)
    except(IndexError):
        print("Data Not Present in DB")
        
#===========================================
    GV.library_mapping=[]
    GV.library_mapping = get_LibMap()
    
#============================sysConfiguation================================================
    config=DownloadConfiguration(1)
    GV.AssetCodeScan=str(config[0][0])
    GV.CableNos=str(config[0][1])
    GV.LeakageChannel=str(config[0][2])
    GV.LeakageTestTime=str(config[0][3])
    GV.LeakIterations=str(config[0][4])
    GV.ConectorVisual=str(config[0][5])
    GV.TesterNetwork=str(config[0][6])
    GV.Tracebility=str(config[0][7])
    GV.ProductionMonitoring=str(config[0][8])
    GV.DeviceInterface=str(config[0][9])
    GV.Report=str(config[0][10])
#======================userconfig==========================
    usecon=DownloadUserConfiguration(1)
    GV.AutoPartLoad=str(usecon[0][0])
    GV.PartNoLoc=str(usecon[0][1])
    GV.PartNO_Length=str(usecon[0][2])
    GV.UserVar1_Loc=str(usecon[0][3])
    GV.Var1_Length=str(usecon[0][4])
    GV.UserVar2_Loc=str(usecon[0][5])
    GV.Var2_Length=str(usecon[0][6])
    GV.UserVar3_Loc=str(usecon[0][7])
    GV.Var3_Length=str(usecon[0][8])
    GV.UserVar4_Loc=str(usecon[0][9])
    GV.Var4_Length=str(usecon[0][10])
    GV.Weekday_STD=str(usecon[0][11])
    GV.Shift_A=str(usecon[0][12])
    GV.A_timing=str(usecon[0][13])
    GV.Shift_B=str(usecon[0][14])
    GV.B_timing=str(usecon[0][15])
    GV.Shift_C=str(usecon[0][16])
    GV.C_timing=str(usecon[0][17])
#=========================cablesetting======================================
    DownloadCable_Settings(GV.Location_No)
    
    GV.Local_Cable_Info=DownloadCable_Info(GV.Location_No)
#=========================================================================
##    print("GV.Local_Cable_Info",GV.Local_Cable_Info)
    GV.Pass_Count=[]
    GV.Fail_Count=[]
    GV.Pass_Count=GV.Local_Cable_Info[0][0]
    GV.Fail_Count=GV.Local_Cable_Info[0][1]
    GV.Stage1_status=GV.Local_Cable_Info[0][2]
    GV.Stage1_Points_No=GV.Local_Cable_Info[0][3]
    GV.Stage2_status=GV.Local_Cable_Info[0][4]
    GV.Stage2_Points_No=GV.Local_Cable_Info[0][5]

    GV.circuits=[]
    GV.circuits1=[]
    DownloadComp_data(GV.Location_No,1)
    
    DownloadHarnessData(GV.Location_No,1)
    
    print("GV.Pass_Count,GV.Fail_Count",GV.Pass_Count,GV.Fail_Count)
  
    
    GV.QC_data_list=DownloadQC_Data(GV.Location_No)
    try:
        GV.Local_Label_Data=GV.QC_data_list[0][0]
        GV.Local_Label_Data2=GV.QC_data_list[0][1]
        GV.Local_Barcode1_Data=GV.QC_data_list[0][2]
        GV.Local_Barcode2_Data=GV.QC_data_list[0][3]
    except(TypeError):
        print("Data not available")
    GV.System_Info=DownloadSystemInfo(1)
    GV.admin_user=GV.System_Info[0]
    
    GV.super_user = DownloadSystemInfo(6)
##    print("super_user",GV.super_user)
    global_var.user_1 = GV.admin_user[0]
    global_var.user_1_pw = GV.admin_user[1]
    GV.System_Info=DownloadSystemInfo(2)
    GV.kt_user=GV.System_Info[0]
    global_var.user_2 = GV.kt_user[0]
    global_var.user_2_pw = GV.kt_user[1]



    
if __name__ == '__main__':
    print("1")
    # get_lastCTpin()
    # for i in range(1,129):
    #     print(i)
    #     UploadQC1_Data(i,'TestLBL1','testbarcode111','testbarcode222')
    #     UploadQC2_Data(i,'TestLBL2','testbarcode111','testbarcode222')
        # UploadQC_Data(100,'testdata2222','testbarcode111','testbarcode222')
##    Sqdb_to_Ram(1)
#     # Get_num_stages(1)
#     # print(GV.Num_Stages)
    # DownloadGlobal_Grp2()
##    conn  = sqlite3.connect(GV.DBpath)
##    my_database = conn.cursor()
##    for i in range (127):
##        PartName='TestPart'+ str(i+1)
##        sql_statement="""update tblCable_Id set PartName = ? where Location = ?"""
##        my_database.execute(sql_statement,(PartName,i+1))
##        
##    conn.commit()
    
    
##    Delete_Database_Table()
##    circuits=[]
##    circuits1=[]
##    circuits = [[1,2,3], [4,10]]
##    circuits1 = [[1,2,3,4,10]]
##    print(len(circuits))
##    stage=2
##    Type="cnt"
##    value= 0
##    Tolerence=0
##    Wire_Type = [('W1'),('W2'),('W3'),('W4')]
##    Wire_color1 = [('BLU'),('BLK'),('BLU'),('BLK')]
##    Wire_color2 = [('BLU'),('BLK'),('BLU'),('BLK')]
##    Wire_Gauge = [(0.5),(0.5),(0.5),(1)]
##    if(stage==1):
##        UploadHarnessData(2,stage,Type,value,Tolerence,circuits,Wire_Type,Wire_color1,Wire_color2,Wire_Gauge)
##    else:
##        UploadHarnessData(2,stage,Type,value,Tolerence,circuits1,Wire_Type,Wire_color1,Wire_color2,Wire_Gauge)
##
#    UploadSplice2(1,1,1,2,3,4,5)
##    GV.circuits=[]
##    DownloadHarnessData(1,1)
    #Connector_Image = convertToBinaryData('/home/pi/Desktop/amphenol.png')
    #UploadSplice1(2,3,4)
#    x= DownloadSplice2()
#    print(x)
##    x=DownloadCutting_ChartData()
    # print("1")
##    GV.Local_Group2_File=DownloadLocal_Grp2(5)
##    x=get_Points(1)
##    x=DownloadLocal_Grp2(5)
##    DownloadSplice1(1,1)
##    DownloadComp_data(1,1)
    # z=[1,4,5]
    # DownloadGlobal_Grp2_forlocalgrp(z)
#    Assetcode2data =[(1,"12344","scan barcode1"),(2,"asdc","scan barcode2"),(3,"erewret","scan barcode3")]
#    UploadAssetcode2(3,Assetcode2data)
#    custom_msg = [(1, "message1"), (2, "message2"),(3,"msg5"),(5,"msgdsadccsxczc")]
#    Uploadmsg_lib(custom_msg)
#    UploadAssetcode1()
#    x=Downloadmsg_lib()
#    print(x)
##    x=DownloadAssetcode2(3)
##    y=DownloadAssetcode1(1)
##    print(y)
##    
#    x=get_LibMap('P1')
#    print(x)
##
##    ConectorImages=[]
##    imgs=["/home/pi/Desktop/AWHT/code/tester_files/Connector_Images/conn1.png","/home/pi/Desktop/AWHT/code/tester_files/Connector_Images/conn2.png",
##          "/home/pi/Desktop/AWHT/code/tester_files/Connector_Images/conn3.png","/home/pi/Desktop/AWHT/code/tester_files/Connector_Images/conn4.png"]
##    for i in imgs:
##        
##        Connector_Image = convertToBinaryData(i)
##        ConectorImages.append(Connector_Image)
##    Images=[(1,'con1',ConectorImages[0]),(2,'con2',ConectorImages[1]),(3,'con3',ConectorImages[2]),(4,'con4',ConectorImages[3])]
##    UploadConnectorImages(Images)

##    Fixture_Setting=[(1,'continuity','Yes','No','No','No','No','No','No'),(2,'continuity','No','No','No','No','No','No','No'),(3,'continuity','No','No','No','No','No','No','No'),
##                     (4,'continuity','No','No','No','No','No','No','No'),(5,'continuity','No','No','No','No','No','No','No'),(6,'continuity','No','No','No','No','No','No','No')]
##    UploadFixtureType(Fixture_Setting)
##    x=DownloadFixtureType()
##    x=DownloadConnectorImages()
##    lsfp=[(111,'No','a1','con1','continuity',3,'No','No','No','No','No','No'),(112,'No','a2','con2','continuity',4,'No','No','No','No','No','No'),
##          (113,'No','b1','con3','continuity',4,'No','No','No','No','No','No'),(114,'No','b2','con4','continuity',3,'No','No','No','No','No','No'),
##          (115,'No','c1','con5','continuity',3,'No','No','No','No','No','No')]   
##    y=UploadGlobal_Grp1(lsfp)
    #x=DownloadGlobal_Grp1()
    #print(x)
#    DownloadGlobal_Grp1()
##    CavityMap=[(1,'con1',1,30,40,0,15),(2,'con1',2,40,50,0,25),(3,'con1',3,30,40,0,15),(4,'con2',1,30,40,0,15),(4,'con2',2,30,40,0,15)]
##    UploadCavityMap(CavityMap)
##    x=DownloadCavityMap()



    
    
##    DownloadLog('2020-12-26 14:50:56.774203','2020-12-28 09:15:55.107274')
##    UploadCable_Settings(4)
            
##    UploadSystemInfo('KT1234',2)
##    GV.Location_No=1

##    Sqdb_to_Ram(1)
##    Harnesdata_excel(1)
##    print(x)
##    Upload_Help(1)
    #uploadConfiguration(12)
    #sql_connection()
##    n=DownloadCableId_All()
##    DownloadCable_Info_all()
##    for i in range(101,129):
##    UpLoadCableId(17,'part23')
    
##   DownLoadCableId(1)
    
##    global_test_var.circuits=[]
##    DownloadHarnessData(1,1)
##    for i in range(3,128):
##        x=[(GV.Pass_Count,GV.Fail_Count,GV.Stage1_status,GV.Stage1_Points_No,GV.Stage2_status,GV.Stage2_Points_No)]
##        UploadCable_Info(i,x)
##    DownloadHarnessData1(1)
#    DownLoadCableId_boot()
#    DownLoadCableId_change(2)
   # UpLoadCableId(1,"cableid1234")
##    Local_Cable_Info = [(1,1,1,888,1,545)]
    #Local_Cable_Info=()
##    for i in range(30,128):
##    UploadCable_Info(128,Local_Cable_Info)
##    DownloadCable_Info(2)
##    print(x)
   
##    DownloadQC_Data(5)
##    Local_Settings_File=()
##    x=DownloadCable_Settings(1)
##    print(x)
                            
##    GV.Local_Settings_File = [(11,2,1,0,0,60,30,60,60,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)]
##    for i in range(5,129):
##        UploadCable_Settings(i)
##    DownloadLocal_Grp2(1)
##    x=DownloadGlobal_Grp2()
##    x=DownloadGlobal_Grp2_Cavity()
##    UploadLocal_Grp2(Location_No,lgrp2,cavity):
##    DownloadLocal_Grp1(1)
##    GV.System_Info=DownloadSystemInfo(2)
##    print(GV.System_Info)
##    GV.Barcode_Clear_Flag=GV.System_Info[0][1]
##    print("Barcode_Clear_Flag",GV.Barcode_Clear_Flag)
##    GV.Config_Info=DownloadConfiguration(1)
##    print("Config_Info",GV.Config_Info)
##    UploadLog_Data(1,'TestPart','TestEvent','TestDescription')
##    n_tuple_Data = [(1,5),(3,8,12),(9,10),(16,18,24)]
##    UploadLocal_Grp2(10,n_tuple_Data)
##    x=DownloadGLobal_Cable_Settings()

##    x=Downloadwirecolor()##    x=DownloadGlobal_Grp1()

##    GV.lgrp1=[('1', '2', '1', 'a111', 'a'), ('2', '3', '2', 'a2', 'b'), ('3', '2', '3', 'a3', 'c'),('6', '2', '3', 'a6', 'cu'),('7', '2', '3', 'a7', 'cu'),('8', '2', '3', 'a8', 'cu'),('9', '2', '3', 'a9', 'xy'),('10', '2', '1', 'a111', 'a'),('11', '2', '1', 'a111', 'a'),('12', '2', '1', 'a111', 'a')]
##    lgrp1=[('1', '2'), ('2', '3'), ('3', '2'),('6', '2'),('7', '2'),('8','1'),('9', '2')]
##    GV.lgrp1=[(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (11,), (12,)]
##    UploadLocal_Grp1(1,lgrp1)        
##    n_tuple_Data =[(1,1,3),(1,2,4),(1,3,2),(1,4,2),(1,4,3),(1,4,1),(1,5,6)]
##    UploadGlobal_Grp2(n_tuple_Data)
##    preference = ['W/H presense', 'Leak Test', '1st Stage', 'Printing', 'Match Label', 'Remove Harness', 'Report Generation', 0, 0, 0, 0, 0, 0, 0, 0]
##    UploadCable_OP_Settings(1,preference)
   
