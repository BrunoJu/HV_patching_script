#ScriptAim: Create HV patching ticket automatically
#Maintenance: BrunoJu/MichaelLukeli
#Version: 1.0


#Before using this script, please make sure you have sorted the servers in ervery sheet no matter A-Z or Z-A.
#It means to eliminate the in-between blank row.


import os,re
from openpyxl import load_workbook

#Insert the Work Excel you do.
wb = load_workbook(filename = 'C:\Users\c5258719\Desktop\progress_list_mar_10.xlsx')
#wb = load_workbook(filename = '//DWDF219/CPS_BIT_Ops/L2/tracking/Hypervisor Patching/progress_list_mar_12.xlsx')

#Initialize some Vars.
valid_sheets=[]
#First colum with server name
#You must change the number if it changed in Excel.
start_column= 8
#Find the bottom of every sheet
end_column= 0


#Get valid sheets list
for i in wb.sheetnames:
    if i.lstrip().rstrip().lower().find('summary') + i.lstrip().rstrip().lower().find('pool')== -2:
        valid_sheets.append(i)

#Get Hardware_pool source_server and target_server
for sheets_name in valid_sheets:
        specified_sheet=wb[sheets_name]


#Get the end_column number
        for i in range(start_column,100):
            if specified_sheet['A'+str(i)].value != None:
                ++i
            else:
                end_column = i

#Trun out the vars to create ticket.
        for i in range(start_column,end_column):
            if specified_sheet['D'+str(i)].value == None and \
                specified_sheet['C'+str(i)].value != None:
                print specified_sheet['A'+str(i)].value
                print specified_sheet['C'+str(i)].value
