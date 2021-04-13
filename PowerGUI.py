import tkinter as tk
from tkinter import ttk
        

 
class Power:
    def __init__(self):
        # Initialize Power Data
        self.UseCase: int
        
        # Power Data:
        self.P_AVG: float
        self.P_margin: float
        self.P_AVG_margin: float
        self.P_PDU_loss: float
        
        # Power Budget Tab:
        self.per_margin = 0

        self.mode1_name: str
        self.mode2_name: str
        self.mode3_name: str
        self.mode4_name: str

        self.eclipse_mode: int
        self.standby_mode: int

        self.mode1_duty = 0
        self.mode2_duty = 0
        self.mode3_duty = 0
        self.mode4_duty = 0

        self.ADCS_P1 = 0
        self.ADCS_P2 = 0
        self.ADCS_P3 = 0
        self.ADCS_P4 = 0

        self.CDH_P1 = 0
        self.CDH_P2 = 0
        self.CDH_P3 = 0
        self.CDH_P4 = 0

        self.GNC_P1 = 0
        self.GNC_P2 = 0
        self.GNC_P3 = 0
        self.GNC_P4 = 0

        self.PAY_P1 = 0
        self.PAY_P2 = 0
        self.PAY_P3 = 0
        self.PAY_P4 = 0

        self.STRU_P1 = 0
        self.STRU_P2 = 0
        self.STRU_P3 = 0
        self.STRU_P4 = 0

        self.COMM_P1 = 0
        self.COMM_P2 = 0
        self.COMM_P3 = 0
        self.COMM_P4 = 0

        self.EPS_P1 = 0
        self.EPS_P2 = 0
        self.EPS_P3 = 0
        self.EPS_P4 = 0

        self.THER_P1 = 0
        self.THER_P2 = 0
        self.THER_P3 = 0
        self.THER_P4 = 0


        # Average Values 
        self.ADCS_AVG: float
        self.CDH_AVG: float
        self.COMM_AVG: float
        self.EPS_AVG: float
        self.GNC_AVG: float
        self.PAY_AVG: float
        self.STRU_AVG: float
        self.THER_AVG: float

        # Design Tab
        self.design_option: int
        self.SP_eff_bol: float
        self.SP_degrad_rate: float
        self.SP_degrad_temp: float
        self.SP_temp: float
        self.SP_tracking: int
        self.SP_deployable: int
        self.bat_eff: float
        self.cell_mass: float
        self.cell_dens: float
        self.cell_cap: float
        self.bat_dod: float
        self.PDU_eff: float
        self.PDU_mass: float
        self.PDU_data: float

        # Other Power Parameters:
        self.solar_flux: float
        self.orbit_energy: float
        self.eclipse_energy_avg: float
        self.eclipse_energy_max: float
        self.sun_energy_avg: float
        self.sun_energy_min: float
        

        # Battery Sizing Parameters:
        self.bat_roundtrip_eff: float
        self.bat_cycles: float
        self.bat_degrad_rate: float
        self.bat_degrad: float
        self.bat_discharge_energy: float
        self.num_cells: int
        self.bat_cap: float
        self.bat_mass: float

        # Solar Panel Sizing Parameters:
        self.SP_eff_eol: float
        self.L_degrad: float
        self.T_degrad: float
        self.SP_energy_orbit_worst: float
        self.SP_avg_power_worst: float 
        self.solar_eol: float
        self.SP_area_effective: float


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

        


    
    def powerbudget2powerdesign(self):
        self.powergui = tk.Tk() # Instance of Tk,
        self.powergui.title("Electrical Power Subsystem Design Module") # Name
        self.powerwindow = ttk.Notebook(self.powergui) # tkk module implements "tabs" (Notebook)
        self.tabBudget = ttk.Frame(self.powerwindow)
        self.tabDesign = ttk.Frame(self.powerwindow)
        self.powerwindow.add(self.tabBudget, text = 'Power Budget Input')
        self.powerwindow.add(self.tabDesign, text = 'EPS Design Input')
        self.powerwindow.pack(expand = 1, fill ="both")


        # Budget Tab Entry Values
        w = 10
        self.E_mode1_name = ttk.Entry(self.tabBudget,width=w)
        self.E_mode2_name = ttk.Entry(self.tabBudget,width=w)
        self.E_mode3_name = ttk.Entry(self.tabBudget,width=w)
        self.E_mode4_name = ttk.Entry(self.tabBudget,width=w)

        w = 6
        self.E_per_margin = ttk.Entry(self.tabBudget,width=w)

        self.E_mode1_duty = ttk.Entry(self.tabBudget,width=w)
        self.E_mode2_duty = ttk.Entry(self.tabBudget,width=w)
        self.E_mode3_duty = ttk.Entry(self.tabBudget,width=w)
        self.E_mode4_duty = ttk.Entry(self.tabBudget,width=w)

        self.E_ADCS_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_ADCS_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_CDH_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_GNC_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_PAY_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_STRU_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_COMM_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_EPS_P4 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_P1 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_P2 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_P3 = ttk.Entry(self.tabBudget, width = w)
        self.E_THER_P4 = ttk.Entry(self.tabBudget, width = w)

        # Design Tab Entry Values
        w = 6
        self.E_SP_eff_bol = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_area = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_point = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_deploy = ttk.Entry(self.tabDesign, width = w)
        self.E_bat_eff = ttk.Entry(self.tabDesign, width = w)
        self.E_cell_mass = ttk.Entry(self.tabDesign, width = w)
        self.E_cell_dens = ttk.Entry(self.tabDesign, width = w)
        self.E_cell_cap = ttk.Entry(self.tabDesign, width = w)
        self.E_bat_dod = ttk.Entry(self.tabDesign, width = w)
        self.E_PDU_eff = ttk.Entry(self.tabDesign, width = w)
        self.E_PDU_mass = ttk.Entry(self.tabDesign, width = w)
        self.E_PDU_data = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_degrad_rate  = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_degrad_temp = ttk.Entry(self.tabDesign, width = w)
        self.E_SP_temp = ttk.Entry(self.tabDesign, width = w)

        ### Budget Tab ###
        # Instructions
        t_inst = 'Input your spacecraft power budget below. If their is a mode that will be the standby or eclipse '\
            'mode, click the appropriate buttons to select that mode as it and do not input a duty cycle for those modes. '\
            'The eclipse mode will automatically scale to the maximum eclipse, and the standby will be found out of the '\
            'remaining duty cycles. If a mode is used, make sure to fill out all parameters in it, even if zero.'
        self.budgetTitle = ttk.Label(self.tabBudget, text=t_inst, wraplength = 600)
        self.budgetTitle.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
        
        # Mode Names
        R = 1; C = 1
        ttk.Label(self.tabBudget, text='Mode Name:', anchor = 'e', width = 15).grid(row=R, column=C-1, padx=2.5,pady = 0)
        self.E_mode1_name.grid(row=R, column=C, padx=5, pady=0)
        self.E_mode2_name.grid(row=R, column=C+1, padx=5, pady=0)
        self.E_mode3_name.grid(row=R, column=C+2, padx=5, pady=0)
        self.E_mode4_name.grid(row=R, column=C+3, padx=5, pady=0)

        # Mode Duty Cycles
        R = 2; C = 1
        ttk.Label(self.tabBudget, text='Duty Cycle [%]:', anchor = 'e', width = 15).grid(row=R, column=C-1, padx=2.5, pady=5)
        self.E_mode1_duty.grid(row=R, column=C, padx=5, pady=5)
        self.E_mode2_duty.grid(row=R, column=C+1, padx=5, pady=5)
        self.E_mode3_duty.grid(row=R, column=C+2, padx=5, pady=5)
        self.E_mode4_duty.grid(row=R, column=C+3, padx=5, pady=5)

        # Standby
        R=3; C=0
        ttk.Label(self.tabBudget, text='Standby', anchor = 'e', width = 15).grid(row=R, column=C, padx=2.5, pady=0)
        self.var_standby=tk.IntVar(self.powergui)
        self.var_standby.set(0)
        standby_1 =ttk.Radiobutton(self.tabBudget, variable=self.var_standby, value=1)
        standby_1.grid(row = R, column = C+1, padx = 10, pady = 0)
        standby_2 =ttk.Radiobutton(self.tabBudget, variable=self.var_standby, value=2)
        standby_2.grid(row = R, column = C+2, padx = 10, pady = 0)
        standby_3 =ttk.Radiobutton(self.tabBudget, variable=self.var_standby, value=3)
        standby_3.grid(row = R, column = C+3, padx = 10, pady = 0)
        standby_4 =ttk.Radiobutton(self.tabBudget, variable=self.var_standby, value=4)
        standby_4.grid(row = R, column = C+4, padx = 10, pady = 0)

        # Eclipse
        R=4; C=0
        ttk.Label(self.tabBudget, text='Eclipse', anchor = 'e', width = 15).grid(row=R, column=C, padx=2.5, pady=0)
        self.var_eclipse=tk.IntVar(self.powergui)
        self.var_eclipse.set(0)
        eclipse_1 =ttk.Radiobutton(self.tabBudget, variable=self.var_eclipse, value=1)
        eclipse_1.grid(row = R, column = C+1, padx = 10, pady = 0)
        eclipse_2 =ttk.Radiobutton(self.tabBudget, variable=self.var_eclipse, value=2)
        eclipse_2.grid(row = R, column = C+2, padx = 10, pady = 0)
        eclipse_3 =ttk.Radiobutton(self.tabBudget, variable=self.var_eclipse, value=3)
        eclipse_3.grid(row = R, column = C+3, padx = 10, pady = 0)
        eclipse_4 =ttk.Radiobutton(self.tabBudget, variable=self.var_eclipse, value=4)
        eclipse_4.grid(row = R, column = C+4, padx = 10, pady = 0)


        # Column Titles
        R=5; C=1
        ttk.Label(self.tabBudget, text='Power [W]').grid(row=R, column=C, padx=2.5, pady=5)
        ttk.Label(self.tabBudget, text='Power [W]').grid(row=R, column=C+1, padx=2.5, pady=5)
        ttk.Label(self.tabBudget, text='Power [W]').grid(row=R, column=C+2, padx=2.5, pady=5)
        ttk.Label(self.tabBudget, text='Power [W]').grid(row=R, column=C+3, padx=2.5, pady=5)

        # Row Titles
        R=6; C=0
        ttk.Label(self.tabBudget, text='ADCS', anchor = 'e', width = 15).grid(row=R, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='C&DH', anchor = 'e', width = 15).grid(row=R+1, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='COMMS', anchor = 'e', width = 15).grid(row=R+2, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='EPS', anchor = 'e', width = 15).grid(row=R+3, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='GNC', anchor = 'e', width = 15).grid(row=R+4, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='Payload', anchor = 'e', width = 15).grid(row=R+5, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='Structures', anchor = 'e', width = 15).grid(row=R+6, column=C, padx=5, pady=5)
        ttk.Label(self.tabBudget, text='Thermal', anchor = 'e', width = 15).grid(row=R+7, column=C, padx=5, pady=5)

        # Entries
        R = 6; C = 1
        self.E_ADCS_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_ADCS_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_ADCS_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_ADCS_P4.grid(row = R, column = C+3, padx = 5, pady = 5)
        R = 7; C = 1
        self.E_CDH_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_CDH_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_CDH_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_CDH_P4.grid(row = R, column = C+3, padx = 5, pady = 5)
        R = 8; C = 1
        self.E_COMM_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_COMM_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_COMM_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_COMM_P4.grid(row = R, column = C+3, padx = 5, pady = 5)
        R = 9; C = 1
        self.E_EPS_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_EPS_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_EPS_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_EPS_P4.grid(row = R, column = C+3, padx = 5, pady = 5)
        R = 10; C = 1
        self.E_GNC_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_GNC_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_GNC_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_GNC_P4.grid(row = R, column = C+3, padx = 5, pady = 5)
        R = 11; C = 1
        self.E_PAY_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_PAY_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_PAY_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_PAY_P4.grid(row = R, column = C+3, padx = 5, pady = 5)
        R = 12; C = 1
        self.E_STRU_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_STRU_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_STRU_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_STRU_P4.grid(row = R, column = C+3, padx = 5, pady = 5)
        R = 13; C = 1
        self.E_THER_P1.grid(row = R, column = C, padx = 5, pady = 5)
        self.E_THER_P2.grid(row = R, column = C+1, padx = 5, pady = 5)
        self.E_THER_P3.grid(row = R, column = C+2, padx = 5, pady = 5)
        self.E_THER_P4.grid(row = R, column = C+3, padx = 5, pady = 5)

        # Power Margin
        R = 14; C = 0
        ttk.Label(self.tabBudget, text='Power Margin[%]', anchor = 'e', width = 15).grid(row=R, column=C,padx=5, pady=5)
        self.E_per_margin.grid(row=R,column=C+1,padx=5,pady=5)

        # Next Page:
        ttk.Label(self.tabBudget, text='Now Fill Out Next Tab').grid(row=R, column=C+2,columnspan=3,padx=5, pady=5)

        ### Design Tab ###
        # Title
        self.designTitle = ttk.Label(self.tabDesign, text='Input Spacecraft Design Parameters Here or Select a Spacecraft Bus')
        self.designTitle.grid(row = 0, column = 0,  columnspan = 4, padx = 5, pady = 5)
        
        # Design Method:
        R = 1; C = 0
        t_ins_design = 'Choose whether you want customized parameters or choose a set of assumed parameters:'
        self.choose = ttk.Label(self.tabDesign,text = t_ins_design, wraplength = 450)
        self.choose.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
        self.optionList = ['','Custom', 'Parameters 1', 'Parameters 2']
        self.E_design_option = tk.StringVar(self.powergui)
        self.E_design_option.set(self.optionList[0])
        self.menu = ttk.OptionMenu(self.tabDesign, self.E_design_option, *self.optionList)
        self.menu.grid(row=R,column = C+3, padx = 5, pady = 5,stick='w')

        # Solar Column
        R=2; C=0
        SP_Title = ttk.Label(self.tabDesign, text='Solar Sizing:')
        SP_Title.grid(row=R, column=C, columnspan = 2, padx = 10, pady = 5,sticky='w')

        # Solar Cell Efficiency
        R = 3; C = 0
        ttk.Label(self.tabDesign, text='Efficiency [%]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_SP_eff_bol.grid(row=R, column=C+1, padx=5, pady=5)

        # Solar Cell Degradation
        R = 4; C = 0
        ttk.Label(self.tabDesign, text='Degradation Rate [%/yr]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_SP_degrad_rate.grid(row=R, column=C+1, padx=5, pady=5)

        # Temperature Degradation
        R = 5; C = 0
        ttk.Label(self.tabDesign, text='Temp Degradation [%/C]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_SP_degrad_temp.grid(row=R, column=C+1, padx=5, pady=5)

        # Solar Cell Temperature
        R = 6; C = 0
        ttk.Label(self.tabDesign, text='Temperature [C]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_SP_temp.grid(row=R, column=C+1, padx=5, pady=5)

        # Solar Tracking
        R = 7; C = 0
        st_label = ttk.Label(self.tabDesign, text='Solar Array Pointing:')
        st_label.grid(row=R, column=C, columnspan = 2, padx=10, pady=5,sticky='w')
        self.var_track=tk.IntVar(self.powergui)
        st_btn1 = ttk.Radiobutton(self.tabDesign, text="Tumbling", variable=self.var_track,value=1)
        st_btn1.grid(column=C, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')
        st_btn2 = ttk.Radiobutton(self.tabDesign, text="Nadir Pointing", variable=self.var_track,value=2)
        st_btn2.grid(column=C, row=R+2, columnspan = 2, padx = 25, pady = 5,sticky='w')
        st_btn3 = ttk.Radiobutton(self.tabDesign, text="Sun Tracking", variable=self.var_track,value=3)
        st_btn3.grid(column=C, row=R+3, columnspan = 2, padx = 25, pady = 5,sticky='w')

        # Deployables
        R = 11; C = 0
        dep_label = ttk.Label(self.tabDesign, text='Deployables:')
        dep_label.grid(row=R, column=C, columnspan = 2, padx=10, pady=5,sticky='w')
        self.var_deploy=tk.IntVar(self.powergui)
        dep_btn1 = ttk.Radiobutton(self.tabDesign, text="Body Mounted", variable=self.var_deploy,value=1)
        dep_btn1.grid(column=C, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')
        dep_btn2 = ttk.Radiobutton(self.tabDesign, text="Deployable", variable=self.var_deploy,value=2)
        dep_btn2.grid(column=C, row=R+2, columnspan = 2, padx = 25, pady = 5,sticky='w')

        ## Battery Column
        R=2; C=2
        SP_Title = ttk.Label(self.tabDesign, text='Battery Sizing:')
        SP_Title.grid(row=R, column=C, columnspan = 2, padx = 10, pady = 5,sticky='w')

        # Battery Density:
        R = 3; C = 2
        ttk.Label(self.tabDesign, text='Energy Density [Wh/kg]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_cell_dens.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Cell Capacity:
        R = 4; C = 2
        ttk.Label(self.tabDesign, text='Cell Capacity [Wh]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_cell_cap.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Cell Mass:
        R = 5; C = 2
        ttk.Label(self.tabDesign, text='Cell Mass [kg]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_cell_mass.grid(row=R, column=C+1, padx=5, pady=5,stick='w')
        
        # Battery Efficiency (One Way):
        R = 6; C = 2
        ttk.Label(self.tabDesign, text='One-way Efficiency [%]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_bat_eff.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Battery Depth-of-Discharge:
        R = 7; C = 2
        ttk.Label(self.tabDesign, text='Depth-of-Discharge [%]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_bat_dod.grid(row=R, column=C+1, padx=5, pady=5,stick='w')
  
        ## PDU Column
        R=8; C=2
        SP_Title = ttk.Label(self.tabDesign, text='PDU Sizing:')
        SP_Title.grid(row=R, column=C, columnspan = 2, padx = 10, pady = 5,sticky='w')
        
        # PDU Mass
        R = 9; C = 2
        ttk.Label(self.tabDesign, text='Mass [kg]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_PDU_mass.grid(row=R, column=C+1, padx = 5, pady = 5,stick='w')

        # PDU Efficiency
        R = 10; C = 2
        ttk.Label(self.tabDesign, text='Efficiency [%]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_PDU_eff.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # PDU Data Rate
        R = 11; C = 2
        ttk.Label(self.tabDesign, text='Data Rate [kb/day]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.E_PDU_data.grid(row=R, column=C+1, padx=5, pady=5,stick='w')


        # Submit Button
        R = 13; C = 2
        self.UseCase = 1
        self.sub_btn = ttk.Button(self.tabDesign, text = "Submit", command = self.inputPower)
        self.sub_btn.grid(column = C, row = R)
        # Done Button
        self.fin_btn = ttk.Button(self.tabDesign, text = "Finish", command = self.allDone)
        self.fin_btn.grid(column = C+1, row = R,stick='w')
        # Run
        self.powergui.mainloop()



        
                               
    def payloadcapabilities2powerdesign(self):
        self.powergui = tk.Tk() # Instance of Tk,
        self.powergui.title("Electrical Power Subsystem Design Module") # Name
        self.powerwindow = ttk.Notebook(self.powergui) # tkk module implements "tabs" (Notebook)
        self.tabCap = ttk.Frame(self.powerwindow)
        self.powerwindow.add(self.tabCap, text = 'EPS General Input')
        self.powerwindow.pack(expand = 1, fill ="both")

        self.R0_C0 = ttk.Label(self.tabCap, text='Please input your spacecraft power budget here:', wraplenght = 200)
        self.R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.powergui.mainloop()


    def inputPower(self):
        print('here')
        if self.UseCase == 1:
            print('got here')
            try:
                self.per_margin = float(self.E_per_margin.get())
            except:
                pass
            try:
                self.mode1_name = str(self.E_mode1_name.get())
            except:
                pass
            try:
                self.mode2_name = str(self.E_mode2_name.get())
            except:
                pass
            try:
                self.mode3_name = str(self.E_mode3_name.get())
            except:
                pass
            try:
                self.mode4_name = str(self.E_mode4_name.get())
            except:
                pass
            self.eclipse_mode = self.var_eclipse.get()
            self.standby_mode = self.var_standby.get()
            try:  
                self.mode1_duty = float(self.E_mode1_duty.get())
                self.ADCS_P1 = float(self.E_ADCS_P1.get())
                self.CDH_P1 = float(self.E_CDH_P1.get())
                self.COMM_P1 = float(self.E_COMM_P1.get())
                self.EPS_P1 = float(self.E_EPS_P1.get())
                self.GNC_P1 = float(self.E_GNC_P1.get())
                self.PAY_P1 = float(self.E_PAY_P1.get())
                self.STRU_P1 = float(self.E_STRU_P1.get())
                self.THER_P1 = float(self.E_THER_P1.get())
            except:
                pass
            try:
                self.mode2_duty = float(self.E_mode2_duty.get())
                self.ADCS_P2 = float(self.E_ADCS_P2.get())
                self.CDH_P2 = float(self.E_CDH_P2.get())
                self.COMM_P2 = float(self.E_COMM_P2.get())
                self.EPS_P2 = float(self.E_EPS_P2.get())
                self.GNC_P2 = float(self.E_GNC_P2.get())
                self.PAY_P2 = float(self.E_PAY_P2.get())
                self.STRU_P2 = float(self.E_STRU_P2.get())
                self.THER_P2 = float(self.E_THER_P2.get())
            except:
                pass
            try:
                self.mode3_duty = float(self.E_mode3_duty.get())
                self.ADCS_P3 = float(self.E_ADCS_P3.get())
                self.CDH_P3 = float(self.E_CDH_P3.get())
                self.COMM_P3 = float(self.E_COMM_P3.get())
                self.EPS_P3 = float(self.E_EPS_P3.get())
                self.GNC_P3 = float(self.E_GNC_P3.get())
                self.PAY_P3 = float(self.E_PAY_P3.get())
                self.STRU_P3 = float(self.E_STRU_P3.get())
                self.THER_P3 = float(self.E_THER_P3.get())
            except:
                pass
            try:
                self.mode4_duty = float(self.E_mode4_duty.get())
                self.ADCS_P4 = float(self.E_ADCS_P4.get())
                self.CDH_P4 = float(self.E_CDH_P4.get()) 
                self.COMM_P4 = float(self.E_COMM_P4.get())
                self.EPS_P4 = float(self.E_EPS_P4.get())
                self.GNC_P4 = float(self.E_GNC_P4.get())
                self.PAY_P4 = float(self.E_PAY_P4.get())
                self.STRU_P4 = float(self.E_STRU_P4.get())
                self.THER_P4 = float(self.E_THER_P4.get())
            except:
                pass
            try:
                self.design_option = str(self.E_design_option.get())                
                if self.design_option == self.optionList[1]:
                    self.SP_eff_bol = float(self.E_SP_eff_bol.get())
                    self.SP_degrad_rate = float(self.E_SP_degrad_rate.get())
                    self.SP_degrad_temp = float(self.E_SP_degrad_temp.get())
                    self.SP_temp = float(self.E_SP_temp.get())
                    self.SP_tracking = int(self.var_track.get())
                    self.SP_deployable = int(self.var_deploy.get())

                    self.cell_dens = float(self.E_cell_dens.get())
                    self.cell_cap = float(self.E_cell_cap.get())
                    self.cell_mass = float(self.E_cell_mass.get())
                    self.bat_eff = float(self.E_bat_eff.get())
                    self.bat_dod = float(self.E_bat_dod.get())

                    self.PDU_mass = float(self.E_PDU_mass.get())
                    self.PDU_eff = float(self.E_PDU_eff.get())
                    self.PDU_data = float(self.E_PDU_data.get())
                elif self.design_option == self.optionList[2]:
                    pass
                elif self.design_option == self.optionList[3]:
                    pass
                print('and here')
            except:
                print('error')
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
        
    def allDone(self):
        self.powergui.destroy()  



