# Python:
import tkinter as tk                     
from tkinter import ttk
from tkinter.ttk import Combobox
import csv

# Subsystem Modules:
import PowerGUI as p
import CommsGUI as c
import PowerTool as PT
import CommsTool as CM
import Orbit_Test as OT
import Pay_Test as PayT
import Comm_Test as CT
import Ther_Test as TT
import ADCS_Test as AT
import GNC_Test as GT
import CDH_Test as CDHT
import Stru_Test as ST

def openPower():
    if v0.get() == 1:
        EPS.powerbudget2powerdesign()
    elif v0.get() == 2:
        EPS.subsystemdesign2powerdesign()
    else:
        EPS.selectionError()
        
def openComms():
        cD.linkbudget4demo()

def openOrbits():
    oD.selectOrbit()

def powerInfo(infoX):
    p.Power().moreInfo(infoX)

def runDesign():
    """
    pd = PT.PowerTool()
    p = pd.case1_PowerBudget2PowerDesign(EPS,oD,payD,cD,tD,aD,gD,cdhD,sD)
    pd.writeData(p) """
    
    cd = CM.CommsTool()
    tool = cd.LinkBudget4Demo(cD)
    cd.writeData(tool)
    
def outPutData():
    with open('parameters.csv', mode='w') as parameters:
        paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        paramWriter.writerow('something')

      
root = tk.Tk() # Instance of Tk,
root.title("CubeSat Design Tool") # Name
window = ttk.Notebook(root) # tkk module implements "tabs" (Notebook)

  
# Create the Various Tabs
tabMain = ttk.Frame(window) 
tabOrbits = ttk.Frame(window)
tabPayload = ttk.Frame(window)
tabPower = ttk.Frame(window)
tabComms = ttk.Frame(window)
tabThermal = ttk.Frame(window)
tabADCS = ttk.Frame(window)
tabProps = ttk.Frame(window)
tabGNC = ttk.Frame(window)
tabCDH = ttk.Frame(window)
tabStructures = ttk.Frame(window)
tabRun = ttk.Frame(window)
window.add(tabMain, text ='Main') 
window.add(tabOrbits, text ='Orbits')
window.add(tabPayload, text ='Payload')
window.add(tabPower, text ='EPS') 
window.add(tabComms, text ='Comms')
window.add(tabThermal, text ='Thermal') 
window.add(tabADCS, text ='ADCS')
window.add(tabGNC, text ='GNC')
window.add(tabCDH, text ='C&DH') 
window.add(tabProps, text = 'Propulsion')
window.add(tabStructures, text ='Structures')
window.add(tabRun, text ='Finish')
window.pack(expand = 1, fill ="both")

# Initialize Module Classes
oD = OT.Orbits()
payD = PayT.Payload()
cD = c.Comms() #Comms GUI start
tD = TT.Thermal()
aD = AT.ADCS()
gD = GT.GNC()
cdhD = CDHT.CDH()
sD = ST.Structures()
EPS = p.Power() # Power GUI start

# Initialize System Variables
CubeSat_Size = ''
CubeSat_Name = ''

### Tab 1: Main ###
Header_1 = ttk.Label(tabMain,text ="Welcome to CubeSat Conceptual Design Tool!")
Header_1.grid(column = 0, row = 0, padx = 10, pady = 10,columnspan=2)


M1_L1 = ttk.Label(tabMain, text = 'Instructions:')
M1_L1.grid(column = 0, row = 1, padx = 10, pady = 10, sticky='nw')
instructions = 'Make your way through the conceptual design tool entering data into the '\
    'different tabs as requested. Follow instructions for the individual subsystems. Some '\
    'tabs will require selecting design Use Cases to be selected based on what the '\
    'available inputs are.'
M1_L2= ttk.Label(tabMain, text = instructions, wraplength = 450)
M1_L2.grid(column = 1, row = 1, padx = 10, pady = 10)

M2_L1 = ttk.Label(tabMain, text='Estimated CubeSat Size:')
M2_L1.grid(column = 0, row = 2, padx = 10, pady = 10, sticky = 'w')
CubeSat_Sizes = ['','1U', '1.5U', '2U', '3U', '6U', '12U']
var_Size = tk.StringVar(root)
var_Size.set(CubeSat_Sizes[0])
M2_DD1 = ttk.OptionMenu(tabMain, var_Size, *CubeSat_Sizes) # Drop-Down
M2_DD1.grid(column = 1, row = 2, padx = 10, pady = 10, sticky = 'w')

M3_L1 = ttk.Label(tabMain, text='Design Name:')
M3_L1.grid(column = 0, row = 3, padx = 10, pady = 10, sticky='w')
M3_E2 = ttk.Entry(tabMain)
M3_E2.grid(column = 1, row = 3, padx = 10, pady = 10, sticky='w')

sub_btn = ttk.Button(tabMain, text = "Submit")
sub_btn.grid(column = 1, row = 4, sticky = 'e')


### Tab 2: Orbits ###
Header_2 = ttk.Label(tabOrbits,text ="Welcome to the Orbit Test Module!", anchor = 'w')
Header_2.grid(column = 0, row = 0, padx = 10, pady = 10,columnspan = 2)
Orb_instructions = ttk.Label(tabOrbits, text='Push button to select orbital parameters')
Orb_instructions.grid(column = 0, row = 1, padx = 10, pady = 10)
Orb_btn = ttk.Button(tabOrbits, text = 'Input Orbit', command=openOrbits)
Orb_btn.grid(column = 2, row = 1)


### Tab 3: Payload ###
Header_3 = ttk.Label(tabPayload,text ="Welcome to Payload!")
Header_3.grid(column = 0, row = 0, padx = 10, pady = 10)

### Tab 4: Power ###
Header_4 = ttk.Label(tabPower,text ="Welcome to Power!")
Header_4.grid(column = 0, row = 0, padx = 10, pady = 10)

# Radiobutton Use Case Selection
v0=tk.IntVar(root)
P_RB1=ttk.Radiobutton(tabPower, text=" Power Budget to \n Power Design", variable=v0,value=1)
P_RB1.grid(column = 0, row = 2, padx = 10, pady = 10,sticky='w')
P_RB2=ttk.Radiobutton(tabPower, text=" Subsystem Design to \n Power Design", variable=v0,value=2)
P_RB2.grid(column = 0, row = 3, padx = 10, pady = 10,sticky='w')

P_L1L = P_L2 = ttk.Label(tabPower, text='Use Case:')
P_L1L.grid(column = 0, row = 1, padx = 10, pady = 10)
P_L1M = P_L2 = ttk.Label(tabPower, text='Description:')
P_L1M.grid(column = 1, row = 1, padx = 10, pady = 10)
t = 'A power budget is already developed and needs to be input. An EPS design is desired.'
P_L2M = ttk.Label(tabPower, text=t, wraplength = 300)
P_L2M.grid(column = 1, row = 2, padx = 10, pady = 10,sticky='w')
t = 'The subsystems are all developed, leading to their power requirements in '\
    'the tool already. An EPS design is desired based on this.' 
P_L3M = ttk.Label(tabPower, text=t, wraplength = 300)
P_L3M.grid(column = 1, row = 3, padx = 10, pady = 10,sticky='w')


P_L2R = ttk.Label(tabPower, text='Inputs, Outputs, and Assumptions:', wraplength = 150)
P_L2R.grid(column = 2, row = 1, padx = 10, pady = 10)
P_btn2 = ttk.Button(tabPower, text = "More Info", command = lambda: powerInfo(1))
P_btn2.grid(column = 2, row = 2)
P_btn3 = ttk.Button(tabPower, text = "More Info", command = lambda: powerInfo(2))
P_btn3.grid(column = 2, row = 3)

P_btn = ttk.Button(tabPower, text = "Select", command = openPower)
P_btn.grid(column = 2, row = 4, padx = 10, pady = 10)

### Tab 5: Comms ###
Header_5 = ttk.Label(tabComms,text ="Welcome to Communications!")
Header_5.grid(column = 0, row = 0, padx = 10, pady = 10)

# Radiobutton Use Case Selection
v1=tk.IntVar(root)
C_RB1=ttk.Radiobutton(tabComms, text=" Link Budget for \n Demo Mission", variable=v0,value=1)
C_RB1.grid(column = 0, row = 2, padx = 10, pady = 10,sticky='w')
C_RB2=ttk.Radiobutton(tabComms, text=" TBD", variable=v0,value=2)
C_RB2.grid(column = 0, row = 3, padx = 10, pady = 10,sticky='w')

C_L1L = P_L2 = ttk.Label(tabComms, text='Use Case:')
C_L1L.grid(column = 0, row = 1, padx = 10, pady = 10)
C_L1M = P_L2 = ttk.Label(tabComms, text='Description:')
C_L1M.grid(column = 1, row = 1, padx = 10, pady = 10)
t = 'Standard Communications Design for a technology demonstration mission.'
C_L2M = ttk.Label(tabComms, text=t, wraplength = 300)
C_L2M.grid(column = 1, row = 2, padx = 10, pady = 10,sticky='w')
t = 'TBD '
C_L3M = ttk.Label(tabComms, text=t, wraplength = 300)
C_L3M.grid(column = 1, row = 3, padx = 10, pady = 10,sticky='w')


C_L2R = ttk.Label(tabComms, text='Inputs, Outputs, and Assumptions:', wraplength = 150)
C_L2R.grid(column = 2, row = 1, padx = 10, pady = 10)
C_btn2 = ttk.Button(tabComms, text = "More Info", command = lambda: powerInfo(1))
C_btn2.grid(column = 2, row = 2)
C_btn3 = ttk.Button(tabComms, text = "More Info", command = lambda: powerInfo(2))
C_btn3.grid(column = 2, row = 3)

P_btn = ttk.Button(tabComms, text = "Select", command = openComms)
P_btn.grid(column = 2, row = 4, padx = 10, pady = 10)


### Tab 6: Thermal ###
Header_6 = ttk.Label(tabThermal,text ="Welcome to Thermal!")
Header_6.grid(column = 0, row = 0, padx = 10, pady = 10)

### Tab 7: Thermal ###
Header_7 = ttk.Label(tabADCS,text ="Welcome to ADCS!")
Header_7.grid(column = 0, row = 0, padx = 10, pady = 10)

### Tab 8: GNC ###
Header_8 = ttk.Label(tabGNC,text ="Welcome to GNC!")
Header_8.grid(column = 0, row = 0, padx = 10, pady = 10)

### Tab 9: C&DH ###
Header_9 = ttk.Label(tabCDH,text ="Welcome to C&DH!")
Header_9.grid(column = 0, row = 0, padx = 10, pady = 10)

### Tab 8: GNC ###
Header_10 = ttk.Label(tabStructures,text ="Welcome to Structures!")
Header_10.grid(column = 0, row = 0, padx = 10, pady = 10)

### Tab 11: Finish ###
Header_11 = ttk.Label(tabRun,text ="Press Button to Run the Conceptual Design Process\n")
Header_11.pack()
instr =  'Resulting output file may be found in the folder the encloses the tool, as a '\
        'CSV file with the design name as the file name. Follow the Instructions on file to import this '\
        'data into the MBSE CubeSat Model'
Instruction_11 = ttk.Label(tabRun,text = instr, wraplength = 500, anchor='w')
Instruction_11.pack()
RUN_btn = ttk.Button(tabRun, text = "Run", command = runDesign) # Note: Only outputs parameters now
RUN_btn.pack()

root.mainloop() # run it







