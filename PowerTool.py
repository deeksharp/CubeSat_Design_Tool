import csv
import math as m

class PowerTool:
    def __init__(self):
        pass

    def case1_PowerBudget2PowerDesign(self,p,oD,payD,cD,tD,aD,gD,cdhD,sD):
        # Read in Assumptions from File
        with open('powerAssumptions.csv', mode='r') as file:
            reader = csv.reader(file)
            data = [0]
            for row in reader:
                d = row[2]
                data.append(d)

        # Assign Assumptions:
        p.UseCase = data[2]
        p.solar_flux = float(data[71]) # Solar Flux 
        #p.SP_eff_bol = float(data[47]) # Solar Cell Efficiency, BOL
        #p.cell_dens = float(data[50])        

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
        print('1: ' + str(p.orbit_energy))
        # Eclipse Energy
        if p.eclipse_mode == 0:
            p.eclipse_energy_max = p.P_AVG_margin * (oD.max_eclipse_time/3600)
        elif p.eclipse_mode == 1:
            p.eclipse_energy_max = p.P_D1 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = ((p.P_AVG_margin - (p.P_D1*p.mode1_duty))/(1-p.mode1_duty))*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 2:
            p.eclipse_energy_max = p.P_D2 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D1*p.mode1_duty))/(1-p.mode1_duty)*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 3:
            p.eclipse_energy_max = p.P_D3 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D1*p.mode1_duty))/(1-p.mode1_duty)*(oD.min_sun_time/3600)
        elif p.eclipse_mode == 4:
            p.eclipse_energy_max = p.P_D4 * (oD.max_eclipse_time/3600)
            p.sun_energy_min = (p.P_AVG_margin - (p.P_D1*p.mode1_duty))/(1-p.mode1_duty)*(oD.min_sun_time/3600)

        print('2: ' + str(p.orbit_energy))

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
        p.bat_mass =  p.bat_cap * p.cell_dens

        # Solar Sizing:
        p.L_degrad = (1 - (p.SP_degrad_rate/100))**oD.mission_lifetime
        p.T_degrad = (1 - (p.SP_degrad_temp/100))**p.SP_temp
        p.SP_eff_eol = p.SP_eff_bol * p.L_degrad * p.T_degrad 
        p.solar_eol = p.solar_flux * p.SP_eff_eol # W/m^2
        p.SP_area_effective = p.solar_eol / p.SP_avg_power_worst

        if p.SP_tracking == 1:
            pass
        elif p.SP_tracking == 2:
            pass
        elif p.SP_tracking == 3:
            pass

        return p
                
    # def batterySizing(self,p,oD):
    #     p.bat_cycles = p
    #     p.bat_cap = bat_
    #     p.bat_

    #     return p
    
    # def systemMass(self,p)
    #     pass

    # def solarSizing(self,p,oD):
    #     pass

    def writeData(self, pd):
        with open('parameters.csv', mode='w') as parameters:
            paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            dataList = [pd.UseCase,
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
                        pd.design_option,
                        pd.SP_eff_bol,
                        pd.SP_degrad_rate,
                        pd.SP_degrad_temp,
                        pd.SP_temp,
                        pd.SP_tracking,
                        pd.SP_deployable,
                        pd.bat_eff,
                        pd.cell_mass,
                        pd.cell_dens,
                        pd.cell_cap,
                        pd.bat_dod,
                        pd.PDU_eff,
                        pd.PDU_mass,
                        pd.PDU_data,
                        pd.solar_flux,
                        pd.orbit_energy,
                        pd.eclipse_energy_avg,
                        pd.eclipse_energy_max,
                        pd.sun_energy_avg,
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
                        pd.SP_area_effective]
            paramWriter.writecolumn(dataList)
            # paramWriter.writerow(pd.UseCase)
            # paramWriter.writerow(pd.ADCS_P1)
            # paramWriter.writerow(pd.ADCS_D1)
            # paramWriter.writerow(pd.ADCS_P2)
            # paramWriter.writerow(pd.ADCS_D2)
            # paramWriter.writerow(pd.ADCS_AVG)
            # paramWriter.writerow(pd.CDH_P1)
            # paramWriter.writerow(pd.CDH_D1)
            # paramWriter.writerow(pd.CDH_P2)
            # paramWriter.writerow(pd.CDH_D2)
            # paramWriter.writerow(pd.COMM_P1)
            # paramWriter.writerow(pd.COMM_D1)
            # paramWriter.writerow(pd.COMM_P2)
            # paramWriter.writerow(pd.COMM_D2)
            # paramWriter.writerow(pd.EPS_P1)
            # paramWriter.writerow(pd.EPS_D1)
            # paramWriter.writerow(pd.EPS_P2)
            # paramWriter.writerow(pd.EPS_D2)
            # paramWriter.writerow(pd.EPS_AVG)
            # paramWriter.writerow(pd.GNC_P1)
            # paramWriter.writerow(pd.GNC_D1)
            # paramWriter.writerow(pd.GNC_P2)
            # paramWriter.writerow(pd.GNC_D2)
            # paramWriter.writerow(pd.GNC_AVG)
            # paramWriter.writerow(pd.PAY_P1)
            # paramWriter.writerow(pd.PAY_D1)
            # paramWriter.writerow(pd.PAY_P2)
            # paramWriter.writerow(pd.PAY_D2)
            # paramWriter.writerow(pd.PAY_AVG)
            # paramWriter.writerow(pd.STRU_P1)
            # paramWriter.writerow(pd.STRU_D1)
            # paramWriter.writerow(pd.STRU_P2)
            # paramWriter.writerow(pd.STRU_D2)
            # paramWriter.writerow(pd.STRU_AVG)
            # paramWriter.writerow(pd.THER_P1)
            # paramWriter.writerow(pd.THER_D1)
            # paramWriter.writerow(pd.THER_P2)
            # paramWriter.writerow(pd.THER_D2)
            # paramWriter.writerow(pd.THER_AVG)
            
        
        
    def case2_PowerDesign2PayloadCapabilities(self, pd):
        with open('powerAssumptions.csv', mode='r') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                d = row[4]
                data.append(d)

    def case3_PayloadCapabilities2PowerDesign(self, pd):
        with open('powerAssumptions.csv', mode='r') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                d = row[7]
                data.append(d)