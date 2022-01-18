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
        
        cD.out_up_p_sc_transpower = m.log10(cD.up_p_sc_transpower)*10 if cD.up_p_sc_transpower > 0 else 0
        cD.out_up_p_gs_transpower = m.log10(cD.up_p_gs_transpower)*10 if cD.up_p_gs_transpower > 0 else 0
        cD.out_up_s_sc_transpower = m.log10(cD.up_s_sc_transpower)*10 if cD.up_s_sc_transpower > 0 else 0
        cD.out_up_s_gs_transpower = m.log10(cD.up_s_gs_transpower)*10 if cD.up_s_gs_transpower > 0 else 0
        cD.out_down_p_sc_transpower = m.log10(cD.down_p_sc_transpower)*10 if cD.down_p_sc_transpower > 0 else 0
        cD.out_down_p_gs_transpower = m.log10(cD.down_p_gs_transpower)*10 if cD.down_p_gs_transpower > 0 else 0
        cD.out_down_s_sc_transpower = m.log10(cD.down_s_sc_transpower)*10 if cD.down_s_sc_transpower > 0 else 0
        cD.out_down_s_gs_transpower = m.log10(cD.down_s_gs_transpower)*10 if cD.down_s_gs_transpower > 0 else 0
        cD.out_up_p_sc_antgain = cD.up_p_sc_antgain
        cD.out_up_p_gs_antgain = cD.up_p_gs_antgain
        cD.out_up_s_sc_antgain = cD.up_s_sc_antgain
        cD.out_up_s_gs_antgain = cD.up_s_gs_antgain
        cD.out_down_p_sc_antgain = cD.down_p_sc_antgain
        cD.out_down_p_gs_antgain = cD.down_p_gs_antgain
        cD.out_down_s_sc_antgain = cD.down_s_sc_antgain
        cD.out_down_s_gs_antgain = cD.down_s_gs_antgain
        cD.out_up_p_datarate = m.log10(cD.up_p_datarate)*10 if cD.up_p_datarate > 0 else 0
        cD.out_up_s_datarate = m.log10(cD.up_s_datarate)*10 if cD.up_s_datarate > 0 else 0
        cD.out_down_p_datarate = m.log10(cD.down_p_datarate)*10 if cD.down_p_datarate > 0 else 0
        cD.out_down_s_datarate = m.log10(cD.down_s_datarate)*10 if cD.down_s_datarate > 0 else 0
        cD.out_up_p_EBNo = cD.up_p_EBNo
        cD.out_up_s_EBNo = cD.up_s_EBNo
        cD.out_down_p_EBNo = cD.down_p_EBNo
        cD.out_down_s_EBNo = cD.down_s_EBNo
        cD.out_up_systemp = m.log10(cD.up_systemp)*10 if cD.up_systemp > 0 else 0 #aka Noise temp
        cD.out_down_systemp = m.log10(cD.down_systemp)*10 if cD.down_systemp > 0 else 0
        cD.out_up_p_pathloss = m.log10(4*3.14*cD.up_maxdistanceEarth*cD.up_p_frequency/300000000)*20 if cD.up_maxdistanceEarth > 0 and cD.up_p_frequency > 0 else 0
        cD.out_up_s_pathloss = m.log10(4*3.14*cD.up_maxdistanceEarth*cD.up_s_frequency/300000000)*20 if cD.up_maxdistanceEarth > 0 and cD.up_s_frequency > 0 else 0
        cD.out_down_p_pathloss = m.log10(4*3.14*cD.down_maxdistanceEarth*cD.down_p_frequency/300000000)*20 if cD.down_maxdistanceEarth > 0 and cD.down_p_frequency > 0 else 0
        cD.out_down_s_pathloss = m.log10(4*3.14*cD.down_maxdistanceEarth*cD.down_s_frequency/300000000)*20 if cD.down_maxdistanceEarth > 0 and cD.down_s_frequency > 0 else 0
        cD.out_up_otherloss = cD.up_rainloss + cD.up_lineloss + cD.up_otherloss
        cD.out_down_otherloss = cD.down_rainloss + cD.down_lineloss + cD.down_otherloss
        cD.out_up_p_margin = cD.out_up_p_gs_transpower + cD.out_up_p_gs_antgain + cD.out_up_p_sc_antgain + 228.6 - cD.out_up_p_EBNo - cD.out_up_p_datarate - cD.out_up_systemp - cD.out_up_p_pathloss - cD.out_up_otherloss
        cD.out_up_s_margin = cD.out_up_s_gs_transpower + cD.out_up_s_gs_antgain + cD.out_up_s_sc_antgain + 228.6 - cD.out_up_s_EBNo - cD.out_up_s_datarate - cD.out_up_systemp - cD.out_up_s_pathloss - cD.out_up_otherloss
        cD.out_down_p_margin = cD.out_down_p_sc_transpower + cD.out_down_p_sc_antgain + cD.out_down_p_gs_antgain + 228.6 - cD.out_down_p_EBNo - cD.out_down_p_datarate - cD.out_down_systemp - cD.out_down_p_pathloss - cD.out_down_otherloss
        cD.out_down_s_margin = cD.out_down_s_sc_transpower + cD.out_down_s_sc_antgain + cD.out_down_s_gs_antgain + 228.6 - cD.out_down_s_EBNo - cD.out_down_s_datarate - cD.out_down_systemp - cD.out_down_s_pathloss - cD.out_down_otherloss

        return cD

    def writeData(self, cD):
        print("START WRITE DATA")
        with open('outputCommsParameters.csv', mode='w', newline='') as parameters:
            paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            self.dataList = [self.data[1],
                            cD.out_up_p_sc_transpower,
                            cD.out_up_s_sc_transpower,
                            cD.out_down_p_sc_transpower,
                            cD.out_down_s_sc_transpower,
                            cD.out_up_p_sc_antgain,
                            cD.out_up_s_sc_antgain,
                            cD.out_down_p_sc_antgain,
                            cD.out_down_s_sc_antgain,
                            cD.out_up_p_gs_transpower,
                            cD.out_up_s_gs_transpower,
                            cD.out_down_p_gs_transpower,
                            cD.out_down_s_gs_transpower,
                            cD.out_up_p_gs_antgain,
                            cD.out_up_s_gs_antgain,
                            cD.out_down_p_gs_antgain,
                            cD.out_down_s_gs_antgain,
                            cD.out_up_p_datarate,
                            cD.out_up_s_datarate,
                            cD.out_down_p_datarate,
                            cD.out_down_s_datarate,
                            cD.out_up_p_EBNo,
                            cD.out_up_s_EBNo,
                            cD.out_down_p_EBNo,
                            cD.out_down_s_EBNo,
                            cD.out_up_systemp,
                            cD.out_down_systemp,
                            cD.out_up_p_pathloss,
                            cD.out_up_s_pathloss,
                            cD.out_down_p_pathloss,
                            cD.out_down_s_pathloss,
                            cD.out_up_otherloss,
                            cD.out_down_otherloss,
                            cD.out_up_p_margin,
                            cD.out_up_s_margin,
                            cD.out_down_p_margin,
                            cD.out_down_s_margin]
            length = len(self.data)
            print("HELLOOOOOO I RANNNNNNNNNNNNNJ")
            for row in range(1,length):
                paramWriter.writerow([self.var[row],self.var_name[row],self.dataList[row-1],self.units[row]])