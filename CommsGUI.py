import tkinter as tk
from tkinter import StringVar, ttk
        
#########           NAMING CONVENTION       ########### 
#               TAB_*ORDER_*ENTITY_VARIABLE            #
## TAB specifies which tab: 'up' or 'down' for uplink or downlink
## *ORDER specifies which band: 'p' or 's' for primary or secondary
## *ENTITY specifies which entity: 'sc' or 'gs' for spacecraft or groundstation
## VARIABLE specifies variable name: ex: 'transpower', 'antgain', etc. 
######### please note: * means value is not necessarily required.  ORDER and ENTITY 
######### labels don't apply to certain variables and may be skipped.  Ex: up_systemp or up_p_datarate


class Comms:
    def __init__(self):
        # Initialize Comms Data
        self.UseCase: int


        # UPLINK TAB
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
        
        # Uplink Tab
        #self.transPowerxG = ''
        #self.antGainxG = ''
        #self.dishDiameterG = ''
        #self.transPoweruG = ''
        #self.antGainuG = ''
        #self.xup = ''
        #self.uup = ''
        #self.xfreqG = ''
        #self.ufreqG = ''
        #self.maxDistanceEarthG = ''
        #self.rainLossG = ''
        #self.sysTempG = ''
        #self.ebnoxG = ''
        #self.ebnouG = ''
        #self.lineLossG = ''
        ##self.cenFreq = '' 
        ##self.pointingLoss = ''
        ##self.electronLoss = ''
        ##self.polarLoss = ''
        ##self.maxSlantRange = ''
        ##self.EIRP = ''
        ##self.minElevationAngle = ''
        

        # DOWNLINK TAB
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

        # self.transPowerxS = ''
        # self.antGainxS = ''
        # self.transPoweruS = ''
        # self.antGainuS = ''
        # self.xdown = ''
        # self.udown = ''
        # self.xfreqS = ''
        # self.ufreqS = ''
        # self.maxDistanceEarthS = ''
        # self.rainLossS = ''
        # self.sysTempS = ''
        # self.ebnoxS = ''
        # self.ebnouS = ''
        # self.lineLossS = ''
        ##self.dishDiameterS = ''
        

        # Data Generation
        # self.atomClock = ''
        # self.radiation = ''
        # self.housekeeping = ''
        

        # OUTPUTS 
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

        # self.outTransPowerDXS: float
        # self.outTransPowerDUS: float
        # self.outAntGainDXS: float
        # self.outAntGainDUS: float
        # self.outAntGainUXS: float
        # self.outAntGainUUS: float 
        # self.outTransPowerUXG: float
        # self.outTransPowerUUG: float
        # self.outAntGainDXG: float
        # self.outAntGainDUG: float
        # self.outAntGainUXG: float
        # self.outAntGainUUG: float
        # self.outEBNODXS: float
        # self.outEBNODUS: float
        # self.outEBNOUXG: float
        # self.outEBNOUUG: float
        # self.outDataRateDX: float
        # self.outDataRateDU: float
        # self.outDataRateUX: float
        # self.outDataRateUU: float
        # self.outNoiseTempG: float
        # self.outNoiseTempS: float
        # self.outPathLossXG: float
        # self.outPathLossUG: float
        # self.outPathLossXS: float
        # self.outPathLossUS: float
        # self.outOtherLossG: float
        # self.outOtherLossS: float
        # self.outMarginDX: float
        # self.outMarginDU: float
        # self.outMarginUX: float
        # self.outMarginUU: float


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
            self.T1_R0_C0 = ttk.Label(self.tabInputs, text='Power Budget:', wraplength = 100)
            self.T1_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')
            t='Collected from subsystem design modules.'
            self.T1_R0_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R0_C1.grid(row = 0, column = 1, padx = 5, pady = 5,sticky='w')
            self.T1_R1_C0 = ttk.Label(self.tabInputs, text='EPS Design Parameters:', wraplength = 100)
            self.T1_R1_C0.grid(row = 1, column = 0, padx = 5, pady = 5,sticky='w')
            t ='Parameters for capabilities of solar system, battery system, and PMAD system, along with power margin.'
            self.T1_R1_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R1_C1.grid(row = 1, column = 1, padx = 5, pady = 5,sticky='w')
            
            # Assumptions
            t = 'Assumed values include constants, such as solar flux, '\
                'as well as design sizing parameters for the spacecraft '\
                'if non-custom is chosen'
            self.T2_R0_C0 = ttk.Label(self.tabAssums, text=t, wraplength = 350)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')

            # Calculations
            t = 'Calculated values include sizing of solar panel and batteries, '\
                'based on calculated total power values, with appropriate '\
                'degradating and orbit considerations in place.'
            self.T3_R0_C0 = ttk.Label(self.tabCalcs, text=t, wraplength = 350)
            self.T3_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')

    def linkbudget4demo(self):
        self.commsgui = tk.Tk() # Instance of Tk,
        self.commsgui.title("Communications Subsystem Design Module") # Name
        self.commswindow = ttk.Notebook(self.commsgui) # tkk module implements "tabs" (Notebook)
        self.tabUplink = ttk.Frame(self.commswindow)
        self.tabDownlink = ttk.Frame(self.commswindow)
        self.commswindow.add(self.tabUplink, text = 'Uplink')
        self.commswindow.add(self.tabDownlink, text = 'Downlink')
        ##self.commswindow.add(self.tabDataGen, text = 'Data Generation')
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
        
        # self.ctransPowerxG = ttk.Entry(self.tabGroundStation,width = w)
        # self.ctransPowerxG.insert(0,0)
        # self.cantGainxG = ttk.Entry(self.tabGroundStation, width = w)
        # self.cantGainxG.insert(0,0)
        # ##self.cdishDiameterG = ttk.Entry(self.tabGroundStation, width = w)
        # self.ctransPoweruG = ttk.Entry(self.tabGroundStation,width = w)
        # self.ctransPoweruG.insert(0,0)
        # self.cantGainuG = ttk.Entry(self.tabGroundStation, width = w)
        # self.cantGainuG.insert(0,0)
        # self.cxup = ttk.Entry(self.tabGroundStation, width = w)
        # self.cxup.insert(0,0)
        # self.cuup = ttk.Entry(self.tabGroundStation, width = w)
        # self.cuup.insert(0,0)
        # self.cxUpFreq = ttk.Entry(self.tabGroundStation, width = w)
        # self.cxUpFreq.insert(0,0)
        # self.cuUpFreq = ttk.Entry(self.tabGroundStation, width = w)
        # self.cuUpFreq.insert(0,0)
        # self.cebnoxG = ttk.Entry(self.tabGroundStation, width = w)
        # self.cebnoxG.insert(0,0)
        # self.cebnouG = ttk.Entry(self.tabGroundStation, width = w)
        # self.cebnouG.insert(0,0)
        # self.csysTempG = ttk.Entry(self.tabGroundStation, width = w)
        # self.csysTempG.insert(0, 300)
        # self.cmaxDistanceEarthG = ttk.Entry(self.tabGroundStation, width = w)
        # self.cmaxDistanceEarthG.insert(0, 2704)
        # self.crainLossG = ttk.Entry(self.tabGroundStation, width = w)
        # self.crainLossG.insert(0, 3)
        # self.clineLossG = ttk.Entry(self.tabGroundStation, width = w)
        # self.clineLossG.insert(0, 3)
        # self.clineLossG = ttk.Entry(self.tabGroundStation, width = w)
        # self.cmaxSlantRange = ttk.Entry(self.tabGroundStation, width = w)
        # self.cEIRP = ttk.Entry(self.tabGroundStation, width = w)
        # self.cminElevationAngle = ttk.Entry(self.tabGroundStation, width = w)
        # self.cminElevationAngle.insert(0, 1)
        

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

        # self.ctransPowerxS = ttk.Entry(self.tabDownlink, width = w)
        # self.ctransPowerxS.insert(0,0)
        # self.cantGainxS = ttk.Entry(self.tabDownlink, width = w)
        # self.cantGainxS.insert(0,0)
        # self.ctransPoweruS = ttk.Entry(self.tabDownlink, width = w)
        # self.ctransPoweruS.insert(0,0)
        # self.cantGainuS = ttk.Entry(self.tabDownlink, width = w)
        # self.cantGainuS.insert(0,0)
        # self.cxdown = ttk.Entry(self.tabDownlink, width = w)
        # self.cxdown.insert(0,0)
        # self.cudown = ttk.Entry(self.tabDownlink, width = w)
        # self.cudown.insert(0,0)
        # self.cxDownFreq = ttk.Entry(self.tabDownlink, width = w)
        # self.cxDownFreq.insert(0,0)
        # self.cuDownFreq = ttk.Entry(self.tabDownlink, width = w)
        # self.cuDownFreq.insert(0,0)
        # self.cebnoxS = ttk.Entry(self.tabDownlink, width = w)
        # self.cebnoxS.insert(0,0)
        # self.cebnouS = ttk.Entry(self.tabDownlink, width = w)
        # self.cebnouS.insert(0,0)
        # self.csysTempS = ttk.Entry(self.tabDownlink, width = w)
        # self.csysTempS.insert(0, 300)
        # self.cmaxDistanceEarthS = ttk.Entry(self.tabDownlink, width = w)
        # self.cmaxDistanceEarthS.insert(0, 2704)
        # self.crainLossS = ttk.Entry(self.tabDownlink, width = w)
        # self.crainLossS.insert(0, 3)
        # self.clineLossS = ttk.Entry(self.tabDownlink, width = w)
        # self.clineLossS.insert(0, 3)
        # self.cdishDiameterS = ttk.Entry(self.tabSpacecraft, width = w)
        # self.clineLossS = ttk.Entry(self.tabSpacecraft, width = w)
        # self.clineLossS.insert(0, 1)

        # Data Generation Entry Values
        # w = 6
        # self.catomClock = ttk.Entry(self.tabDataGen, width = w)
        # self.catomClock.insert(0, '1')
        # self.cradiation = ttk.Entry(self.tabDataGen, width = w)
        # self.cradiation.insert(0, '1.5')
        # self.chousekeeping = ttk.Entry(self.tabDataGen, width = w)
        # self.chousekeeping.insert(0, '54')


        ### Uplink: Ground Station to Spacecraft Tab ###
        # Header - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Input appropriate parameter values for Ground Station comms:'
        self.choose = ttk.Label(self.tabUplink,text = t_ins_design, wraplength = 250)
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

        # Dish Diameter
        # R = 5; C = 0
        # ttk.Label(self.tabGroundStation, text='Dish Diameter [m]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cdishDiameterG.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

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

        # Line Loss
        # R = 3; C = 2
        # ttk.Label(self.tabGroundStation, text='Line Loss [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.clineLossG.grid(row=R, column=C+1, padx=5, pady=5)

        # # Maximum Slant Range
        # R = 4; C = 2
        # ttk.Label(self.tabGroundStation, text='Max Slant Range [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cmaxSlantRange.grid(row=R, column=C+1, padx=5, pady=5)

        # # EIRP
        # R = 5; C = 2
        # ttk.Label(self.tabGroundStation, text='EIRP [dBm]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cEIRP.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # # Minimum Elevation Angle
        # R = 6; C = 2
        # ttk.Label(self.tabGroundStation, text='Minimum Elevation Angle [rad]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cminElevationAngle.grid(row=R, column=C+1, padx=5, pady=5,stick='w')
        
        

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

        # Dish Diameter
        # R = 5; C = 0
        # ttk.Label(self.tabGroundStation, text='Dish Diameter [m]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cdishDiameterG.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

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

        # Dish Diameter
        # R = 3; C = 2
        # ttk.Label(self.tabSpacecraft, text='Dish Diameter [m]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cdishDiameterS.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

        


        ## Data Generation Tab ##
        
        # Heading -NOT FINISHED
        # R = 0; C = 0
        # t_ins_design = 'Input appropriate parameter values for Data Generation:'
        # self.choose = ttk.Label(self.tabDataGen,text = t_ins_design, wraplength = 250)
        # self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # # Atomic Clock
        # R = 3; C = 0
        # ttk.Label(self.tabDataGen, text='Atomic Clock [Mbyte/day]       ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.catomClock.grid(row=R, column=C+1, padx=5, pady=5)

        # # Radiation
        # R = 4; C = 0
        # ttk.Label(self.tabDataGen, text='Radiation [Mbyte/day]        ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cradiation.grid(row=R, column=C+1, padx=5, pady=5)

        # # House Keeping
        # R = 5; C = 0
        # ttk.Label(self.tabDataGen, text='House Keeping [Mbyte/day]        ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.chousekeeping.grid(row=R, column=C+1, padx=5, pady=5)

        # # Spacer 
        # R = 6; C = 0
        # ttk.Label(self.tabDataGen, text=' ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        

        # Back Button
        # R = 14; C = 2
        # self.UseCase = 1
        # self.back_btn = ttk.Button(self.tabDataGen, text = "Back", command = self.tabSpacecraft)
        # self.back_btn.grid(column = C, row = R)
        
        # # Next Button
        # self.next_btn = ttk.Button(self.tabDataGen, text = "Next", command = self.tabOther)
        # self.next_btn.grid(column = C+1, row = R,sticky='w')

        # Submit Button
        R = 14; C = 5
        self.UseCase = 1
        self.sub_btn = ttk.Button(self.tabDownlink, text = "Submit", command = self.inputComms)
        self.sub_btn.grid(column = C, row = R)
        # Done Button
        self.fin_btn = ttk.Button(self.tabDownlink, text = "Close", command = self.allDone)
        self.fin_btn.grid(column = C+1, row = R,stick='w')


        ## Other Tab ##

        # # Header - NOT FINISHED
        # R = 0; C = 0
        # t_ins_design = 'Input appropriate parameter values:'
        # self.choose = ttk.Label(self.tabOther,text = t_ins_design, wraplength = 250)
        # self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        

        # # Central Frequency
        # # R = 3; C = 2
        # # ttk.Label(self.tabOther, text='Central Frequency [GHz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # # self.ccenFreq.grid(row=R, column=C+1, padx=5, pady=5)

        # # # Pointing Losses
        # # R = 4; C = 2
        # # ttk.Label(self.tabOther, text='Pointing Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # # self.cpointingLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # # # Election Losses
        # # R = 6; C = 2
        # # ttk.Label(self.tabOther, text='Electron Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # # self.celectronLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # # # Polarization Losses
        # # R = 7; C = 2
        # # ttk.Label(self.tabOther, text='Polarization Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # # self.cpolarLoss.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

        # # # Fixed Data Rate
        # # R = 9; C = 2
        # # ttk.Label(self.tabOther, text='Fixed Data Rate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # # self.cfixedData.grid(row=R, column=C+1, padx=5, pady=5,stick='w') 

        # # System Noise Temp
        # R = 3; C = 2
        # ttk.Label(self.tabOther, text='System Temp [K]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.csysTemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # # Maximum Distance From Earth
        # R = 4; C = 2
        # ttk.Label(self.tabOther, text='Max Distance from Earth [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cmaxDistanceEarth.grid(row=R, column=C+1, padx=5, pady=5)

        # # Rain Losses
        # R = 5; C = 2
        # ttk.Label(self.tabOther, text='Rain Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.crainLoss.grid(row=R, column=C+1, padx=5, pady=5)
        
        # #EBNO Primary
        # R = 6; C=2
        # ttk.Label(self.tabOther, text='Primary Eb/N0[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cebnox.grid(row=R, column=C+1, padx=5, pady=5,stick='w')
        
        # #EBNO Secondary
        # R = 7; C=2
        # ttk.Label(self.tabOther, text='Secondary Eb/N0[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.cebnou.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # # Line Losses
        # R = 8; C = 2
        # ttk.Label(self.tabOther, text='Line Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        # self.clineLoss.grid(row=R, column=C+1, padx=5, pady=5)

        
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
            # try:
            #     self.maxSlantRange = float(self.cmaxSlantRange.get())
            # except:
            #     pass
            # try:
            #     self.dishDiameterS = float(self.cdishDiameterS.get())
            # except:
            #     pass
            # try:
            #     self.EIRP = float(self.cEIRP.get())
            # except:
            #     pass
            # try:
            #     self.minElevationAngle = int(self.cminElevationAngle.get())
            # except:
            #     pass
            # try:
            #     self.atomClock = float(self.catomClock.get())
            # except:
            #     pass
            # try:
            #     self.radiation = float(self.cradiation.get())
            # except:
            #     pass
            # try:
            #     self.housekeeping = float(self.chousekeeping.get())
            # except:
            #     pass   
            """try:
                self.cenFreq= float(self.ccenFreq.get())
            except:
                pass
            try:
                self.pointingLoss = float(self.cpointingLoss.get())
            except:
                pass
            try:
                self.electronLoss = float(self.celectronLoss.get())
            except:
                pass
            try:
                self.polarLoss = float(self.cpolarLoss.get())
            except:
                pass
            try:
                self.fixedData = int(self.cfixedData.get())
            except:
                pass"""
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