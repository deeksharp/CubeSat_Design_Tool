import math as m
#import numpy as np
import tkinter as tk
from tkinter import ttk


class Orbits:
    def __init__(self):
        # Worst Case Ecliptic True Solar Longitude:
        self.Ls = 0 # deg
        # Worst Case Right Ascension of Ascending Node:

        # Earth Standard gravitational parameter (km^3/s^2)
        self.GM = 398600 

        # Earth Radius
        self.R_earth = 6378

        # Initialize
        self.alt = 0
        self.inc = 0
        self.orbital_period = 0
        self.orbital_period = 0
        self.max_eclipse_time = 0
        self.min_sun_time = 0

    def orbitCalc(self):
        print(self.selection.get())
        if self.selection.get() == 1:
            self.orbit = 'ISS'
            self.inc = 51.6 # degrees
            self.alt = 420 # km
            print
        elif self.selection.get() == 2:
            self.orbit = 'SSO - 12AM/12PM'
            self.inc = 97.7 # degrees
            self.alt = 600 # km
        elif self.selection.get() == 3:
            self.orbit = 'LEO - Low Inclination'
            self.inc = 97.7 # degrees
            self.alt = 400 # km
        elif self.selection.get() == 4:
            self.orbit = 'Custom Orbit'
            self.inc = float(self.E_inc.get())
            self.alt = float(self.E_alt.get())
        else:
            print('\nError with orbit calculations: No selection\n')
        
        # Semi-major Axis (km)
        self.a = self.R_earth + self.alt
        # Orbital Period (s)
        self.orbital_period = 2 * m.pi * m.sqrt(m.pow(self.a,3)/self.GM)
        # Angle Until Max Eclipse (rad)
        self.alpha = m.acos(self.R_earth/self.a)
        # Max Time in Eclipse
        self.max_eclipse_time = self.orbital_period * (m.pi - 2*self.alpha)/(2*m.pi)
        # Min Time in Sun
        self.min_sun_time = self.orbital_period * (m.pi + 2*self.alpha)/(2*m.pi)
        # Orbits per Day
        self.orbits_day = (24*3600)/self.orbital_period
        # Mission Lifetime
        self.mission_lifetime = float(self.E_mission_lifetime.get())
        # Lifetime Orbits
        self.num_orbits = ((self.mission_lifetime * 365.25*24*3600)/self.orbital_period) 


    def allDone(self):
        self.orbitgui.destroy()

    def selectOrbit(self):
        self.orbitgui = tk.Tk() # Instance of Tk,
        self.orbitgui.title("Orbit Selection Module") # Name
        self.orbitwindow = ttk.Notebook(self.orbitgui) # tkk module implements "tabs" (Notebook)
        self.orbits = ttk.Frame(self.orbitgui)
        self.orbitwindow.add(self.orbits, text = 'Orbits')
        self.orbitwindow.pack(expand = 1, fill ="both")

        t1 = 'Please select an orbit from the list provided, or input a custom orbit. '\
            'Note that a custom orbit may not be a sun-synchronous orbit at this time and all orbits are assumed circular.'
        Instructions = ttk.Label(self.orbits,text =t1,wraplength = 300)
        Instructions.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 10)

        # Mission Lifetime
        self.E_mission_lifetime = ttk.Entry(self.orbits,width=6)
        ttk.Label(self.orbits,text='Mission Lifetime [yrs]').grid(column = 0, row = 1, padx = 10, pady = 5,sticky='w')
        self.E_mission_lifetime.grid(row = 1, column =1, padx = 10, pady =5, sticky='w')

        # Orbit Selection
        self.selection=tk.IntVar(self.orbitgui)
        Orb_RB1=ttk.Radiobutton(self.orbits, text='ISS Orbit', variable=self.selection,value=1)
        Orb_RB1.grid(column = 0, row = 2, padx = 10, pady = 5)
        Orb_RB2=ttk.Radiobutton(self.orbits, text='SSO - 12AM/12PM', variable=self.selection,value=2)
        Orb_RB2.grid(column = 0, row = 3, padx = 10, pady = 5)
        Orb_RB3=ttk.Radiobutton(self.orbits, text='LEO - Low Inclination', variable=self.selection,value=3)
        Orb_RB3.grid(column = 0, row = 4, padx = 10, pady = 5)
        Orb_RB4=ttk.Radiobutton(self.orbits, text='Custom Orbit', variable=self.selection,value=4)
        Orb_RB4.grid(column = 0, row = 5, padx = 10, pady = 5)
        desc_1 = ttk.Label(self.orbits, text='Inclination: 51.6 degrees\nAltitude: 420 km')
        desc_2 = ttk.Label(self.orbits, text='Inclination: 97.8 degrees\nAltitude: 600 km')
        desc_3 = ttk.Label(self.orbits, text='Inclination: 28.5 degrees\nAltitude: 500 km')
        desc_4 = ttk.Label(self.orbits, text='Input Below')
        desc_1.grid(column = 1, row = 2, columnspan = 2,padx = 10, pady = 5,sticky='w')
        desc_2.grid(column = 1, row = 3, columnspan = 2,padx = 10, pady = 5,sticky='w')
        desc_3.grid(column = 1, row = 4, columnspan = 2,padx = 10, pady = 5,sticky='w')
        desc_4.grid(column = 1, row = 5,columnspan = 2, padx = 10, pady = 5,sticky='w')

        # Custom Orbit Entry
        self.E_inc = ttk.Entry(self.orbits,width=6)
        self.E_alt = ttk.Entry(self.orbits,width=6)
        custom_header = ttk.Label(self.orbits,text ='Custom Oribt:')
        custom_header.grid(column = 0, row = 6, padx = 10, pady = 10,sticky='w')
        ttk.Label(self.orbits,text ='Inclination [deg]').grid(row = 7, column = 0, padx = 10, pady = 5,sticky='w')
        ttk.Label(self.orbits,text = 'Orbit Altitude [km]').grid(row = 8, column = 0, padx = 10, pady = 5,sticky='w')
        self.E_inc.grid(row = 7, column = 1, padx = 10, pady = 5)
        self.E_alt.grid(row = 8, column = 1, padx = 10, pady = 5)

        # Buttons
        submit_Orbit = ttk.Button(self.orbits, text = 'Submit', command = self.orbitCalc)
        submit_Orbit.grid(column = 0, row = 9, padx = 10, pady = 5)
        finish = ttk.Button(self.orbits, text = 'Close', command = self.allDone)
        finish.grid(column = 1, row = 9, padx = 10, pady = 5)

        self.orbitgui.mainloop()
