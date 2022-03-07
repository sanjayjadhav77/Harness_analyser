import sqlite3



def DeleteHarnessData(Location_No):    
    conn  = sqlite3.connect('/home/pi/Desktop/.HA_Editor/Restore/HA_Gen_2.0.db')
    my_database = conn.cursor()
    HarnessData_Location=Location_No
    for i in range(Num_stages):
        sql_statement ='DELETE FROM tblHarness_Data WHERE HarnessData_Location ='+str(HarnessData_Location)+' AND '+'stage='+str(i+1)
        print(sql_statement)
        my_database.execute(sql_statement)
    conn.commit()          
    conn.close()

Location_No=22
Num_stages=3
DeleteHarnessData(Location_No)
