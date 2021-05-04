import csv
import math as m

class PowerTool:
    def __init__(self):
        pass

    def case1_PowerBudget2PowerDesign(self,p,oD,payD,cD,tD,aD,gD,cdhD,sD):
        # Read in Assumptions from File
        if p.design_option == 'Custom':
            # Read in Design Option 
            with open('powerAssumptions.csv', mode='r') as file:
                reader = csv.reader(file) 
                self.var = ['']
                self.var_name = ['']
                self.data = [0]
                self.units = ['']
                for row in reader:
                    v = row[0]
                    n = row[1]
                    d = row[2]
                    u = row[5]
                    self.var.append(v)
                    self.var_name.append(n)
                    self.data.append(d)
                    self.units.append(u)
            # Assign Assumptions
            p.solar_flux = float(self.data[71])
            if p.SP_eff_bol == '':
                p.SP_eff_bol = float(self.data[57])
            if p.SP_degrad_rate == '':
                p.SP_degrad_rate = float(self.data[58])
            if p.SP_degrad_temp == '':
                p.SP_degrad_temp = float(self.data[59])
            if p.SP_temp == '':
                p.SP_temp = float(self.data[60])
            if p.SP_tracking == '':
                p.SP_tracking = float(self.data[61])
            if p.SP_deployable == '':
                p.SP_deployable = float(self.data[62])
            if p.SP_packing == '':
                p.SP_packing = float(self.data[63])
            if p.bat_eff == '':
                p.bat_eff = float(self.data[64])
            if p.cell_mass == '':
                p.cell_mass = float(self.data[65])
            if p.cell_cap == '':
                p.cell_cap = float(self.data[66])
            if p.bat_dod == '':
                p.bat_dod = float(self.data[67])
            if p.PDU_eff == '':
                p.PDU_eff = float(self.data[68])
            if p.PDU_mass == '':
                p.PDU_mass = float(self.data[69])
            if p.PDU_data == '':
                p.PDU_data = float(self.data[70])
            if p.per_margin =='':
                p.per_margin = float(self.data[8])
        elif p.design_option == 'Standard':
            # Read in Design Option 
            with open('powerAssumptions.csv', mode='r') as file:
                reader = csv.reader(file)
                self.var = ['']
                self.var_name = ['']
                self.data = [0]
                self.units = ['']
                for row in reader:
                    v = row[0]
                    n = row[1]
                    d = row[3]
                    u = row[5]
                    self.var.append(v)
                    self.var_name.append(n)
                    self.data.append(d)
                    self.units.append(u)
            # Assign Assumptions
            p.SP_eff_bol = self.data[57]
            p.SP_degrad_rate = self.data[58]
            p.SP_degrad_temp = self.data[59]
            p.SP_temp = self.data[60]
            p.SP_tracking = self.data[61]
            p.SP_deployable = self.data[62]
            p.bat_eff = self.data[63]
            p.cell_mass = self.data[64]
            p.cell_cap = self.data[66]
            p.bat_dod = self.data[67]
            p.PDU_eff = self.data[68]
            p.PDU_mass = self.data[69]
            p.PDU_data = self.data[70] 
            if p.per_margin == '':
                p.per_margin = self.data[8]
        elif p.design_option == 'Advanced':
            # Read in Design Option 
            with open('powerAssumptions.csv', mode='r') as file:
                reader = csv.reader(file)
                self.var = ['']
                self.var_name = ['']
                self.data = [0]
                self.units = ['']
                for row in reader:
                    v = row[0]
                    n = row[1]
                    d = row[4]
                    u = row[5]
                    self.var.append(v)
                    self.var_name.append(n)
                    self.data.append(d)
                    self.units.append(u)
            # Assign Assumptions
            p.SP_eff_bol = self.data[57]
            p.SP_degrad_rate = self.data[58]
            p.SP_degrad_temp = self.data[59]
            p.SP_temp = self.data[60]
            p.SP_tracking = self.data[61]
            p.SP_deployable = self.data[62]
            p.bat_eff = self.data[63]
            p.cell_mass = self.data[64]
            p.cell_cap = self.data[66]
            p.bat_dod = self.data[67]
            p.PDU_eff = self.data[68]
            p.PDU_mass = self.data[69]
            p.PDU_data = self.data[70] 
            if p.per_margin == '':
                p.per_margin = self.data[8]
        else: 
            print('Error, no design option selected')

        

        # Eclipse Mode Seletion (if any)
        if p.eclipse_mode == 0:
            pass
        elif p.eclipse_mode == 1:
            p.mode1_duty = oD.max_eclipse_time/oD.orbital_period
        elif p.eclipse_mode == 2:
            p.mode2_duty = oD.max_eclipse_time/oD.orbital_period
        elif p.eclipse_mode == 3:
            p.mode3_duty = oD.max_eclipse_time/oD.orbital_period
        elif p.eclipse_mode == 4:
            p.mode4_duty = oD.max_eclipse_time/oD.orbital_period

        # Standby Mode Seletion (if any)
        if p.standby_mode == 0:
            pass
        elif p.standby_mode == 1:
            p.mode1_duty = 100 - p.mode2_duty - p.mode3_duty - p.mode4_duty
        elif p.standby_mode == 2:
            p.mode2_duty = 100 - p.mode1_duty - p.mode3_duty - p.mode4_duty
        elif p.standby_mode == 3:
            p.mode3_duty = 100 - p.mode1_duty - p.mode2_duty - p.mode4_duty
        elif p.standby_mode == 4:
            p.mode4_duty = 100 - p.mode1_duty - p.mode2_duty - p.mode3_duty
        
        # Power Budget Calcs
        p.ADCS_AVG = (p.ADCS_P1 * (p.mode1_duty/100)) + (p.ADCS_P2 * (p.mode2_duty/100)) + (p.ADCS_P3 * (p.mode3_duty/100)) + (p.ADCS_P4 * (p.mode4_duty/100))
        p.CDH_AVG = (p.CDH_P1 * (p.mode1_duty/100)) + (p.CDH_P2 * (p.mode2_duty/100)) + (p.CDH_P3 * (p.mode3_duty/100)) + (p.CDH_P4 * (p.mode4_duty/100))
        p.COMM_AVG = (p.COMM_P1 * (p.mode1_duty/100)) + (p.COMM_P2 * (p.mode2_duty/100)) + (p.COMM_P3 * (p.mode3_duty/100)) + (p.COMM_P4 * (p.mode4_duty/100))
        p.EPS_AVG = (p.EPS_P1 * (p.mode1_duty/100)) + (p.EPS_P2 * (p.mode2_duty/100)) + (p.EPS_P3 * (p.mode3_duty/100)) + (p.EPS_P4 * (p.mode4_duty/100))
        p.GNC_AVG = (p.GNC_P1 * (p.mode1_duty/100)) + (p.GNC_P2 * (p.mode2_duty/100)) + (p.GNC_P3 * (p.mode3_duty/100)) + (p.GNC_P4 * (p.mode4_duty/100))
        p.PAY_AVG = (p.PAY_P1 * (p.mode1_duty/100)) + (p.PAY_P2 * (p.mode2_duty/100)) + (p.PAY_P3 * (p.mode3_duty/100)) + (p.PAY_P4 * (p.mode4_duty/100))
        p.STRU_AVG = (p.STRU_P1 * (p.mode1_duty/100)) + (p.STRU_P2 * (p.mode2_duty/100)) + (p.STRU_P3 * (p.mode3_duty/100)) + (p.STRU_P4 * (p.mode4_duty/100))
        p.THER_AVG = (p.THER_P1 * (p.mode1_duty/100)) + (p.THER_P2 * (p.mode2_duty/100)) + (p.THER_P3 * (p.mode3_duty/100)) + (p.THER_P4 * (p.mode4_duty/100))
        p.P_AVG = p.ADCS_AVG + p.CDH_AVG + p.COMM_AVG + p.EPS_AVG + p.GNC_AVG + p.PAY_AVG + p.STRU_AVG + p.THER_AVG
        p.P_D1_raw = p.ADCS_P1 + p.CDH_P1 + p.COMM_P1 + p.EPS_P1 + p.GNC_P1 + p.PAY_P1 + p.STRU_P1 + p.THER_P1
        p.P_D2_raw = p.ADCS_P2 + p.CDH_P2 + p.COMM_P2 + p.EPS_P2 + p.GNC_P2 + p.PAY_P2 + p.STRU_P2 + p.THER_P2
        p.P_D3_raw = p.ADCS_P3 + p.CDH_P3 + p.COMM_P3 + p.EPS_P3 + p.GNC_P3 + p.PAY_P3 + p.STRU_P3 + p.THER_P3
        p.P_D4_raw = p.ADCS_P4 + p.CDH_P4 + p.COMM_P4 + p.EPS_P4 + p.GNC_P4 + p.PAY_P4 + p.STRU_P4 + p.THER_P4
        p.P_D1 = (p.P_D1_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_D2 = (p.P_D2_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_D3 = (p.P_D3_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_D4 = (p.P_D4_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_AVG_PDU_loss = p.P_AVG / (p.PDU_eff/100)
        p.P_margin = p.P_AVG_PDU_loss * (p.per_margin/100)
        p.P_AVG_margin = p.ADCS_AVG + p.P_margin

        # Orbit and Eclipse Energy (all in Wh):
        p.sun_energy_min = p.P_AVG_margin * (oD.min_sun_time/3600)
        p.orbit_energy = p.P_AVG_margin * (oD.orbital_period/3600)

        # Eclipse Energy
        if p.eclipse_mode == 0:
            p.eclipse_energy_max = p.P_AVG_margin * (oD.max_eclipse_time/3600)
            p.sun_energy_min = p.P_AVG_margin * (oD.min_sun_time/3600)
        elif p.eclipse_mode == 1:
            p.eclipse_energy_max = p.P_D1 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = ((p.P_AVG_margin - (p.P_D1*p.mode1_duty/100))/(1-p.mode1_duty/100))*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 2:
            p.eclipse_energy_max = p.P_D2 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D2*p.mode2_duty/100))/(1-p.mode2_duty/100)*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 3:
            p.eclipse_energy_max = p.P_D3 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D3*p.mode3_duty/100))/(1-p.mode3_duty/100)*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 4:
            p.eclipse_energy_max = p.P_D4 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D4*p.mode4_duty/100))/(1-p.mode4_duty/100)*(oD.min_sun_time/3600)

        # Worst Case Scenario (Max Eclipse):
        p.bat_roundtrip_eff = (p.bat_eff**2)/100
        p.SP_energy_orbit_worst = p.sun_energy_min + p.eclipse_energy_max/(p.bat_roundtrip_eff/100)
        p.SP_avg_power_worst = p.SP_energy_orbit_worst / (oD.min_sun_time/3600)

        # Battery Sizing
        p.bat_cycles = oD.num_orbits
        if p.bat_dod < 20:
            p.bat_degrad_rate = 5 #%/5000 cycles
        elif p.bat_dod < 40:
            p.bat_degrad_rate = 10 #%/5000 cycles
        elif p.bat_dod < 60:
            p.bat_degrad_rate = 15 #%/5000 cycles
        elif p.bat_dod < 80:
            p.bat_degrad_rate = 20 #%/5000 cycles
        else:
            p.bat_degrad_rate = 50 #%/5000 cycles

        p.bat_degrad = (1 - p.bat_degrad_rate/100)**(p.bat_cycles/5000)
        p.bat_discharge_energy = p.eclipse_energy_max / ((p.bat_eff/100) * p.bat_degrad)
        p.bat_cap = p.bat_discharge_energy/(p.bat_dod/100)
        p.num_cells =  m.ceil(p.bat_cap/p.cell_cap)
        p.bat_cap = p.num_cells*p.cell_cap
        p.bat_mass =  p.num_cells * p.cell_mass

        # Solar Area Sizing:
        p.L_degrad = (1 - (p.SP_degrad_rate/100))**oD.mission_lifetime
        p.T_degrad = (1 - (p.SP_degrad_temp/100))**p.SP_temp
        p.SP_eff_eol = p.SP_eff_bol * p.L_degrad * p.T_degrad 
        p.solar_eol = p.solar_flux * p.SP_eff_eol # W/m^2
        p.SP_area_effective = p.SP_avg_power_worst/ p.solar_eol 

        if p.SP_tracking == 1 and p.SP_deployable == 1: # Tumbling and no deployables
            p.SP_area = 3*p.SP_area_effective
        elif p.SP_tracking == 1 and p.SP_deployable == 2: # Tumbling and Deployables
            p.SP_area = 0
        elif p.SP_tracking == 2 and p.SP_deployable == 1: # Nadir Pointing and no deployables
            p.SP_area = 0
        elif p.SP_tracking == 2 and p.SP_deployable == 2: # Nadir Pointing and Deployables
            p.SP_area = 0
        elif p.SP_tracking == 3 and p.SP_deployable == 1: # Sun Pointing and no deployables
            p.SP_area = 2*(p.SP_area_effective/m.cos(m.pi/4))
        elif p.SP_tracking == 3 and p.SP_deployable == 2: # Sun Pointing and Deployables
            p.SP_area = p.SP_area_effective
        else:
            pass

        return p
                
    def case2_SubsystemDesign2PowerDesign(self,p,oD,payD,cD,tD,aD,gD,cdhD,sD):
        # Read in Assumptions from File
        if p.design_option == 'Custom':
            # Read in Design Option 
            with open('powerAssumptions.csv', mode='r') as file:
                reader = csv.reader(file) 
                self.var = ['']
                self.var_name = ['']
                self.data = [0]
                self.units = ['']
                for row in reader:
                    v = row[0]
                    n = row[1]
                    d = row[2]
                    u = row[3]
                    self.var.append(v)
                    self.var_name.append(n)
                    self.data.append(d)
                    self.units.append(u)
            # Assign Assumptions
            if p.SP_eff_bol == '':
                p.SP_eff_bol = self.data[57]
            if p.SP_degrad_rate == '':
                p.SP_degrad_rate = self.data[58]
            if p.SP_degrad_temp == '':
                p.SP_degrad_temp = self.data[59]
            if p.SP_temp == '':
                p.SP_temp = self.data[60]
            if p.SP_tracking == '':
                p.SP_tracking = self.data[61]
            if p.SP_deployable == '':
                p.SP_deployable = self.data[62]
            if p.SP_packing == '':
                p.SP_packing = self.data[63]
            if p.bat_eff == '':
                p.bat_eff = self.data[64]
            if p.cell_mass == '':
                p.cell_mass = self.data[65]
            if p.cell_cap == '':
                p.cell_cap = self.data[66]
            if p.bat_dod == '':
                p.bat_dod = self.data[67]
            if p.PDU_eff == '':
                p.PDU_eff = self.data[68]
            if p.PDU_mass == '':
                p.PDU_mass = self.data[69]
            if p.PDU_data == '':
                p.PDU_data = self.data[70] 
            if p.per_margin =='':
                p.per_margin = self.data[8]
        elif p.design_option == 'Standard':
            # Read in Design Option 
            with open('powerAssumptions.csv', mode='r') as file:
                reader = csv.reader(file)
                self.var = ['']
                self.var_name = ['']
                self.data = [0]
                self.units = ['']
                for row in reader:
                    v = row[4]
                    n = row[5]
                    d = row[6]
                    u = row[7]
                    self.var.append(v)
                    self.var_name.append(n)
                    self.data.append(d)
                    self.units.append(u)
            # Assign Assumptions
            p.SP_eff_bol = self.data[57]
            p.SP_degrad_rate = self.data[58]
            p.SP_degrad_temp = self.data[59]
            p.SP_temp = self.data[60]
            p.SP_tracking = self.data[61]
            p.SP_deployable = self.data[62]
            p.bat_eff = self.data[63]
            p.cell_mass = self.data[64]
            p.cell_cap = self.data[66]
            p.bat_dod = self.data[67]
            p.PDU_eff = self.data[68]
            p.PDU_mass = self.data[69]
            p.PDU_data = self.data[70] 
            if p.per_margin == '':
                p.per_margin = self.data[8]
        elif p.design_option == 'Advanced':
            # Read in Design Option 
            with open('powerAssumptions.csv', mode='r') as file:
                reader = csv.reader(file)
                self.var = ['']
                self.var_name = ['']
                self.data = [0]
                self.units = ['']
                for row in reader:
                    v = row[8]
                    n = row[9]
                    d = row[10]
                    u = row[11]
                    self.var.append(v)
                    self.var_name.append(n)
                    self.data.append(d)
                    self.units.append(u)
            # Assign Assumptions
            p.SP_eff_bol = self.data[57]
            p.SP_degrad_rate = self.data[58]
            p.SP_degrad_temp = self.data[59]
            p.SP_temp = self.data[60]
            p.SP_tracking = self.data[61]
            p.SP_deployable = self.data[62]
            p.bat_eff = self.data[63]
            p.cell_mass = self.data[64]
            p.cell_cap = self.data[66]
            p.bat_dod = self.data[67]
            p.PDU_eff = self.data[68]
            p.PDU_mass = self.data[69]
            p.PDU_data = self.data[70] 
            if p.per_margin == '':
                p.per_margin = self.data[8]
        else: 
            print('Error, no design option selected')
        
        self.mode1_duty = oD.D_standby
        self.mode2_duty = aD.D_desat
        self.mode3_duty = cD.D_comms
        self.mode4_duty = payD.D_active

        self,p,oD,payD,cD,tD,aD,gD,cdhD,sD
        self.ADCS_P1 = aD.Power_Mode1
        self.ADCS_P2 = aD.Power_Mode2
        self.ADCS_P3 = aD.Power_Mode3
        self.ADCS_P4 = aD.Power_Mode4

        self.CDH_P1 = cdhD.Power_Mode1
        self.CDH_P2 = cdhD.Power_Mode2
        self.CDH_P3 = cdhD.Power_Mode3
        self.CDH_P4 = cdhD.Power_Mode4

        self.GNC_P1 = gD.Power_Mode1
        self.GNC_P2 = gD.Power_Mode2
        self.GNC_P3 = gD.Power_Mode3
        self.GNC_P4 = gD.Power_Mode4

        self.PAY_P1 = payD.Power_Mode1
        self.PAY_P2 = payD.Power_Mode2
        self.PAY_P3 = payD.Power_Mode3
        self.PAY_P4 = payD.Power_Mode4

        self.STRU_P1 = sD.Power_Mode1
        self.STRU_P2 = sD.Power_Mode2
        self.STRU_P3 = sD.Power_Mode3
        self.STRU_P4 = sD.Power_Mode4

        self.COMM_P1 = cD.Power_Mode1
        self.COMM_P2 = cD.Power_Mode2
        self.COMM_P3 = cD.Power_Mode3
        self.COMM_P4 = cD.Power_Mode4

        self.THER_P1 = tD.Power_Mode1
        self.THER_P2 = tD.Power_Mode2
        self.THER_P3 = tD.Power_Mode3
        self.THER_P4 = tD.Power_Mode4

        # Power Budget Calcs
        p.ADCS_AVG = (p.ADCS_P1 * (p.mode1_duty/100)) + (p.ADCS_P2 * (p.mode2_duty/100)) + (p.ADCS_P3 * (p.mode3_duty/100)) + (p.ADCS_P4 * (p.mode4_duty/100))
        p.CDH_AVG = (p.CDH_P1 * (p.mode1_duty/100)) + (p.CDH_P2 * (p.mode2_duty/100)) + (p.CDH_P3 * (p.mode3_duty/100)) + (p.CDH_P4 * (p.mode4_duty/100))
        p.COMM_AVG = (p.COMM_P1 * (p.mode1_duty/100)) + (p.COMM_P2 * (p.mode2_duty/100)) + (p.COMM_P3 * (p.mode3_duty/100)) + (p.COMM_P4 * (p.mode4_duty/100))
        p.EPS_AVG = (p.EPS_P1 * (p.mode1_duty/100)) + (p.EPS_P2 * (p.mode2_duty/100)) + (p.EPS_P3 * (p.mode3_duty/100)) + (p.EPS_P4 * (p.mode4_duty/100))
        p.GNC_AVG = (p.GNC_P1 * (p.mode1_duty/100)) + (p.GNC_P2 * (p.mode2_duty/100)) + (p.GNC_P3 * (p.mode3_duty/100)) + (p.GNC_P4 * (p.mode4_duty/100))
        p.PAY_AVG = (p.PAY_P1 * (p.mode1_duty/100)) + (p.PAY_P2 * (p.mode2_duty/100)) + (p.PAY_P3 * (p.mode3_duty/100)) + (p.PAY_P4 * (p.mode4_duty/100))
        p.STRU_AVG = (p.STRU_P1 * (p.mode1_duty/100)) + (p.STRU_P2 * (p.mode2_duty/100)) + (p.STRU_P3 * (p.mode3_duty/100)) + (p.STRU_P4 * (p.mode4_duty/100))
        p.THER_AVG = (p.THER_P1 * (p.mode1_duty/100)) + (p.THER_P2 * (p.mode2_duty/100)) + (p.THER_P3 * (p.mode3_duty/100)) + (p.THER_P4 * (p.mode4_duty/100))
        p.P_AVG = p.ADCS_AVG + p.CDH_AVG + p.COMM_AVG + p.EPS_AVG + p.GNC_AVG + p.PAY_AVG + p.STRU_AVG + p.THER_AVG
        p.P_D1_raw = p.ADCS_P1 + p.CDH_P1 + p.COMM_P1 + p.EPS_P1 + p.GNC_P1 + p.PAY_P1 + p.STRU_P1 + p.THER_P1
        p.P_D2_raw = p.ADCS_P2 + p.CDH_P2 + p.COMM_P2 + p.EPS_P2 + p.GNC_P2 + p.PAY_P2 + p.STRU_P2 + p.THER_P2
        p.P_D3_raw = p.ADCS_P3 + p.CDH_P3 + p.COMM_P3 + p.EPS_P3 + p.GNC_P3 + p.PAY_P3 + p.STRU_P3 + p.THER_P3
        p.P_D4_raw = p.ADCS_P4 + p.CDH_P4 + p.COMM_P4 + p.EPS_P4 + p.GNC_P4 + p.PAY_P4 + p.STRU_P4 + p.THER_P4
        p.P_D1 = (p.P_D1_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_D2 = (p.P_D2_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_D3 = (p.P_D3_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_D4 = (p.P_D4_raw/(p.PDU_eff/100)) * (1 + p.per_margin/100)
        p.P_AVG_PDU_loss = p.P_AVG / (p.PDU_eff/100)
        p.P_margin = p.P_AVG_PDU_loss * (p.per_margin/100)
        p.P_AVG_margin = p.ADCS_AVG + p.P_margin

        # Orbit and Eclipse Energy (all in Wh):
        p.sun_energy_min = p.P_AVG_margin * (oD.min_sun_time/3600)
        p.orbit_energy = p.P_AVG_margin * (oD.orbital_period/3600)

        # Eclipse Energy
        if p.eclipse_mode == 0:
            p.eclipse_energy_max = p.P_AVG_margin * (oD.max_eclipse_time/3600)
            p.sun_energy_min = p.P_AVG_margin * (oD.min_sun_time/3600)
        elif p.eclipse_mode == 1:
            p.eclipse_energy_max = p.P_D1 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = ((p.P_AVG_margin - (p.P_D1*p.mode1_duty/100))/(1-p.mode1_duty/100))*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 2:
            p.eclipse_energy_max = p.P_D2 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D2*p.mode2_duty/100))/(1-p.mode2_duty/100)*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 3:
            p.eclipse_energy_max = p.P_D3 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D3*p.mode3_duty/100))/(1-p.mode3_duty/100)*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 4:
            p.eclipse_energy_max = p.P_D4 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D4*p.mode4_duty/100))/(1-p.mode4_duty/100)*(oD.min_sun_time/3600)

        # Worst Case Scenario (Max Eclipse):
        p.bat_roundtrip_eff = (p.bat_eff**2)/100
        p.SP_energy_orbit_worst = p.sun_energy_min + p.eclipse_energy_max/(p.bat_roundtrip_eff/100)
        p.SP_avg_power_worst = p.SP_energy_orbit_worst / (oD.min_sun_time/3600)

        # Battery Sizing
        p.bat_cycles = oD.num_orbits
        if p.bat_dod < 20:
            p.bat_degrad_rate = 5 #%/5000 cycles
        elif p.bat_dod < 40:
            p.bat_degrad_rate = 10 #%/5000 cycles
        elif p.bat_dod < 60:
            p.bat_degrad_rate = 15 #%/5000 cycles
        elif p.bat_dod < 80:
            p.bat_degrad_rate = 20 #%/5000 cycles
        else:
            p.bat_degrad_rate = 50 #%/5000 cycles

        p.bat_degrad = (1 - p.bat_degrad_rate/100)**(p.bat_cycles/5000)
        p.bat_discharge_energy = p.eclipse_energy_max / ((p.bat_eff/100) * p.bat_degrad)
        p.bat_cap = p.bat_discharge_energy/(p.bat_dod/100)
        p.num_cells =  m.ceil(p.bat_cap/p.cell_cap)
        p.bat_cap = p.num_cells*p.cell_cap
        p.bat_mass =  p.num_cells * p.cell_mass

        
        # Solar Area Sizing:
        p.L_degrad = (1 - (p.SP_degrad_rate/100))**oD.mission_lifetime
        p.T_degrad = (1 - (p.SP_degrad_temp/100))**p.SP_temp
        p.SP_eff_eol = p.SP_eff_bol/100 * p.L_degrad * p.T_degrad 
        p.solar_eol = p.solar_flux * (p.SP_eff_eol/100) # W/m^2
        p.SP_area_effective = p.SP_avg_power_worst/ p.solar_eol 

        if p.SP_tracking == 1 and p.SP_deployable == 1: # Tumbling and no deployables
            p.SP_area = 3*p.SP_area_effective
        elif p.SP_tracking == 1 and p.SP_deployable == 2: # Tumbling and Deployables
            p.SP_area = 0
        elif p.SP_tracking == 2 and p.SP_deployable == 1: # Nadir Pointing and no deployables
            p.SP_area = 0
        elif p.SP_tracking == 2 and p.SP_deployable == 2: # Nadir Pointing and Deployables
            p.SP_area = 0
        elif p.SP_tracking == 3 and p.SP_deployable == 1: # Sun Pointing and no deployables
            p.SP_area = 2*(p.SP_area_effective/m.cos(m.pi/4))
        elif p.SP_tracking == 3 and p.SP_deployable == 2: # Sun Pointing and Deployables
            p.SP_area = p.SP_area_effective
        else:
            pass

        return p

    def writeData(self, pd):
        with open('outputParameters.csv', mode='w') as parameters:
            paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            self.dataList = [self.data[1],
                            pd.UseCase,
                            pd.design_option,
                            pd.P_AVG,
                            pd.P_AVG_PDU_loss,
                            pd.P_margin,
                            pd.P_AVG_margin,
                            pd.per_margin,
                            pd.mode1_name,
                            pd.mode2_name,
                            pd.mode3_name,
                            pd.mode4_name,
                            pd.mode1_duty,
                            pd.mode2_duty,
                            pd.mode3_duty,
                            pd.mode4_duty,
                            pd.ADCS_P1,
                            pd.ADCS_P2,
                            pd.ADCS_P3,
                            pd.ADCS_P4,
                            pd.ADCS_AVG,
                            pd.CDH_P1,
                            pd.CDH_P2,
                            pd.CDH_P3,
                            pd.CDH_P4,
                            pd.CDH_AVG,
                            pd.COMM_P1,
                            pd.COMM_P2,
                            pd.COMM_P3,
                            pd.COMM_P4,
                            pd.COMM_AVG,
                            pd.EPS_P1,
                            pd.EPS_P2,
                            pd.EPS_P3,
                            pd.EPS_P4,
                            pd.EPS_AVG,
                            pd.GNC_P1,
                            pd.GNC_P2,
                            pd.GNC_P3,
                            pd.GNC_P4,
                            pd.GNC_AVG,
                            pd.PAY_P1,
                            pd.PAY_P2,
                            pd.PAY_P3,
                            pd.PAY_P4,
                            pd.PAY_AVG,
                            pd.STRU_P1,
                            pd.STRU_P2,
                            pd.STRU_P3,
                            pd.STRU_P4,
                            pd.STRU_AVG,
                            pd.THER_P1,
                            pd.THER_P2,
                            pd.THER_P3,
                            pd.THER_P4,
                            pd.THER_AVG,
                            pd.SP_eff_bol,
                            pd.SP_degrad_rate,
                            pd.SP_degrad_temp,
                            pd.SP_temp,
                            pd.SP_tracking,
                            pd.SP_deployable,
                            pd.SP_packing,
                            pd.bat_eff,
                            pd.cell_mass,
                            pd.cell_cap,
                            pd.bat_dod,
                            pd.PDU_eff,
                            pd.PDU_mass,
                            pd.PDU_data,
                            pd.solar_flux,
                            pd.orbit_energy,
                            pd.eclipse_energy_max,
                            pd.sun_energy_min,
                            pd.bat_roundtrip_eff,
                            pd.bat_cycles,
                            pd.bat_degrad_rate,
                            pd.bat_degrad,
                            pd.bat_discharge_energy,
                            pd.num_cells,
                            pd.bat_cap,
                            pd.bat_mass,
                            pd.SP_eff_eol,
                            pd.L_degrad,
                            pd.T_degrad,
                            pd.SP_energy_orbit_worst,
                            pd.SP_avg_power_worst,
                            pd.solar_eol,
                            pd.SP_area_effective,
                            pd.SP_area]
            length = len(self.data)
            for row in range(1,length):
                paramWriter.writerow([self.var[row],self.var_name[row],self.dataList[row-1],self.units[row]])