import tkinter as tk
from tkinter import ttk
        

 
class Power:
    def __init__(self):
        # Initialize Power Data
        self.UseCase: int
        
        # Power Data:
        self.P_AVG: float
        self.per_margin: float
        self.P_margin: float
        self.P_AVG_margin: float
        
        # Use Case #1 Inputs:
        self.mode1_name: str
        self.mode2_name: str
        self.mode3_name: str
        self.mode4_name: str

        self.ADCS_P1: float
        self.ADCS_D1: float
        self.ADCS_P2: float
        self.ADCS_D2: float
        self.ADCS_P3: float
        self.ADCS_D3: float
        self.ADCS_P4: float
        self.ADCS_D4: float

        self.CDH_P1: float
        self.CDH_D1: float
        self.CDH_P2: float
        self.CDH_D2: float
        self.CDH_P3: float
        self.CDH_D3: float
        self.CDH_P4: float
        self.CDH_D4: float

        self.GNC_P1: float
        self.GNC_D1: float
        self.GNC_P2: float
        self.GNC_D2: float
        self.GNC_P3: float
        self.GNC_D3: float
        self.GNC_P4: float
        self.GNC_D4: float

        self.PAY_P1: float
        self.PAY_D1: float
        self.PAY_P2: float
        self.PAY_D2: float
        self.PAY_P3: float
        self.PAY_D3: float
        self.PAY_P4: float
        self.PAY_D4: float

        self.STRU_P1: float
        self.STRU_D1: float
        self.STRU_P2: float
        self.STRU_D2: float
        self.STRU_P3: float
        self.STRU_D3: float
        self.STRU_P4: float
        self.STRU_D4: float

        self.COMM_P1: float
        self.COMM_D1: float
        self.COMM_P2: float
        self.COMM_D2: float
        self.COMM_P3: float
        self.COMM_D3: float
        self.COMM_P4: float
        self.COMM_D4: float

        self.EPS_P1: float
        self.EPS_D1: float
        self.EPS_P2: float
        self.EPS_D2: float
        self.EPS_P3: float
        self.EPS_D3: float
        self.EPS_P4: float
        self.EPS_D4: float

        self.THER_P1: float
        self.THER_D1: float
        self.THER_P2: float
        self.THER_D2: float
        self.THER_P3: float
        self.THER_D3: float
        self.THER_P4: float
        self.THER_D4: float


        # Use Case #2 Inputs
        self.ADCS_AVG: float
        self.CDH_AVG: float
        self.COMM_AVG: float
        self.EPS_AVG: float
        self.GNC_AVG: float
        self.PAY_AVG: float
        self.STRU_AVG: float
        self.THER_AVG: float
        self.SP_eff_bol: float
        self.SP_area: float
        self.SP_point: bool
        self.SP_deploy: bool
        self.cell_eff: float
        self.cell_mass: float
        self.cell_dens: float
        self.bat_cap: float
        self.bat_dod: float
        self.PDU_eff: float
        self.PDU_mass: float
        self.PDU_data: float

        # Total Design:


        # Other Power Parameters:
        self.solar_flux: float
    
    def moreInfo(self, x):
        self.powergui = tk.Tk() # Instance of Tk,
        self.powergui.title("Electrical Power Subsystem Design Module") # Name
        self.powerwindow = ttk.Notebook(self.powergui) # tkk module implements "tabs" (Notebook)
        self.tabInputs = ttk.Frame(self.powerwindow)
        self.tabAssums = ttk.Frame(self.powerwindow)
        self.tabCalcs = ttk.Frame(self.powerwindow)
        self.powerwindow.add(self.tabInputs, text = 'Inputs')
        self.powerwindow.add(self.tabAssums, text = 'Assumptions')
        self.powerwindow.add(self.tabCalcs, text = 'Calculations')
        self.powerwindow.pack(expand = 1, fill ="both")

        if x == 1:
            self.T1_R0_C0 = ttk.Label(self.tabInputs, text='Power Budget:', wraplength = 200)
            self.T1_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
            self.T1_R0_C1 = ttk.Label(self.tabInputs, text='Power [W] and Duty Cycle [%] for all subsystems', wraplength = 200)
            self.T1_R0_C1.grid(row = 0, column = 1, padx = 5, pady = 5)
            self.T1_R1_C0 = ttk.Label(self.tabInputs, text='Power Margin:', wraplength = 200)
            self.T1_R1_C0.grid(row = 1, column = 0, padx = 5, pady = 5)
            self.T1_R1_C1 = ttk.Label(self.tabInputs, text='Margin for the power budget', wraplength = 200)
            self.T1_R1_C1.grid(row = 1, column = 1, padx = 5, pady = 5)
            
            t = 'Assumed values include constants, such as solar flux, \
                as well as design sizing parameters for the spacecraft.'
            self.T2_R0_C0 = ttk.Label(self.tabAssums, text=t, wraplength = 200)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)

            t = 'Calculated values include size of solar panel and batteries, \
                as well as total power values.'
            self.T2_R0_C0 = ttk.Label(self.tabCalcs, text=t, wraplength = 200)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
            
        elif x == 2:
            t = 'Input values include basic power levels for subsystems, \
                as well as design sizing parameters for the spacecraft.'
            self.T1_R0_C0 = ttk.Label(self.tabInputs, text=t, wraplength = 200)
            self.T1_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)

            t = 'Assumed values include constants, such as solar flux, \
                as well as design sizing parameters for the spacecraft.'
            self.T2_R0_C0 = ttk.Label(self.tabAssums, text=t, wraplength = 200)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)

            t = 'Calculated values include size of solar panel and batteries, \
                as well as total power values.'
            self.T3_R0_C0 = ttk.Label(self.tabCalcs, text=t, wraplength = 200)
            self.T3_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)

        elif x == 3:
            t = 'something'
            self.T1_R0_C0 = ttk.Label(self.tabInputs, text=t, wraplength = 200)
            self.T1_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)

            t = 'something'
            self.T2_R0_C0 = ttk.Label(self.tabAssums, text=t, wraplength = 200)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)

            t = 'something'
            self.T3_R0_C0 = ttk.Label(self.tabCalcs, text=t, wraplength = 200)
            self.T3_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
            pass


    #def notEnoughInfo(self):
    #def wrongUnits(self):

    def allDone(self):
        self.powergui.destroy()

    
    def powerbudget2powerdesign(self):
        self.powergui = tk.Tk() # Instance of Tk,
        self.powergui.title("Electrical Power Subsystem Design Module") # Name
        self.powerwindow = ttk.Notebook(self.powergui) # tkk module implements "tabs" (Notebook)
        self.tabBudget = ttk.Frame(self.powerwindow)

        w = 5
        self.E_per_margin = ttk.Entry(self.tabBudget,width=w)

        self.E_ADCS_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_D4 = ttk.Entry(self.tabBudget, width = w)

        self.E_CDH_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_D4 = ttk.Entry(self.tabBudget, width = w)

        self.E_GNC_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_D4 = ttk.Entry(self.tabBudget, width = w)

        self.E_PAY_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_D4 = ttk.Entry(self.tabBudget, width = w)

        self.E_STRU_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_D4 = ttk.Entry(self.tabBudget, width = w)

        self.E_COMM_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_D4 = ttk.Entry(self.tabBudget, width = w)

        self.E_EPS_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_D4 = ttk.Entry(self.tabBudget, width = w)

        self.E_THER_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_D1 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_D2 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_D3 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_D4 = ttk.Entry(self.tabBudget, width = w)

        # Create Tab
        self.powerwindow.add(self.tabBudget, text = 'Power Budget Input')
        self.powerwindow.pack(expand = 1, fill ="both")

        # Instructions
        self.R0_C0 = ttk.Label(self.tabBudget, text='Please input your spacecraft power budget here:', wraplength = 500)
        self.R0_C0.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
        
        # Row Titles
        R=2; C=0
        ttk.Label(self.tabBudget, text='ADCS', anchor = 'e', width = 15).grid(row=R, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='C&DH', anchor = 'e', width = 15).grid(row=R+1, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='COMMS', anchor = 'e', width = 15).grid(row=R+2, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='EPS', anchor = 'e', width = 15).grid(row=R+3, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='GNC', anchor = 'e', width = 15).grid(row=R+4, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='Payload', anchor = 'e', width = 15).grid(row=R+5, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='Structures', anchor = 'e', width = 15).grid(row=R+6, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='Thermal', anchor = 'e', width = 15).grid(row=R+7, column=C, padx=5, pady=5)

        # Column Titles
        R=1; C=1
        ttk.Label(self.tabBudget, text='Mode 1: Power [W]').grid(row=R, column=C, padx=2.5, pady=5)
        ttk.Label(self.tabBudget, text='Mode 1: Duty Cycle [%]').grid(row=R, column=C+1, padx=2.5, pady=5)
        ttk.Label(self.tabBudget, text='Mode 2: Power [W]').grid(row=R, column=C+2, padx=2.5, pady=5)
        ttk.Label(self.tabBudget, text='Mode 2: Duty Cycle [%]').grid(row=R, column=C+3, padx=2.5, pady=5)
        
        # Entries
        self.E_ADCS_P1.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.E_ADCS_D1.grid(row = 2, column = 2, padx = 5, pady = 5)
        self.E_ADCS_P2.grid(row = 2, column = 3, padx = 5, pady = 5)
        self.E_ADCS_D2.grid(row = 2, column = 4, padx = 5, pady = 5)
        self.E_ADCS_P3.grid(row = 2, column = 5, padx = 5, pady = 5)
        self.E_ADCS_D3.grid(row = 2, column = 6, padx = 5, pady = 5)
        self.E_ADCS_P4.grid(row = 2, column = 7, padx = 5, pady = 5)
        self.E_ADCS_D4.grid(row = 2, column = 8, padx = 5, pady = 5)

        self.E_CDH_P1.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.E_CDH_D1.grid(row = 3, column = 2, padx = 5, pady = 5)
        self.E_CDH_P2.grid(row = 3, column = 3, padx = 5, pady = 5)
        self.E_CDH_D2.grid(row = 3, column = 4, padx = 5, pady = 5)
        self.E_CDH_P3.grid(row = 3, column = 5, padx = 5, pady = 5)
        self.E_CDH_D3.grid(row = 3, column = 6, padx = 5, pady = 5)
        self.E_CDH_P4.grid(row = 3, column = 7, padx = 5, pady = 5)
        self.E_CDH_D4.grid(row = 3, column = 8, padx = 5, pady = 5)

        self.E_COMM_P1.grid(row = 4, column = 1, padx = 5, pady = 5)
        self.E_COMM_D1.grid(row = 4, column = 2, padx = 5, pady = 5)
        self.E_COMM_P2.grid(row = 4, column = 3, padx = 5, pady = 5)
        self.E_COMM_D2.grid(row = 4, column = 4, padx = 5, pady = 5)
        self.E_COMM_P3.grid(row = 4, column = 5, padx = 5, pady = 5)
        self.E_COMM_D3.grid(row = 4, column = 6, padx = 5, pady = 5)
        self.E_COMM_P4.grid(row = 4, column = 7, padx = 5, pady = 5)
        self.E_COMM_D4.grid(row = 4, column = 8, padx = 5, pady = 5)

        self.E_EPS_P1.grid(row = 5, column = 1, padx = 5, pady = 5)
        self.E_EPS_D1.grid(row = 5, column = 2, padx = 5, pady = 5)
        self.E_EPS_P2.grid(row = 5, column = 3, padx = 5, pady = 5)
        self.E_EPS_D2.grid(row = 5, column = 4, padx = 5, pady = 5)
        self.E_EPS_P3.grid(row = 5, column = 5, padx = 5, pady = 5)
        self.E_EPS_D3.grid(row = 5, column = 6, padx = 5, pady = 5)
        self.E_EPS_P4.grid(row = 5, column = 7, padx = 5, pady = 5)
        self.E_EPS_D4.grid(row = 5, column = 8, padx = 5, pady = 5)

        self.E_GNC_P1.grid(row = 6, column = 1, padx = 5, pady = 5)
        self.E_GNC_D1.grid(row = 6, column = 2, padx = 5, pady = 5)
        self.E_GNC_P2.grid(row = 6, column = 3, padx = 5, pady = 5)
        self.E_GNC_D2.grid(row = 6, column = 4, padx = 5, pady = 5)
        self.E_GNC_P3.grid(row = 6, column = 5, padx = 5, pady = 5)
        self.E_GNC_D3.grid(row = 6, column = 6, padx = 5, pady = 5)
        self.E_GNC_P4.grid(row = 6, column = 7, padx = 5, pady = 5)
        self.E_GNC_D4.grid(row = 6, column = 8, padx = 5, pady = 5)

        self.E_PAY_P1.grid(row = 7, column = 1, padx = 5, pady = 5)
        self.E_PAY_D1.grid(row = 7, column = 2, padx = 5, pady = 5)
        self.E_PAY_P2.grid(row = 7, column = 3, padx = 5, pady = 5)
        self.E_PAY_D2.grid(row = 7, column = 4, padx = 5, pady = 5)
        self.E_PAY_P3.grid(row = 7, column = 5, padx = 5, pady = 5)
        self.E_PAY_D3.grid(row = 7, column = 6, padx = 5, pady = 5)
        self.E_PAY_P4.grid(row = 7, column = 7, padx = 5, pady = 5)
        self.E_PAY_D4.grid(row = 7, column = 8, padx = 5, pady = 5)

        self.E_STRU_P1.grid(row = 8, column = 1, padx = 5, pady = 5)
        self.E_STRU_D1.grid(row = 8, column = 2, padx = 5, pady = 5)
        self.E_STRU_P2.grid(row = 8, column = 3, padx = 5, pady = 5)
        self.E_STRU_D2.grid(row = 8, column = 4, padx = 5, pady = 5)
        self.E_STRU_P3.grid(row = 8, column = 5, padx = 5, pady = 5)
        self.E_STRU_D3.grid(row = 8, column = 6, padx = 5, pady = 5)
        self.E_STRU_P4.grid(row = 8, column = 7, padx = 5, pady = 5)
        self.E_STRU_D4.grid(row = 8, column = 8, padx = 5, pady = 5)

        self.E_THER_P1.grid(row = 9, column = 1, padx = 5, pady = 5)
        self.E_THER_D1.grid(row = 9, column = 2, padx = 5, pady = 5)
        self.E_THER_P2.grid(row = 9, column = 3, padx = 5, pady = 5)
        self.E_THER_D2.grid(row = 9, column = 4, padx = 5, pady = 5)
        self.E_THER_P3.grid(row = 9, column = 5, padx = 5, pady = 5)
        self.E_THER_D3.grid(row = 9, column = 6, padx = 5, pady = 5)
        self.E_THER_P4.grid(row = 9, column = 7, padx = 5, pady = 5)
        self.E_THER_D4.grid(row = 9, column = 8, padx = 5, pady = 5)

        # Power Margin
        ttk.Label(self.tabBudget, text='Power Margin [%]').grid(row=10, column=0,padx=5, pady=5)
        self.E_per_margin.grid(row=10,column=1,padx=5,pady=5)
        # Submit Button
        self.UseCase = 1
        self.sub_btn = ttk.Button(self.tabBudget, text = "Submit", command = self.inputPower)
        self.sub_btn.grid(column = 3, row = 10)
        # Done Button
        self.fin_btn = ttk.Button(self.tabBudget, text = "Finish", command = self.allDone)
        self.fin_btn.grid(column = 4, row = 10)
        # Run
        self.powergui.mainloop()

        
            
        

    def powerdesign2payloadcapabilities(self):
        self.powergui = tk.Tk() # Instance of Tk,
        self.powergui.title("Electrical Power Subsystem Design Module") # Name
        self.powerwindow = ttk.Notebook(self.powergui) # tkk module implements "tabs" (Notebook)
        self.tabDesign = ttk.Frame(self.powerwindow)
        self.powerwindow.add(self.tabDesign, text = 'EPS Design Input')
        self.powerwindow.pack(expand = 1, fill ="both")

        w = 4

        self.E_SP_eff_bol = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_area = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_point = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_deploy = ttk.Entry(self.tabDesign, width = w)
        self.E_cell_eff = ttk.Entry(self.tabDesign, width = w)
        self.E_cell_mass = ttk.Entry(self.tabDesign, width = w)
        self.E_cell_density = ttk.Entry(self.tabDesign, width = w)
        self.E_bat_cap = ttk.Entry(self.tabDesign, width = w)
        self.E_bat_dod = ttk.Entry(self.tabDesign, width = w)
        self.E_PDU_eff = ttk.Entry(self.tabDesign, width = w)
        self.E_PDU_mass = ttk.Entry(self.tabDesign, width = w)
        self.E_PDU_data = ttk.Entry(self.tabDesign, width = w)

        self.E_ADCS_AVG = ttk.Entry(self.tabDesign, width = w)
        self.E_CDH_AVG = ttk.Entry(self.tabDesign, width = w)
        self.E_COMM_AVG = ttk.Entry(self.tabDesign, width = w)
        self.E_EPS_AVG = ttk.Entry(self.tabDesign, width = w)
        self.E_GNC_AVG = ttk.Entry(self.tabDesign, width = w)
        self.E_PAY_AVG = ttk.Entry(self.tabDesign, width = w)
        self.E_STRU_AVG = ttk.Entry(self.tabDesign, width = w)
        self.E_THER_AVG = ttk.Entry(self.tabDesign, width = w)

        # Title
        self.R0_C0 = ttk.Label(self.tabDesign, text='Input Spacecraft Design Parameters Here or Select a Spacecraft Bus')
        self.R0_C0.grid(row = 0, column = 0,  columnspan = 4, padx = 5, pady = 5)

        # Spacecraft Selection:
##        self.R1_C0 = ttk.Label(self.tabDesign, text = 'Select a SpaceCraft Bus (if desired)')
##        self.R1_C0.grid(row = 1, column = 0, padx = 5, pady = 5)
##        self.SC_Buses = ['Customize', '1U Bus', '3U Bus']
##        self.var_Bus = tk.StringVar()
##        self.R1_C1 = ttk.OptionMenu(self.tabDesign, self.var_Bus, self.SC_Buses[0], *self.SC_Buses)
##        self.R1_C1.grid(row = 1, column = 1, padx = 5, pady = 5)
##        self.R1_C2 = ttk.Button(self.tabDesign, text = 'Bus Info')
##        self.R1_C2.grid(row = 1, column = 2, padx = 5, pady = 5)
##        self.R1_C3 = ttk.Button(self.tabDesign, text = "Submit Selection")
##        self.R1_C3.grid(row = 1, column = 3, padx = 5, pady = 5)
        
##        # Enter Custom Values
##        R2_C0 = ttk.Label(self.tabDesign, text='Input Power Design Parameters:')
##        R2_C0.grid(row = 1, column = 0, padx = 5, pady = 5)

        # Subsystem Average Values
        R=1; C=0
        AVG_Title = ttk.Label(self.tabDesign, text='Subsystem Average Power [W]:', wraplength = 125, justify = 'center')
        AVG_Title.grid(row=R, column=C, columnspan = 2, padx = 5, pady = 5)
        R=2; C=0; w = 7; x = 3; y = 3
        ttk.Label(self.tabDesign, text='ADCS', anchor = 'w', width = w).grid(row=R, column=C, padx=x, pady=y)
        ttk.Label(self.tabDesign, text='C&DH', anchor = 'w', width = w).grid(row=R+1, column=C, padx=x, pady=y)
        ttk.Label(self.tabDesign, text='COMMS', anchor = 'w', width = w).grid(row=R+2, column=C, padx=x, pady=y)
        ttk.Label(self.tabDesign, text='EPS', anchor = 'w', width = w).grid(row=R+3, column=C, padx=x, pady=y)
        ttk.Label(self.tabDesign, text='GNC', anchor = 'w', width = w).grid(row=R+4, column=C, padx=x, pady=y)
        ttk.Label(self.tabDesign, text='Structures', anchor = 'w', width = w).grid(row=R+5, column=C, padx=x, pady=y)
        ttk.Label(self.tabDesign, text='Thermal', anchor = 'w', width = w).grid(row=R+6, column=C, padx=x, pady=y)
        self.E_ADCS_AVG.grid(row = R, column = C+1, padx = x, pady = y)
        self.E_CDH_AVG.grid(row = R+1, column = C+1, padx = x, pady = y)
        self.E_COMM_AVG.grid(row = R+2, column = C+1, padx = x, pady = y)
        self.E_EPS_AVG.grid(row = R+3, column = C+1, padx = x, pady = y)
        self.E_GNC_AVG.grid(row = R+4, column = C+1, padx = x, pady = y)
        self.E_STRU_AVG.grid(row = R+5, column = C+1, padx = x, pady = y)
        self.E_THER_AVG.grid(row = R+6, column = C+1, padx = x, pady = y)

        # Solar Column
        R=1; C=2
        SP_Title = ttk.Label(self.tabDesign, text='Solar Sizing:', wraplength = 125, justify = 'center')
        SP_Title.grid(row=R, column=C, columnspan = 2, padx = 5, pady = 5)

        # Solar Cell Efficiency
        R = 2; C = 2
        ttk.Label(self.tabDesign, text='Solar Cell Efficiency').grid(row=R, column=C, padx=5, pady=5)
        self.E_SP_eff_bol.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='%').grid(row=R, column=C+2, padx=5, pady=5)

        # Solar Cell Area
        R = 3; C = 2
        ttk.Label(self.tabDesign, text='Solar Cell Area').grid(row=R, column=C, padx=5, pady=5)
        self.E_SP_area.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='m^2').grid(row=R, column=C+2, padx=5, pady=5)

        # Pointing
        R = 4; C = 2
        ttk.Label(self.tabDesign, text='Does?').grid(row=R, column=C, columnspan=3, padx=5, pady=5)
        
        # Deployable
        R = 6; C = 2
        ttk.Label(self.tabDesign, text='Are the panels pointing?').grid(row=R, column=C, columnspan=3, padx=5, pady=5)

        self.E_cell_eff = ttk.Entry(self.tabDesign, width = 6)
        self.E_cell_mass = ttk.Entry(self.tabDesign, width = 6)
        self.E_cell_density = ttk.Entry(self.tabDesign, width = 6)
        self.E_bat_cap = ttk.Entry(self.tabDesign, width = 6)
        self.E_bat_dod = ttk.Entry(self.tabDesign, width = 6)

        # Battery Density:
        R = 2; C = 5
        ttk.Label(self.tabDesign, text='Energy Density').grid(row=R, column=C, padx=5, pady=5)
        self.E_cell_density.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='Wh/kg').grid(row=R, column=C+2, padx=5, pady=5)

        # Battery Capacity:
        R = 3; C = 5
        ttk.Label(self.tabDesign, text='Battery Capacity').grid(row=R, column=C, padx=5, pady=5)
        self.E_bat_cap.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='Wh').grid(row=R, column=C+2, padx=5, pady=5)

        # Cell Mass:
        R = 4; C = 5
        ttk.Label(self.tabDesign, text='Cell Mass').grid(row=R, column=C, padx=5, pady=5)
        self.E_cell_mass.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='kg').grid(row=R, column=C+2, padx=5, pady=5)
        
        # Battery Efficiency (One Way):
        R = 5; C = 5
        ttk.Label(self.tabDesign, text='One-way Efficiency').grid(row=R, column=C, padx=5, pady=5)
        self.E_cell_eff.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='%').grid(row=R, column=C+2, padx=5, pady=5)

        # Battery Depth-of-Discharge:
        R = 6; C = 5
        ttk.Label(self.tabDesign, text='Depth-of-Discharge').grid(row=R, column=C, padx=5, pady=5)
        self.E_bat_dod.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='%').grid(row=R, column=C+2, padx=5, pady=5)

        
        # PDU Mass
        R = 2; C = 8
        ttk.Label(self.tabDesign, text='PDU Mass').grid(row=R, column=C, padx=5, pady=5)
        self.E_PDU_mass.grid(row=R, column=C+1, padx = 5, pady = 5)
        ttk.Label(self.tabDesign, text='kg').grid(row=R, column=C+2, padx=5, pady=5)
        # PDU Efficiency
        R = 3; C = 8
        ttk.Label(self.tabDesign, text='PDU Efficiency').grid(row=R, column=C, padx=5, pady=5)
        self.E_PDU_eff.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='%').grid(row=R, column=C+2, padx=5, pady=5)
        # PDU Data Rate
        R = 4; C = 8
        ttk.Label(self.tabDesign, text='PDU Data Rate').grid(row=R, column=C, padx=5, pady=5)
        self.E_PDU_data.grid(row=R, column=C+1, padx=5, pady=5)
        ttk.Label(self.tabDesign, text='bps').grid(row=R, column=C+2, padx=5, pady=5)

        # Submit Button
        self.UseCase = 2
        self.pow_btn = ttk.Button(self.tabDesign, text = "Submit", command = self.inputPower)
        self.pow_btn.grid(column=C+2, row=R+1)
        
        # Run
        self.powergui.mainloop()


        
                               
    def payloadcapabilities2powerdesign(self):
        self.powergui = tk.Tk() # Instance of Tk,
        self.powergui.title("Electrical Power Subsystem Design Module") # Name
        self.powerwindow = ttk.Notebook(self.powergui) # tkk module implements "tabs" (Notebook)
        self.tabCap = ttk.Frame(self.powerwindow)
        self.powerwindow.add(self.tabCap, text = 'EPS General Input')
        self.powerwindow.pack(expand = 1, fill ="both")

        self.R0_C0 = ttk.Label(self.tabCap, text='Please input your spacecraft power budget here:', wraplength = 200)
        self.R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.powergui.mainloop()


    def inputPower(self):
        if self.UseCase == 1:
            try:
                self.per_margin = float(self.E_per_margin)
                
                self.ADCS_P1 = float(self.E_ADCS_P1.get())
                self.ADCS_D1 = float(self.E_ADCS_D1.get())
                self.ADCS_P2 = float(self.E_ADCS_P2.get())
                self.ADCS_D2 = float(self.E_ADCS_D2.get())
                self.ADCS_P3 = float(self.E_ADCS_P3.get())
                self.ADCS_D3 = float(self.E_ADCS_D3.get())
                self.ADCS_P4 = float(self.E_ADCS_P4.get())
                self.ADCS_D4 = float(self.E_ADCS_D4.get())

                self.CDH_P1 = float(self.E_CDH_P1.get())
                self.CDH_D1 = float(self.E_CDH_D1.get())
                self.CDH_P2 = float(self.E_CDH_P2.get())
                self.CDH_D2 = float(self.E_CDH_D2.get())
                self.CDH_P3 = float(self.E_CDH_P3.get())
                self.CDH_D3 = float(self.E_CDH_D3.get())
                self.CDH_P4 = float(self.E_CDH_P4.get())
                self.CDH_D4 = float(self.E_CDH_D4.get())

                self.COMM_P1 = float(self.E_COMM_P1.get())
                self.COMM_D1 = float(self.E_COMM_D1.get())
                self.COMM_P2 = float(self.E_COMM_P2.get())
                self.COMM_D2 = float(self.E_COMM_D2.get())
                self.COMM_P3 = float(self.E_COMM_P1.get())
                self.COMM_D3 = float(self.E_COMM_D1.get())
                self.COMM_P4 = float(self.E_COMM_P2.get())
                self.COMM_D4 = float(self.E_COMM_D2.get())

                self.EPS_P1 = float(self.E_EPS_P1.get())
                self.EPS_D1 = float(self.E_EPS_D1.get())
                self.EPS_P2 = float(self.E_EPS_P2.get())
                self.EPS_D2 = float(self.E_EPS_D2.get())
                self.EPS_P3 = float(self.E_EPS_P3.get())
                self.EPS_D3 = float(self.E_EPS_D3.get())
                self.EPS_P4 = float(self.E_EPS_P4.get())
                self.EPS_D4 = float(self.E_EPS_D4.get())

                self.GNC_P1 = float(self.E_GNC_P1.get())
                self.GNC_D1 = float(self.E_GNC_D1.get())
                self.GNC_P2 = float(self.E_GNC_P2.get())
                self.GNC_D2 = float(self.E_GNC_D2.get())
                self.GNC_P3 = float(self.E_GNC_P3.get())
                self.GNC_D3 = float(self.E_GNC_D3.get())
                self.GNC_P4 = float(self.E_GNC_P4.get())
                self.GNC_D4 = float(self.E_GNC_D4.get())

                self.PAY_P1 = float(self.E_PAY_P1.get())
                self.PAY_D1 = float(self.E_PAY_D1.get())
                self.PAY_P2 = float(self.E_PAY_P2.get())
                self.PAY_D2 = float(self.E_PAY_D2.get())
                self.PAY_P3 = float(self.E_PAY_P3.get())
                self.PAY_D3 = float(self.E_PAY_D3.get())
                self.PAY_P4 = float(self.E_PAY_P4.get())
                self.PAY_D4 = float(self.E_PAY_D4.get())

                self.STRU_P1 = float(self.E_STRU_P1.get())
                self.STRU_D1 = float(self.E_STRU_D1.get())
                self.STRU_P2 = float(self.E_STRU_P2.get())
                self.STRU_D2 = float(self.E_STRU_D2.get())
                self.STRU_P3 = float(self.E_STRU_P3.get())
                self.STRU_D3 = float(self.E_STRU_D3.get())
                self.STRU_P4 = float(self.E_STRU_P4.get())
                self.STRU_D4 = float(self.E_STRU_D4.get())

                self.THER_P1 = float(self.E_THER_P1.get())
                self.THER_D1 = float(self.E_THER_D1.get())
                self.THER_P2 = float(self.E_THER_P2.get())
                self.THER_D2 = float(self.E_THER_D2.get())
                self.THER_P3 = float(self.E_THER_P3.get())
                self.THER_D3 = float(self.E_THER_D3.get())
                self.THER_P4 = float(self.E_THER_P4.get())
                self.THER_D4 = float(self.E_THER_D4.get())

            except:
                pass
        elif self.UseCase == 2:
            try:
                self.ADCS_AVG = float(self.E_ADCS_AVG.get())
                self.CDH_AVG = float(self.E_CDH_AVG.get())
                self.COMM_AVG = float(self.E_COMM_AVG.get())
                self.EPS_AVG = float(self.E_EPS_AVG.get())
                self.GNC_AVG = float(self.E_GNC_AVG.get())
                self.PAY_AVG = float(self.E_PAY_AVG.get())
                self.STRU_AVG = float(self.E_STRU_AVG.get())
                self.THER_AVG = float(self.E_THER_AVG.get())
                self.SP_eff_bol = float(self.E_SP_eff_bol.get())
                self.SP_area = float(self.E_SP_area.get())
                self.SP_point = int(self.E_SP_point.get())
                self.SP_deploy = int(self.E_SP_deploy.get())
                self.cell_eff = float(self.E_cell_eff.get())
                self.cell_mass = float(self.E_cell_mass.get())
                self.cell_density = float(self.E_cell_density.get())
                self.bat_cap = float(self.E_bat_cap.get())
                self.bat_dod = float(self.E_bat_dod.get())
                self.PDU_eff = float(self.E_PDU_eff.get())
                self.PDU_mass = float(self.E_PDU_mass.get())
                self.PDU_data = float(self.E_PDU_data.get())
            except:
                pass

    def selectionError(self):
            self.powergui = tk.Tk() # Instance of Tk,
            self.powergui.title("Electrical Power Subsystem Design Module") # Name
            self.powerwindow = ttk.Notebook(self.powergui) # tkk module implements "tabs" (Notebook)
            self.tabError = ttk.Frame(self.powerwindow)
            # Create Tab
            self.powerwindow.add(self.tabError, text = 'Error')
            self.powerwindow.pack(expand = 1, fill ="both")
            # Error Message
            self.R0_C0 = ttk.Label(self.tabError, text='Please make a selection!', wraplength = 200)
            self.R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
            # Close Button
            self.cls_btn = ttk.Button(self.tabError, text = "Close", command = self.allDone) 
            self.cls_btn.grid(column = 0, row = 1, padx = 5, pady = 5)
            self.powergui.mainloop()
        
        



