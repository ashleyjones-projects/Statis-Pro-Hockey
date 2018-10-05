# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:54:14 2017

@author: w9641432
"""

def make_weight(v_stats,h_stats,Linvf,Linvd,Linhf,Linhd,Linvg,Linhg,param,stamina):
    
    if "PENALTY" in param:
        ind=22;indg=15
        statind=48;statindg=45
        
         
    # LW - visitor
    if Linvf["VF"][0] != "NONE":
        for i in range(0,len(v_stats)):
            if stamina[Linvf["VF"][0]][Linvf["VF"][0]][0] == v_stats[i][0]:
                Lwv = int(v_stats[i][ind])
                Lws = int(v_stats[i][statind])
                break
    else:
        Lwv = 0
        Lws = 0     
    # C - visitor
    for i in range(0,len(v_stats)):
        if stamina[Linvf["VF"][1]][Linvf["VF"][1]][0] == v_stats[i][0]:
            cv = int(v_stats[i][ind])
            cs = int(v_stats[i][statind])
            break
    # RW - visitor
    if Linvf["VF"][2] != "NONE":
        for i in range(0,len(v_stats)):
            if stamina[Linvf["VF"][2]][Linvf["VF"][2]][0] == v_stats[i][0]:
                Rwv = int(v_stats[i][ind])
                Rws = int(v_stats[i][statind])
                break
    else:
        Rwv = 0
        Rws = 0            
    # LD - visitor
    for i in range(0,len(v_stats)):
        if stamina[Linvd["VD"][0]][Linvd["VD"][0]][0] == v_stats[i][0]:
            Ldv = int(v_stats[i][ind])
            Lds = int(v_stats[i][statind])
            break
    # RD - visitor
    if Linvd["VD"][1] != "NONE":
        for i in range(0,len(v_stats)):
            if stamina[Linvd["VD"][1]][Linvd["VD"][1]][0] == v_stats[i][0]:
                Rdv = int(v_stats[i][ind])
                Rds = int(v_stats[i][statind])
                break
    else:
        Rdv=0
        Rds=0
    # G - visitor
    for i in range(0,len(v_stats)):
        if stamina[Linvg["VG"]][Linvg["VG"]][0] == v_stats[i][0]:
            Gv = int(v_stats[i][indg])
            Gs = int(v_stats[i][statindg])
            break
            
    Tvw = Lwv + cv + Rwv + Ldv + Rdv + Gv 
    v_weight = {"weights": [Lwv/Tvw*100, cv/Tvw*100, Rwv/Tvw*100, Ldv/Tvw*100, Rdv/Tvw*100, Gv/Tvw*100],"values":[Lws,cs,Rws,Lds,Rds,Gs] }   # LW,C,RW,LD,RD,G!    
        
    # LW - home
    if Linhf["HF"][0] != "NONE":
        for i in range(0,len(h_stats)):
            if stamina[Linhf["HF"][0]][Linhf["HF"][0]][0] == h_stats[i][0]:
                Lwh = int(h_stats[i][ind])
                Lws = int(h_stats[i][statind])
                break
    else:
        Lwh = 0
        Lws = 0    
    # C - home
    for i in range(0,len(h_stats)):
        if stamina[Linhf["HF"][1]][Linhf["HF"][1]][0] == h_stats[i][0]:
            ch = int(h_stats[i][ind])
            cs = int(h_stats[i][statind])
            break
    # RW - home
    if Linhf["HF"][2] != "NONE":
        for i in range(0,len(h_stats)):
            if stamina[Linhf["HF"][2]][Linhf["HF"][2]][0] == h_stats[i][0]:
                Rwh = int(h_stats[i][ind])
                Rws = int(h_stats[i][statind])
                break
    else:
        Rwh = 0
        Rws = 0
               
    # LD - home
    for i in range(0,len(h_stats)):
        if stamina[Linhd["HD"][0]][Linhd["HD"][0]][0] == h_stats[i][0]:
            Ldh = int(h_stats[i][ind])
            Lds = int(h_stats[i][statind])
            break
    # RD - home
    if Linhd["HD"][1] != "NONE":
        for i in range(0,len(h_stats)):
            
            if stamina[Linhd["HD"][1]][Linhd["HD"][1]][0] == h_stats[i][0]:
                Rdh = int(h_stats[i][ind])
                Rds = int(h_stats[i][statind])
                break
    else:
        Rdh=0
        Rds=0        
    # G - home
    
    for i in range(0,len(h_stats)):
        if stamina[Linhg["HG"]][Linhg["HG"]][0] == h_stats[i][0]:
            Gh = int(h_stats[i][indg])
            Gs = int(h_stats[i][statindg])
            break
     
    x=1        
    Thw = Lwh + ch + Rwh + Ldh + Rdh + Gh 
    h_weight = {"weights": [Lwh/Thw*100, ch/Thw*100, Rwh/Thw*100, Ldh/Thw*100, Rdh/Thw*100, Gh/Thw*100],"values":[Lws,cs,Rws,Lds,Rds,Gs] }   # LW,C,RW,LD,RD,G! 
    
    return v_weight, h_weight