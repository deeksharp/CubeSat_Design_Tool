import tkinter as tk
from tkinter import StringVar, ttk
        

class Comms:
    def __init__(self):
        # Initialize Comms Data
        self.UseCase: int

        # Ground Station Tab
        self.transPowerxG = ''
        self.antGainxG = ''
        self.dishDiameterG = ''
        self.transPoweruG = ''
        self.antGainuG = ''
        ##self.lineLossG = ''
        ##self.maxSlantRange = ''
        ##self.EIRP = ''
        ##self.minElevationAngle = ''
        

        # Spacecraft
        self.transPowerxS = ''
        self.antGainxS = ''
        self.transPoweruS = ''
        self.antGainuS = ''
        ##self.dishDiameterS = ''
        ##self.lineLossS = ''
        

        # Data Generation
        self.atomClock = ''
        self.radiation = ''
        self.housekeeping = ''

        # Other 
        self.xdown = ''
        self.udown = ''
        self.xup = ''
        self.uup = ''
        self.xfreq = ''
        self.ufreq = ''
        self.maxDistanceEarth = ''
        ##self.cenFreq = ''
        ##self.pointingLoss = ''
        self.rainLoss = ''
        ##self.electronLoss = ''
        ##self.polarLoss = ''
        self.sysTemp = ''
        self.ebnox = ''
        self.ebnou = ''
        self.lineLoss = ''
        ##self.fixedData = ''

        # outputs
        self.outTransPowerDXS: float
        self.outTransPowerDUS: float
        self.outAntGainDXS: float
        self.outAntGainDUS: float
        self.outAntGainUXS: float
        self.outAntGainUUS: float 
        self.outTransPowerUXG: float
        self.outTransPowerUUG: float
        self.outAntGainDXG: float
        self.outAntGainDUG: float
        self.outAntGainUXG: float
        self.outAntGainUUG: float
        self.outEBNODX: float
        self.outEBNODU: float
        self.outEBNOUX: float
        self.outEBNOUU: float
        self.outDataRateDX: float
        self.outDataRateDU: float
        self.outDataRateUX: float
        self.outDataRateUU: float
        self.outNoiseTemp: float
        self.outPathLossX: float
        self.outPathLossU: float
        self.outOtherLoss: float
        self.outMarginDX: float
        self.outMarginDU: float
        self.outMarginUX: float
        self.outMarginUU: float


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
            self.T1_R0_C0 = ttk.Label(self.tabInputs, text='Line Budget:', wraplength = 100)
            self.T1_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')
            t='Ground Station and Spacecraft parameters are prepopulated with assumed values and can be changed to reflect current design parameters. '
            self.T1_R0_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R0_C1.grid(row = 0, column = 1, padx = 5, pady = 5,sticky='w')
            self.T1_R1_C0 = ttk.Label(self.tabInputs, text='EPS Design Parameters:', wraplength = 100)
            self.T1_R1_C0.grid(row = 1, column = 0, padx = 5, pady = 5,sticky='w')
            t ='Parameters for capabilities of solar system, battery system, and PMAD system.'
            self.T1_R1_C1 = ttk.Label(self.tabInputs, text=t, wraplength = 300)
            self.T1_R1_C1.grid(row = 1, column = 1, padx = 5, pady = 5,sticky='w')
            
            # Assumptions
            t = 'Assumed values include constants, such as solar flux, '\
                'as well as design sizing parameters for the spacecraft '\
                'if non-custom is chosen.'
            self.T2_R0_C0 = ttk.Label(self.tabAssums, text=t, wraplength = 350)
            self.T2_R0_C0.grid(row = 0, column = 0, padx = 5, pady = 5,sticky='w')

            # Calculations
            t = 'Calculated values include sizing of solar panel and batteries, '\
                'based on calculated total power values, with appropriate '\
                'degradating and orbit considerations in place.'
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
        self.tabGroundStation = ttk.Frame(self.commswindow)
        self.tabSpacecraft = ttk.Frame(self.commswindow)
        self.tabDataGen = ttk.Frame(self.commswindow)
        self.tabOther = ttk.Frame(self.commswindow)
        self.commswindow.add(self.tabGroundStation, text = 'Ground Station')
        self.commswindow.add(self.tabSpacecraft, text = 'Spacecraft')
        self.commswindow.add(self.tabDataGen, text = 'Data Generation')
        self.commswindow.add(self.tabOther, text = 'Other')
        self.commswindow.pack(expand = 1, fill ="both")


        # Ground Station Tab Entry Values
        w = 6
        self.ctransPowerxG = ttk.Entry(self.tabGroundStation,width = w)
        self.cantGainxG = ttk.Entry(self.tabGroundStation, width = w)
        ##self.cdishDiameterG = ttk.Entry(self.tabGroundStation, width = w)
        self.ctransPoweruG = ttk.Entry(self.tabGroundStation,width = w)
        self.cantGainuG = ttk.Entry(self.tabGroundStation, width = w)
        """self.clineLossG = ttk.Entry(self.tabGroundStation, width = w)
        self.cmaxSlantRange = ttk.Entry(self.tabGroundStation, width = w)
        self.cEIRP = ttk.Entry(self.tabGroundStation, width = w)
        self.cminElevationAngle = ttk.Entry(self.tabGroundStation, width = w)
        self.cminElevationAngle.insert(0, 1)
        """

        # Spacecraft Tab Entry Values
        w = 6
        self.ctransPowerxS = ttk.Entry(self.tabSpacecraft, width = w)
        self.cantGainxS = ttk.Entry(self.tabSpacecraft, width = w)
        self.ctransPoweruS = ttk.Entry(self.tabSpacecraft, width = w)
        self.cantGainuS = ttk.Entry(self.tabSpacecraft, width = w)
        """self.cdishDiameterS = ttk.Entry(self.tabSpacecraft, width = w)
        self.clineLossS = ttk.Entry(self.tabSpacecraft, width = w)
        self.clineLossS.insert(0, 1)"""

        # Data Generation Entry Values
        w = 6
        self.catomClock = ttk.Entry(self.tabDataGen, width = w)
        self.catomClock.insert(0, '1')
        self.cradiation = ttk.Entry(self.tabDataGen, width = w)
        self.cradiation.insert(0, '1.5')
        self.chousekeeping = ttk.Entry(self.tabDataGen, width = w)
        self.chousekeeping.insert(0, '54')

        # Other Entry Values
        w = 6
        self.cxdown = ttk.Entry(self.tabOther, width = w)
        self.cudown = ttk.Entry(self.tabOther, width = w)
        self.cxup = ttk.Entry(self.tabOther, width = w)
        self.cuup = ttk.Entry(self.tabOther, width = w)
        self.cxFreq = ttk.Entry(self.tabOther, width = w)
        self.cuFreq = ttk.Entry(self.tabOther, width = w)
        """self.ccenFreq = ttk.Entry(self.tabOther, width = w)
        self.cpointingLoss = ttk.Entry(self.tabOther, width = w)
        self.celectronLoss = ttk.Entry(self.tabOther, width = w)
        self.cpolarLoss = ttk.Entry(self.tabOther, width = w)
        self.cfixedData = ttk.Entry(self.tabOther, width = w)"""
        self.cebnox = ttk.Entry(self.tabOther, width = w)
        self.cebnou = ttk.Entry(self.tabOther, width = w)
        self.csysTemp = ttk.Entry(self.tabOther, width = w)
        self.csysTemp.insert(0, "300")
        self.cmaxDistanceEarth = ttk.Entry(self.tabOther, width = w)
        self.cmaxDistanceEarth.insert(0, "2704")
        self.crainLoss = ttk.Entry(self.tabOther, width = w)
        self.crainLoss.insert(0, "3")
        self.clineLoss = ttk.Entry(self.tabOther, width = w)
        self.clineLoss.insert(0, "3")


        ### Ground Station Tab ###
        # Header - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Input appropriate parameter values for Ground Station comms:'
        self.choose = ttk.Label(self.tabGroundStation,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Transmitter Power Primary
        R = 3; C = 0
        ttk.Label(self.tabGroundStation, text='Primary Transmitter Power[W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ctransPowerxG.grid(row=R, column=C+1, padx=5, pady=5)

        # Antenna Gain Primary 
        R = 4; C = 0
        ttk.Label(self.tabGroundStation, text='Primary Antenna Gain[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cantGainxG.grid(row=R, column=C+1, padx=5, pady=5)

        # Dish Diameter
        """R = 5; C = 0
        ttk.Label(self.tabGroundStation, text='Dish Diameter [m]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cdishDiameterG.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')"""

        # Transmitter Power Secondary
        R = 6; C = 0
        ttk.Label(self.tabGroundStation, text='Secondary Transmitter Power[W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ctransPoweruG.grid(row=R, column=C+1, padx=5, pady=5)

        # Antenna Gain Secondary
        R = 7; C = 0
        ttk.Label(self.tabGroundStation, text='Secondary Antenna Gain[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cantGainuG.grid(row=R, column=C+1, padx=5, pady=5)

        # Line Loss
        """R = 3; C = 2
        ttk.Label(self.tabGroundStation, text='Line Loss [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.clineLossG.grid(row=R, column=C+1, padx=5, pady=5)

        # Maximum Slant Range
        R = 4; C = 2
        ttk.Label(self.tabGroundStation, text='Max Slant Range [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cmaxSlantRange.grid(row=R, column=C+1, padx=5, pady=5)

        # EIRP
        R = 5; C = 2
        ttk.Label(self.tabGroundStation, text='EIRP [dBm]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cEIRP.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Minimum Elevation Angle
        R = 6; C = 2
        ttk.Label(self.tabGroundStation, text='Minimum Elevation Angle [rad]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cminElevationAngle.grid(row=R, column=C+1, padx=5, pady=5,stick='w')
        """
        

        ## Spacecraft Tab ##
        
        # Heading - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Input appropriate parameter values for Spacecraft comms:'
        self.choose = ttk.Label(self.tabSpacecraft,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Transmitter Power Primary
        R = 3; C = 0
        ttk.Label(self.tabSpacecraft, text='Primary Transmitter Power[W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ctransPowerxS.grid(row=R, column=C+1, padx=5, pady=5)

        # Antenna Gain Primary
        R = 4; C = 0
        ttk.Label(self.tabSpacecraft, text='Primary Antenna Gain[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cantGainxS.grid(row=R, column=C+1, padx=5, pady=5)

        # Transmitter Power Secondary
        R = 5; C = 0
        ttk.Label(self.tabSpacecraft, text='Secondary Transmitter Power[W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ctransPoweruS.grid(row=R, column=C+1, padx=5, pady=5)

        # Antenna Gain Secondary
        R = 6; C = 0
        ttk.Label(self.tabSpacecraft, text='Secondary Antenna Gain[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cantGainuS.grid(row=R, column=C+1, padx=5, pady=5)

        # Dish Diameter
        """R = 3; C = 2
        ttk.Label(self.tabSpacecraft, text='Dish Diameter [m]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cdishDiameterS.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

        # Line Loss
        R = 4; C = 2
        ttk.Label(self.tabSpacecraft, text='Line Loss [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.clineLossS.grid(row=R, column=C+1, padx=5, pady=5)"""



        ## Data Generation Tab ##
        
        # Heading -NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Input appropriate parameter values for Data Generation:'
        self.choose = ttk.Label(self.tabDataGen,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Atomic Clock
        R = 3; C = 0
        ttk.Label(self.tabDataGen, text='Atomic Clock [Mbyte/day]       ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.catomClock.grid(row=R, column=C+1, padx=5, pady=5)

        # Radiation
        R = 4; C = 0
        ttk.Label(self.tabDataGen, text='Radiation [Mbyte/day]        ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cradiation.grid(row=R, column=C+1, padx=5, pady=5)

        # House Keeping
        R = 5; C = 0
        ttk.Label(self.tabDataGen, text='House Keeping [Mbyte/day]        ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.chousekeeping.grid(row=R, column=C+1, padx=5, pady=5)

        # Spacer 
        R = 6; C = 0
        ttk.Label(self.tabDataGen, text=' ').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        

        # Back Button
        """R = 14; C = 2
        self.UseCase = 1
        self.back_btn = ttk.Button(self.tabDataGen, text = "Back", command = self.tabSpacecraft)
        self.back_btn.grid(column = C, row = R)
        
        # Next Button
        self.next_btn = ttk.Button(self.tabDataGen, text = "Next", command = self.tabOther)
        self.next_btn.grid(column = C+1, row = R,sticky='w')"""


        ## Other Tab ##

        # Header - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Input appropriate parameter values:'
        self.choose = ttk.Label(self.tabOther,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        #Downlink Rate Primary
        R = 3; C = 0
        ttk.Label(self.tabOther, text='Primary Downlink Datarate[bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cxdown.grid(row=R, column=C+1, padx=5, pady=5)

        #Downlink Rate Secondary
        R = 4; C = 0
        ttk.Label(self.tabOther, text='Secondary Downlink Datarate[bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cudown.grid(row=R, column=C+1, padx=5, pady=5)

        #Uplink Rate Primary
        R = 5; C = 0
        ttk.Label(self.tabOther, text='Primary Uplink Datarate[bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cxup.grid(row=R, column=C+1, padx=5, pady=5)

        #Uplink Rate Secondary
        R = 6; C = 0
        ttk.Label(self.tabOther, text='Secondary Uplink Datarate[bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cuup.grid(row=R, column=C+1, padx=5, pady=5)

        #Frequency Primary
        R = 7; C = 0
        ttk.Label(self.tabOther, text='Primary Uplink/Downlink Frequency[Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cxFreq.grid(row=R, column=C+1, padx=5, pady=5)

        #Frequency Secondary
        R = 8; C = 0
        ttk.Label(self.tabOther, text='Secondary Uplink/Downlink Frequency[Hz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cuFreq.grid(row=R, column=C+1, padx=5, pady=5)

        # Central Frequency
        """R = 3; C = 2
        ttk.Label(self.tabOther, text='Central Frequency [GHz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ccenFreq.grid(row=R, column=C+1, padx=5, pady=5)

        # Pointing Losses
        R = 4; C = 2
        ttk.Label(self.tabOther, text='Pointing Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cpointingLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # Election Losses
        R = 6; C = 2
        ttk.Label(self.tabOther, text='Electron Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.celectronLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # Polarization Losses
        R = 7; C = 2
        ttk.Label(self.tabOther, text='Polarization Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cpolarLoss.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

        # Fixed Data Rate
        R = 9; C = 2
        ttk.Label(self.tabOther, text='Fixed Data Rate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cfixedData.grid(row=R, column=C+1, padx=5, pady=5,stick='w') """

        # System Noise Temp
        R = 3; C = 2
        ttk.Label(self.tabOther, text='System Temp [K]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.csysTemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Maximum Distance From Earth
        R = 4; C = 2
        ttk.Label(self.tabOther, text='Max Distance from Earth [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cmaxDistanceEarth.grid(row=R, column=C+1, padx=5, pady=5)

        # Rain Losses
        R = 5; C = 2
        ttk.Label(self.tabOther, text='Rain Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.crainLoss.grid(row=R, column=C+1, padx=5, pady=5)
        
        #EBNO Primary
        R = 6; C=2
        ttk.Label(self.tabOther, text='Primary Eb/N0[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cebnox.grid(row=R, column=C+1, padx=5, pady=5,stick='w')
        
        #EBNO Secondary
        R = 7; C=2
        ttk.Label(self.tabOther, text='Secondary Eb/N0[dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cebnou.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Line Losses
        R = 8; C = 2
        ttk.Label(self.tabOther, text='Line Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.clineLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # Submit Button
        R = 14; C = 2
        self.UseCase = 1
        self.sub_btn = ttk.Button(self.tabOther, text = "Submit", command = self.inputComms)
        self.sub_btn.grid(column = C, row = R)
        # Done Button
        self.fin_btn = ttk.Button(self.tabOther, text = "Close", command = self.allDone)
        self.fin_btn.grid(column = C+1, row = R,stick='w')
        # Run
        self.commsgui.mainloop()
   

    def inputComms(self):
        if self.UseCase == 1:
            try:
                self.transPowerxG= float(self.ctransPowerxG.get())
            except:
                pass
            try:
                self.antGainxG= float(self.cantGainxG.get())
            except:
                pass       
            """try:
                self.dishDiameterG= float(self.cdishDiameterG.get())
            except:
                pass"""
            try:
                self.transPoweruG= float(self.ctransPoweruG.get())
            except:
                pass
            try:
                self.antGainuG= float(self.cantGainuG.get())
            except:
                pass         
            try:
                self.lineLossG = float(self.clineLossG.get())
            except:
                pass
            """try:
                self.maxSlantRange = float(self.cmaxSlantRange.get())
            except:
                pass
            try:
                self.dishDiameterS = float(self.cdishDiameterS.get())
            except:
                pass
            try:
                self.EIRP = float(self.cEIRP.get())
            except:
                pass
            try:
                self.minElevationAngle = int(self.cminElevationAngle.get())
            except:
                pass"""
            try:
                self.transPowerxS= float(self.ctransPowerxS.get())
            except:
                pass
            try:
                self.antGainxS = float(self.cantGainxS.get())
            except:
                pass
            try:
                self.transPoweruS= float(self.ctransPoweruS.get())
            except:
                pass
            try:
                self.antGainuS = float(self.cantGainuS.get())
            except:
                pass
            """try:
                self.lineLossS = float(self.clineLossS.get())
            except:
                pass"""
            try:
                self.atomClock = float(self.catomClock.get())
            except:
                pass
            try:
                self.radiation = float(self.cradiation.get())
            except:
                pass
            try:
                self.housekeeping = float(self.chousekeeping.get())
            except:
                pass   
            try:
                self.xdown = float(self.cxdown.get())
            except:
                pass
            try:
                self.udown = float(self.cudown.get())
            except:
                pass
            try:
                self.xup = float(self.cxup.get())
            except:
                pass
            try:
                self.uup = float(self.cuup.get())
            except:
                pass
            try:
                self.xfreq = float(self.cxFreq.get())
            except:
                pass
            try:
                self.ufreq = float(self.cuFreq.get())
            except:
                pass
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
                self.sysTemp = float(self.csysTemp.get())
            except:
                pass
            try:
                self.maxDistanceEarth = float(self.cmaxDistanceEarth.get())
            except:
                pass
            try:
                self.rainLoss = float(self.crainLoss.get())
            except:
                pass
            try:
                self.ebnox = int(self.cebnox.get())
            except:
                pass            
            try:
                self.ebnou = int(self.cebnou.get())
            except:
                pass
            try:
                self.lineLoss = float(self.clineLoss.get())
            except:
                pass
    
    def selectionError(self):
            self.commsgui = tk.Tk() # Instance of Tk,
            self.commsgui.title("EPS Design Module") # Name
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
            self.commsgui.title("EPS Design Module") # Name
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