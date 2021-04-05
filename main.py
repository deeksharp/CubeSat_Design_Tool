# Python:
import tkinter as tk                     
from tkinter import ttk
from tkinter.ttk import Combobox
import csv
# Subsystem Modules:
import PowerGUI as p
import PowerTool as PT
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
        plist = EPS_GUI.powerbudget2powerdesign()
    elif v0.get() == 2:
        EPS_GUI.powerdesign2payloadcapabilities()
    elif v0.get() == 3:
        EPS_GUI.payloadcapabilities2powerdesign()
    else:
        EPS_GUI.selectionError()

def runDesign():
    pd = PT.PowerTool().case1_PowerBudget2PowerDesign(EPS_GUI,oD,payD,cD,tD,aD,gD,cdhD,sD)
    print(pd.P_AVG_margin)
    
    
    
def outPutData():
    with open('parameters.csv', mode='w') as parameters:
        paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        paramWriter.writerow(comms)
        

# Initialize Parameter Class:
      
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
tabGNC = ttk.Frame(window)
tabCDH = ttk.Frame(window)
tabStructures = ttk.Frame(window)
tabRun = ttk.Frame(window)
window.add(tabMain, text ='Main') 
window.add(tabOrbits, text ='Orbits')
window.add(tabPayload, text ='Payload')
window.add(tabPower, text ='Power') 
window.add(tabComms, text ='Comms')
window.add(tabThermal, text ='Thermal') 
window.add(tabADCS, text ='ADCS')
window.add(tabGNC, text ='GNC')
window.add(tabCDH, text ='C&DH') 
window.add(tabStructures, text ='Structures')
window.add(tabRun, text ='Finish')
window.pack(expand = 1, fill ="both")

# Initialize Module Classes
oD = OT.Orbits()
payD = PayT.Payload()
cD = CT.Comms()
tD = TT.Thermal()
aD = AT.ADCS()
gD = GT.GNC()
cdhD = CDHT.CDH()
sD = ST.Structures()
EPS_GUI = p.Power() # Power GUI start

### Tab 1: Main ###
Header_1 = ttk.Label(tabMain,text ="Welcome to CubeSat Design Tool!")
Header_1.grid(column = 0, row = 0, padx = 10, pady = 10)


M1_L1 = ttk.Label(tabMain, text = 'Instructions:')
M1_L1.grid(column = 0, row = 1, padx = 10, pady = 10)
M1_L2= ttk.Label(tabMain, text = 'Read the instructions here when I write them.')
M1_L2.grid(column = 1, row = 1, padx = 10, pady = 10)

M2_L1 = ttk.Label(tabMain, text="CubeSat Size")
M2_L1.grid(column = 0, row = 2, padx = 10, pady = 10)
CubeSat_Sizes = ['1U', '2U', '3U']
var_Size = tk.StringVar(root)
var_Size.set(CubeSat_Sizes[0])
M2_DD1 = tk.OptionMenu(tabMain, var_Size, *CubeSat_Sizes) # Drop-Down
M2_DD1.grid(column = 1, row = 2, padx = 10, pady = 10)

M3_L1 = ttk.Label(tabMain, text='Design Name:')
M3_L1.grid(column = 0, row = 3, padx = 10, pady = 10)
M3_E2 = ttk.Entry(tabMain)
M3_E2.grid(column = 1, row = 3, padx = 10, pady = 10)

### Tab 2: Orbits ###
Header_2 = ttk.Label(tabOrbits,text ="Welcome to Orbits")
Header_2.grid(column = 0, row = 0, padx = 10, pady = 10)
L1 = tk.Label(tabOrbits, text="User Name")
L1.grid(column = 0, row = 1)
E1 = tk.Entry(tabOrbits)
E1.grid(column = 1, row = 1)

### Tab 3: Payload ###
Header_3 = ttk.Label(tabPayload,text ="Welcome to Orbits")
Header_3.grid(column = 0, row = 0, padx = 10, pady = 10)

### Tab 4: Power ###
Header_4 = tk.Label(tabPower,text ="Welcome to Power!")
Header_4.grid(column = 0, row = 0, padx = 10, pady = 10)

# Radiobutton Use Case Selection
v0=tk.IntVar()
P_RB1=ttk.Radiobutton(tabPower, text=" Power Budget to \n Power Design", variable=v0,value=1)
P_RB1.grid(column = 0, row = 2, padx = 10, pady = 10)
P_RB2=ttk.Radiobutton(tabPower, text=" Power Design to \n Payload Capabilities", variable=v0,value=2)
P_RB2.grid(column = 0, row = 3, padx = 10, pady = 10)
P_RB3=ttk.Radiobutton(tabPower, text=" Payload Capabilities \n to Power Design", variable=v0,value=3)
P_RB3.grid(column = 0, row = 4, padx = 10, pady = 10)

P_L1L = P_L2 = ttk.Label(tabPower, text='Use Case:')
P_L1L.grid(column = 0, row = 1, padx = 10, pady = 10)
P_L1M = P_L2 = ttk.Label(tabPower, text='Description:')
P_L1M.grid(column = 1, row = 1, padx = 10, pady = 10)
P_L2M = ttk.Label(tabPower, text='A power budget is already developed, and an EPS '+
                 'design is desired', wraplength = 200)
P_L2M.grid(column = 1, row = 2, padx = 10, pady = 10)
P_L3M = ttk.Label(tabPower, text='An EPS design is baselined, and the ' +
                 'subsequent spacecraft performance is desired', wraplength = 200)
P_L3M.grid(column = 1, row = 3, padx = 10, pady = 10)
P_L4M = ttk.Label(tabPower, text='Payload capability requirements are provided, and an ' +
                 'EPS design is desired.', wraplength = 200)
P_L4M.grid(column = 1, row = 4, padx = 10, pady = 10)

P_L2R = ttk.Label(tabPower, text='Inputs, Outputs, and Assumptions:', wraplength = 125)
P_L2R.grid(column = 2, row = 1, padx = 10, pady = 10)
P_btn2 = ttk.Button(tabPower, text = "More Info")
P_btn2.grid(column = 2, row = 2)
P_btn3 = ttk.Button(tabPower, text = "More Info")
P_btn3.grid(column = 2, row = 3)
P_btn4 = ttk.Button(tabPower, text = "More Info")
P_btn4.grid(column = 2, row = 4)


P_btn = ttk.Button(tabPower, text = "Input", command = openPower)
P_btn.grid(column = 2, row = 5, padx = 10, pady = 10)



### Tab 5: Comms ###
Header_5 = ttk.Label(tabComms,text ="Welcome to Communications")
Header_5.grid(column = 0, row = 0, padx = 10, pady = 10)

# Drop Down List for Use Cases
CM_UseCases = ['Use Case 1', 'Use Case 2', 'Use Case 3']
var_CM = tk.StringVar(root)
var_CM.set(CM_UseCases[0])
CM_dropdown = tk.OptionMenu(tabComms, var_CM, *CM_UseCases)
CM_dropdown.grid(column = 2, row = 0, padx = 5, pady = 5)


### Tab 6: Finish ###
Header_6 = ttk.Label(tabRun,text ="Press Button to Run Design and Output Parameters")
Header_6.pack()
RUN_btn = ttk.Button(tabRun, text = "Run", command = runDesign) # Note: Only outputs parameters now
RUN_btn.pack()


root.mainloop() # run it







