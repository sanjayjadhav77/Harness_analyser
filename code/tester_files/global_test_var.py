
#======================================================
# from _typeshed import SupportsKeysAndGetItem
#------------------------------------------Database path-------------------------------------------------------------------------------------
global DBpath
DBpath='/home/pi/Desktop/.HA_Editor/code/tester_files/HA_Gen_2.0.db'
global exit
exit=0
global led1
led1=[]
#----------------------------------------------------------------------------------------------------------------------------------

global System_Shuffle
System_Shuffle=0
#=======================================================
global test_count
test_count=0
global library_mapping
library_mapping=[]
# ======================================leak Test=======================================
global switch_status,Stop_Leakage
switch_status=[]
Stop_Leakage=0
# Cable Id
# =============================================================================
global Location_No, Part_Name,part_name_list
part_name_list=[]
##Location_No=1
# =============================================================================
#Global Grp1
#==============================================================================
global Leakage_Test_status
global Fixture_Position

global No_Of_Cavities
global CavityNo
global Connector_Part_Name
#============================componenttesting=================================
global Component_Type
global Comp_value
global Tollerance
global Unit
global point1
global point2
global comp_display,component_test
component_test=[]

comp_display=[]
Component_Type=''
Comp_value=0
Tollerance=0
Unit=''
point1=0
point2=0
#====================================eventbutonflag=========================
global Abort_Event_flag,Start_Event_flag
Abort_Event_flag=0
Start_Event_flag=0
global Clear_scan
Clear_scan=0
global PrvEstate
PrvEstate=0
global Check_bypass
Check_bypass=0
global checkboard_to_engine
checkboard_to_engine=0
global is_card_sequential
is_card_sequential=0
#===========================testing Flow====================================
global Sample
Sample=0
global List_message
List_message=''
global Num_Stages
Num_Stages=0
global Holdstate
Holdstate=0
global stage_list
stage_list=[]
global source
source=''
global GRP_source
GRP_source=''
global Allcircuit_error
Allcircuit_error=0
#====================================report===================================
global Serial_No
Serial_No=0
global filename,name
name=' '
filename=[]
#===============================================================================
# Cable Info
# =============================================================================
global Pass_Count, Fail_Count, Stage1_status,Stage1_Points_No,Stage2_status, Stage2_Points_No,Local_Cable_Info
global Stage2
global Sflag
global Second_stage
Second_stage=1
Pass_Count=0
Fail_Count=0
# =============================================================================
#===============================================congiguration==============================
global barcode_master_data
global AssetCodeScan
global CableNos
global LeakageChannel
global LeakageTestTime
global LeakIterations
global ConectorVisual
global TesterNetwork
global Tracebility
global ProductionMonitoring
global DeviceInterface
global AutoPartLoad
global PartNoLoc
global PartNO_Length
global UserVar1_Loc
global Var1_Length
global UserVar2_Loc
global Var2_Length
global UserVar3_Loc
global Var3_Length
global UserVar4_Loc
global Var4_Length
global Weekday_STD
global Shift_A
global A_timing
global Shift_B
global B_timing
global Shift_C
global C_timing
global Report
global user_config_flag
user_config_flag=0
barcode_master_data=''
Report=''
AssetCodeScan=''
CableNos='0'
LeakageChannel=''
LeakageTestTime='0'
LeakIterations='0'
ConectorVisual=''
TesterNetwork=''
Tracebility=''
ProductionMonitoring=''
DeviceInterface=''
AutoPartLoad=''
PartNoLoc=''
PartNO_Length=''
UserVar1_Loc=''
Var1_Length=''
UserVar2_Loc=''
Var2_Length=''
UserVar3_Loc=''
Var3_Length=''
UserVar4_Loc=''
Var4_Length=''
Weekday_STD='0'
Shift_A=''
A_timing='0'
Shift_B=''
B_timing='0'
Shift_C=''
C_timing='0'


# =============================================================================
# QC data
# =============================================================================
global QC_data_list
global Local_Label_Data,Local_Label_Data2, Local_Barcode1_Data, Local_Barcode2_Data
# =============================================================================
# Local_Group2_File
# =============================================================================
global special_pins,leakage,switch,led,virtual_pins,Actual_pins
global leakage_gbl,switch_gbl,led_gbl
global ckt_net,chekb_data
global data_Available,data_delivered
global selftest_pin,Switch_status,Switch_display,Group_data,Local_Group_data
global Local_Group_data_display
global LocalGrpNo
leakage_gbl=[]
switch_gbl=[]
led_gbl=[]
LocalGrpNo=[]
Local_Group_data_display=[]
Group_data=[]
Local_Group_data=[]
Switch_display=[]
Switch_status=[]
selftest_pin=[]
data_Available=0
data_delivered=0
chekb_data=[]
ckt_net=[]
special_pins=[]
Actual_pins=[]
leakage=[]
switch=[]
led=[]
virtual_pins=[]
global Local_Group2_File,Local_Group1_File
global group_sort
global Local_Group3_File
group_sort=[]
Local_Group2_File=[]
Local_Group3_File=[]
global unused_pin
unused_pin=[]
# =============================================================================
# System_info
# =============================================================================
global System_Info
global OneD_Barcode_Sample,TwoD_Barcode_Sample,Barcode_Clear_Flag,kt_user,admin_user,super_user
# =============================================================================
# setting file
# =============================================================================

global Local_Settings_File
global Release_Time,Fail_Time, Q_Mark_Time,Buzzer_Status,Cutter_status, Open_point_Timeout, Short_point_Timeout
global Interchange_point_Timeout,Extra_point_Timeout, LabelPrint,LabelNos,Barcode_Match, No_Of_Barcodes,Component_status,All_Error
global Auto_Mode,External_Interface,Leak_test_yn,NoofStages,All_circuits_Mode
NoofStages=0
Release_Time=1
Q_Mark_Time=1
Fail_Time=1
Buzzer_Status=1
ExtraPointTest=0
Cutter_status=0
Open_point_Timeout=10
Short_point_Timeout=10
Interchange_point_Timeout=10
Extra_point_Timeout=10
LabelPrint=1
LabelNos=1
Barcode_Match=0
No_Of_Barcodes=0
Component_status=0
All_Error=0
All_circuits_Mode=1
Testing_Mode=0
WH_on_bar=0
WH_Presense=0
Leak_test=0
Leak_test_yn=0
External_Interface=0
Auto_Mode=0
Buzzer_Status=0
Cutter_status=0
LabelPrint=0

LabelNos=1
Barcode_Match=0
No_Of_Barcodes=1

# ========================================FOQTY=============================================================================================
global prod_data
global Fo_test_Flag
Fo_test_Flag=0

prod_data=[]
global prod_Setting
prod_Setting = []
global flow
global Noofbar
global FoQty
global Opcount
global Shcount
global Intercount
global Extracount
global OpenPoint
global ShortPoint
global Interchange
global ExtraPoint
global barcount
global Sample_result
Sample_result=0
barcount=0
flow=''
Noofbar='0'
FoQty='0'
Opcount='0'
Shcount='0'
Intercount='0'
Extracount='0'
OpenPoint= '0'
ShortPoint= '0'
Interchange= '0'
ExtraPoint= '0'
#=============================fixture library=================================================
global FixtureInfo
FixtureInfo=[]
#==============================group library====================================
global lstCTP
global LstHWP
global r_data
r_data=[]
lstCTP=0
LstHWP=0
global Leakage
Leakage=0
global navigation
navigation=0
global connpresence
connpresence=0
global seclock
seclock=0
global sensor_input
sensor_input=0
global ejectorstatus
ejectorstatus =0
global fix_actuation
fix_actuation=0
#========================================================================================================
# Help Data
# =============================================================================
global Leakage_Testing
# =============================================================================
# Harness Data
# =============================================================================
global circuits
global circuits1,circuits2,circuits3,circuits4,circuits5,circuits6,circuits7
global circuits_temp
global Temp_circuits
global All_circuits
global Wire_Name
global Wire_color1
global Wire_color2
global Wire_Gauge
global Wire_Type
global stage
global method


global cavity1
global connector1
global connector1_name
global wtype1
global wcolor1a
global wcolor1b
global wgauge1

global cavity2
global connector2
global connector2_name
global wtype2
global wcolor2a
global wcolor2b
global wgauge2

global Visual_Engine_Start
global GroupEditFlag
global ClickOn_Next
global Cutting_circuits
stage=0
method=0
circuits_temp=[]
GroupEditFlag=0
ClickOn_Next=0
Visual_Engine_Start=0
cavity1=0
connector1=0
connector1_name=0
wtype1=0
wcolor1a=' '
wcolor1b=' '
wgauge1=0

cavity2=0
connector2=0
connector2_name=0
wtype2=0
wcolor2a=' '
wcolor2b=' '
wgauge2=0
#===============================================================================
# Date time variables
global HMS,hrs,mint,sec,DMY,date,mon,year,week_no,week_day
#=================================================================================
#barcode file var
global bar1_data,bar2_data
#===============================================================================
# led navigation  variables
global Connetor_present_flag,connector_count,connector_message
Connetor_present_flag=0
connector_count=0

global leakage_message
global Remove_connector_message

# connector Remove
global Connector_remove_flag
Connector_remove_flag=0

global database_save_flag
database_save_flag=0

global short_array,Self_test_flag
short_array=[]
Self_test_flag=0

# =============================================================================
# General variables.
# =============================================================================
global Printer_Flag

global conn
conn=0
global tested_circuits
global x,y
global msg
global pass_harness
global remove_cable
global put_cable
global test_cycle
global loop_flag
# global HA
global open_point
global open_pt1
global open_pt2
global open_point_continue
global extra_point
global short_point
global grp_short_point
global interchange
global intpoint1,intpoint2
global enter_flag
global extra_point_continue
global short_point_continue
global grp_short_point_continue
global interchange_point_continue
global interchange_flag
global change
global check_point
global checkboard_list  ##CheckBoard
global stop_event
global total_point
global count
global cir_length
global cir_length1
global open_timeout
global learn_flag
global checkboard_flag
global msg_update

global Leakage_Test
global Previous_Time
global Current_Time
global time_gap

# global Privious_x
# global Privious_y
global code_1
global code_2
global lbl_print_done
global flagx
global mission_abort
global Grid1,Grid2
global Connector_test_abort
global Stage2_start
global lsfp
global short_pin
short_pin=[]
#====================================Cutiing Chart============================================
# global Wire_Type
# global Wire_color1
global Cutting_tuple
Cutting_tuple=[(1,'W3','BLK'),(2,'W3','BLU')]
global From_Temp
global To_Temp
global Name_Temp
global Color_Temp
global WireGauge_Temp
global cutting_chartData
cutting_chartData=[]
From_Temp=[]
To_Temp=[]
Name_Temp=[]
Color_Temp=[]
WireGauge_Temp=[]


global Board_Learn
Board_Learn=1
#=====================================engine variables=========================

global serialobj,Hold
Hold=0
serialobj='0'
global Cutter_Action
Cutter_Action=0
global scan_data,SERIAL_NUMBER
SERIAL_NUMBER=0
scan_data=''
global module_no,Estate,scan_complete,HA,Display_Message,Abort_flag
Abort_flag=0
Display_Message=''
HA=0
scan_complete=0
module_no=0
Estate=0
global bus
global Card_counter
global message
global s
global error_flag
global pin_number
global pin_status
global IO_error_code
global Intruption_code
global Intruption_flag
global update
global Privious_x,Privious_intpoint1
global Privious_y,Privious_intpoint2
global Multi_stage,Stages_complete
global Open_points
global sample_counter
global Sample_Production
global msgpriority
global OpenPoint_test
global OpenPoint_sample1
global OpenPoint_count
global OpenPoint_count_temp
global ShortPoint_sample
global Interchange_sample
global ExtraPoint_sample
global temp_openflag,temp_shortflag,temp_extraflag,temp_interchangeflag
temp_openflag=0
temp_shortflag=0
temp_extraflag=0
temp_interchangeflag=0
Sample_Production=0
Privious_x=0
Privious_y=0
Privious_intpoint1=0
Privious_intpoint2=0
Multi_stage=1
Stages_complete=0
update=0
Intruption_code=0
Intruption_flag=1
IO_error_code=0
error_flag=0
Card_counter = 0
Open_points=[]
sample_counter=0
msgpriority=0
OpenPoint_test=0
OpenPoint_sample1=0
OpenPoint_count=0
ShortPoint_sample=0
Interchange_sample=0
ExtraPoint_sample=0
OpenPoint_count_temp=0

#====================================Connector Visuals============================================
global grp_id
#===========================================led navigation=============================================================
global lastled1,lastled2
lastled1=0
lastled2=0
#=======================================================================================
#leakage state fixture position
grp_id=" "
Connector_test_abort=0
Grid1=" "
Grid2=" "
mission_abort=1

lbl_print_done=0
code_1=0
code_2=0
Cutter_status=1



Previous_Time=0
Current_Time=0
time_gap=0

# Privious_x=0
# Privious_y=0

count=0
msg=15
enter_flag=0
stop_event=0
# HA=0

Leakage_Test_status=[]
Fixture_Position=[]
No_Of_Cavities=[]
Connector_Part_Name=[]
CavityNo=[]

circuits=[[1,2],[3,4],[5,6]]
circuits1=[[1,2],[3,4]]
circuits2=[]
circuits3=[]
circuits4=[]
circuits5=[]
circuits6=[]
circuits7=[]

Temp_circuits=[]
cir_length1=len(circuits1)
cir_length=len(circuits)
pin_number=0
read_value=0
data=0

calbytes=[]
total_card=7
total_card1=0
card_array=[0,128,256,384,512,640,768,896,1024,1152,1280]
total_point=card_array[total_card]
x=1
y=1
tested_circuits=[]
open_timeout=10

learn_flag=0
checkboard_flag=0
checkboard_list=[]
msg_update=0

Printer_Flag=0
flagx=1
Stage2_start=0
Sflag=0

global message_color
message_color=1

global point_count
point_count=0

