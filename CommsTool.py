import csv
import math as m

class CommsTool:
    def __init__(self):
        pass
                
    def LinkBudget4Demo_case1(self,cD):
        #CSV FILE READ
        print("start open csv comms file 1")
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
        cD.out_up_p_EbNo = cD.up_p_EbNo
        cD.out_up_s_EbNo = cD.up_s_EbNo
        cD.out_down_p_EbNo = cD.down_p_EbNo
        cD.out_down_s_EbNo = cD.down_s_EbNo
        cD.out_up_p_systemp = m.log10(cD.up_p_systemp)*10 if cD.up_p_systemp > 0 else 0 #aka Noise temp
        cD.out_up_s_systemp = m.log10(cD.up_s_systemp)*10 if cD.up_s_systemp > 0 else 0 #aka Noise temp
        cD.out_down_p_systemp = m.log10(cD.down_p_systemp)*10 if cD.down_p_systemp > 0 else 0
        cD.out_down_s_systemp = m.log10(cD.down_s_systemp)*10 if cD.down_s_systemp > 0 else 0
        cD.out_up_p_pathloss = m.log10(4*3.141592653589793*cD.up_p_maxdistanceEarth*cD.up_p_frequency/300000000)*20 if cD.up_p_maxdistanceEarth > 0 and cD.up_p_frequency > 0 else 0
        cD.out_up_s_pathloss = m.log10(4*3.141592653589793*cD.up_s_maxdistanceEarth*cD.up_s_frequency/300000000)*20 if cD.up_s_maxdistanceEarth > 0 and cD.up_s_frequency > 0 else 0
        cD.out_down_p_pathloss = m.log10(4*3.141592653589793*cD.down_p_maxdistanceEarth*cD.down_p_frequency/300000000)*20 if cD.down_p_maxdistanceEarth > 0 and cD.down_p_frequency > 0 else 0
        cD.out_down_s_pathloss = m.log10(4*3.141592653589793*cD.down_s_maxdistanceEarth*cD.down_s_frequency/300000000)*20 if cD.down_s_maxdistanceEarth > 0 and cD.down_s_frequency > 0 else 0
        cD.out_up_p_otherloss = cD.up_p_rainloss + cD.up_p_lineloss + cD.up_p_otherloss 
        cD.out_up_s_otherloss = cD.up_s_rainloss + cD.up_s_lineloss + cD.up_s_otherloss 
        cD.out_down_p_otherloss = cD.down_p_rainloss + cD.down_p_lineloss + cD.down_p_otherloss
        cD.out_down_s_otherloss = cD.down_s_rainloss + cD.down_s_lineloss + cD.down_s_otherloss
        cD.out_up_p_margin = cD.out_up_p_gs_transpower + cD.out_up_p_gs_antgain + cD.out_up_p_sc_antgain + 228.6 - cD.out_up_p_EbNo - cD.out_up_p_datarate - cD.out_up_p_systemp - cD.out_up_p_otherloss- cD.out_up_p_pathloss
        cD.out_up_s_margin = cD.out_up_s_gs_transpower + cD.out_up_s_gs_antgain + cD.out_up_s_sc_antgain + 228.6 - cD.out_up_s_EbNo - cD.out_up_s_datarate - cD.out_up_s_systemp - cD.out_up_s_pathloss - cD.out_up_s_otherloss 
        cD.out_down_p_margin = cD.out_down_p_sc_transpower + cD.out_down_p_sc_antgain + cD.out_down_p_gs_antgain + 228.6 - cD.out_down_p_EbNo - cD.out_down_p_datarate - cD.out_down_p_systemp - cD.out_down_p_otherloss- cD.out_down_p_pathloss
        cD.out_down_s_margin = cD.out_down_s_sc_transpower + cD.out_down_s_sc_antgain + cD.out_down_s_gs_antgain + 228.6 - cD.out_down_s_EbNo - cD.out_down_s_datarate - cD.out_down_s_systemp - cD.out_down_s_pathloss - cD.out_down_s_otherloss

        return cD

    def LinkBudget4Demo_case2(self,cD):
        #CSV FILE READ
        print("start open csv comms file 2")
        with open('commsAssumptions2.csv', mode='r') as file:
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


        secondary = True if cD.up_2_datarate > 0 or cD.up_2_transmitterpower > 0 or cD.up_2_margin > 0 else False 
        def findSolve(first, second, third):
            return 1 if first == 0 and second > 0 and third > 0 else 2 if second == 0 and first > 0 and third > 0 else 3 if third == 0 and first > 0 and second > 0 else 0 
        up_1_missing = findSolve(cD.up_1_transmitterpower, cD.up_1_datarate, cD.up_1_margin)
        down_1_missing = findSolve(cD.down_1_transmitterpower, cD.down_1_datarate, cD.down_1_margin)
        up_2_missing = findSolve(cD.up_2_transmitterpower, cD.up_2_datarate, cD.up_2_margin)
        down_2_missing = findSolve(cD.down_2_transmitterpower, cD.down_2_datarate, cD.down_2_margin)
        boltzman = -228.6

        # Line Budget Calcs
        cD.out_up_1_frequency = cD.up_1_frequency
        cD.out_up_2_frequency = cD.up_2_frequency if secondary else 0
        cD.out_down_1_frequency = cD.down_1_frequency
        cD.out_down_2_frequency = cD.down_2_frequency if secondary else 0
        cD.out_up_1_transmitterantgain = m.log10(cD.up_1_transmitterdishdiameter)*20 + m.log10(cD.up_1_frequency)*20 + m.log10(cD.up_1_transmitterefficiency)*10 - 159.59
        cD.out_up_2_transmitterantgain = m.log10(cD.up_2_transmitterdishdiameter)*20 + m.log10(cD.up_2_frequency)*20 + m.log10(cD.up_2_transmitterefficiency)*10 - 159.59  if secondary else 0
        cD.out_down_1_transmitterantgain = m.log10(cD.down_1_transmitterdishdiameter)*20 + m.log10(cD.down_1_frequency)*20 + m.log10(cD.down_1_transmitterefficiency)*10 - 159.59
        cD.out_down_2_transmitterantgain = m.log10(cD.down_2_transmitterdishdiameter)*20 + m.log10(cD.down_2_frequency)*20 + m.log10(cD.down_2_transmitterefficiency)*10 - 159.59  if secondary else 0
        cD.out_up_1_transmitterefficiency = cD.up_1_transmitterefficiency
        cD.out_up_2_transmitterefficiency = cD.up_2_transmitterefficiency if secondary else 0
        cD.out_down_1_transmitterefficiency = cD.down_1_transmitterefficiency
        cD.out_down_2_transmitterefficiency = cD.down_2_transmitterefficiency if secondary else 0
        cD.out_up_1_transmitterdishdiameter = cD.up_1_transmitterdishdiameter
        cD.out_up_2_transmitterdishdiameter = cD.up_2_transmitterdishdiameter if secondary else 0
        cD.out_down_1_transmitterdishdiameter = cD.down_1_transmitterdishdiameter
        cD.out_down_2_transmitterdishdiameter = cD.down_2_transmitterdishdiameter if secondary else 0
        cD.out_up_1_beamwidth = cD.up_1_beamwidth
        cD.out_up_2_beamwidth = cD.up_2_beamwidth if secondary else 0
        cD.out_down_1_beamwidth = cD.down_1_beamwidth
        cD.out_down_2_beamwidth = cD.down_2_beamwidth if secondary else 0
        cD.out_up_1_spaceloss = cD.up_1_spaceloss
        cD.out_up_2_spaceloss = cD.up_2_spaceloss if secondary else 0
        cD.out_down_1_spaceloss = cD.down_1_spaceloss
        cD.out_down_2_spaceloss = cD.down_2_spaceloss if secondary else 0
        cD.out_up_1_atmosphereattenuation = cD.up_1_atmosphereattenuation
        cD.out_up_2_atmosphereattenuation = cD.up_2_atmosphereattenuation if secondary else 0
        cD.out_down_1_atmosphereattenuation = cD.down_1_atmosphereattenuation
        cD.out_down_2_atmosphereattenuation = cD.down_2_atmosphereattenuation if secondary else 0
        cD.out_up_1_receiverdishdiameter = cD.up_1_receiverdishdiameter
        cD.out_up_2_receiverdishdiameter = cD.up_2_receiverdishdiameter if secondary else 0
        cD.out_down_1_receiverdishdiameter = cD.down_1_receiverdishdiameter
        cD.out_down_2_receiverdishdiameter = cD.down_2_receiverdishdiameter if secondary else 0
        cD.out_up_1_receiverefficiency = cD.up_1_receiverefficiency
        cD.out_up_2_receiverefficiency = cD.up_2_receiverefficiency if secondary else 0
        cD.out_down_1_receiverefficiency = cD.down_1_receiverefficiency
        cD.out_down_2_receiverefficiency = cD.down_2_receiverefficiency if secondary else 0
        cD.out_up_1_EbNo = cD.up_1_EbNo
        cD.out_up_2_EbNo = cD.up_2_EbNo if secondary else 0
        cD.out_down_1_EbNo = cD.down_1_EbNo
        cD.out_down_2_EbNo = cD.down_2_EbNo if secondary else 0
        cD.out_up_1_systemtemp = cD.up_1_systemtemp
        cD.out_up_2_systemtemp = cD.up_2_systemtemp if secondary else 0
        cD.out_down_1_systemtemp = cD.down_1_systemtemp
        cD.out_down_2_systemtemp = cD.down_2_systemtemp if secondary else 0
        cD.out_up_1_systemtemp2 = m.log10(cD.up_1_systemtemp)*10
        cD.out_up_2_systemtemp2 = m.log10(cD.up_2_systemtemp)*10 if secondary else 0
        cD.out_down_1_systemtemp2 = m.log10(cD.down_1_systemtemp)*10
        cD.out_down_2_systemtemp2 = m.log10(cD.down_2_systemtemp)*10 if secondary else 0


        cD.out_up_1_receiverantgain = m.log10(cD.up_1_receiverdishdiameter)*20 + m.log10(cD.up_1_frequency)*20 + m.log10(cD.up_1_receiverefficiency)*10 - 159.5
        cD.out_up_2_receiverantgain = m.log10(cD.up_2_receiverdishdiameter)*20 + m.log10(cD.up_2_frequency)*20 + m.log10(cD.up_2_receiverefficiency)*10 - 159.59 if secondary else 0
        cD.out_down_1_receiverantgain = m.log10(cD.down_1_receiverdishdiameter)*20 + m.log10(cD.down_1_frequency)*20 + m.log10(cD.down_1_receiverefficiency)*10 - 159.59
        cD.out_down_2_receiverantgain = m.log10(cD.down_2_receiverdishdiameter)*20 + m.log10(cD.down_2_frequency)*20 + m.log10(cD.down_2_receiverefficiency)*10 - 159.59 if secondary else 0
        
        cD.out_up_1_receiversensitivity = cD.out_up_1_receiverantgain - cD.out_up_1_systemtemp2
        cD.out_up_2_receiversensitivity = cD.out_up_2_receiverantgain - cD.out_up_2_systemtemp2 if secondary else 0
        cD.out_down_1_receiversensitivity = cD.out_down_1_receiverantgain - cD.out_down_1_systemtemp2
        cD.out_down_2_receiversensitivity = cD.out_down_2_receiverantgain - cD.out_down_2_systemtemp2 if secondary else 0
        
        cD.out_up_1_datarate2 = 0
        cD.out_up_2_datarate2 = 0
        cD.out_down_1_datarate2 = 0
        cD.out_down_2_datarate2 = 0
        cD.out_up_1_transmitterpower2 = 0
        cD.out_up_2_transmitterpower2 = 0
        cD.out_down_1_transmitterpower2 = 0
        cD.out_down_2_transmitterpower2 = 0
        cD.out_up_1_transmitterpower = 0
        cD.out_up_2_transmitterpower = 0
        cD.out_down_1_transmitterpower = 0
        cD.out_down_2_transmitterpower = 0
        cD.out_up_1_datarate = 0
        cD.out_up_2_datarate = 0
        cD.out_down_1_datarate = 0
        cD.out_down_2_datarate = 0
        cD.out_up_1_eirp = 0
        cD.out_up_2_eirp = 0
        cD.out_down_1_eirp = 0
        cD.out_down_2_eirp = 0
        cD.out_up_1_powerdensity = 0
        cD.out_up_2_powerdensity = 0
        cD.out_down_1_powerdensity = 0
        cD.out_down_2_powerdensity = 0
        cD.out_up_1_EbNocalc = 0 
        cD.out_up_2_EbNocalc = 0 
        cD.out_down_1_EbNocalc = 0 
        cD.out_down_2_EbNocalc = 0
        cD.out_up_1_margin = 0
        cD.out_up_2_margin = 0
        cD.out_down_1_margin = 0
        cD.out_down_2_margin = 0

        
        if up_1_missing == 1 : 
            cD.out_up_1_EbNocalc = cD.up_1_margin + cD.up_1_EbNo - cD.up_1_implementationloss
            cD.out_up_1_margin = cD.up_1_margin
            cD.out_up_1_datarate2 = m.log10(cD.up_1_datarate)*10
            cD.out_up_1_datarate = cD.up_1_datarate
            cD.out_up_1_powerdensity = cD.out_up_1_EbNocalc + cD.out_up_1_datarate2
            cD.out_up_1_transmitterpower2 = cD.out_up_1_powerdensity - cD.up_1_lineloss - cD.out_up_1_transmitterantgain - cD.out_up_1_receiversensitivity + boltzman - (cD.up_1_spaceloss + cD.up_1_transmitterpointingloss + cD.up_1_polarizationloss + cD.up_1_atmosphereattenuation + cD.up_1_rainattenuation + cD.up_1_receiverpointingloss)
            cD.out_up_1_transmitterpower = 10**(cD.out_up_1_transmitterpower2/10)
            cD.out_up_1_eirp = cD.out_up_1_transmitterpower2 + cD.up_1_lineloss + cD.up_1_transmitterpointingloss + cD.out_up_1_transmitterantgain
            
        if up_2_missing == 1 : 
            cD.out_up_2_EbNocalc = cD.up_2_margin + cD.up_2_EbNo - cD.up_2_implementationloss
            cD.out_up_2_margin = cD.up_2_margin
            cD.out_up_2_datarate2 = m.log10(cD.up_2_datarate)*10
            cD.out_up_2_datarate = cD.up_2_datarate
            cD.out_up_2_powerdensity = cD.out_up_2_EbNocalc + cD.out_up_2_datarate2
            cD.out_up_2_transmitterpower2 = cD.out_up_2_powerdensity - cD.up_2_lineloss - cD.out_up_2_transmitterantgain - cD.out_up_2_receiversensitivity + boltzman - (cD.up_2_spaceloss + cD.up_2_transmitterpointingloss + cD.up_2_polarizationloss + cD.up_2_atmosphereattenuation + cD.up_2_rainattenuation + cD.up_2_receiverpointingloss)
            cD.out_up_2_transmitterpower = 10**(cD.out_up_2_transmitterpower2/10)
            cD.out_up_2_eirp = cD.out_up_2_transmitterpower2 + cD.up_2_lineloss + cD.out_up_2_transmitterantgain
            
        if down_1_missing == 1 : 
            cD.out_down_1_EbNocalc = cD.down_1_margin + cD.down_1_EbNo - cD.down_1_implementationloss
            cD.out_down_1_margin = cD.down_1_margin
            cD.out_down_1_datarate2 = m.log10(cD.down_1_datarate)*10
            cD.out_down_1_datarate = cD.down_1_datarate
            cD.out_down_1_powerdensity = cD.out_down_1_EbNocalc + cD.out_down_1_datarate2
            cD.out_down_1_transmitterpower2 = cD.out_down_1_powerdensity - cD.down_1_lineloss - cD.out_down_1_transmitterantgain - cD.out_down_1_receiversensitivity + boltzman - (cD.down_1_spaceloss + cD.down_1_transmitterpointingloss + cD.down_1_polarizationloss + cD.down_1_atmosphereattenuation + cD.down_1_rainattenuation + cD.down_1_receiverpointingloss)
            cD.out_down_1_transmitterpower = 10**(cD.out_down_1_transmitterpower2/10)
            cD.out_down_1_eirp = cD.out_down_1_transmitterpower2 + cD.down_1_lineloss + cD.out_down_1_transmitterantgain
            
        if down_2_missing == 1 : 
            cD.out_down_2_EbNocalc = cD.down_2_margin + cD.down_2_EbNo - cD.down_2_implementationloss
            cD.out_down_2_margin = cD.down_2_margin
            cD.out_down_2_datarate2 = m.log10(cD.down_2_datarate)*10
            cD.out_down_2_datarate = cD.down_2_datarate
            cD.out_down_2_powerdensity = cD.out_down_2_EbNocalc + cD.out_down_2_datarate2
            cD.out_down_2_transmitterpower2 = cD.out_down_2_powerdensity - cD.down_2_lineloss - cD.out_down_2_transmitterantgain - cD.out_down_2_receiversensitivity + boltzman - (cD.down_2_spaceloss + cD.down_2_transmitterpointingloss + cD.down_2_polarizationloss + cD.down_2_atmosphereattenuation + cD.down_2_rainattenuation + cD.down_2_receiverpointingloss)
            cD.out_down_2_transmitterpower = 10**(cD.out_down_2_transmitterpower2/10)
            cD.out_down_2_eirp = cD.out_down_2_transmitterpower2 + cD.down_2_lineloss + cD.out_down_2_transmitterantgain
            

        if up_1_missing == 2 : 
            cD.out_up_1_EbNocalc = cD.up_1_margin + cD.up_1_EbNo - cD.up_1_implementationloss
            cD.out_up_1_margin = cD.up_1_margin
            cD.out_up_1_transmitterpower2 = m.log10(cD.up_1_transmitterpower)*10
            cD.out_up_1_transmitterpower = cD.up_1_transmitterpower 
            cD.out_up_1_eirp = cD.out_up_1_transmitterpower2 + cD.up_1_lineloss + cD.out_up_1_transmitterantgain
            cD.out_up_1_powerdensity = cD.out_up_1_eirp + cD.up_1_spaceloss + cD.up_1_transmitterpointingloss + cD.up_1_polarizationloss + cD.up_1_atmosphereattenuation + cD.up_1_rainattenuation + cD.up_1_receiverpointingloss - boltzman + cD.out_up_1_receiversensitivity
            cD.out_up_1_datarate2 = cD.out_up_1_powerdensity - cD.out_up_1_EbNocalc 
            cD.out_up_1_datarate = 10**(cD.out_up_1_datarate2/10)

        if up_2_missing == 2 : 
            cD.out_up_2_EbNocalc = cD.up_2_margin + cD.up_2_EbNo - cD.up_2_implementationloss
            cD.out_up_2_margin = cD.up_2_margin
            cD.out_up_2_transmitterpower2 = m.log10(cD.up_2_transmitterpower)*10
            cD.out_up_2_transmitterpower = cD.up_2_transmitterpower 
            cD.out_up_2_eirp = cD.out_up_2_transmitterpower2 + cD.up_2_lineloss + cD.out_up_2_transmitterantgain
            cD.out_up_2_powerdensity = cD.out_up_2_eirp + cD.up_2_spaceloss + cD.up_2_transmitterpointingloss + cD.up_2_polarizationloss + cD.up_2_atmosphereattenuation + cD.up_2_rainattenuation + cD.up_2_receiverpointingloss - boltzman + cD.out_up_2_receiversensitivity
            cD.out_up_2_datarate2 = cD.out_up_2_powerdensity - cD.out_up_2_EbNocalc 
            cD.out_up_2_datarate = 10**(cD.out_up_2_datarate2/10)

        if down_1_missing == 2 : 
            cD.out_down_1_EbNocalc = cD.down_1_margin + cD.down_1_EbNo - cD.down_1_implementationloss
            cD.out_down_1_margin = cD.down_1_margin
            cD.out_down_1_transmitterpower2 = m.log10(cD.down_1_transmitterpower)*10
            cD.out_down_1_transmitterpower = cD.down_1_transmitterpower 
            cD.out_down_1_eirp = cD.out_down_1_transmitterpower2 + cD.down_1_lineloss + cD.out_down_1_transmitterantgain
            cD.out_down_1_powerdensity = cD.out_down_1_eirp + cD.down_1_spaceloss + cD.down_1_transmitterpointingloss + cD.down_1_polarizationloss + cD.down_1_atmosphereattenuation + cD.down_1_rainattenuation + cD.down_1_receiverpointingloss - boltzman + cD.out_down_1_receiversensitivity
            cD.out_down_1_datarate2 = cD.out_down_1_powerdensity - cD.out_down_1_EbNocalc 
            cD.out_down_1_datarate = 10**(cD.out_down_1_datarate2/10)

        if down_2_missing == 2 : 
            cD.out_down_2_EbNocalc = cD.down_2_margin + cD.down_2_EbNo - cD.down_2_implementationloss
            cD.out_down_2_margin = cD.down_2_margin
            cD.out_down_2_transmitterpower2 = m.log10(cD.down_2_transmitterpower)*10
            cD.out_down_2_transmitterpower = cD.down_2_transmitterpower 
            cD.out_down_2_eirp = cD.out_down_2_transmitterpower2 + cD.down_2_lineloss + cD.out_down_2_transmitterantgain
            cD.out_down_2_powerdensity = cD.out_down_2_eirp + cD.down_2_spaceloss + cD.down_2_transmitterpointingloss + cD.down_2_polarizationloss + cD.down_2_atmosphereattenuation + cD.down_2_rainattenuation + cD.down_2_receiverpointingloss - boltzman + cD.out_down_2_receiversensitivity
            cD.out_down_2_datarate2 = cD.out_down_2_powerdensity - cD.out_down_2_EbNocalc 
            cD.out_down_2_datarate = 10**(cD.out_down_2_datarate2/10)


        if up_1_missing == 3 : 
            cD.out_up_1_datarate2 = m.log10(cD.up_1_datarate)*10 
            cD.out_up_1_datarate = cD.up_1_datarate
            cD.out_up_1_transmitterpower2 = m.log10(cD.up_1_transmitterpower)*10 
            cD.out_up_1_transmitterpower = cD.up_1_transmitterpower 
            cD.out_up_1_eirp = cD.out_up_1_transmitterpower2 + cD.up_1_lineloss + cD.out_up_1_transmitterantgain
            cD.out_up_1_powerdensity = cD.out_up_1_eirp + cD.up_1_spaceloss + cD.up_1_transmitterpointingloss + cD.up_1_polarizationloss + cD.up_1_atmosphereattenuation + cD.up_1_rainattenuation + cD.up_1_receiverpointingloss - boltzman + cD.out_up_1_receiversensitivity
            cD.out_up_1_EbNocalc = cD.out_up_1_powerdensity - cD.out_up_1_datarate2
            cD.out_up_1_margin = cD.out_up_1_EbNocalc - cD.up_1_EbNo + cD.up_1_implementationloss

        if up_2_missing == 3 : 
            cD.out_up_2_datarate2 = m.log10(cD.up_2_datarate)*10
            cD.out_up_2_datarate = cD.up_2_datarate
            cD.out_up_2_transmitterpower2 = m.log10(cD.up_2_transmitterpower)*10 
            cD.out_up_2_transmitterpower = cD.up_2_transmitterpower 
            cD.out_up_2_eirp = cD.out_up_2_transmitterpower2 + cD.up_2_lineloss + cD.out_up_2_transmitterantgain 
            cD.out_up_2_powerdensity = cD.out_up_2_eirp + cD.up_2_spaceloss + cD.up_2_transmitterpointingloss + cD.up_2_polarizationloss + cD.up_2_atmosphereattenuation + cD.up_2_rainattenuation + cD.up_2_receiverpointingloss - boltzman + cD.out_up_2_receiversensitivity
            cD.out_up_2_EbNocalc = cD.out_up_2_powerdensity - cD.out_up_2_datarate2
            cD.out_up_2_margin = cD.out_up_2_EbNocalc - cD.up_2_EbNo + cD.up_2_implementationloss

        if down_1_missing == 3 : 
            cD.out_down_1_datarate2 = m.log10(cD.down_1_datarate)*10
            cD.out_down_1_datarate = cD.down_1_datarate
            cD.out_down_1_transmitterpower2 = m.log10(cD.down_1_transmitterpower)*10 
            cD.out_down_1_transmitterpower = cD.down_1_transmitterpower 
            cD.out_down_1_eirp = cD.out_down_1_transmitterpower2 + cD.down_1_lineloss + cD.out_down_1_transmitterantgain
            cD.out_down_1_powerdensity = cD.out_down_1_eirp + cD.down_1_spaceloss + cD.down_1_transmitterpointingloss + cD.down_1_polarizationloss + cD.down_1_atmosphereattenuation + cD.down_1_rainattenuation + cD.down_1_receiverpointingloss - boltzman + cD.out_down_1_receiversensitivity
            cD.out_down_1_EbNocalc = cD.out_down_1_powerdensity - cD.out_down_1_datarate2
            cD.out_down_1_margin = cD.out_down_1_EbNocalc - cD.down_1_EbNo + cD.down_1_implementationloss

        if down_2_missing == 3 : 
            cD.out_down_2_datarate2 = m.log10(cD.down_2_datarate)*10
            cD.out_down_2_datarate = cD.down_2_datarate
            cD.out_down_2_transmitterpower2 = m.log10(cD.down_2_transmitterpower)*10 
            cD.out_down_2_transmitterpower = cD.down_2_transmitterpower 
            cD.out_down_2_eirp = cD.out_down_2_transmitterpower2 + cD.down_2_lineloss + cD.out_down_2_transmitterantgain 
            cD.out_down_2_powerdensity = cD.out_down_2_eirp + cD.down_2_spaceloss + cD.down_2_transmitterpointingloss + cD.down_2_polarizationloss + cD.down_2_atmosphereattenuation + cD.down_2_rainattenuation + cD.down_2_receiverpointingloss - boltzman + cD.out_down_2_receiversensitivity if secondary else 0
            cD.out_down_2_EbNocalc = cD.out_down_2_powerdensity - cD.out_down_2_datarate2 
            cD.out_down_2_margin = cD.out_down_2_EbNocalc - cD.down_2_EbNo + cD.down_2_implementationloss
        
        return cD

    def writeData(self, cD):
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
                            cD.out_up_p_EbNo,
                            cD.out_up_s_EbNo,
                            cD.out_down_p_EbNo,
                            cD.out_down_s_EbNo,
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
            for row in range(1,length):
                paramWriter.writerow([self.var[row],self.var_name[row],self.dataList[row-1],self.units[row]])

    
    def writeData2(self, cD):
        with open('outputCommsParameters.csv', mode='w', newline='') as parameters:
            paramWriter = csv.writer(parameters, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            self.dataList = [self.data[1],
                            cD.out_up_1_frequency,
                            cD.out_up_2_frequency,
                            cD.out_down_1_frequency,
                            cD.out_down_2_frequency,
                            cD.out_up_1_transmitterpower,
                            cD.out_up_2_transmitterpower,
                            cD.out_down_1_transmitterpower,
                            cD.out_down_2_transmitterpower,
                            cD.out_up_1_transmitterpower2,
                            cD.out_up_2_transmitterpower2,
                            cD.out_down_1_transmitterpower2,
                            cD.out_down_2_transmitterpower2,
                            cD.out_up_1_transmitterantgain,
                            cD.out_up_2_transmitterantgain,
                            cD.out_down_1_transmitterantgain,
                            cD.out_down_2_transmitterantgain,
                            cD.out_up_1_transmitterefficiency,
                            cD.out_up_2_transmitterefficiency,
                            cD.out_down_1_transmitterefficiency,
                            cD.out_down_2_transmitterefficiency,
                            cD.out_up_1_transmitterdishdiameter,
                            cD.out_up_2_transmitterdishdiameter,
                            cD.out_down_1_transmitterdishdiameter,
                            cD.out_down_2_transmitterdishdiameter,
                            cD.out_up_1_beamwidth,
                            cD.out_up_2_beamwidth,
                            cD.out_down_1_beamwidth,
                            cD.out_down_2_beamwidth,
                            cD.out_up_1_eirp,
                            cD.out_up_2_eirp,
                            cD.out_down_1_eirp,
                            cD.out_down_2_eirp,
                            cD.out_up_1_spaceloss,
                            cD.out_up_2_spaceloss,
                            cD.out_down_1_spaceloss,
                            cD.out_down_2_spaceloss,
                            cD.out_up_1_atmosphereattenuation,
                            cD.out_up_2_atmosphereattenuation,
                            cD.out_down_1_atmosphereattenuation,
                            cD.out_down_2_atmosphereattenuation,
                            cD.out_up_1_receiverdishdiameter,
                            cD.out_up_2_receiverdishdiameter,
                            cD.out_down_1_receiverdishdiameter,
                            cD.out_down_2_receiverdishdiameter,
                            cD.out_up_1_receiverefficiency,
                            cD.out_up_2_receiverefficiency,
                            cD.out_down_1_receiverefficiency,
                            cD.out_down_2_receiverefficiency,
                            cD.out_up_1_receiverantgain,
                            cD.out_up_2_receiverantgain,
                            cD.out_down_1_receiverantgain,
                            cD.out_down_2_receiverantgain,
                            cD.out_up_1_systemtemp,
                            cD.out_up_2_systemtemp,
                            cD.out_down_1_systemtemp,
                            cD.out_down_2_systemtemp,
                            cD.out_up_1_systemtemp2,
                            cD.out_up_2_systemtemp2,
                            cD.out_down_1_systemtemp2,
                            cD.out_down_2_systemtemp2,
                            cD.out_up_1_receiversensitivity,
                            cD.out_up_2_receiversensitivity,
                            cD.out_down_1_receiversensitivity,
                            cD.out_down_2_receiversensitivity,
                            cD.out_up_1_powerdensity,
                            cD.out_up_2_powerdensity,
                            cD.out_down_1_powerdensity,
                            cD.out_down_2_powerdensity,
                            cD.out_up_1_EbNo,
                            cD.out_up_2_EbNo,
                            cD.out_down_1_EbNo,
                            cD.out_down_2_EbNo,
                            cD.out_up_1_EbNocalc,
                            cD.out_up_2_EbNocalc,
                            cD.out_down_1_EbNocalc,
                            cD.out_down_2_EbNocalc,
                            cD.out_up_1_datarate,
                            cD.out_up_2_datarate,
                            cD.out_down_1_datarate,
                            cD.out_down_2_datarate,
                            cD.out_up_1_datarate2,
                            cD.out_up_2_datarate2,
                            cD.out_down_1_datarate2,
                            cD.out_down_2_datarate2,
                            cD.out_up_1_margin,
                            cD.out_up_2_margin,
                            cD.out_down_1_margin,
                            cD.out_down_2_margin]
            length = len(self.data)
            for row in range(1,length):
                paramWriter.writerow([self.var[row],self.var_name[row],self.dataList[row-1],self.units[row]])