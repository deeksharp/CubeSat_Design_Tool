import csv
import math as m

class CommsTool:
    def __init__(self):
        pass
                
    def LinkBudget4Demo(self,p,oD,payD,cD,tD,aD,gD,cdhD,sD):

        # Line Budget Calcs
        
        """
                    self.transPowerG= float(self.ctransPowerG.get())
             
                    self.lineLossG = float(self.clineLossG.get())
               
                    self.antGainG = float(self.cantGainG.get())
                
                    self.maxSlantRange = float(self.cmaxSlantRange.get())
                
                    self.dishDiameter = float(self.cdishDiameter.get())
                
                    self.EIRP = float(self.cEIRP.get())
                
                    self.minElevationAngle = int(self.cminElevationAngle.get())
               
                    self.ebno = int(self.cebno.get())
                
                    self.transPowerS= float(self.ctransPowerS.get())
                
                    self.lineLossS = float(self.clineLossS.get())
                
                    self.antGainS = float(self.cantGainS.get())
                
                    self.maxDistanceEarth = float(self.cmaxDistanceEarth.get())
              
                    self.atomClock = float(self.catomClock.get())
                
                    self.radiation = float(self.cradiation.get())
               
                    self.housekeeping = float(self.chousekeeping.get())
                
                    self.cenFreq= float(self.ccenFreq.get())
                
                    self.pointingLoss = float(self.cpointingLoss.get())
                
                    self.rainLoss = float(self.crainLoss.get())
               
                    self.electronLoss = float(self.celectronLoss.get())
                
                    self.polarLoss = float(self.cpolarLoss.get())
                
                    self.sysNoiseTemp = float(self.csysNoiseTemp.get())
                
                    self.fixedData = int(self.cfixedData.get())
                    """
                
        return cD

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