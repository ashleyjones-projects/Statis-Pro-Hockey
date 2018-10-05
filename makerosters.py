# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:17:37 2017

@author: w9641432
"""

def make_rosters(penbox,line_seq,Linhf,Linhd,Linvf,Linvd):
    
            # LOAD LINEUP FOR HOME TEAM
    inpath='C:/Users/w9641432/Documents/Work/Python_learning/StatisproHockey/teams/'
    
    ph_lines=[]
    
    f = open(inpath+'lineup.csv','r')
    for line in f:
        
        cells = line.split(",")
        ph_lines.append((cells[0],cells[1],cells[2],cells[3]))
    f.close()
    
    
    
     # LOAD LINEUP FOR AWAY TEAM
    inpath='C:/Users/w9641432/Documents/Work/Python_learning/StatisproHockey/teams/'
    
    pv_lines=[]
    
    f = open(inpath+'lineup.csv','r')
    for line in f:
        
        cells = line.split(",")
        pv_lines.append((cells[0],cells[1],cells[2],cells[3]))
    f.close()
    
    ##########################################################################
    #MAKE HOME TEAM
    
    rosth = {"LWH1":ph_lines[0][0],"CH1":ph_lines[0][1],"RWH1":ph_lines[0][2],
             "LWH2":ph_lines[1][0],"CH2":ph_lines[1][1],"RWH2":ph_lines[1][2],
              "LWH3":ph_lines[2][0],"CH3":ph_lines[2][1],"RWH3":ph_lines[2][2],
              "LWH4":ph_lines[3][0],"CH4":ph_lines[3][1],"RWH4":ph_lines[3][2],
              "LDH1":ph_lines[4][0],"RDH1":ph_lines[4][1],
              "LDH2":ph_lines[5][0],"RDH2":ph_lines[5][1],
              "LDH3":ph_lines[6][0],"RDH3":ph_lines[6][1],
              "GH1":ph_lines[8][0],"GH2":ph_lines[9][0],
                            # PP 5V4
              "5LWH1":ph_lines[11][0],"5CH1":ph_lines[11][1],"5RWH1":ph_lines[11][2],
              "5LWH2":ph_lines[12][0],"5CH2":ph_lines[12][1],"5RWH2":ph_lines[12][2],
              "5LDH1":ph_lines[13][0],"5RDH1":ph_lines[13][1],
              "5LDH2":ph_lines[14][0],"5RDH2":ph_lines[14][1],
                            # PK 5V4
              "4KLWH1":ph_lines[16][0],"4KCH1":ph_lines[16][1],
              "4KLWH2":ph_lines[17][0],"4KCH2":ph_lines[17][1],                 
              "4KLDH1":ph_lines[18][0],"4KRDH1":ph_lines[18][1],
              "4KLDH2":ph_lines[19][0],"4KRDH2":ph_lines[19][1],
                            # PP 4V3 OR 4V4
              "4LWH1":ph_lines[21][0],"4CH1":ph_lines[21][1],
              "4LWH2":ph_lines[22][0],"4CH2":ph_lines[22][1],                 
              "4LDH1":ph_lines[23][0],"4RDH1":ph_lines[23][1],
              "4LDH2":ph_lines[24][0],"4RDH2":ph_lines[24][1],
                            # PK 4V3   
              "3KLDH1":ph_lines[27][0],"3KCH1":ph_lines[26][1],"3KRDH1":ph_lines[27][1],
              "3KLDH2":ph_lines[29][0],"3KCH2":ph_lines[28][1],"3KRDH2":ph_lines[29][1], 
                            # 3V3
              "3LWH1":ph_lines[31][0],"3CH1":ph_lines[31][1],"3LDH1":ph_lines[32][0],
              "3LWH2":ph_lines[33][0],"3CH2":ph_lines[33][1],"3LDH2":ph_lines[34][0], 
              "3LWH3":ph_lines[35][0],"3CH3":ph_lines[35][1],"3LDH3":ph_lines[36][0],
                            # EXTRAMEN OFF
              "EXFH1":ph_lines[0][0],"EXFH2":ph_lines[0][1],"EXFH3":ph_lines[0][2],
              "EXFH4":ph_lines[1][0],"EXFH5":ph_lines[1][1],"EXFH6":ph_lines[1][2],
                            # EXTRAMEN DEF
              "EXFBH1":ph_lines[2][0],"EXFBH2":ph_lines[2][1],"EXFBH3":ph_lines[2][2],
              "EXFBH4":ph_lines[3][0],"EXFBH5":ph_lines[3][1],"EXFBH6":ph_lines[3][2],             
                            # EXTRAS DEF  
              "EXHD1":ph_lines[4][0],"EXHD2":ph_lines[4][1],
              "EXHD3":ph_lines[5][0],"EXHD4":ph_lines[5][1],
              "EXHD5":ph_lines[6][0],"EXHD6":ph_lines[6][1],
              "NONE":"NONE"}               
    #MAKE VOME TEAM
    
    rostv = {"LWV1":pv_lines[0][0],"CV1":pv_lines[0][1],"RWV1":pv_lines[0][2],
             "LWV2":pv_lines[1][0],"CV2":pv_lines[1][1],"RWV2":pv_lines[1][2],
              "LWV3":pv_lines[2][0],"CV3":pv_lines[2][1],"RWV3":pv_lines[2][2],
              "LWV4":pv_lines[3][0],"CV4":pv_lines[3][1],"RWV4":pv_lines[3][2],
              "LDV1":pv_lines[4][0],"RDV1":pv_lines[4][1],
              "LDV2":pv_lines[5][0],"RDV2":pv_lines[5][1],
              "LDV3":pv_lines[6][0],"RDV3":pv_lines[6][1],
              "GV1":pv_lines[8][0],"GV2":pv_lines[9][0],
                            # PP 5V4
              "5LWV1":pv_lines[11][0],"5CV1":pv_lines[11][1],"5RWV1":pv_lines[11][2],
              "5LWV2":pv_lines[12][0],"5CV2":pv_lines[12][1],"5RWV2":pv_lines[12][2],
              "5LDV1":pv_lines[13][0],"5RDV1":pv_lines[13][1],
              "5LDV2":pv_lines[14][0],"5RDV2":pv_lines[14][1],
                            # PK 5V4
              "4KLWV1":pv_lines[16][0],"4KCV1":pv_lines[16][1],
              "4KLWV2":pv_lines[17][0],"4KCV2":pv_lines[17][1],                 
              "4KLDV1":pv_lines[18][0],"4KRDV1":pv_lines[18][1],
              "4KLDV2":pv_lines[19][0],"4KRDV2":pv_lines[19][1],
                            # PP 4V3 OR 4V4
              "4LWV1":pv_lines[21][0],"4CV1":pv_lines[21][1],
              "4LWV2":pv_lines[22][0],"4CV2":pv_lines[22][1],                 
              "4LDV1":pv_lines[23][0],"4RDV1":pv_lines[23][1],
              "4LDV2":pv_lines[24][0],"4RDV2":pv_lines[24][1],
                            # PK 4V3   
              "3KLDV1":pv_lines[27][0],"3KCV1":pv_lines[26][1],"3KRDV1":pv_lines[27][1],
              "3KLDV2":pv_lines[29][0],"3KCV2":pv_lines[28][1],"3KRDV2":pv_lines[29][1], 
                            # 3V3
              "3LWV1":pv_lines[31][0],"3CV1":pv_lines[31][1],"3LDV1":pv_lines[32][0],
              "3LWV2":pv_lines[33][0],"3CV2":pv_lines[33][1],"3LDV2":pv_lines[34][0], 
              "3LWV3":pv_lines[35][0],"3CV3":pv_lines[35][1],"3LDV3":pv_lines[36][0],
                            # Extras OFF
              "EXFV1":pv_lines[0][0],"EXFV2":pv_lines[0][1],"EXFV3":pv_lines[0][2],
              "EXFV4":pv_lines[1][0],"EXFV5":pv_lines[1][1],"EXFV6":pv_lines[1][2],
                              # EXTRAMEN DEF
              "EXFBV1":pv_lines[2][0],"EXFBV2":pv_lines[2][1],"EXFBV3":pv_lines[2][2],
              "EXFBV4":pv_lines[3][0],"EXFBV5":pv_lines[3][1],"EXFBV6":pv_lines[3][2],   
                            # EXTRAS DEF  
              "EXVD1":pv_lines[4][0],"EXVD2":pv_lines[4][1],
              "EXVD3":pv_lines[5][0],"EXVD4":pv_lines[5][1],
              "EXVD5":pv_lines[6][0],"EXVD6":pv_lines[6][1],
              "NONE":"NONE"} 

    namesh=[]
    
    if line_seq["PENH"]>0:
        
        pos = ['GH1','GH2','5LWH1','5CH1','5RWH1','5LWH2',
             '5CH2','5RWH2','5LDH1','5RDH1','5LDH2','5RDH2','4KLWH1','4KCH1','4KLWH2','4KCH2',
             '4KLDH1','4KRDH1','4KLDH2','4KRDH2','4LWH1','4CH1','4LWH2','4CH2','4LDH1','4RDH1',
             '4LDH2','4RDH2','3KLDH1','3KCH1','3KRDH1','3KLDH2','3KCH2','3KRDH2','3LWH1','3CH1',
             '3LDH1','3LWH2','3CH2','3LDH2','3LWH3','3CH3','3LDH3']
        
        if penbox["PEN_H_NAME1"] != "NONE":
            namesh.append(penbox["PEN_H_NAME1"])
        if penbox["PEN_H_NAME2"] != "NONE":
            namesh.append(penbox["PEN_H_NAME2"])    
        if penbox["PEN_H_NAME3"] != "NONE":
            namesh.append(penbox["PEN_H_NAME3"])    
        if penbox["PEN_H_NAME4"] != "NONE":
            namesh.append(penbox["PEN_H_NAME4"])    
        if penbox["PEN_H_NAME5"] != "NONE":
            namesh.append(penbox["PEN_H_NAME5"])
            
        for i in range(0,len(namesh)):
            for j in range(0,len(pos)):
                if namesh[i] in rosth[pos[j]]:
                    # NEED A REPLACEMENT!
                    pos1 = Linhf["HF"][0]; pos2 = Linhf["HF"][1]; pos3 = Linhf["HF"][2]
                    pos4 = Linhd["HD"][0]; pos5 = Linhd["HD"][1];
                    if "LW" in pos[j] or "C" in pos[j] or "RW" in pos[j]:
                        if rosth["EXFBH1"] not in namesh and rosth["EXFBH1"] not in rosth[pos1] and rosth["EXFBH1"] not in rosth[pos2] and rosth["EXFBH1"] not in rosth[pos3]:
                            rosth[pos[j]]=rosth["EXFBH1"]
                        elif rosth["EXFBH2"] not in namesh and rosth["EXFBH2"] not in rosth[pos1] and rosth["EXFBH2"] not in rosth[pos2] and rosth["EXFBH2"] not in rosth[pos3]:
                            rosth[pos[j]]=rosth["EXFBH2"]
                        elif rosth["EXFBH3"] not in namesh and rosth["EXFBH3"] not in rosth[pos1] and rosth["EXFBH3"] not in rosth[pos2] and rosth["EXFBH3"] not in rosth[pos3]:
                            rosth[pos[j]]=rosth["EXFBH3"]
                        elif rosth["EXFBH4"] not in namesh and rosth["EXFBH4"] not in rosth[pos1] and rosth["EXFBH4"] not in rosth[pos2] and rosth["EXFBH4"] not in rosth[pos3]:
                            rosth[pos[j]]=rosth["EXFBH4"]
                        elif rosth["EXFBH5"] not in namesh and rosth["EXFBH5"] not in rosth[pos1] and rosth["EXFBH5"] not in rosth[pos2] and rosth["EXFBH5"] not in rosth[pos3]:
                            rosth[pos[j]]=rosth["EXFBH5"]
                        elif rosth["EXFBH6"] not in namesh and rosth["EXFBH6"] not in rosth[pos1] and rosth["EXFBH6"] not in rosth[pos2] and rosth["EXFBH6"] not in rosth[pos3]:
                            rosth[pos[j]]=rosth["EXFBH6"] 
                    
                    elif "D" in pos[j]:
                        if rosth["EXHD1"] not in namesh and rosth["EXHD1"] not in rosth[pos4] and rosth["EXHD1"] not in rosth[pos5]:
                            rosth[pos[j]]=rosth["EXHD1"]
                        elif rosth["EXHD2"] not in namesh and rosth["EXHD2"] not in rosth[pos4] and rosth["EXHD2"] not in rosth[pos5]:
                            rosth[pos[j]]=rosth["EXHD2"]
                        elif rosth["EXHD3"] not in namesh and rosth["EXHD3"] not in rosth[pos4] and rosth["EXHD3"] not in rosth[pos5]:
                            rosth[pos[j]]=rosth["EXHD3"]
                        elif rosth["EXHD4"] not in namesh and rosth["EXHD4"] not in rosth[pos4] and rosth["EXHD4"] not in rosth[pos5]:
                            rosth[pos[j]]=rosth["EXHD4"]
                        elif rosth["EXHD5"] not in namesh and rosth["EXHD5"] not in rosth[pos4] and rosth["EXHD5"] not in rosth[pos5]:
                            rosth[pos[j]]=rosth["EXHD5"]
                        elif rosth["EXHD6"] not in namesh and rosth["EXHD6"] not in rosth[pos4] and rosth["EXHD6"] not in rosth[pos5]:
                            rosth[pos[j]]=rosth["EXHD6"] 
                        
                    
    namesv=[]
    
    if line_seq["PENV"]>0:
        
        pos = ['GV1','GV2','5LWV1','5CV1','5RWV1','5LWV2',
             '5CV2','5RWV2','5LDV1','5RDV1','5LDV2','5RDV2','4KLWV1','4KCV1','4KLWV2','4KCV2',
             '4KLDV1','4KRDV1','4KLDV2','4KRDV2','4LWV1','4CV1','4LWV2','4CV2','4LDV1','4RDV1',
             '4LDV2','4RDV2','3KLDV1','3KCV1','3KRDV1','3KLDV2','3KCV2','3KRDV2','3LWV1','3CV1',
             '3LDV1','3LWV2','3CV2','3LDV2','3LWV3','3CV3','3LDV3']
        
        if penbox["PEN_V_NAME1"] != "NONE":
            namesv.append(penbox["PEN_V_NAME1"])
        if penbox["PEN_V_NAME2"] != "NONE":
            namesv.append(penbox["PEN_V_NAME2"])    
        if penbox["PEN_V_NAME3"] != "NONE":
            namesv.append(penbox["PEN_V_NAME3"])    
        if penbox["PEN_V_NAME4"] != "NONE":
            namesv.append(penbox["PEN_V_NAME4"])    
        if penbox["PEN_V_NAME5"] != "NONE":
            namesv.append(penbox["PEN_V_NAME5"])
            
        for i in range(0,len(namesv)):
            for j in range(0,len(pos)):
                if namesv[i] in rostv[pos[j]]:
                    # NEED A REPLACEMENT!
                    pos1 = Linvf["VF"][0]; pos2 = Linvf["VF"][1]; pos3 = Linvf["VF"][2]
                    pos4 = Linvd["VD"][0]; pos5 = Linvd["VD"][1];
                    if "LW" in pos[j] or "C" in pos[j] or "RW" in pos[j]:
                        if rostv["EXFBV1"] not in namesv and rostv["EXFBV1"] not in rostv[pos1] and rostv["EXFBV1"] not in rostv[pos2] and rostv["EXFBV1"] not in rostv[pos3]:
                            rostv[pos[j]]=rostv["EXFBV1"]
                        elif rostv["EXFBV2"] not in namesv and rostv["EXFBV2"] not in rostv[pos1] and rostv["EXFBV2"] not in rostv[pos2] and rostv["EXFBV2"] not in rostv[pos3]:
                            rostv[pos[j]]=rostv["EXFBV2"]
                        elif rostv["EXFBV3"] not in namesv and rostv["EXFBV3"] not in rostv[pos1] and rostv["EXFBV3"] not in rostv[pos2] and rostv["EXFBV3"] not in rostv[pos3]:
                            rostv[pos[j]]=rostv["EXFBV3"]
                        elif rostv["EXFBV4"] not in namesv and rostv["EXFBV4"] not in rostv[pos1] and rostv["EXFBV4"] not in rostv[pos2] and rostv["EXFBV4"] not in rostv[pos3]:
                            rostv[pos[j]]=rostv["EXFBV4"]
                        elif rostv["EXFBV5"] not in namesv and rostv["EXFBV5"] not in rostv[pos1] and rostv["EXFBV5"] not in rostv[pos2] and rostv["EXFBV5"] not in rostv[pos3]:
                            rostv[pos[j]]=rostv["EXFBV5"]
                        elif rostv["EXFBV6"] not in namesv and rostv["EXFBV6"] not in rostv[pos1] and rostv["EXFBV6"] not in rostv[pos2] and rostv["EXFBV6"] not in rostv[pos3]:
                            rostv[pos[j]]=rostv["EXFBV6"] 
                    
                    elif "D" in pos[j]:
                        if rostv["EXVD1"] not in namesv and rostv["EXVD1"] not in rostv[pos4] and rostv["EXVD1"] not in rostv[pos5]:
                            rostv[pos[j]]=rostv["EXVD1"]
                        elif rostv["EXVD2"] not in namesv and rostv["EXVD2"] not in rostv[pos4] and rostv["EXVD2"] not in rostv[pos5]:
                            rostv[pos[j]]=rostv["EXVD2"]
                        elif rostv["EXVD3"] not in namesv and rostv["EXVD3"] not in rostv[pos4] and rostv["EXVD3"] not in rostv[pos5]:
                            rostv[pos[j]]=rostv["EXVD3"]
                        elif rostv["EXVD4"] not in namesv and rostv["EXVD4"] not in rostv[pos4] and rostv["EXVD4"] not in rostv[pos5]:
                            rostv[pos[j]]=rostv["EXVD4"]
                        elif rostv["EXVD5"] not in namesv and rostv["EXVD5"] not in rostv[pos4] and rostv["EXVD5"] not in rostv[pos5]:
                            rostv[pos[j]]=rostv["EXVD5"]
                        elif rostv["EXVD6"] not in namesv and rostv["EXVD6"] not in rostv[pos4] and rostv["EXVD6"] not in rostv[pos5]:
                            rostv[pos[j]]=rostv["EXVD6"] 
                        
                    
           
    return rosth, rostv                        
                          
                  
              
        
        
        