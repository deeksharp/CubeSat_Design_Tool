import csv
import math as m

class CommsTool:
    def __init__(self):
        pass
                
    def LinkBudget4Demo_case1(self,cD):
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
        cD.out_up_p_EbNo = cD.up_p_EbNo
        cD.out_up_s_EbNo = cD.up_s_EbNo
        cD.out_down_p_EbNo = cD.down_p_EbNo
        cD.out_down_s_EbNo = cD.down_s_EbNo
        cD.out_up_systemp = m.log10(cD.up_systemp)*10 if cD.up_systemp > 0 else 0 #aka Noise temp
        cD.out_down_systemp = m.log10(cD.down_systemp)*10 if cD.down_systemp > 0 else 0
        cD.out_up_p_pathloss = m.log10(4*3.14*cD.up_maxdistanceEarth*cD.up_p_frequency/300000000)*20 if cD.up_maxdistanceEarth > 0 and cD.up_p_frequency > 0 else 0
        cD.out_up_s_pathloss = m.log10(4*3.14*cD.up_maxdistanceEarth*cD.up_s_frequency/300000000)*20 if cD.up_maxdistanceEarth > 0 and cD.up_s_frequency > 0 else 0
        cD.out_down_p_pathloss = m.log10(4*3.14*cD.down_maxdistanceEarth*cD.down_p_frequency/300000000)*20 if cD.down_maxdistanceEarth > 0 and cD.down_p_frequency > 0 else 0
        cD.out_down_s_pathloss = m.log10(4*3.14*cD.down_maxdistanceEarth*cD.down_s_frequency/300000000)*20 if cD.down_maxdistanceEarth > 0 and cD.down_s_frequency > 0 else 0
        cD.out_up_otherloss = cD.up_rainloss + cD.up_lineloss + cD.up_otherloss
        cD.out_down_otherloss = cD.down_rainloss + cD.down_lineloss + cD.down_otherloss
        cD.out_up_p_margin = cD.out_up_p_gs_transpower + cD.out_up_p_gs_antgain + cD.out_up_p_sc_antgain + 228.6 - cD.out_up_p_EbNo - cD.out_up_p_datarate - cD.out_up_systemp - cD.out_up_p_pathloss - cD.out_up_otherloss
        cD.out_up_s_margin = cD.out_up_s_gs_transpower + cD.out_up_s_gs_antgain + cD.out_up_s_sc_antgain + 228.6 - cD.out_up_s_EbNo - cD.out_up_s_datarate - cD.out_up_systemp - cD.out_up_s_pathloss - cD.out_up_otherloss
        cD.out_down_p_margin = cD.out_down_p_sc_transpower + cD.out_down_p_sc_antgain + cD.out_down_p_gs_antgain + 228.6 - cD.out_down_p_EbNo - cD.out_down_p_datarate - cD.out_down_systemp - cD.out_down_p_pathloss - cD.out_down_otherloss
        cD.out_down_s_margin = cD.out_down_s_sc_transpower + cD.out_down_s_sc_antgain + cD.out_down_s_gs_antgain + 228.6 - cD.out_down_s_EbNo - cD.out_down_s_datarate - cD.out_down_systemp - cD.out_down_s_pathloss - cD.out_down_otherloss

        return cD

    def LinkBudget4Demo_case2(self,cD):
        #CSV FILE READ
        print("start open csv comms file")
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


        secondary = True if cD.up_2_datarate > 0 or cD.up_2_transmitterpower > 0 else False 
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
        cD.out_up_1_receiverantgain = m.log10(cD.up_1_receiverdishdiameter)*20 + m.log10(cD.up_1_frequency)*20 + m.log10(cD.up_1_receiverefficiency)*10 - 159.59
        cD.out_up_2_receiverantgain = m.log10(cD.up_2_receiverdishdiameter)*20 + m.log10(cD.up_2_frequency)*20 + m.log10(cD.up_2_receiverefficiency)*10 - 159.59 if secondary else 0
        cD.out_down_1_receiverantgain = m.log10(cD.down_1_receiverdishdiameter)*20 + m.log10(cD.down_1_frequency)*20 + m.log10(cD.down_1_receiverefficiency)*10 - 159.59
        cD.out_down_2_receiverantgain = m.log10(cD.down_2_receiverdishdiameter)*20 + m.log10(cD.down_2_frequency)*20 + m.log10(cD.down_2_receiverefficiency)*10 - 159.59 if secondary else 0
        cD.out_up_1_systemtemp = cD.up_1_systemtemp
        cD.out_up_2_systemtemp = cD.up_2_systemtemp if secondary else 0
        cD.out_down_1_systemtemp = cD.down_1_systemtemp
        cD.out_down_2_systemtemp = cD.down_2_systemtemp if secondary else 0
        cD.out_up_1_systemtemp2 = m.log10(cD.up_1_systemtemp)*10
        cD.out_up_2_systemtemp2 = m.log10(cD.up_2_systemtemp)*10 if secondary else 0
        cD.out_down_1_systemtemp2 = m.log10(cD.down_1_systemtemp)*10
        cD.out_down_2_systemtemp2 = m.log10(cD.down_2_systemtemp)*10 if secondary else 0
        cD.out_up_1_receiversensitivity = cD.out_up_1_receiverantgain - cD.out_up_1_systemtemp2
        cD.out_up_2_receiversensitivity = cD.out_up_2_receiverantgain - cD.out_up_2_systemtemp2 if secondary else 0
        cD.out_down_1_receiversensitivity = cD.out_down_1_receiverantgain - cD.out_down_1_systemtemp2
        cD.out_down_2_receiversensitivity = cD.out_down_2_receiverantgain - cD.out_down_2_systemtemp2 if secondary else 0
        
        cD.out_up_1_datarate2 = 0
        cD.out_up_2_datarate2 = 0
        cD.out_down_1_datarate2 = 0
        cD.out_down_2_datarate2 = 0
        cD.out_up_2_transmitterpower2 = 0
        cD.out_down_2_transmitterpower2 = 0
        cD.out_up_2_transmitterpower = 0
        cD.out_down_2_transmitterpower = 0
        cD.out_up_1_datarate = 0
        cD.out_up_2_datarate = 0
        cD.out_down_1_datarate = 0
        cD.out_down_2_datarate = 0


        if cD.up_1_datarate > 0 : 
            cD.out_up_1_datarate2 = m.log10(cD.up_1_datarate)*10
        if cD.up_2_datarate > 0 : 
            cD.out_up_2_datarate2 = m.log10(cD.up_2_datarate)*10
        if cD.down_1_datarate > 0 : 
            cD.out_down_1_datarate2 = m.log10(cD.down_1_datarate)*10
        if cD.down_2_datarate > 0 : 
            cD.out_down_2_datarate2 = m.log10(cD.down_2_datarate)*10
        
        cD.out_up_1_transmitterpower2 = m.log10(cD.up_1_transmitterpower)*10 if cD.up_1_transmitterpower > 0 else cD.up_1_EbNo + cD.out_up_1_datarate2 + cD.out_up_1_systemtemp2 + boltzman - cD.out_up_1_receiverantgain - cD.out_up_1_transmitterantgain - (cD.up_1_spaceloss + cD.up_1_transmitterpointingloss + cD.up_1_polarizationloss + cD.up_1_atmosphereattenuation + cD.up_1_rainattenuation + cD.up_1_receiverpointingloss)
        cD.out_down_1_transmitterpower2 = m.log10(cD.down_1_transmitterpower)*10 if cD.down_1_transmitterpower > 0 else cD.down_1_EbNo + cD.out_down_1_datarate2 + cD.out_down_1_systemtemp2 + boltzman - cD.out_down_1_receiverantgain - cD.out_down_1_transmitterantgain - (cD.down_1_spaceloss + cD.down_1_transmitterpointingloss + cD.down_1_polarizationloss + cD.down_1_atmosphereattenuation + cD.down_1_rainattenuation + cD.down_1_receiverpointingloss)
        cD.out_up_1_transmitterpower = cD.up_1_transmitterpower if cD.up_1_transmitterpower > 0 else 10**(cD.out_up_1_transmitterpower2/10)
        cD.out_down_1_transmitterpower = cD.down_1_transmitterpower if cD.down_1_transmitterpower > 0 else 10**(cD.out_down_1_transmitterpower2/10)
        
        if secondary : 
            cD.out_up_2_transmitterpower2 = m.log10(cD.up_2_transmitterpower)*10 if cD.up_2_transmitterpower > 0 else cD.up_2_EbNo + cD.out_up_2_datarate2 + cD.out_up_2_systemtemp2 + boltzman - cD.out_up_2_receiverantgain - cD.out_up_2_transmitterantgain - (cD.up_2_spaceloss + cD.up_2_transmitterpointingloss + cD.up_2_polarizationloss + cD.up_2_atmosphereattenuation + cD.up_2_rainattenuation + cD.up_2_receiverpointingloss)
            cD.out_down_2_transmitterpower2 = m.log10(cD.down_2_transmitterpower)*10 if cD.down_2_transmitterpower > 0 else cD.down_2_EbNo + cD.out_down_2_datarate2 + cD.out_down_2_systemtemp2 + boltzman - cD.out_down_2_receiverantgain - cD.out_down_2_transmitterantgain - (cD.down_2_spaceloss + cD.down_2_transmitterpointingloss + cD.down_2_polarizationloss + cD.down_2_atmosphereattenuation + cD.down_2_rainattenuation + cD.down_2_receiverpointingloss)
            cD.out_up_2_transmitterpower = cD.up_2_transmitterpower if cD.up_2_transmitterpower > 0 else 10**(cD.out_up_2_transmitterpower2/10)
            cD.out_down_2_transmitterpower = cD.down_2_transmitterpower if cD.down_2_transmitterpower > 0 else 10**(cD.out_down_2_transmitterpower2/10)
    

        cD.out_up_1_eirp = cD.out_up_1_transmitterpower2 + cD.up_1_lineloss + cD.out_up_1_transmitterantgain
        cD.out_up_2_eirp = cD.out_up_2_transmitterpower2 + cD.up_2_lineloss + cD.out_up_2_transmitterantgain if secondary else 0
        cD.out_down_1_eirp = cD.out_down_1_transmitterpower2 + cD.down_1_lineloss + cD.out_up_1_transmitterantgain
        cD.out_down_2_eirp = cD.out_down_2_transmitterpower2 + cD.down_2_lineloss + cD.out_down_2_transmitterantgain if secondary else 0
        cD.out_up_1_powerdensity = cD.out_up_1_eirp + cD.up_1_spaceloss + cD.up_1_transmitterpointingloss + cD.up_1_polarizationloss + cD.up_1_atmosphereattenuation + cD.up_1_rainattenuation + cD.up_1_receiverpointingloss - boltzman + cD.out_up_1_transmitterantgain
        cD.out_up_2_powerdensity = cD.out_up_2_eirp + cD.up_2_spaceloss + cD.up_2_transmitterpointingloss + cD.up_2_polarizationloss + cD.up_2_atmosphereattenuation + cD.up_2_rainattenuation + cD.up_2_receiverpointingloss - boltzman + cD.out_up_2_transmitterantgain if secondary else 0
        cD.out_down_1_powerdensity = cD.out_down_1_eirp + cD.down_1_spaceloss + cD.down_1_transmitterpointingloss + cD.down_1_polarizationloss + cD.down_1_atmosphereattenuation + cD.down_1_rainattenuation + cD.down_1_receiverpointingloss - boltzman + cD.out_down_1_transmitterantgain
        cD.out_down_2_powerdensity = cD.out_down_2_eirp + cD.down_2_spaceloss + cD.down_2_transmitterpointingloss + cD.down_2_polarizationloss + cD.down_2_atmosphereattenuation + cD.down_2_rainattenuation + cD.down_2_receiverpointingloss - boltzman + cD.out_down_2_transmitterantgain if secondary else 0
        cD.out_up_1_datarate2 = m.log10(cD.up_1_datarate)*10 if cD.up_1_datarate > 0 else cD.out_up_1_eirp + cD.up_1_spaceloss + cD.up_1_transmitterpointingloss + cD.up_1_polarizationloss + cD.up_1_atmosphereattenuation + cD.up_1_rainattenuation + cD.up_1_receiverpointingloss + cD.out_up_1_receiverantgain - cD.up_1_EbNo - cD.out_up_1_systemtemp2 - boltzman + cD.out_up_1_receiverantgain
        cD.out_down_1_datarate2 = m.log10(cD.down_1_datarate)*10 if cD.down_1_datarate > 0 else cD.out_down_1_eirp + cD.down_1_spaceloss + cD.down_1_transmitterpointingloss + cD.down_1_polarizationloss + cD.down_1_atmosphereattenuation + cD.down_1_rainattenuation + cD.down_1_receiverpointingloss + cD.out_down_1_receiverantgain - cD.down_1_EbNo - cD.out_down_1_systemtemp2 - boltzman + cD.out_down_1_receiverantgain
        cD.out_up_1_datarate = cD.up_1_datarate if cD.up_1_datarate > 0 else 10**(cD.out_up_1_datarate2/10)
        cD.out_down_1_datarate = cD.down_1_datarate if cD.down_1_datarate > 0 else 10**(cD.out_down_1_datarate2/10)

        if secondary : 
            cD.out_up_2_datarate2 = m.log10(cD.up_2_datarate)*10 if cD.up_2_datarate > 0 else cD.out_up_2_eirp + cD.up_2_spaceloss + cD.up_2_transmitterpointingloss + cD.up_2_polarizationloss + cD.up_2_atmosphereattenuation + cD.up_2_rainattenuation + cD.up_2_receiverpointingloss + cD.out_up_2_receiverantgain - cD.up_2_EbNo - cD.out_up_2_systemtemp2 - boltzman + cD.out_up_2_receiverantgain
            cD.out_down_2_datarate2 = m.log10(cD.down_2_datarate)*10 if cD.down_2_datarate > 0 else cD.out_down_2_eirp + cD.down_2_spaceloss + cD.down_2_transmitterpointingloss + cD.down_2_polarizationloss + cD.down_2_atmosphereattenuation + cD.down_2_rainattenuation + cD.down_2_receiverpointingloss + cD.out_down_2_receiverantgain - cD.down_2_EbNo - cD.out_down_2_systemtemp2 - boltzman + cD.out_down_2_receiverantgain
            cD.out_up_2_datarate = cD.up_2_datarate if cD.up_2_datarate > 0 else 10**(cD.out_up_2_datarate2/10)
            cD.out_down_2_datarate = cD.down_2_datarate if cD.down_2_datarate > 0 else 10**(cD.out_down_2_datarate2/10)

        cD.out_up_1_EbNocalc = cD.out_up_1_powerdensity - cD.out_up_1_datarate2
        cD.out_up_2_EbNocalc = cD.out_up_2_powerdensity - cD.out_up_2_datarate2 if secondary else 0
        cD.out_down_1_EbNocalc = cD.out_down_1_powerdensity - cD.out_down_1_datarate2
        cD.out_down_2_EbNocalc = cD.out_down_2_powerdensity - cD.out_down_2_datarate2 if secondary else 0
        cD.out_up_1_margin = cD.out_up_1_EbNocalc - cD.up_1_EbNo
        cD.out_up_2_margin = cD.out_up_2_EbNocalc - cD.up_2_EbNo if secondary else 0
        cD.out_down_1_margin = cD.out_down_1_EbNocalc - cD.down_1_EbNo
        cD.out_down_2_margin = cD.out_down_2_EbNocalc - cD.down_2_EbNo if secondary else 0

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