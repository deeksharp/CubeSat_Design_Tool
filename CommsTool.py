import csv
import math as m

class CommsTool:
    def __init__(self):
        pass
                
    def LinkBudget4Demo(self,cD):
        #CSV FILE READ
        print("start open csv comms file")
        with open('commsAssumptions.csv', mode='r') as file:
                reader = csv.reader(file)
                self.var = ['']
                self.var_name = ['']
                self.data = [0]
                self.units = ['']
                print("start reading rows")
                for row in reader:
                    v = row[0]
                    n = row[1]
                    d = row[2]
                    u = row[3]
                    self.var.append(v)
                    self.var_name.append(n)
                    self.data.append(d)
                    self.units.append(u)
                    ##print("Index: ",row)

        # Line Budget Calcs
        
        cD.outTransPowerDXS = m.log10(cD.transPowerxS)*10
        cD.outTransPowerDUS = m.log10(cD.transPoweruS)*10
        cD.outAntGainDXS = cD.antGainxS
        cD.outAntGainDUS = cD.antGainuS
        cD.outAntGainUXS = cD.antGainxS
        cD.outAntGainUUS = cD.antGainuS
        cD.outTransPowerUXG = m.log10(cD.transPowerxG)*10
        cD.outTransPowerUUG = m.log10(cD.transPoweruG)*10
        cD.outAntGainDXG = cD.antGainxG
        cD.outAntGainDUG = cD.antGainuG
        cD.outAntGainUXG = cD.antGainxG
        cD.outAntGainUUG = cD.antGainuG
        cD.outEBNODX = cD.ebnox
        cD.outEBNODU = cD.ebnou
        cD.outEBNOUX = cD.ebnox
        cD.outEBNOUU = cD.ebnou
        cD.outDataRateDX = m.log10(cD.xdown)*10
        cD.outDataRateDU = m.log10(cD.udown)*10
        cD.outDataRateUX = m.log10(cD.xup)*10
        cD.outDataRateUU = m.log10(cD.uup)*10
        cD.outNoiseTemp = m.log10(cD.sysTemp)*10
        cD.outPathLossX = m.log10(4*3.14*cD.maxDistanceEarth*cD.xfreq/300000000)*20
        cD.outPathLossU = m.log10(4*3.14*cD.maxDistanceEarth*cD.ufreq/300000000)*20
        cD.outOtherLoss = cD.rainLoss + cD.lineLoss ##cD.pointingLoss + cD.rainLoss + cD.electronLoss + cD.polarLoss + cD.lineLoss
        cD.outMarginDX = cD.outTransPowerDXS + cD.outAntGainDXS + cD.outAntGainDXG + 228.6 - cD.outEBNODX - cD.outDataRateDX - cD.outNoiseTemp - cD.outPathLossX - cD.outOtherLoss
        cD.outMarginDU = cD.outTransPowerDUS + cD.outAntGainDUS + cD.outAntGainDUG + 228.6 - cD.outEBNODU - cD.outDataRateDU - cD.outNoiseTemp - cD.outPathLossU - cD.outOtherLoss
        cD.outMarginUX = cD.outTransPowerUXG + cD.outAntGainUXS + cD.outAntGainUXG + 228.6 - cD.outEBNOUX - cD.outDataRateUX - cD.outNoiseTemp - cD.outPathLossX - cD.outOtherLoss
        cD.outMarginUU = cD.outTransPowerUUG + cD.outAntGainUUS + cD.outAntGainUUG + 228.6 - cD.outEBNOUU - cD.outDataRateUU - cD.outNoiseTemp - cD.outPathLossU - cD.outOtherLoss
                
        return cD

    def writeData(self, cD):
        with open('outputCommsParameters.csv', mode='w', newline='') as parameters:
            paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            self.dataList = [self.data[1],
                            cD.outTransPowerDXS,
                            cD.outTransPowerDUS,
                            cD.outAntGainDXS,
                            cD.outAntGainDUS,
                            cD.outAntGainUXS,
                            cD.outAntGainUUS,
                            cD.outTransPowerUXG,
                            cD.outTransPowerUUG,
                            cD.outAntGainDXG,
                            cD.outAntGainDUG,
                            cD.outAntGainUXG,
                            cD.outAntGainUUG,
                            cD.outEBNODX, 
                            cD.outEBNODU,
                            cD.outEBNOUX,
                            cD.outEBNOUU,
                            cD.outDataRateDX,
                            cD.outDataRateDU,
                            cD.outDataRateUX,
                            cD.outDataRateUU,
                            cD.outNoiseTemp,
                            cD.outPathLossX,
                            cD.outPathLossU,
                            cD.outOtherLoss,
                            cD.outMarginDX,
                            cD.outMarginDU,
                            cD.outMarginUX,
                            cD.outMarginUU]
            length = len(self.data)
            for row in range(1,length):
                paramWriter.writerow([self.var[row],self.var_name[row],self.dataList[row-1],self.units[row]])