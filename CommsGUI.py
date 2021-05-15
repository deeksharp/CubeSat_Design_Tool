import tkinter as tk
from tkinter import ttk
        

class Comms:
    def __init__(self):
        # Initialize Comms Data
        self.UseCase: int

        # Ground Station Tab
        self.transPowerG = ''
        self.lineLossG = ''
        self.antGainG = ''
        self.maxSlantRange = ''
        self.dishDiameter = ''
        self.EIRP = ''
        self.minElevationAngle = ''
        self.ebno = ''

        # Spacecraft
        self.transPowerS = ''
        self.lineLossS = ''
        self.antGainS = ''
        self.maxDistanceEarth = ''

        # Data Generation
        self.atomClock = ''
        self.radiation = ''
        self.housekeeping = ''

        # Other 
        self.cenFreq = ''
        self.pointingLoss = ''
        self.rainLoss = ''
        self.electronLoss = ''
        self.polarLoss = ''
        self.sysNoiseTemp = ''
        self.fixedData = ''

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
        self.commsgui.title("Electrical Power Subsystem Design Module") # Name
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
        self.ctransPowerG = ttk.Entry(self.tabGroundStation, width = w)
        self.clineLossG = ttk.Entry(self.tabGroundStation, width = w)
        self.cantGainG = ttk.Entry(self.tabGroundStation, width = w)
        self.cmaxSlantRange = ttk.Entry(self.tabGroundStation, width = w)
        self.cdishDiameter = ttk.Entry(self.tabGroundStation, width = w)
        self.cEIRP = ttk.Entry(self.tabGroundStation, width = w)
        self.cminElevationAngle = ttk.Entry(self.tabGroundStation, width = w)
        self.cebno = ttk.Entry(self.tabGroundStation, width = w)

        # Spacecraft Tab Entry Values
        w = 6
        self.ctransPowerS = ttk.Entry(self.tabSpacecraft, width = w)
        self.clineLossS = ttk.Entry(self.tabSpacecraft, width = w)
        self.cantGainS = ttk.Entry(self.tabSpacecraft, width = w)
        self.cmaxDistanceEarth = ttk.Entry(self.tabSpacecraft, width = w)

        # Data Generation Entry Values
        w = 6
        self.catomClock = ttk.Entry(self.tabDataGen, width = w)
        self.cradiation = ttk.Entry(self.tabDataGen, width = w)
        self.chousekeeping = ttk.Entry(self.tabDataGen, width = w)
        
        # Other Entry Values
        w = 6
        self.ccenFreq = ttk.Entry(self.tabOther, width = w)
        self.cpointingLoss = ttk.Entry(self.tabOther, width = w)
        self.crainLoss = ttk.Entry(self.tabOther, width = w)
        self.celectronLoss = ttk.Entry(self.tabOther, width = w)
        self.cpolarLoss = ttk.Entry(self.tabOther, width = w)
        self.csysNoiseTemp = ttk.Entry(self.tabOther, width = w)
        self.cfixedData = ttk.Entry(self.tabOther, width = w)
        
        ### Ground Station Tab ###
        # Header - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Choose whether you want customized EPS design parameters or choose a set of assumed parameters:'
        self.choose = ttk.Label(self.tabGroundStation,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Transmitter Power
        R = 3; C = 0
        ttk.Label(self.tabGroundStation, text='Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ctransPowerG.grid(row=R, column=C+1, padx=5, pady=5)

        # Line Loss
        R = 4; C = 0
        ttk.Label(self.tabGroundStation, text='Line Loss [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.clineLossG.grid(row=R, column=C+1, padx=5, pady=5)

        # Antenna Gain
        R = 5; C = 0
        ttk.Label(self.tabGroundStation, text='Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cantGainG.grid(row=R, column=C+1, padx=5, pady=5)

        # Maximum Slant Range
        R = 6; C = 0
        ttk.Label(self.tabGroundStation, text='Max Slant Range [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cmaxSlantRange.grid(row=R, column=C+1, padx=5, pady=5)

        # Dish Diameter
        R = 7; C = 0
        ttk.Label(self.tabGroundStation, text='Dish Diameter [m]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cdishDiameter.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

        # EIRP
        R = 3; C = 2
        ttk.Label(self.tabGroundStation, text='EIRP [dBm]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cEIRP.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Minimum Elveation Angle
        R = 4; C = 2
        ttk.Label(self.tabGroundStation, text='Minimum Elevation Angle [rad]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cminElevationAngle.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Last value.  weird lookin thing
        R = 5; C=2
        ttk.Label(self.tabGroundStation, text='Eb/N0 (SNR) [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cebno.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        ## Spacecraft Tab ##
        
        # Heading - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Choose whether you want customized EPS design parameters or choose a set of assumed parameters:'
        self.choose = ttk.Label(self.tabSpacecraft,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Transmitter Power
        R = 3; C = 0
        ttk.Label(self.tabSpacecraft, text='Transmitter Power [W]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ctransPowerS.grid(row=R, column=C+1, padx=5, pady=5)

        # Line Loss
        R = 4; C = 0
        ttk.Label(self.tabSpacecraft, text='Line Loss [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.clineLossS.grid(row=R, column=C+1, padx=5, pady=5)

        # Antenna Gain
        R = 5; C = 0
        ttk.Label(self.tabSpacecraft, text='Antenna Gain [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cantGainS.grid(row=R, column=C+1, padx=5, pady=5)

        # Maximum Distance From Earth
        R = 6; C = 0
        ttk.Label(self.tabSpacecraft, text='Max Distance from Earth [km]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cmaxDistanceEarth.grid(row=R, column=C+1, padx=5, pady=5)


        ## Data Generation Tab ##
        
        # Heading -NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Choose whether you want customized EPS design parameters or choose a set of assumed parameters:'
        self.choose = ttk.Label(self.tabDataGen,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Atomic Clock
        R = 3; C = 0
        ttk.Label(self.tabDataGen, text='Atomic Clock [Mbyte/day]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.catomClock.grid(row=R, column=C+1, padx=5, pady=5)

        # Radiation
        R = 4; C = 0
        ttk.Label(self.tabDataGen, text='Radiation [Mbyte/day]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cradiation.grid(row=R, column=C+1, padx=5, pady=5)

        # House Keeping
        R = 5; C = 0
        ttk.Label(self.tabDataGen, text='House Keeping [Mbyte/day]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.chousekeeping.grid(row=R, column=C+1, padx=5, pady=5)
        

        ## Other Tab ##

        # Header - NOT FINISHED
        R = 0; C = 0
        t_ins_design = 'Choose whether you want customized EPS design parameters or choose a set of assumed parameters:'
        self.choose = ttk.Label(self.tabOther,text = t_ins_design, wraplength = 250)
        self.choose.grid(row = R, column = C, columnspan = 2,rowspan=2, padx = 5, pady = 5)

        # Central Frequency
        R = 3; C = 0
        ttk.Label(self.tabOther, text='Central Frequency [GHz]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.ccenFreq.grid(row=R, column=C+1, padx=5, pady=5)

        # Pointing Losses
        R = 4; C = 0
        ttk.Label(self.tabOther, text='Pointing Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cpointingLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # Rain Losses
        R = 5; C = 0
        ttk.Label(self.tabOther, text='Rain Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.crainLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # Election Losses
        R = 6; C = 0
        ttk.Label(self.tabOther, text='Electron Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.celectronLoss.grid(row=R, column=C+1, padx=5, pady=5)

        # Polarization Losses
        R = 7; C = 0
        ttk.Label(self.tabOther, text='Polarization Losses [dB]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cpolarLoss.grid(row=R, column=C+1, padx=5, pady=5,sticky='w')

        # System Noise Temp
        R = 3; C = 2
        ttk.Label(self.tabOther, text='System Noise Temp [K]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.csysNoiseTemp.grid(row=R, column=C+1, padx=5, pady=5,stick='w')

        # Fixed Data Rate
        R = 4; C = 2
        ttk.Label(self.tabOther, text='Fixed Data Rate [bps]').grid(row=R, column=C, padx=25, pady=5,sticky='w')
        self.cfixedData.grid(row=R, column=C+1, padx=5, pady=5,stick='w')


        # Submit Button
        R = 14; C = 2
        self.UseCase = 1
        self.sub_btn = ttk.Button(self.tabOther, text = "Submit", command = self.inputPower)
        self.sub_btn.grid(column = C, row = R)
        # Done Button
        self.fin_btn = ttk.Button(self.tabOther, text = "Close", command = self.allDone)
        self.fin_btn.grid(column = C+1, row = R,stick='w')
        # Run
        self.commsgui.mainloop()

    def inputPower(self):
        if self.UseCase == 1:
                try:
                    self.transPowerG= float(self.ctransPowerG.get())
                except:
                    pass
                try:
                    self.lineLossG = float(self.clineLossG.get())
                except:
                    pass
                try:
                    self.antGainG = float(self.cantGainG.get())
                except:
                    pass
                try:
                    self.maxSlantRange = float(self.cmaxSlantRange.get())
                except:
                    pass
                try:
                    self.dishDiameter = float(self.cdishDiameter.get())
                except:
                    pass
                try:
                    self.EIRP = float(self.cEIRP.get())
                except:
                    pass
                try:
                    self.minElevationAngle = int(self.cminElevationAngle.get())
                except:
                    pass
                try:
                    self.ebno = int(self.cebno.get())
                except:
                    pass
                try:
                    self.transPowerS= float(self.ctransPowerS.get())
                except:
                    pass
                try:
                    self.lineLossS = float(self.clineLossS.get())
                except:
                    pass
                try:
                    self.antGainS = float(self.cantGainS.get())
                except:
                    pass
                try:
                    self.maxDistanceEarth = float(self.cmaxDistanceEarth.get())
                except:
                    pass
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
                    self.cenFreq= float(self.ccenFreq.get())
                except:
                    pass
                try:
                    self.pointingLoss = float(self.cpointingLoss.get())
                except:
                    pass
                try:
                    self.rainLoss = float(self.crainLoss.get())
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
                    self.sysNoiseTemp = float(self.csysNoiseTemp.get())
                except:
                    pass
                try:
                    self.fixedData = int(self.cfixedData.get())
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