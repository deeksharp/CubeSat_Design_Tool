import csv
import math

class PowerTool:
    def __init__(self):
        pass

    def case1_PowerBudget2PowerDesign(self,p,oD,payD,cD,tD,aD,gD,cdhD,sD):
        # Read in Assumptions from File
        with open('powerAssumptions.csv', mode='r') as file:
            reader = csv.reader(file)
            data = [0]
            for row in reader:
                d = row[1]
                data.append(d)
        #Assign Assumptions
        p.UseCase = data[2]
        p.per_margin = float(data[4])
        p.solar_flux = float(data[46]) # Solar Flux 
        p.SP_eff_bol = float(data[47]) # Solar Cell Efficiency, BOL
        p.cell_dens = float(data[50])
        #p.orbitalPeriod = 

        # Power Budget Calcs
        p.ADCS_AVG = (p.ADCS_P1 * (p.ADCS_D1/100)) + (p.ADCS_P2 * (p.ADCS_D2/100))
        p.CDH_AVG = (p.CDH_P1 * (p.CDH_D1/100)) + (p.CDH_P2 * (p.CDH_D2/100))
        p.COMM_AVG = (p.COMM_P1 * (p.COMM_D1/100)) + (p.COMM_P2 * (p.COMM_D2/100))
        p.EPS_AVG = (p.EPS_P1 * (p.EPS_D1/100)) + (p.EPS_P2 * (p.EPS_D2/100))
        p.GNC_AVG = (p.GNC_P1 * (p.GNC_D1/100)) + (p.GNC_P2 * (p.GNC_D2/100))
        p.PAY_AVG = (p.PAY_P1 * (p.PAY_D1/100)) + (p.PAY_P2 * (p.PAY_D2/100))
        p.STRU_AVG = (p.STRU_P1 * (p.STRU_D1/100)) + (p.STRU_P2 * (p.STRU_D2/100))
        p.THER_AVG = (p.THER_P1 * (p.THER_D1/100)) + (p.THER_P2 * (p.THER_D2/100))
        p.P_AVG = p.ADCS_AVG + p.CDH_AVG + p.COMM_AVG + p.EPS_AVG + p.GNC_AVG + p.PAY_AVG + p.STRU_AVG + p.THER_AVG
        p.P_AVG_margin = p.ADCS_AVG * (1 + (p.per_margin/100))

        orbit_hr = p
        return p
                
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

    def writeData(self, pd):
        with open('parameters.csv', mode='w') as parameters:
            paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            paramWriter.writerow(pd.UseCase)
            paramWriter.writerow(pd.ADCS_P1)
            paramWriter.writerow(pd.ADCS_D1)
            paramWriter.writerow(pd.ADCS_P2)
            paramWriter.writerow(pd.ADCS_D2)
            paramWriter.writerow(pd.ADCS_AVG)
            paramWriter.writerow(pd.CDH_P1)
            paramWriter.writerow(pd.CDH_D1)
            paramWriter.writerow(pd.CDH_P2)
            paramWriter.writerow(pd.CDH_D2)
            paramWriter.writerow(pd.COMM_P1)
            paramWriter.writerow(pd.COMM_D1)
            paramWriter.writerow(pd.COMM_P2)
            paramWriter.writerow(pd.COMM_D2)
            paramWriter.writerow(pd.EPS_P1)
            paramWriter.writerow(pd.EPS_D1)
            paramWriter.writerow(pd.EPS_P2)
            paramWriter.writerow(pd.EPS_D2)
            paramWriter.writerow(pd.EPS_AVG)
            paramWriter.writerow(pd.GNC_P1)
            paramWriter.writerow(pd.GNC_D1)
            paramWriter.writerow(pd.GNC_P2)
            paramWriter.writerow(pd.GNC_D2)
            paramWriter.writerow(pd.GNC_AVG)
            paramWriter.writerow(pd.PAY_P1)
            paramWriter.writerow(pd.PAY_D1)
            paramWriter.writerow(pd.PAY_P2)
            paramWriter.writerow(pd.PAY_D2)
            paramWriter.writerow(pd.PAY_AVG)
            paramWriter.writerow(pd.STRU_P1)
            paramWriter.writerow(pd.STRU_D1)
            paramWriter.writerow(pd.STRU_P2)
            paramWriter.writerow(pd.STRU_D2)
            paramWriter.writerow(pd.STRU_AVG)
            paramWriter.writerow(pd.THER_P1)
            paramWriter.writerow(pd.THER_D1)
            paramWriter.writerow(pd.THER_P2)
            paramWriter.writerow(pd.THER_D2)
            paramWriter.writerow(pd.THER_AVG)
            

        # Power Design to Power Capabilities
        
        self.SP_eff_bol: float
        self.SP_area: float
        self.SP_point: int
        self.SP_deploy: int
        self.cell_eff: float
        self.cell_mass: float
        self.cell_density: float
        self.bat_cap: float
        self.bat_dod: float
        self.PDU_eff: float
        self.PDU_mass: float
        self.PDU_data: float
        
