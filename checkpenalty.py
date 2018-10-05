# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:00:14 2017

@author: w9641432
"""


def check_penalty(v_stats,vt_stats,h_stats,ht_stats,Linvf,Linvd,Linhf,Linhd,Linvg,Linhg,Line_seq,stamina):
    from random import randint
    import makeweight
    import numpy as np
    
    Pen_analysis = {"PEN_V_NAME":'NONE',"POS_V":'NONE',"PEN_TYPE_V":'NONE',"DURAT_V":'NONE',"PEN_H_NAME":'NONE',"POS_H":'NONE',"PEN_TYPE_H":'NONE',"DURAT_H":'NONE'}
    
    rand = randint(1,100)
    
    vind = int(vt_stats[1][1])
    hind = int(ht_stats[1][1])
  
    if vind == 8 and hind==8:
        if rand > 1 and rand <= 42:
            pen = "Home"
        elif rand > 42 and rand <=58: 
            pen = "Coincin"    
        elif rand > 58 and rand <=100: 
            pen = "Visitor"
    
    if vind == 8 and hind==7:    
        if rand > 1 and rand <= 35:
            pen = "Home"
        elif rand > 35 and rand <=50: 
            pen = "Coincin"
        elif rand > 50 and rand <=93: 
            pen = "Visitor"
        else:
            pen = "None"
   
    if vind == 8 and hind==6:    
        if rand > 1 and rand <= 29:
            pen = "Home"
        elif rand > 29 and rand <=43: 
            pen = "Coincin"    
        elif rand > 43 and rand <=87: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 8 and hind==5:    
        if rand > 1 and rand <= 23:
            pen = "Home"
        elif rand > 23 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=81: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 8 and hind==4:    
        if rand > 1 and rand <= 17:
            pen = "Home"
        elif rand > 17 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=75: 
            pen = "Visitor"
        else:
            pen = "None"
    
    if vind == 8 and hind==3:    
        if rand > 1 and rand <= 10:
            pen = "Home"
        elif rand > 10 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=68: 
            pen = "Visitor"
        else:
            pen = "None"
    
    if vind == 8 and hind==2:    
        if rand > 1 and rand <= 4:
            pen = "Home"
        elif rand > 4 and rand <=14: 
            pen = "Coincin"    
        elif rand > 14 and rand <=62: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 8 and hind==1:    
        if rand > 1 and rand <= 3:
            pen = "Home"
        elif rand > 3 and rand <=10: 
            pen = "Coincin"    
        elif rand > 10 and rand <=56: 
            pen = "Visitor"
        else:
            pen = "None"
   
    ############################################################################
    if vind == 7 and hind==8:    
        if rand > 1 and rand <= 43:
            pen = "Home"
        elif rand > 43 and rand <=58: 
            pen = "Coincin"    
        elif rand > 58 and rand <=93: 
            pen = "Visitor"
        else:
            pen = "None"
    
    if vind == 7 and hind==7:    
        if rand > 1 and rand <= 36:
            pen = "Home"
        elif rand > 36 and rand <=50: 
            pen = "Coincin"    
        elif rand > 50 and rand <=86: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 7 and hind==6:    
        if rand > 1 and rand <= 31:
            pen = "Home"
        elif rand > 31 and rand <=44: 
            pen = "Coincin"    
        elif rand > 44 and rand <=80: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 7 and hind==5:    
        if rand > 1 and rand <= 24:
            pen = "Home"
        elif rand > 24 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=74: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 7 and hind==4:    
        if rand > 1 and rand <= 18:
            pen = "Home"
        elif rand > 18 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=68: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 7 and hind==3:    
        if rand > 1 and rand <= 11:
            pen = "Home"
        elif rand > 11 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=61: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 7 and hind==2:    
        if rand > 1 and rand <= 5:
            pen = "Home"
        elif rand > 5 and rand <=14: 
            pen = "Coincin"    
        elif rand > 14 and rand <=55: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 7 and hind==1:    
        if rand > 1 and rand <= 4:
            pen = "Home"
        elif rand > 4 and rand <=12: 
            pen = "Coincin"    
        elif rand > 12 and rand <=49: 
            pen = "Visitor"
        else:
            pen = "None"
    
    ##########################################################################
    
    if vind == 6 and hind==8:    
        if rand > 1 and rand <= 44:
            pen = "Home"
        elif rand > 44 and rand <=52: 
            pen = "Coincin"    
        elif rand > 52 and rand <=87: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 6 and hind==7:    
        if rand > 1 and rand <= 37:
            pen = "Home"
        elif rand > 37 and rand <=46: 
            pen = "Coincin"    
        elif rand > 46 and rand <=80: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 6 and hind==6:    
        if rand > 1 and rand <= 31:
            pen = "Home"
        elif rand > 31 and rand <=43: 
            pen = "Coincin"    
        elif rand > 43 and rand <=74: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 6 and hind==5:    
        if rand > 1 and rand <= 25:
            pen = "Home"
        elif rand > 25 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=68: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 6 and hind==4:    
        if rand > 1 and rand <= 19:
            pen = "Home"
        elif rand > 19 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=62: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 6 and hind==3:    
        if rand > 1 and rand <= 12:
            pen = "Home"
        elif rand > 12 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=55: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 6 and hind==2:    
        if rand > 1 and rand <= 6:
            pen = "Home"
        elif rand > 6 and rand <=8: 
            pen = "Coincin"    
        elif rand > 8 and rand <=49: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 6 and hind==1:    
        if rand > 1 and rand <= 5:
            pen = "Home"
        elif rand > 5 and rand <=12: 
            pen = "Coincin"    
        elif rand > 12 and rand <=43: 
            pen = "Visitor"
        else:
            pen = "None"

###############################################################################
    if vind == 5 and hind==8:    
        if rand > 1 and rand <= 45:
            pen = "Home"
        elif rand > 45 and rand <=58: 
            pen = "Coincin"    
        elif rand > 58 and rand <=81: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 5 and hind==7:    
        if rand > 1 and rand <= 38:
            pen = "Home"
        elif rand > 38 and rand <=50: 
            pen = "Coincin"   
        elif rand > 50 and rand <=74: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 5 and hind==6:    
        if rand > 1 and rand <= 32:
            pen = "Home"
        elif rand > 32 and rand <=43: 
            pen = "Coincin"    
        elif rand > 43 and rand <=68: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 5 and hind==5:    
        if rand > 1 and rand <= 26:
            pen = "Home"
        elif rand > 26 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=62: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 5 and hind==4:    
        if rand > 1 and rand <= 20:
            pen = "Home"
        elif rand > 20 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=56: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 5 and hind==3:    
        if rand > 1 and rand <= 13:
            pen = "Home"
        elif rand > 13 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=49: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 5 and hind==2:    
        if rand > 1 and rand <= 8:
            pen = "Home"
        elif rand > 8 and rand <=15: 
            pen = "Coincin"    
        elif rand > 15 and rand <=43: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 5 and hind==1:    
        if rand > 1 and rand <= 6:
            pen = "Home"
        elif rand > 6 and rand <=12: 
            pen = "Coincin"    
        elif rand > 12 and rand <=37: 
            pen = "Visitor"
        else:
            pen = "None"
###############################################################################
    if vind == 4 and hind==8:    
        if rand > 1 and rand <= 46:
            pen = "Home"
        elif rand > 46 and rand <=56: 
            pen = "Coincin"    
        elif rand > 56 and rand <=75: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 4 and hind==7:    
        if rand > 1 and rand <= 39:
            pen = "Home"
        elif rand > 39 and rand <=50: 
            pen = "Coincin"    
        elif rand > 50 and rand <=68: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 4 and hind==6:    
        if rand > 1 and rand <= 33:
            pen = "Home"
        elif rand > 33 and rand <=43: 
            pen = "Coincin"
        elif rand > 43 and rand <=62: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 4 and hind==5:    
        if rand > 1 and rand <= 27:
            pen = "Home"
        elif rand > 27 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=56: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 4 and hind==4:    
        if rand > 1 and rand <= 21:
            pen = "Home"
        elif rand > 21 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=50: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 4 and hind==3:    
        if rand > 1 and rand <= 14:
            pen = "Home"
        elif rand > 14 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=43: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 4 and hind==2:    
        if rand > 1 and rand <= 8:
            pen = "Home"
        elif rand > 8 and rand <=14: 
            pen = "Coincin"    
        elif rand > 14 and rand <=37: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 4 and hind==1:    
        if rand > 1 and rand <= 6:
            pen = "Home"
        elif rand > 6 and rand <=11: 
            pen = "Coincin"    
        elif rand > 11 and rand <=31: 
            pen = "Visitor"
        else:
            pen = "None"
###############################################################################
    if vind == 3 and hind==8:    
        if rand > 1 and rand <= 47:
            pen = "Home"
        elif rand > 47 and rand <=58: 
            pen = "Coincin"    
        elif rand > 58 and rand <=69: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 3 and hind==7:    
        if rand > 1 and rand <= 40:
            pen = "Home"
        elif rand > 40 and rand <=50: 
            pen = "Coincin"    
        elif rand > 50 and rand <=61: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 3 and hind==6:    
        if rand > 1 and rand <= 34:
            pen = "Home"
        elif rand > 34 and rand <=43: 
            pen = "Coincin"    
        elif rand > 43 and rand <=55: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 3 and hind==5:    
        if rand > 1 and rand <= 28:
            pen = "Home"
        elif rand > 28 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=49: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 3 and hind==4:    
        if rand > 1 and rand <= 22:
            pen = "Home"
        elif rand > 22 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=43: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 3 and hind==3:    
        if rand > 1 and rand <= 15:
            pen = "Home"
        elif rand > 15 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=36: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 3 and hind==2:    
        if rand > 1 and rand <= 9:
            pen = "Home"
        elif rand > 9 and rand <=14: 
            pen = "Coincin"    
        elif rand > 14 and rand <=30: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 3 and hind==1:    
        if rand > 1 and rand <= 6:
            pen = "Home"
        elif rand > 6 and rand <=10: 
            pen = "Coincin"    
        elif rand > 10 and rand <=24: 
            pen = "Visitor"
        else:
            pen = "None"
###############################################################################
    if vind == 2 and hind==8:    
        if rand > 1 and rand <= 48:
            pen = "Home"
        elif rand > 48 and rand <=58: 
            pen = "Coincin"    
        elif rand > 58 and rand <=63: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 2 and hind==7:    
        if rand > 1 and rand <= 41:
            pen = "Home"
        elif rand > 41 and rand <=50: 
            pen = "Coincin"    
        elif rand > 50 and rand <=55: 
            pen = "Visitor"
        else:
            pen = "None"
            
    if vind == 2 and hind==6:    
        if rand > 1 and rand <= 35:
            pen = "Home"
        elif rand > 35 and rand <=43: 
            pen = "Coincin"    
        elif rand > 43 and rand <=49: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 2 and hind==5:    
        if rand > 1 and rand <= 29:
            pen = "Home"
        elif rand > 29 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=43: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 2 and hind==4:    
        if rand > 1 and rand <= 23:
            pen = "Home"
        elif rand > 23 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=37: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 2 and hind==3:    
        if rand > 1 and rand <= 16:
            pen = "Home"
        elif rand > 16 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=30: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 2 and hind==2:    
        if rand > 1 and rand <= 10:
            pen = "Home"
        elif rand > 10 and rand <=14: 
            pen = "Coincin"    
        elif rand > 14 and rand <=24: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 2 and hind==1:    
        if rand > 1 and rand <= 6:
            pen = "Home"
        elif rand > 6 and rand <=9: 
            pen = "Coincin"    
        elif rand > 9 and rand <=18: 
            pen = "Visitor"
        else:
            pen = "None"
###############################################################################
    if vind == 1 and hind==8:    
        if rand > 1 and rand <= 49:
            pen = "Home"
        elif rand > 49 and rand <=50: 
            pen = "Coincin"    
        elif rand > 50 and rand <=57: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 1 and hind==7:    
        if rand > 1 and rand <= 42:
            pen = "Home"
        elif rand > 42 and rand <=50: 
            pen = "Coincin"    
        elif rand > 50 and rand <=50: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 1 and hind==6:    
        if rand > 1 and rand <= 36:
            pen = "Home"
        elif rand > 36 and rand <=43: 
            pen = "Coincin"    
        elif rand > 43 and rand <=43: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 1 and hind==5:    
        if rand > 1 and rand <= 30:
            pen = "Home"
        elif rand > 30 and rand <=36: 
            pen = "Coincin"    
        elif rand > 36 and rand <=37: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 1 and hind==4:    
        if rand > 1 and rand <= 24:
            pen = "Home"
        elif rand > 24 and rand <=29: 
            pen = "Coincin"    
        elif rand > 29 and rand <=31: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 1 and hind==3:    
        if rand > 1 and rand <= 17:
            pen = "Home"
        elif rand > 17 and rand <=21: 
            pen = "Coincin"    
        elif rand > 21 and rand <=24: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 1 and hind==2:    
        if rand > 1 and rand <= 11:
            pen = "Home"
        elif rand > 11 and rand <=14: 
            pen = "Coincin"    
        elif rand > 14 and rand <=18: 
            pen = "Visitor"
        else:
            pen = "None"
    if vind == 1 and hind==1:    
        if rand > 1 and rand <= 6:
            pen = "Home"
        elif rand > 6 and rand <=8: 
            pen = "Coincin"    
        elif rand > 8 and rand <=14: 
            pen = "Visitor"
        else:
            pen = "None"
            
    ###############################3
    
    [v_weight,h_weight]=makeweight.make_weight(v_stats,h_stats,Linvf,Linvd,Linhf,Linhd,Linvg,Linhg,'PENALTY',stamina)
    rand = randint(1,100)
    
    tv_weight = np.cumsum([v_weight["weights"][0],v_weight["weights"][1],v_weight["weights"][2],v_weight["weights"][3],v_weight["weights"][4],v_weight["weights"][5]])
    th_weight = np.cumsum([h_weight["weights"][0],h_weight["weights"][1],h_weight["weights"][2],h_weight["weights"][3],h_weight["weights"][4],h_weight["weights"][5]])

    if "Coincin" in pen:
        #Line_seq["PENH"]+=1    coincidental penalties dont need 4v4, shall be played at full-strength
        if rand <= th_weight[0]:
            pen_playerh = {"Pen_player":stamina[Linhf["HF"][0]][Linhf["HF"][0]][0],"POS":'LW'}
            rateh = h_weight["values"][0]
        elif rand > th_weight[0] and rand <= th_weight[1]:
            pen_playerh = {"Pen_player":stamina[Linhf["HF"][1]][Linhf["HF"][1]][0],"POS":'C'}
            rateh = h_weight["values"][1]
        elif rand > th_weight[1] and rand <= th_weight[2]:
            pen_playerh = {"Pen_player":stamina[Linhf["HF"][2]][Linhf["HF"][2]][0],"POS":'RW'}
            rateh = h_weight["values"][2]
        elif rand > th_weight[2] and rand <= th_weight[3]:
            pen_playerh = {"Pen_player":stamina[Linhd["HD"][0]][Linhd["HD"][0]][0],"POS":'LD'}
            rateh = h_weight["values"][3]
        elif rand > th_weight[3] and rand <= th_weight[4]:
            pen_playerh ={"Pen_player": stamina[Linhd["HD"][1]][Linhd["HD"][1]][0],"POS":'RD'}
            rateh = h_weight["values"][4]
        elif rand > th_weight[4] and rand <= th_weight[5]:
            pen_playerh = {"Pen_player":stamina[Linhg["HG"][0]][Linhg["HG"][0]][0],"POS":'G'}
            rateh = h_weight["values"][5]
        
        rand = randint(1,100)    
        #Line_seq["PENV"]+=1
        if rand <= tv_weight[0]:
            pen_playerv = {"Pen_player":stamina[Linvf["VF"][0]][Linvf["VF"][0]][0],"POS":'LW'}
            ratev = v_weight["values"][0]
        elif rand > tv_weight[0] and rand <= tv_weight[1]:
            pen_playerv = {"Pen_player":stamina[Linvf["VF"][1]][Linvf["VF"][1]][0],"POS":'C'}
            ratev = v_weight["values"][1]
        elif rand > tv_weight[1] and rand <= tv_weight[2]:
            pen_playerv = {"Pen_player":stamina[Linvf["VF"][2]][Linvf["VF"][2]][0],"POS":'RW'}
            ratev = v_weight["values"][2]
        elif rand > tv_weight[2] and rand <= tv_weight[3]:
            pen_playerv = {"Pen_player":stamina[Linvd["VD"][0]][Linvd["VD"][0]][0],"POS":'LD'}
            ratev = v_weight["values"][3]
        elif rand > tv_weight[3] and rand <= tv_weight[4]:
            pen_playerv = {"Pen_player":stamina[Linvd["VD"][1]][Linvd["VD"][1]][0],"POS":'RD'}
            ratev = v_weight["values"][4]
        elif rand > tv_weight[4] and rand <= tv_weight[5]:
            pen_playerv = {"Pen_player":stamina[Linvg["VG"][0]][Linvg["VG"][0]][0] ,"POS":'G'}
            ratev = v_weight["values"][5]    
        
    elif "Home" in pen:
        Line_seq["PENH"]+=1
        if rand <= th_weight[0]:
            pen_playerh = {"Pen_player":stamina[Linhf["HF"][0]][Linhf["HF"][0]][0],"POS":'LW'}
            rateh = h_weight["values"][0]
        elif rand > th_weight[0] and rand <= th_weight[1]:
            pen_playerh = {"Pen_player":stamina[Linhf["HF"][1]][Linhf["HF"][1]][0],"POS":'C'}
            rateh = h_weight["values"][1]
        elif rand > th_weight[1] and rand <= th_weight[2]:
            pen_playerh = {"Pen_player":stamina[Linhf["HF"][2]][Linhf["HF"][2]][0],"POS":'RW'}
            rateh = h_weight["values"][2]
        elif rand > th_weight[2] and rand <= th_weight[3]:
            pen_playerh = {"Pen_player":stamina[Linhd["HD"][0]][Linhd["HD"][0]][0],"POS":'LD'}
            rateh = h_weight["values"][3]
        elif rand > th_weight[3] and rand <= th_weight[4]:
            pen_playerh ={"Pen_player": stamina[Linhd["HD"][1]][Linhd["HD"][1]][0],"POS":'RD'}
            rateh = h_weight["values"][4]
        elif rand > th_weight[4] and rand <= th_weight[5]:
            pen_playerh = {"Pen_player":stamina[Linhg["HG"][0]][Linhg["HG"][0]][0],"POS":'G'}
            rateh = h_weight["values"][5]
    
    elif "Visitor" in pen:
        Line_seq["PENV"]+=1
        if rand <= tv_weight[0]:
            pen_playerv = {"Pen_player":stamina[Linvf["VF"][0]][Linvf["VF"][0]][0],"POS":'LW'}
            ratev = v_weight["values"][0]
        elif rand > tv_weight[0] and rand <= tv_weight[1]:
            pen_playerv = {"Pen_player":stamina[Linvf["VF"][1]][Linvf["VF"][1]][0],"POS":'C'}
            ratev = v_weight["values"][1]
        elif rand > tv_weight[1] and rand <= tv_weight[2]:
            pen_playerv = {"Pen_player":stamina[Linvf["VF"][2]][Linvf["VF"][2]][0],"POS":'RW'}
            ratev = v_weight["values"][2]
        elif rand > tv_weight[2] and rand <= tv_weight[3]:
            pen_playerv = {"Pen_player":stamina[Linvd["VD"][0]][Linvd["VD"][0]][0],"POS":'LD'}
            ratev = v_weight["values"][3]
        elif rand > tv_weight[3] and rand <= tv_weight[4]:
            pen_playerv = {"Pen_player":stamina[Linvd["VD"][1]][Linvd["VD"][1]][0],"POS":'RD'}
            ratev = v_weight["values"][4]
        elif rand > tv_weight[4] and rand <= tv_weight[5]:
            pen_playerv = {"Pen_player":stamina[Linvg["VG"][0]][Linvg["VG"][0]][0] ,"POS":'G'}
            ratev = v_weight["values"][5]
            
    else:
         
         return Pen_analysis,Line_seq
     
     # CONSULT PENALTY CHART FOR TYPE AND LENGTH OF PENALTY
     
    rand = randint(1,100)
    
    if "Coincin" in pen:
        if ratev >= 5 and rateh >= 5:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"FIGHT","DURAT_V":5,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"FIGHT","DURAT_H":5}
        
        elif ratev >= 5 and rateh >= 4:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"FIGHT","DURAT_V":5,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"FIGHT","DURAT_H":5}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 5 and rateh >= 3:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":5,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":5}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 5 and rateh >= 2:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 5 and rateh >= 1:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 5 and rateh >= 0:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

###############################################################################
        
        elif ratev >= 4 and rateh >= 5:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"FIGHT","DURAT_V":5,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"FIGHT","DURAT_H":5}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
 
        elif ratev >= 4 and rateh >= 4:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"FIGHT","DURAT_V":5,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"FIGHT","DURAT_H":5}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 4 and rateh >= 3:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 4 and rateh >= 2:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 4 and rateh >= 1:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 4 and rateh >= 0:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
    
###############################################################################         
        
        elif ratev >= 3 and rateh >= 5:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
 
        elif ratev >= 3 and rateh >= 4:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
       
        elif ratev >= 3 and rateh >= 3:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 3 and rateh >= 2:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 3 and rateh >= 1:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 3 and rateh >= 0:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

###############################################################################

        elif ratev >= 2 and rateh >= 5:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
 
        elif ratev >= 2 and rateh >= 4:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
       
        elif ratev >= 2 and rateh >= 3:
            if rand <= 25:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 25 and rand <= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 60 and rand <= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
            elif rand > 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 2 and rateh >= 2:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 2 and rateh >= 1:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 2 and rateh >= 0:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

###############################################################################

        elif ratev >= 1 and rateh >= 5:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
 
        elif ratev >= 1 and rateh >= 4:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
       
        elif ratev >= 1 and rateh >= 3:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 1 and rateh >= 2:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 1 and rateh >= 1:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 1 and rateh >= 0:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

###############################################################################

        elif ratev >= 0 and rateh >= 5:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
 
        elif ratev >= 0 and rateh >= 4:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
       
        elif ratev >= 0 and rateh >= 3:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 0 and rateh >= 2:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

        elif ratev >= 0 and rateh >= 1:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        
        elif ratev >= 0 and rateh >= 0:
            if rand <= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 40 and rand <= 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
            elif rand > 70:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}

    elif "Home" in pen:

        if rand <= 10:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"TRIPPING","DURAT_H":2}
        elif rand > 10 and rand <= 20:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLASHING","DURAT_H":2}
        elif rand > 20 and rand <= 30:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"DELAYOG","DURAT_H":2}
        elif rand > 30 and rand <= 40:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"INTERFERENCE","DURAT_H":2}
        elif rand > 40 and rand <= 50:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"HOOKING","DURAT_H":2}
        elif rand > 50 and rand <= 60:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"X_CHECK","DURAT_H":2}
        elif rand > 60 and rand <= 70:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"HOLDING","DURAT_H":2}
        elif rand > 70 and rand <= 80:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"HIGHSTICK","DURAT_H":2}
        elif rand > 80 and rand <= 90:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"ROUGHING","DURAT_H":2}
        elif rand > 90 and rand <= 91:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"CLIPPING","DURAT_H":2}
        elif rand > 91 and rand <= 92:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"UNSPORTSMANLIKE","DURAT_H":2}
        elif rand > 92 and rand <= 94:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"TOOMANYMEN","DURAT_H":2}
        elif rand > 94 and rand <= 95:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"EMBELLISHMENT","DURAT_H":2}
        elif rand > 95 and rand <= 97:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"BOARDING","DURAT_H":5}
        elif rand > 97 and rand <= 98:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"CLOSEHANDPUCK","DURAT_H":2}
        elif rand > 98 and rand <= 99:
            Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"GOALTENDINT","DURAT_H":2}
        elif rand > 99 and rand <= 100:
            rand2 = randint(1,100)
            if rand2< 20:
                Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"CHARGING","DURAT_H":5}
            elif rand2 > 20 and rand2<= 30:
                Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"KNEEING","DURAT_H":5}
            elif rand2 > 30 and rand2<= 40:
                Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SPEARING","DURAT_H":5}
            elif rand2 > 40 and rand2<= 60:
                Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"CHECKINGFBEHIND","DURAT_H":5}
            elif rand2 > 60 and rand2<= 80:
                Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"INSTIGATING","DURAT_H":5}
            elif rand2 > 80 and rand2<= 95:
                Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"SLEWFOOTING","DURAT_H":5}
            elif rand2 > 95 and rand2<= 100:
                Pen_analysis = {"PEN_V_NAME":"NONE","POS_V":"NONE","PEN_TYPE_V":"NONE","DURAT_V":0,"PEN_H_NAME":pen_playerh["Pen_player"],"POS_H":pen_playerh["POS"],"PEN_TYPE_H":"BUTTENDING","DURAT_H":5}

    elif "Visitor" in pen:
       
        if rand <= 10:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"TRIPPING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 10 and rand <= 20:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLASHING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 20 and rand <= 30:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"DELAYOG","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 30 and rand <= 40:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"INTERFERENCE","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 40 and rand <= 50:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"HOOKING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 50 and rand <= 60:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"X_CHECK","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 60 and rand <= 70:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"HOLDING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 70 and rand <= 80:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"HIGHSTICK","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 80 and rand <= 90:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"ROUGHING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 90 and rand <= 91:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"CLIPPING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 91 and rand <= 92:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"UNSPORTSMANLIKE","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 92 and rand <= 94:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"TOOMANYMEN","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 94 and rand <= 95:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"EMBELLISHMENT","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 95 and rand <= 97:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"BOARDING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 97 and rand <= 98:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"CLOSEHANDPUCK","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 98 and rand <= 99:
            Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"GOALTENDINT","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
        elif rand > 99 and rand <= 100:
            rand2 = randint(1,100)
            if rand2< 20:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"CHARGING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
            elif rand2 > 20 and rand2<= 30:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"KNEEING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
            elif rand2 > 30 and rand2<= 40:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SPEERING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
            elif rand2 > 40 and rand2<= 60:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"CHECKFBEHIND","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
            elif rand2 > 60 and rand2<= 80:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"INSTIGATING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
            elif rand2 > 80 and rand2<= 95:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"SLEWFOOTING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}
            elif rand2 > 95 and rand2<= 100:
                Pen_analysis = {"PEN_V_NAME":pen_playerv["Pen_player"],"POS_V":pen_playerv["POS"],"PEN_TYPE_V":"BUTTENDING","DURAT_V":2,"PEN_H_NAME":"NONE","POS_H":"NONE","PEN_TYPE_H":"NONE","DURAT_H":0}

    return Pen_analysis,Line_seq

         