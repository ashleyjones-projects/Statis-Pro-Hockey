# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:53:57 2017

@author: w9641432
"""
from random import randint
import numpy as np

def facmaker(Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,puckposs,line_seq):
    
    # ACTION FLOW
    if Linhf['NUM']==1 or Linvf['NUM']==1:
        shot_thresh=39
    else:
        shot_thresh  = 28
    hit_thresh   = 10                           # Hits
    Gw_thresh    = 8                            # Give away
    TW_thresh    = 8                            # Take away
    pen_thresh   = 3                            # Penalties
    other_thresh = 10                           # Other, eg, icing,offside,frozen,special action,forechking,puck deflected
    pass_space   = 100 - shot_thresh - hit_thresh - Gw_thresh - TW_thresh - pen_thresh - other_thresh  # No major action in time allocated
    
    # SHOTS
    shot_type_weight   = [62,27,11]#[62,27,11]             # A,B,C 
    stw = np.cumsum(shot_type_weight)
    shot_player_weight = [21,22,21,18,18]    # Lw,C,Rw,Ld,Rd,UNDEFUNED
    spw = np.cumsum(shot_player_weight)
    
    # ASSISTS
    #ass_type           = [57,43]                # predefined (LW-LD-C SOG-A), undefined (2 HIGHEST ASS to C SOG-B)
    ass_player_weight  = [20,23,20,18,18,1]     # Lw,C,Rw,Ld,Rd,G
    apw = np.cumsum(ass_player_weight)
    ass_number         = [76,18,6]              # 2 assists, 1 assist, 0 assists
    anw = np.cumsum(ass_number)
    
    # HITS
    hit_weight         = [20,20,20,20,20]
    hw = np.cumsum(hit_weight)
    
    # GIVE AWAYS
    gv_weight         = [20,20,20,20,20]
    gvw = np.cumsum(gv_weight)
    
    # TAKE AWAYS
    tk_weight         = [20,20,20,20,20]
    tkw = np.cumsum(tk_weight)
    
    # OTHER
    other_weight      = [20,20,30,10,10,10]                      # icing,offside,frozen,special action,forechking,puck deflected
    ow = np.cumsum(other_weight) 
    
    
#    stats=[]
    for j in range(1,101):                     
        fac_random = randint(1,100)                     # FAC RANDOM NUMBER
        
        if fac_random <= shot_thresh:
            
            # FIGURE OUT PLAYER TYPE
            shot_player_rand = randint(1,100)
            
            if shot_player_rand <= spw[0]:
                 if puckposs["HOME"]==1:
                     if "3K" in Linhf["HF"]:
                         s_player_type = 'C'
                     else:
                         s_player_type = 'LW'
                 elif puckposs["VISITOR"]==1:
                     if "3K" in Linvf["VF"]:
                        s_player_type = 'C'
                     else:
                        s_player_type = 'LW'
                         
            elif shot_player_rand > spw[0] and shot_player_rand <= spw[1] :
                s_player_type = 'C'
            
            elif shot_player_rand > spw[1] and shot_player_rand <= spw[2] :
                if puckposs["HOME"]==1:
                    if "3K" in Linhf["HF"]:
                        s_player_type = 'C'
                    elif "4" in Linhf["HF"] or "3" in Linhf["HF"]:
                        s_player_type = 'LW'
                    else:    
                        s_player_type = 'RW'
                elif puckposs["VISITOR"]==1:
                    if "3K" in Linvf["VF"]:
                        s_player_type = 'C'
                    elif "4" in Linvf["VF"] or "3" in Linvf["VF"]:
                        s_player_type = 'LW'
                    else:    
                        s_player_type = 'RW'
            elif shot_player_rand > spw[2] and shot_player_rand <= spw[3] :
                s_player_type = 'LD'
            elif shot_player_rand > spw[3] and shot_player_rand <= spw[4] :
                if puckposs["HOME"]==1:
                    if "4" in Linhd["HD"] or "3K" in Linhd["HD"]:
                        s_player_type = 'LD'
                    elif "3" in Linhd["HD"]:
                        s_player_type = 'LD'
                    else:    
                        s_player_type = 'RD'
                elif puckposs["VISITOR"]==1:
                    if "4" in Linvd["VD"] or "3K" in Linvd["VD"]:
                        s_player_type = 'LD'
                    elif "3" in Linvd["VD"]:
                        s_player_type = 'LD'
                    else:  
                        s_player_type = 'RD'
             
             # FIGURE OUT SHOT TYPE 
            shot_type_rand = randint(1,100)
            
            if shot_type_rand <= stw[0]:
                s_type = 'SOG-A'
            elif shot_type_rand > stw[0] and shot_type_rand <= stw[1] :
                s_type = 'SOG-B'
            elif shot_type_rand > stw[1] and shot_type_rand <= stw[2] :
                s_type = 'SOG-C'   
            
            s_player_type = s_player_type + '-' + s_type      
           
            # FIGURE OUT NUMBER OF ASSISTS
            
            ass_num_rand = randint(1,100)
            
            if ass_num_rand <= anw[0]:
                noa = [1,1]
            elif ass_num_rand > anw[0] and ass_num_rand <= anw[1]:
                noa = [1]
            elif ass_num_rand > anw[1]:
                noa = []
            
            if len(noa) > 0:
                
                for i in range(0,len(noa)):
                    count=0
                    while count==0:
                        rand = randint(1,100)
                        if rand <=apw[0] and "LW" not in s_player_type:
                            s_player_type = s_player_type + '-' + "LW"
                            count=1
                        elif rand > apw[0] and rand <= apw[1] and "C" not in s_player_type:
                            s_player_type = s_player_type + '-' + "C"
                            count=1
                        elif rand > apw[1] and rand <= apw[2] and "RW" not in s_player_type:
                            s_player_type = s_player_type + '-' + "RW"
                            count=1
                        elif rand > apw[2] and rand <= apw[3] and "LD" not in s_player_type:
                            s_player_type = s_player_type + '-' + "LD"
                            count=1
                        elif rand > apw[3] and rand <= apw[4] and "RD" not in s_player_type:
                            s_player_type = s_player_type + '-' + "RD"
                            count=1
                        elif rand > apw[4] and "G" not in s_player_type:
                            s_player_type = s_player_type + '-' + "G"
                            count=1     
         
        elif fac_random > shot_thresh and fac_random <= (shot_thresh + hit_thresh): 
            
            rand = randint(1,100)
            
            if rand <= hw[0]:
                s_player_type = "HIT:LW"
            elif rand > hw[0] and rand <= hw[1]:
                s_player_type = "HIT:C"    
            elif rand > hw[1] and rand <= hw[2]:
                s_player_type = "HIT:RW"
            elif rand > hw[2] and rand <= hw[3]:
                s_player_type = "HIT:LD"    
            elif rand > hw[3] and rand <= hw[4]:
                s_player_type = "HIT:RD"
        
        elif fac_random > (shot_thresh + hit_thresh) and fac_random <= (shot_thresh + hit_thresh + Gw_thresh):
            
            rand = randint(1,100)
            
            if rand <= gvw[0]:
                s_player_type = "GV:LW"
            elif rand > gvw[0] and rand <= gvw[1]:
                s_player_type = "GV:C"    
            elif rand > gvw[1] and rand <= gvw[2]:
                s_player_type = "GV:RW"
            elif rand > gvw[2] and rand <= gvw[3]:
                s_player_type = "GV:LD"    
            elif rand > gvw[3] and rand <= gvw[4]:
                s_player_type = "GV:RD"
        
        elif fac_random > (shot_thresh + hit_thresh + Gw_thresh) and fac_random <= (shot_thresh + hit_thresh + Gw_thresh + TW_thresh): 
            
            rand = randint(1,100)
            
            if rand <= tkw[0]:
                s_player_type = "TK:LW"
            elif rand > tkw[0] and rand <= tkw[1]:
                s_player_type = "TK:C"    
            elif rand > tkw[1] and rand <= tkw[2]:
                s_player_type = "TK:RW"
            elif rand > tkw[2] and rand <= tkw[3]:
                s_player_type = "TK:LD"    
            elif rand > tkw[3] and rand <= tkw[4]:
                s_player_type = "TK:RD"
        
        elif fac_random > (shot_thresh + hit_thresh + Gw_thresh + TW_thresh) and fac_random <= (shot_thresh + hit_thresh + Gw_thresh + TW_thresh + pen_thresh): 
        
            s_player_type = "PENALTY?"
        
        elif fac_random > (shot_thresh + hit_thresh + Gw_thresh + TW_thresh + pen_thresh) and fac_random <= (shot_thresh + hit_thresh + Gw_thresh + TW_thresh + pen_thresh + pass_space): 
            
            rand = randint(1,100)
            
            if rand <= ow[0]:
                teamr= randint(0,1) # 0 home team, 1 visiting
                s_player_type = "ICING_" + str(teamr) 
            elif rand > ow[0] and rand <= ow[1]:
                s_player_type = "OFFSIDE"    
            elif rand > ow[1] and rand <= ow[2]:
                s_player_type = "FROZENPUCK"
            elif rand > ow[2] and rand <= ow[3]:
                s_player_type = "SAC"    
            elif rand > ow[3] and rand <= ow[4]:
                s_player_type = "FC"
            else:
                s_player_type = "PUCKDEFLECTEDOUT"
                
        else:
    
            s_player_type = "PASSSPACE" 
            

                
                
            
        
    
    fac = fac_random,s_player_type
    
    return fac