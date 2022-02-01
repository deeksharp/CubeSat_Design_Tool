import tkinter as tk
from tkinter import StringVar, ttk
        
#########           NAMING CONVENTION USE CASE 1      ########### 
#               TAB_*ORDER_*ENTITY_VARIABLE            #
## TAB specifies which tab: 'up' or 'down' for uplink or downlink
## *ORDER specifies which band: 'p' or 's' for primary or secondary
## *ENTITY specifies which entity: 'sc' or 'gs' for spacecraft or groundstation
## VARIABLE specifies variable name: ex: 'transpower', 'antgain', etc. 
######### please note: * means value is not necessarily required.  ORDER and ENTITY 
######### labels don't apply to certain variables and may be skipped.  Ex: up_systemp or up_p_datarate

#########           NAMING CONVENTION USE CASE 2      ########### 
#               TAB_*ORDER_VARIABLE            #
## TAB specifies which tab: 'up' or 'down' for uplink or downlink
## *ORDER specifies which band: '1' or '2' for primary or secondary.  different from use case 1 to avoid clashing variable names
## VARIABLE specifies variable name: ex: 'transpower', 'antgain', etc. 

class Comms:
    def __init__(self):
        # Initialize Comms Data
        self.UseCase: int

        # UPLINK TAB - 1
        self.up_p_sc_transpower = ''
        self.up_p_sc_antgain = ''
        self.up_p_gs_transpower = ''
        self.up_p_gs_antgain = ''
        self.up_p_datarate = ''
        self.up_p_frequency = '' 
        self.up_p_EBNo = '' 
        self.up_s_sc_transpower = ''
        self.up_s_sc_antgain = ''
        self.up_s_gs_transpower = ''
        self.up_s_gs_antgain = ''
        self.up_s_datarate = ''
        self.up_s_frequency = '' 
        self.up_s_EBNo = '' 
        self.up_systemp = '' 
        self.up_maxdistanceEarth = ''
        self.up_rainloss = '' 
        self.up_lineloss = '' 
        self.up_otherloss = '' 
        
        # DOWNLINK TAB - 1
        self.down_p_sc_transpower = ''
        self.down_p_sc_antgain = ''
        self.down_p_gs_transpower = ''
        self.down_p_gs_antgain = ''
        self.down_p_datarate = ''
        self.down_p_frequency = '' 
        self.down_p_EBNo = '' 
        self.down_s_sc_transpower = ''
        self.down_s_sc_antgain = ''
        self.down_s_gs_transpower = ''
        self.down_s_gs_antgain = ''
        self.down_s_datarate = ''
        self.down_s_frequency = '' 
        self.down_s_EBNo = '' 
        self.down_systemp = '' 
        self.down_maxdistanceEarth = ''
        self.down_rainloss = ''
        self.down_lineloss = '' 
        self.down_otherloss = ''
        
        # UPLINK TAB - 2
        self.up_1_frequency = ''
        self.up_1_EBNo = ''
        self.up_1_BER = ''
        self.up_1_antennatype = ''
        self.up_1_beamwidth = ''
        self.up_1_atmosphereattenuation = ''
        self.up_1_rainattenuation = ''
        self.up_1_systemtemp = ''
        self.up_1_lineloss = ''
        self.up_1_spaceloss = ''
        self.up_1_polarizationloss = ''
        self.up_1_transmitterpointingloss = ''
        self.up_1_receiverpointingloss = ''
        self.up_1_transmitterdishdiameter = ''
        self.up_1_receiverdishdiameter = ''
        self.up_1_transmitterefficiency = ''
        self.up_1_receiverefficiency = ''
        self.up_2_frequency = ''
        self.up_2_EBNo = ''
        self.up_2_BER = ''
        self.up_2_antennatype = ''
        self.up_2_beamwidth = ''
        self.up_2_atmosphereattenuation = ''
        self.up_2_rainattenuation = ''
        self.up_2_systemtemp = ''
        self.up_2_lineloss = ''
        self.up_2_spaceloss = ''
        self.up_2_polarizationloss = ''
        self.up_2_transmitterpointingloss = ''
        self.up_2_receiverpointingloss = ''
        self.up_2_transmitterdishdiameter = ''
        self.up_2_receiverdishdiameter = ''
        self.up_2_transmitterefficiency = ''
        self.up_2_receiverefficiency = ''

        # DOWNLINK TAB - 2
        self.down_1_frequency = ''
        self.down_1_EBNo = ''
        self.down_1_BER = ''
        self.down_1_antennatype = ''
        self.down_1_beamwidth = ''
        self.down_1_atmosphereattenuation = ''
        self.down_1_rainattenuation = ''
        self.down_1_systemtemp = ''
        self.down_1_lineloss = ''
        self.down_1_spaceloss = ''
        self.down_1_polarizationloss = ''
        self.down_1_transmitterpointingloss = ''
        self.down_1_receiverpointingloss = ''
        self.down_1_transmitterdishdiameter = ''
        self.down_1_receiverdishdiameter = ''
        self.down_1_transmitterefficiency = ''
        self.down_1_receiverefficiency = ''
        self.down_2_frequency = ''
        self.down_2_EBNo = ''
        self.down_2_BER = ''
        self.down_2_antennatype = ''
        self.down_2_beamwidth = ''
        self.down_2_atmosphereattenuation = ''
        self.down_2_rainattenuation = ''
        self.down_2_systemtemp = ''
        self.down_2_lineloss = ''
        self.down_2_spaceloss = ''
        self.down_2_polarizationloss = ''
        self.down_2_transmitterpointingloss = ''
        self.down_2_receiverpointingloss = ''
        self.down_2_transmitterdishdiameter = ''
        self.down_2_receiverdishdiameter = ''
        self.down_2_transmitterefficiency = ''
        self.down_2_receiverefficiency = ''

        # OUTPUTS - 1
        self.out_up_p_sc_transpower: float
        self.out_up_p_gs_transpower: float
        self.out_up_s_sc_transpower: float
        self.out_up_s_sc_transpower: float
        self.out_down_p_sc_transpower: float
        self.out_down_p_gs_transpower: float
        self.out_down_s_sc_transpower: float
        self.out_down_s_sc_transpower: float
        self.out_up_p_sc_antgain: float
        self.out_up_p_gs_antgain: float
        self.out_up_s_sc_antgain: float
        self.out_up_s_gs_antgain: float
        self.out_down_p_sc_antgain: float
        self.out_down_p_gs_antgain: float
        self.out_down_s_sc_antgain: float
        self.out_down_s_gs_antgain: float
        self.out_up_p_EBNo: float
        self.out_up_s_EBNo: float
        self.out_down_p_EBNo: float
        self.out_down_s_EBNo: float
        self.out_up_p_datarate: float
        self.out_up_s_datarate: float
        self.out_down_p_datarate: float
        self.out_down_s_datarate: float
        self.out_up_systemp: float
        self.out_down_systemp: float
        self.out_up_p_pathloss: float
        self.out_up_s_pathloss: float
        self.out_down_p_pathloss: float
        self.out_down_s_pathloss: float
        self.out_up_otherloss: float
        self.out_down_otherloss: float
        self.out_up_p_margin: float
        self.out_up_s_margin: float
        self.out_down_p_margin: float
        self.out_down_s_margin: float

        #OUTPUT - 2
        self.out_up_1_frequency: float
        self.out_up_2_frequency: float
        self.out_down_1_frequency: float
        self.out_down_2_frequency: float
        self.out_up_1_EBNo: float
        self.out_up_2_EBNo: float
        self.out_down_1_EBNo: float
        self.out_down_2_EBNo: float
        self.out_up_1_BER: float
        self.out_up_2_BER: float
        self.out_down_1_BER: float
        self.out_down_2_BER: float
        self.out_up_1_antennatype: float
        self.out_up_2_antennatype: float
        self.out_down_1_antennatype: float
        self.out_down_2_antennatype: float
        self.out_up_1_beamwidth: float
        self.out_up_2_beamwidth: float
        self.out_down_1_beamwidth: float
        self.out_down_2_beamwidth: float
        self.out_up_1_atmosphereattenuation: float
        self.out_up_2_atmosphereattenuation: float
        self.out_down_1_atmosphereattenuation: float
        self.out_down_2_atmosphereattenuation: float
        self.out_up_1_rainattenuation: float
        self.out_up_2_rainattenuation: float
        self.out_down_1_rainattenuation: float
        self.out_down_2_rainattenuation: float
        self.out_up_1_systemtemp: float
        self.out_up_2_systemtemp: float
        self.out_down_1_systemtemp: float
        self.out_down_2_systemtemp: float
        self.out_up_1_lineloss: float
        self.out_up_2_lineloss: float
        self.out_down_1_lineloss: float
        self.out_down_2_lineloss: float
        self.out_up_1_spaceloss: float
        self.out_up_2_spaceloss: float
        self.out_down_1_spaceloss: float
        self.out_down_2_spaceloss: float
        self.out_up_1_polarizationloss: float
        self.out_up_2_polarizationloss: float
        self.out_down_1_polarizationloss: float
        self.out_down_2_polarizationloss: float
        self.out_up_1_transmitterpointingloss: float
        self.out_up_2_transmitterpointingloss: float
        self.out_down_1_transmitterpointingloss: float
        self.out_down_2_transmitterpointingloss: float
        self.out_up_1_receiverpointingloss: float
        self.out_up_2_receiverpointingloss: float
        self.out_down_1_receiverpointingloss: float
        self.out_down_2_receiverpointingloss: float
        self.out_up_1_transmitterdishdiameter: float
        self.out_up_2_transmitterdishdiameter: float
        self.out_down_1_transmitterdishdiameter: float
        self.out_down_2_transmitterdishdiameter: float
        self.out_up_1_receiverdishdiameter: float
        self.out_up_2_receiverdishdiameter: float
        self.out_down_1_receiverdishdiameter: float
        self.out_down_2_receiverdishdiameter: float
        self.out_up_1_transmitterefficiency: float
        self.out_up_2_transmitterefficiency: float
        self.out_down_1_transmitterefficiency: float
        self.out_down_2_transmitterefficiency: float
        self.out_up_1_receiverefficiency: float
        self.out_up_2_receiverefficiency: float
        self.out_down_1_receiverefficiency: float
        self.out_down_2_receiverefficiency: float

    def moreInfo(self, x):
        self.commsgui = tk.Tk() # Instance of Tk,
        self.commsgui.title("Communications Subsystem Design Module") # Name
        self.commswindow = ttk.Notebook(self.commsgui) # tkk module implements "tabs" (Notebook)
        self.tabInputs = ttk.Frame(self.commswindow)
        self.tabAssums = ttk.Frame(self.commswindow)
        self.tabCalcs = ttk.Frame(self.commswindow)
        self.commswindow.add(self.tabInputs, text = 'Inputs')
        self.commswindow.add(self.tabAssums, text = 'Assumptions')
        self.commswindow.add(self.tabCalcs, text = 'Calculations')
        self.commswindow.pack(expand = 1, fill ="both")

        if x == 1:
            # Inputs
            self.T1_R0_C0 = ttk.Label(self.tabInputs, text='Link Budget:', wraplength = 100)
            self.T1_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')
            t='Ground Station and Spacecraft parameters are prepopulated with assumed values and can be changed to reflect current design parameters. '
            self.T1_R0_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R0_C1.grid(row = 0, column = 1, padx = 5, pady = 5,sticky='w')
            self.T1_R1_C0 = ttk.Label(self.tabInputs, text='Comms Design Parameters:', wraplength = 100)
            self.T1_R1_C0.grid(row = 1, column = 0, padx = 5, pady = 5,sticky='w')
            t ='Parameters for a link budget based off of antenna sizing.'
            self.T1_R1_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R1_C1.grid(row = 1, column = 1, padx = 5, pady = 5,sticky='w')
            
            # Assumptions
            t = 'Assumed values include line losses, system temp, '\
                'as well as design sizing parameters for the spacecraft '\
                'if standard comms is chosen.'
            self.T2_R0_C0 = ttk.Label(self.tabAssums, text=t, wraplength = 350)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')

            # Calculations
            t = 'Calculated values include data rates and link margin, '\
                'based on calculated transmit power values, with appropriate '\
                'losses and orbit radius considerations in place.'
            self.T3_R0_C0 = ttk.Label(self.tabCalcs, text=t, wraplength = 350)
            self.T3_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')
            
        elif x == 2:
             # Inputs
            self.T1_R0_C0 = ttk.Label(self.tabInputs, text='Link Budget:', wraplength = 100)
            self.T1_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')
            t='Ground Sation and Spacecraft parameters for an uplink and downlink budget.'
            self.T1_R0_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R0_C1.grid(row = 0, column = 1, padx = 5, pady = 5,sticky='w')
            self.T1_R1_C0 = ttk.Label(self.tabInputs, text='EPS Design Parameters:', wraplength = 100)
            self.T1_R1_C0.grid(row = 1, column = 0, padx = 5, pady = 5,sticky='w')
            t ='Parameters for calculating transmitter power or max data rates, along with link margin.'
            self.T1_R1_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R1_C1.grid(row = 1, column = 1, padx = 5, pady = 5,sticky='w')
            
            # Assumptions
            t = 'Assumed values include frequency (Hz), Eb/No for FSK and BSK modulation, '\
                'as well as values for losses '\
                'if non-custom is chosen'
            self.T2_R0_C0 = ttk.Label(self.tabAssums, text=t, wraplength = 350)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')

            # Calculations
            t = 'Calculated values include antenna gains, EIRP, power, data rate, '\
                'based on selected frequency and modulation. '
            self.T3_R0_C0 = ttk.Label(self.tabCalcs, text=t, wraplength = 350)
            self.T3_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')

    def linkbudget4demo_standard(self):
        self.commsgui = tk.Tk() # Instance of Tk,
        self.commsgui.title("Communications Subsystem Design Module") # Name
        self.commswindow = ttk.Notebook(self.commsgui) # tkk module implements "tabs" (Notebook)
        self.tabUplink = ttk.Frame(self.commswindow)
        self.tabDownlink = ttk.Frame(self.commswindow)
        self.commswindow.add(self.tabUplink, text = 'Uplink')
        self.commswindow.add(self.tabDownlink, text = 'Downlink')
        self.commswindow.pack(expand = 1, fill ="both")


        # Uplink Tab Entry Values
        w = 6
        self.entry_up_p_sc_transpower = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_p_sc_transpower.insert(0,0)
        self.entry_up_p_sc_antgain = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_p_sc_antgain.insert(0,0)
        self.entry_up_p_gs_transpower = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_p_gs_transpower.insert(0,0)
        self.entry_up_p_gs_antgain = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_p_gs_antgain.insert(0,0)
        self.entry_up_p_datarate = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_p_datarate.insert(0,0)
        self.entry_up_p_frequency = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_p_frequency.insert(0,0)
        self.entry_up_p_EBNo = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_p_EBNo.insert(0,0)
        self.entry_up_s_sc_transpower = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_s_sc_transpower.insert(0,0)
        self.entry_up_s_sc_antgain = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_s_sc_antgain.insert(0,0)
        self.entry_up_s_gs_transpower = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_s_gs_transpower.insert(0,0)
        self.entry_up_s_gs_antgain = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_s_gs_antgain.insert(0,0)
        self.entry_up_s_datarate = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_s_datarate.insert(0,0)
        self.entry_up_s_frequency = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_s_frequency.insert(0,0)
        self.entry_up_s_EBNo = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_s_EBNo.insert(0,0)
        self.entry_up_systemp = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_systemp.insert(0, 300)
        self.entry_up_maxdistanceEarth = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_maxdistanceEarth.insert(0, 2704)
        self.entry_up_rainloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_rainloss.insert(0,3)
        self.entry_up_lineloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_lineloss.insert(0,3)
        self.entry_up_otherloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_otherloss.insert(0,0)

        # Downlink Tab Entry Values
        w = 6
        self.entry_down_p_sc_transpower = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_p_sc_transpower.insert(0,0)
        self.entry_down_p_sc_antgain = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_p_sc_antgain.insert(0,0)
        self.entry_down_p_gs_transpower = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_p_gs_transpower.insert(0,0)
        self.entry_down_p_gs_antgain = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_p_gs_antgain.insert(0,0)
        self.entry_down_p_datarate = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_p_datarate.insert(0,0)
        self.entry_down_p_frequency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_p_frequency.insert(0,0)
        self.entry_down_p_EBNo = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_p_EBNo.insert(0,0)
        self.entry_down_s_sc_transpower = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_s_sc_transpower.insert(0,0)
        self.entry_down_s_sc_antgain = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_s_sc_antgain.insert(0,0)
        self.entry_down_s_gs_transpower = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_s_gs_transpower.insert(0,0)
        self.entry_down_s_gs_antgain = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_s_gs_antgain.insert(0,0)
        self.entry_down_s_datarate = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_s_datarate.insert(0,0)
        self.entry_down_s_frequency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_s_frequency.insert(0,0)
        self.entry_down_s_EBNo = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_s_EBNo.insert(0,0)
        self.entry_down_systemp = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_systemp.insert(0, 300)
        self.entry_down_maxdistanceEarth = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_maxdistanceEarth.insert(0, 2704)
        self.entry_down_rainloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_rainloss.insert(0,3)
        self.entry_down_lineloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_lineloss.insert(0,3)
        self.entry_down_otherloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_otherloss.insert(0,0)

        ### Uplink: Ground Station to Spacecraft Tab ###
        # Header - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Uplink is Ground Station to Spacecraft communication. '\
        'Input appropriate parameter values for Ground Station communications. Change assumed values for parameters according to desired link budget. '    
        self.choose = ttk.Label(self.tabUplink,text = t_ins_design, wraplength = 450)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Primary Spacecraft Transmitter Power
        R = 3; C = 0
        ttk.Label(self.tabUplink, text='Primary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_p_sc_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Primary Spacecraft Antenna Gain 
        R = 4; C = 0
        ttk.Label(self.tabUplink, text='Primary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_p_sc_antgain.grid(row=R, column=C+1, padx=5, pady=5)

         # Primary GroundStation Transmitter Power
        R = 5; C = 0
        ttk.Label(self.tabUplink, text='Primary GroundStation Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_p_gs_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Primary GroundStation Antenna Gain 
        R = 6; C = 0
        ttk.Label(self.tabUplink, text='Primary GroundStation Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_p_gs_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Datarate
        R = 7; C = 0
        ttk.Label(self.tabUplink, text='Primary Datarate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_p_datarate.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Frequency
        R = 8; C = 0
        ttk.Label(self.tabUplink, text='Primary Frequency [Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_p_frequency.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Eb/N0 
        R = 9; C = 0
        ttk.Label(self.tabUplink, text='Primary Eb/N0 [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_p_EBNo.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Secondary Spacecraft Transmitter Power
        R = 3; C = 2
        ttk.Label(self.tabUplink, text='Secondary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_sc_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Antenna Gain
        R = 4; C = 2
        ttk.Label(self.tabUplink, text='Secondary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_sc_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Transmitter Power
        R = 5; C = 2
        ttk.Label(self.tabUplink, text='Secondary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_gs_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Antenna Gain
        R = 6; C = 2
        ttk.Label(self.tabUplink, text='Secondary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_gs_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        #Secondary Datarate
        R = 7; C = 2
        ttk.Label(self.tabUplink, text='Secondary Datarate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_datarate.grid(row=R, column=C+1, padx=5, pady=5)

        #Frequency Secondary
        R = 8; C = 2
        ttk.Label(self.tabUplink, text='Secondary Frequency [Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_frequency.grid(row=R, column=C+1, padx=5, pady=5)

        #EBNO Secondary 
        R = 9; C = 2 
        ttk.Label(self.tabUplink, text='Secondary Eb/N0 [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_EBNo.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

         # System Noise Temp
        R = 3; C = 4
        ttk.Label(self.tabUplink, text='System Temp [K]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_systemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Maximum Distance From Earth
        R = 4; C = 4
        ttk.Label(self.tabUplink, text='Max Distance from Earth [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_maxdistanceEarth.grid(row=R, column=C+1, padx=5, pady=5)

        # Rain Losses
        R = 5; C = 4
        ttk.Label(self.tabUplink, text='Rain Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_rainloss.grid(row=R, column=C+1, padx=5, pady=5)
        
        # Line Losses
        R = 6; C = 4
        ttk.Label(self.tabUplink, text='Line Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_lineloss.grid(row=R, column=C+1, padx=5, pady=5)

        # Other Losses
        R = 7; C = 4
        ttk.Label(self.tabUplink, text='Other Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_otherloss.grid(row=R, column=C+1, padx=5, pady=5)

        ## Downlink: Spacecraft to Groundstation Tab ##
        
        # Heading - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Downlink is Spacecraft to Ground Station Communication. Input appropriate parameter values for Spacecraft communications:'
        self.choose = ttk.Label(self.tabDownlink,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Primary Spacecraft Transmitter Power
        R = 3; C = 0
        ttk.Label(self.tabDownlink, text='Primary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_sc_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Primary Spacecraft Antenna Gain 
        R = 4; C = 0
        ttk.Label(self.tabDownlink, text='Primary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_sc_antgain.grid(row=R, column=C+1, padx=5, pady=5)

         # Primary GroundStation Transmitter Power
        R = 5; C = 0
        ttk.Label(self.tabDownlink, text='Primary GroundStation Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_gs_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Primary GroundStation Antenna Gain 
        R = 6; C = 0
        ttk.Label(self.tabDownlink, text='Primary GroundStation Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_gs_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Datarate
        R = 7; C = 0
        ttk.Label(self.tabDownlink, text='Primary Datarate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_datarate.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Frequency
        R = 8; C = 0
        ttk.Label(self.tabDownlink, text='Primary Frequency [Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_frequency.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Eb/N0 
        R = 9; C = 0
        ttk.Label(self.tabDownlink, text='Primary Eb/N0 [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_EBNo.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Secondary Spacecraft Transmitter Power
        R = 3; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_sc_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Antenna Gain
        R = 4; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_sc_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Transmitter Power
        R = 5; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_gs_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Antenna Gain
        R = 6; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_gs_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        #Secondary Datarate
        R = 7; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Datarate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_datarate.grid(row=R, column=C+1, padx=5, pady=5)

        #Frequency Secondary
        R = 8; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Frequency [Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_frequency.grid(row=R, column=C+1, padx=5, pady=5)

        #EBNO Secondary 
        R = 9; C = 2 
        ttk.Label(self.tabDownlink, text='Secondary Eb/N0 [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_EBNo.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

         # System Noise Temp
        R = 3; C = 4
        ttk.Label(self.tabDownlink, text='System Temp [K]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_systemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Maximum Distance From Earth
        R = 4; C = 4
        ttk.Label(self.tabDownlink, text='Max Distance from Earth [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_maxdistanceEarth.grid(row=R, column=C+1, padx=5, pady=5)

        # Rain Losses
        R = 5; C = 4
        ttk.Label(self.tabDownlink, text='Rain Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_rainloss.grid(row=R, column=C+1, padx=5, pady=5)
        
        # Line Losses
        R = 6; C = 4
        ttk.Label(self.tabDownlink, text='Line Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_lineloss.grid(row=R, column=C+1, padx=5, pady=5)

        # Other Losses
        R = 7; C = 4
        ttk.Label(self.tabDownlink, text='Other Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_otherloss.grid(row=R, column=C+1, padx=5, pady=5)

        # Submit Button
        R = 14; C = 5
        self.UseCase = 1
        self.sub_btn = ttk.Button(self.tabDownlink, text = "Submit", command = self.inputComms)
        self.sub_btn.grid(column = C, row = R)
        # Done Button
        self.fin_btn = ttk.Button(self.tabDownlink, text = "Close", command = self.allDone)
        self.fin_btn.grid(column = C+1, row = R,stick='w')
        
        # Run
        self.commsgui.mainloop()
   
    def linkbudget4demo_custom(self):
        self.commsgui = tk.Tk() # Instance of Tk,
        self.commsgui.title("Communications Subsystem Custom Design Module") # Name
        self.commswindow = ttk.Notebook(self.commsgui) # tkk module implements "tabs" (Notebook)
        self.tabUplink = ttk.Frame(self.commswindow)
        self.tabDownlink = ttk.Frame(self.commswindow)
        self.commswindow.add(self.tabUplink, text = 'Uplink')
        self.commswindow.add(self.tabDownlink, text = 'Downlink')
        self.commswindow.pack(expand = 1, fill ="both")

        ## Function to check which menu option is selected.  Sets entry field accordingly
        def bandCheck(value):
            if value == 'UHF':
                self.entry_up_1_frequency.set(435000000)
            elif value == 'S-Band':
                self.entry_up_1_frequency.set(2400000000)
            elif value == 'Other': 
                self.entry_up_1_frequency.set(0)
        
        ## Function to check which menu uption is selected.  Sets entry field accordingly
        def antCheck(value):
            if value == 'Patch':
                self.entry_up_1_beamwidth.set(90)
            elif value == 'Monopole' or value == 'Dipole':
                self.entry_up_1_beamwidth.set(156.2)
            elif value == 'Other': 
                self.entry_up_1_beamwidth.set(0)

        ## Function to check which menu uption is selected.  Sets entry field accordingly
        def BERCheck(val1):                   # ..is getting the right value of modulationtype 
            val2 = self.entry_up_1_modulationtype.get()
            if val1 == '10^-2':
                print('\n2\n')
                if val2 == 'FSK':
                    self.entry_up_1_EBNo.set(8.9)
                elif val2 == 'BPSK':
                    print('\n1\n')
                    self.entry_up_1_EBNo.set(4.3)
            elif val1 == '10^-3':
                if val2 == 'FSK':
                    self.entry_up_1_EBNo.set(10.9)
                elif val2 == 'BPSK':
                    print('\n3\n')
                    self.entry_up_1_EBNo.set(6.5)
            elif val1 == '10^-4':
                if val2 == 'FSK':
                    self.entry_up_1_EBNo.set(12)
                elif val2 == 'BPSK':
                    print('\n4\n')
                    self.entry_up_1_EBNo.set(8.1)
            elif val1 == '10^-5':
                if val2 == 'FSK':
                    self.entry_up_1_EBNo.set(13.5)
                elif val2 == 'BPSK':
                    print('\n5\n')
                    self.entry_up_1_EBNo.set(9.6)
            elif val1 == '10^-6':
                if val2 == 'FSK':
                    self.entry_up_1_EBNo.set(0.0)
                elif val2 == 'BPSK':
                    self.entry_up_1_EBNo.set(10.6)

        ## Function to check which menu uption is selected.  Sets entry field accordingly
        def modCheck(val1):
            if val1 == 'Other':
                self.up_1_BERmenu.configure(state='disabled')
                #enable entry
            else :
                self.up_1_BERmenu.configure(state='normal')
                #disable entry
            

        # Uplink Tab Entry Values

        w = 6
        
        self.entry_up_1_frequencytype = tk.StringVar(self.commsgui)
        self.entry_up_1_frequency= tk.IntVar(self.commsgui)
        self.entry_up_1_frequencyVal = ttk.Entry(self.tabUplink, textvariable=self.entry_up_1_frequency, width = w+4)
        self.entry_up_1_frequencyVal.delete(0)
        self.entry_up_1_frequencyVal.insert(0,435000000)
        self.up_1_frequencies = ('UHF', 'S-Band', 'Other')
        self.up_1_freqmenu = ttk.OptionMenu(self.tabUplink, self.entry_up_1_frequencytype, self.up_1_frequencies[0], *self.up_1_frequencies, command=lambda e=self.entry_up_1_frequencytype: bandCheck(e))

        # self.entry_up_2_frequency = ttk.Radiobutton(self.tabUplink, text="Secondary Frequency")##, variable=,value=)
        # self.entry_up_2_frequency.grid(column = 0, row = 3, padx = 10, pady = 10,sticky='w')

        self.entry_up_1_modulationtype = tk.StringVar(self.commsgui)
        self.entry_up_1_EBNo = tk.DoubleVar(self.commsgui)
        self.entry_up_1_EBNoVal = ttk.Entry(self.tabUplink, textvariable=self.entry_up_1_EBNo, width = w)
        self.entry_up_1_EBNoVal.delete(0, tk.END)
        self.entry_up_1_EBNoVal.insert(0, 8.9)
        #self.entry_up_1_EBNoVal.configure(state='disabled')
        #
        self.up_1_modulationtypes = ('FSK', 'BPSK', 'Other')
        self.entry_up_1_BER = tk.StringVar(self.commsgui)
        self.up_1_BERs = ('10^-2', '10^-3', '10^-4', '10^-5', '10^-6')
        self.up_1_modmenu = ttk.OptionMenu(self.tabUplink, self.entry_up_1_modulationtype, self.up_1_modulationtypes[0], *self.up_1_modulationtypes, command=lambda e=self.entry_up_1_modulationtype.get(): modCheck(e))
        self.up_1_BERmenu = ttk.OptionMenu(self.tabUplink, self.entry_up_1_BER, self.up_1_BERs[0], *self.up_1_BERs, command=lambda e=self.entry_up_1_BER.get() : BERCheck(e))


        self.entry_up_1_antennatype = tk.StringVar(self.commsgui)
        self.entry_up_1_beamwidth= tk.DoubleVar(self.commsgui)
        self.entry_up_1_beamwidthVal = ttk.Entry(self.tabUplink, textvariable=self.entry_up_1_beamwidth, width = w)
        self.entry_up_1_beamwidthVal.delete(0)
        self.entry_up_1_beamwidthVal.insert(0,90)
        self.up_1_antennas = ('Patch', 'Monopole', 'Dipole', 'Other')
        self.up_1_antmenu = ttk.OptionMenu(self.tabUplink, self.entry_up_1_antennatype, self.up_1_antennas[0], *self.up_1_antennas, command=lambda e=self.entry_up_1_antennatype: antCheck(e))
        
        self.entry_up_2_antennatype = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_antennatype.insert(0,0)
        self.entry_up_2_beamwidth = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_beamwidth.insert(0,0)

        self.entry_up_2_EBNo = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_EBNo.insert(0,0)
        self.entry_up_1_BER = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_BER.insert(0,0)
        self.entry_up_2_BER = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_BER.insert(0,0)
        self.entry_up_1_atmosphereattenuation = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_atmosphereattenuation.insert(0,0)
        self.entry_up_2_atmosphereattenuation = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_atmosphereattenuation.insert(0,0)
        self.entry_up_1_rainattenuation = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_rainattenuation.insert(0,0)
        self.entry_up_2_rainattenuation = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_rainattenuation.insert(0,0)
        self.entry_up_1_systemtemp = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_systemtemp.insert(0,0)
        self.entry_up_2_systemtemp = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_systemtemp.insert(0,0)
        self.entry_up_1_lineloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_lineloss.insert(0,0)
        self.entry_up_2_lineloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_lineloss.insert(0,0)
        self.entry_up_1_spaceloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_spaceloss.insert(0,0)
        self.entry_up_2_spaceloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_spaceloss.insert(0,0)
        self.entry_up_1_polarizationloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_polarizationloss.insert(0,0)
        self.entry_up_1_transmitterpointingloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_transmitterpointingloss.insert(0,0)
        self.entry_up_2_transmitterpointingloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_transmitterpointingloss.insert(0,0)
        self.entry_up_1_receiverpointingloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_receiverpointingloss.insert(0,0)
        self.entry_up_2_receiverpointingloss = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_receiverpointingloss.insert(0,0)
        self.entry_up_1_transmitterdishdiameter = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_transmitterdishdiameter.insert(0,0)
        self.entry_up_2_transmitterdishdiameter = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_transmitterdishdiameter.insert(0,0)
        self.entry_up_1_receiverdishdiameter = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_receiverdishdiameter.insert(0,0)
        self.entry_up_2_receiverdishdiameter = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_receiverdishdiameter.insert(0,0)
        self.entry_up_1_transmitterefficiency = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_transmitterefficiency.insert(0,0)
        self.entry_up_2_transmitterefficiency = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_transmitterefficiency.insert(0,0)
        self.entry_up_1_receiverefficiency = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_1_receiverefficiency.insert(0,0)
        self.entry_up_2_receiverefficiency = ttk.Entry(self.tabUplink, width = w)
        self.entry_up_2_receiverefficiency.insert(0,0)

        # Downlink Tab Entry Values
        w = 6
        self.entry_down_1_frequency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_frequency.insert(0,0)
        self.entry_down_2_frequency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_frequency.insert(0,0)
        self.entry_down_1_EBNo = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_EBNo.insert(0,0)
        self.entry_down_2_EBNo = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_EBNo.insert(0,0)
        self.entry_down_1_BER = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_BER.insert(0,0)
        self.entry_down_2_BER = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_BER.insert(0,0)
        self.entry_down_1_antennatype = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_antennatype.insert(0,0)
        self.entry_down_2_antennatype = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_antennatype.insert(0,0)
        self.entry_down_1_beamwidth = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_beamwidth.insert(0,0)
        self.entry_down_2_beamwidth = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_beamwidth.insert(0,0)
        self.entry_down_1_atmosphereattenuation = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_atmosphereattenuation.insert(0,0)
        self.entry_down_2_atmosphereattenuation = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_atmosphereattenuation.insert(0,0)
        self.entry_down_1_rainattenuation = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_rainattenuation.insert(0,0)
        self.entry_down_2_rainattenuation = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_rainattenuation.insert(0,0)
        self.entry_down_1_systemtemp = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_systemtemp.insert(0,0)
        self.entry_down_2_systemtemp = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_systemtemp.insert(0,0)
        self.entry_down_1_lineloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_lineloss.insert(0,0)
        self.entry_down_2_lineloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_lineloss.insert(0,0)
        self.entry_down_1_spaceloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_spaceloss.insert(0,0)
        self.entry_down_2_spaceloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_spaceloss.insert(0,0)
        self.entry_down_1_polarizationloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_polarizationloss.insert(0,0)
        self.entry_down_1_transmitterpointingloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_transmitterpointingloss.insert(0,0)
        self.entry_down_2_transmitterpointingloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_transmitterpointingloss.insert(0,0)
        self.entry_down_1_receiverpointingloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_receiverpointingloss.insert(0,0)
        self.entry_down_2_receiverpointingloss = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_receiverpointingloss.insert(0,0)
        self.entry_down_1_transmitterdishdiameter = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_transmitterdishdiameter.insert(0,0)
        self.entry_down_2_transmitterdishdiameter = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_transmitterdishdiameter.insert(0,0)
        self.entry_down_1_receiverdishdiameter = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_receiverdishdiameter.insert(0,0)
        self.entry_down_2_receiverdishdiameter = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_receiverdishdiameter.insert(0,0)
        self.entry_down_1_transmitterefficiency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_transmitterefficiency.insert(0,0)
        self.entry_down_2_transmitterefficiency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_transmitterefficiency.insert(0,0)
        self.entry_down_1_receiverefficiency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_1_receiverefficiency.insert(0,0)
        self.entry_down_2_receiverefficiency = ttk.Entry(self.tabDownlink, width = w)
        self.entry_down_2_receiverefficiency.insert(0,0)

        ##Start hereee##


        ### Uplink: Ground Station to Spacecraft Tab ###

        ## Need to figure out placement and entry type/formatting

        #Header
        R = 0; C = 0
        t_ins_design = 'Input appropriate parameter values for Ground Station comms:'
        self.choose = ttk.Label(self.tabUplink,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Primary Uplink Frequency
        R = 3; C = 0
        ttk.Label(self.tabUplink, text='Frequency Type').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        ttk.Label(self.tabUplink, text='Frequency [Hz]').grid(row=R, column=C+1, padx=25, pady=5,sticky='w')
        self.up_1_freqmenu.grid(column=C, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')
        self.entry_up_1_frequencyVal.grid(column=C+1, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')
        
        # Primary Uplink EB/No 
        R = 5; C = 0
        ttk.Label(self.tabUplink, text='Modulation Type').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        ttk.Label(self.tabUplink, text='BER').grid(row=R, column=C+1, padx=25, pady=5,sticky='w')
        ttk.Label(self.tabUplink, text='EB/No [dB]').grid(row=R, column=C+2, padx=25, pady=5,sticky='w')
        self.up_1_modmenu.grid(column=C, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')
        self.up_1_BERmenu.grid(column=C+1, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')
        self.entry_up_1_EBNoVal.grid(row=R+1, column=C+2, padx=25, pady=5,sticky='w')

        # Primary Uplink Antenna Type 
        R = 7; C = 0
        ttk.Label(self.tabUplink, text='Antenna Type').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        ttk.Label(self.tabUplink, text='Beamwidth [deg]').grid(row=R, column=C+1, padx=25, pady=5,sticky='w')
        self.up_1_antmenu.grid(column=C, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')
        self.entry_up_1_beamwidthVal.grid(column=C+1, row=R+1, columnspan = 2, padx = 25, pady = 5,sticky='w')


        #Primary Uplink Atmosphere Attenuation
        R = 8; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Atmosphere Attenuation').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_atmosphereattenuation.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Uplink Rain Attenuation
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Rain Attenuation').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_rainattenuation.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink System Temperature
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink System Temperature').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_systemtemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Line Loss
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Line Loss').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_lineloss.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Space Loss
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Space Loss').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_spaceloss.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Polarization Loss
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Polarization Loss').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_polarizationloss.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Transmitter Pointing Loss
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Transmitter Pointing Loss').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_transmitterpointingloss.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Receiving Pointing Loss
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Receiver Pointing Loss').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_receiverpointingloss.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Transmitter Dish Diameter
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Transmitter Dish Diameter').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_transmitterdishdiameter.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Receiver Dish Diameter
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Receiver Dish Diameter').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_receiverdishdiameter.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Transmitter Efficiency
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Transmitter Efficiency').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_transmitterefficiency.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        #Primary Uplink Receiver Efficiency
        R = 9; C = 2
        ttk.Label(self.tabUplink, text='Primary Uplink Receiver Efficiency').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_1_receiverefficiency.grid(row=R, column=C+1, padx=5, pady=5,stick='w')


        ### Secondary Spacecraft Transmitter Power ###
        R = 3; C = 2
        ttk.Label(self.tabUplink, text='Secondary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_s_sc_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        

         # System Noise Temp
        R = 3; C = 4
        ttk.Label(self.tabUplink, text='System Temp [K]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_systemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Maximum Distance From Earth
        R = 4; C = 4
        ttk.Label(self.tabUplink, text='Max Distance from Earth [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_maxdistanceEarth.grid(row=R, column=C+1, padx=5, pady=5)

        # Rain Losses
        R = 5; C = 4
        ttk.Label(self.tabUplink, text='Rain Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_rainloss.grid(row=R, column=C+1, padx=5, pady=5)
        
        # Line Losses
        R = 6; C = 4
        ttk.Label(self.tabUplink, text='Line Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_lineloss.grid(row=R, column=C+1, padx=5, pady=5)

        # Other Losses
        R = 7; C = 4
        ttk.Label(self.tabUplink, text='Other Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_up_otherloss.grid(row=R, column=C+1, padx=5, pady=5)

        ## Downlink: Spacecraft to Groundstation Tab ##
        
        # Heading - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Input appropriate parameter values for Spacecraft comms:'
        self.choose = ttk.Label(self.tabDownlink,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Primary Spacecraft Transmitter Power
        R = 3; C = 0
        ttk.Label(self.tabDownlink, text='Primary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_sc_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Primary Spacecraft Antenna Gain 
        R = 4; C = 0
        ttk.Label(self.tabDownlink, text='Primary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_sc_antgain.grid(row=R, column=C+1, padx=5, pady=5)

         # Primary GroundStation Transmitter Power
        R = 5; C = 0
        ttk.Label(self.tabDownlink, text='Primary GroundStation Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_gs_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Primary GroundStation Antenna Gain 
        R = 6; C = 0
        ttk.Label(self.tabDownlink, text='Primary GroundStation Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_gs_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Datarate
        R = 7; C = 0
        ttk.Label(self.tabDownlink, text='Primary Datarate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_datarate.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Frequency
        R = 8; C = 0
        ttk.Label(self.tabDownlink, text='Primary Frequency [Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_frequency.grid(row=R, column=C+1, padx=5, pady=5)

        #Primary Eb/N0 
        R = 9; C = 0
        ttk.Label(self.tabDownlink, text='Primary Eb/N0 [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_p_EBNo.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Secondary Spacecraft Transmitter Power
        R = 3; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_sc_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Antenna Gain
        R = 4; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_sc_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Transmitter Power
        R = 5; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_gs_transpower.grid(row=R, column=C+1, padx=5, pady=5)

        # Secondary Spacecraft Antenna Gain
        R = 6; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Spacecraft Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_gs_antgain.grid(row=R, column=C+1, padx=5, pady=5)

        #Secondary Datarate
        R = 7; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Datarate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_datarate.grid(row=R, column=C+1, padx=5, pady=5)

        #Frequency Secondary
        R = 8; C = 2
        ttk.Label(self.tabDownlink, text='Secondary Frequency [Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_frequency.grid(row=R, column=C+1, padx=5, pady=5)

        #EBNO Secondary 
        R = 9; C = 2 
        ttk.Label(self.tabDownlink, text='Secondary Eb/N0 [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_s_EBNo.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

         # System Noise Temp
        R = 3; C = 4
        ttk.Label(self.tabDownlink, text='System Temp [K]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_systemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Maximum Distance From Earth
        R = 4; C = 4
        ttk.Label(self.tabDownlink, text='Max Distance from Earth [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_maxdistanceEarth.grid(row=R, column=C+1, padx=5, pady=5)

        # Rain Losses
        R = 5; C = 4
        ttk.Label(self.tabDownlink, text='Rain Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_rainloss.grid(row=R, column=C+1, padx=5, pady=5)
        
        # Line Losses
        R = 6; C = 4
        ttk.Label(self.tabDownlink, text='Line Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_lineloss.grid(row=R, column=C+1, padx=5, pady=5)

        # Other Losses
        R = 7; C = 4
        ttk.Label(self.tabDownlink, text='Other Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.entry_down_otherloss.grid(row=R, column=C+1, padx=5, pady=5)

        # Submit Button
        R = 14; C = 5
        self.UseCase = 2
        self.sub_btn = ttk.Button(self.tabDownlink, text = "Submit", command = self.inputComms)
        self.sub_btn.grid(column = C, row = R)
        # Done Button
        self.fin_btn = ttk.Button(self.tabDownlink, text = "Close", command = self.allDone)
        self.fin_btn.grid(column = C+1, row = R,stick='w')
        
        # Run
        self.commsgui.mainloop()
   
    def inputComms(self):
        if self.UseCase == 1:
            try:
                self.up_p_sc_transpower= float(self.entry_up_p_sc_transpower.get())
            except:
                pass
            try:
                self.up_p_sc_antgain= float(self.entry_up_p_sc_antgain.get())
            except:
                pass     
            try:
                self.up_p_gs_transpower= float(self.entry_up_p_gs_transpower.get())
            except:
                pass
            try:
                self.up_p_gs_antgain= float(self.entry_up_p_gs_antgain.get())
            except:
                pass         
            try:
                self.up_p_datarate = float(self.entry_up_p_datarate.get())
            except:
                pass
            try:
                self.up_p_frequency = float(self.entry_up_p_frequency.get())
            except:
                pass
            try:
                self.up_p_EBNo = float(self.entry_up_p_EBNo.get())
            except:
                pass
            try:
                self.up_s_sc_transpower= float(self.entry_up_s_sc_transpower.get())
            except:
                pass
            try:
                self.up_s_sc_antgain= float(self.entry_up_s_sc_antgain.get())
            except:
                pass     
            try:
                self.up_s_gs_transpower= float(self.entry_up_s_gs_transpower.get())
            except:
                pass
            try:
                self.up_s_gs_antgain= float(self.entry_up_s_gs_antgain.get())
            except:
                pass         
            try:
                self.up_s_datarate = float(self.entry_up_s_datarate.get())
            except:
                pass
            try:
                self.up_s_frequency = float(self.entry_up_s_frequency.get())
            except:
                pass
            try:
                self.up_s_EBNo = float(self.entry_up_s_EBNo.get())
            except:
                pass
            try:
                self.up_systemp = float(self.entry_up_systemp.get())
            except:
                pass
            try:
                self.up_maxdistanceEarth = float(self.entry_up_maxdistanceEarth.get())
            except:
                pass
            try:
                self.up_rainloss = float(self.entry_up_rainloss.get())
            except:
                pass
            try:
                self.up_lineloss = int(self.entry_up_lineloss.get())
            except:
                pass            
            try:
                self.up_otherloss = int(self.entry_up_otherloss.get())
            except:
                pass
            try:
                self.down_p_sc_transpower= float(self.entry_down_p_sc_transpower.get())
            except:
                pass
            try:
                self.down_p_sc_antgain= float(self.entry_down_p_sc_antgain.get())
            except:
                pass     
            try:
                self.down_p_gs_transpower= float(self.entry_down_p_gs_transpower.get())
            except:
                pass
            try:
                self.down_p_gs_antgain= float(self.entry_down_p_gs_antgain.get())
            except:
                pass         
            try:
                self.down_p_datarate = float(self.entry_down_p_datarate.get())
            except:
                pass
            try:
                self.down_p_frequency = float(self.entry_down_p_frequency.get())
            except:
                pass
            try:
                self.down_p_EBNo = float(self.entry_down_p_EBNo.get())
            except:
                pass
            try:
                self.down_s_sc_transpower= float(self.entry_down_s_sc_transpower.get())
            except:
                pass
            try:
                self.down_s_sc_antgain= float(self.entry_down_s_sc_antgain.get())
            except:
                pass     
            try:
                self.down_s_gs_transpower= float(self.entry_down_s_gs_transpower.get())
            except:
                pass
            try:
                self.down_s_gs_antgain= float(self.entry_down_s_gs_antgain.get())
            except:
                pass         
            try:
                self.down_s_datarate = float(self.entry_down_s_datarate.get())
            except:
                pass
            try:
                self.down_s_frequency = float(self.entry_down_s_frequency.get())
            except:
                pass
            try:
                self.down_s_EBNo = float(self.entry_down_s_EBNo.get())
            except:
                pass
            try:
                self.down_systemp = float(self.entry_down_systemp.get())
            except:
                pass
            try:
                self.down_maxdistanceEarth = float(self.entry_down_maxdistanceEarth.get())
            except:
                pass
            try:
                self.down_rainloss = float(self.entry_down_rainloss.get())
            except:
                pass
            try:
                self.down_lineloss = int(self.entry_down_lineloss.get())
            except:
                pass            
            try:
                self.down_otherloss = int(self.entry_down_otherloss.get())
            except:
                pass
        # elif self.UseCase == 2:
        #     try:
        #         #self.up_p_sc_transpower= float(self.entry_up_p_sc_transpower.get())
        #     except:
        #         pass
    
    def selectionError(self):
            self.commsgui = tk.Tk() # Instance of Tk,
            self.commsgui.title("Communications Module") # Name
            self.commswindow = ttk.Notebook(self.commsgui) # tkk module implements "tabs" (Notebook)
            self.tabError = ttk.Frame(self.commswindow)
            # Create Tab
            self.commswindow.add(self.tabError, text = 'Error')
            self.commswindow.pack(expand = 1, fill ="both")
            # Error Message
            self.R0_C0 = ttk.Label(self.tabError, text='Please select a Use Case!', wraplength = 200)
            self.R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
            # Close Button
            self.cls_btn = ttk.Button(self.tabError, text = "Close", command = self.allDone) 
            self.cls_btn.grid(column = 0, row = 1, padx = 5, pady = 5)
            self.commsgui.mainloop()
    
    def designOptionError(self):
            self.commsgui = tk.Tk() # Instance of Tk,
            self.commsgui.title("Communications Module") # Name
            self.commswindow = ttk.Notebook(self.commsgui) # tkk module implements "tabs" (Notebook)
            self.tabError = ttk.Frame(self.commswindow)
            # Create Tab
            self.commswindow.add(self.tabError, text = 'Error')
            self.commswindow.pack(expand = 1, fill ="both")
            # Error Message
            self.R0_C0 = ttk.Label(self.tabError, text='Please select a Design Option from the EPS Design Tab!', wraplength = 200)
            self.R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5)
            # Close Button
            self.cls_btn = ttk.Button(self.tabError, text = "Close", command = self.allDone) 
            self.cls_btn.grid(column = 0, row = 1, padx = 5, pady = 5)
            self.commsgui.mainloop()
        
    def allDone(self):
        self.commsgui.destroy() 