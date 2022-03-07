import global_test_var as GV
import sqlite3
from  Sql_db import *

z=[]
w=[]
HWCTPin=[]
tempGrp_data=[]
GV.Local_Group_data=[]
for i in range (len(GV.circuits)):
	for j in range (len(GV.circuits[i])):
		for k in range (len(GV.Group_data)):
			if (GV.circuits[i][j] in (GV.Group_data[k])):
				if(((GV.Group_data.index(GV.Group_data[k]))+1) not in z):
					z.append(GV.Group_data.index((GV.Group_data[k]))+1)


DownloadGlobal_Grp2_forlocalgrp(z)



for i in range (len(w)):
        tuple_data=w[i]
        for j in range (len(tuple_data)):
                if ('CT' in tuple_data[j]):
                        HWCTPin.append(tuple_data[j])
##        print(tuple_data)
print("HWCTPin",HWCTPin)


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

# print("GV.Local_Group_data",GV.Local_Group_data)
##        UploadLocal_Grp2(GV.Location_No,tuple_data)
