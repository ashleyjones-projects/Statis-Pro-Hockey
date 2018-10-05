# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:49:19 2017

@author: w9641432
"""

def shot_potential(h_stats,v_stats,scoreboard,s_player_type,puckposs,Linhf,Linhd,Linhg,Linvf,Linvd,Linvg,stamina,line_seq):
    import getdefense 
    
    inds = [pos for pos, char in enumerate(s_player_type) if char=='-']
    
    shooter = s_player_type[:inds[0]] 
    stype    = s_player_type[inds[1]+1]
    # TO PREVENT RW OR LW OR RD COMING UP IN VARIOUS PENALTY SITUATIONS. CHANGES S-PLAYER-TYPE SHOT OUTCOME
    if puckposs["HOME"]==1 and "SOG" in s_player_type:        
        if "3K" in Linhf["HF"][1]:
            if "RW" in s_player_type or "LW" in s_player_type:
               s_player_type = "C" + '-SOG-' + stype
        if "3LD" in Linhd["HD"][0]:
            if "RD" in s_player_type:
               s_player_type = "C" + '-SOG-' + stype       
        if "3L" in Linhf["HF"][0] or "4" in Linhf["HF"][0]:
            if "RW" in s_player_type:
               s_player_type = "LW" + '-SOG-' + stype
        
    elif puckposs["VISITOR"]==1 and "SOG" in s_player_type:         
        if "3K" in Linvf["VF"][1]:
            if "RW" in s_player_type or "LW" in s_player_type:
               s_player_type = "C" + '-SOG-' + stype
        if "3LD" in Linvd["VD"][0]:
            if "RD" in s_player_type:
               s_player_type = "C" + '-SOG-' + stype       
        if "3L" in Linvf["VF"][0] or "4" in Linvf["VF"][0]: # STUCK HERE! NEED TO BE MORE SPECIFIC THAN 3
            if "RW" in s_player_type:
               s_player_type = "LW" + '-SOG-' + stype
        
    # redo inds just incase changed from the above statements
    inds = [pos for pos, char in enumerate(s_player_type) if char=='-']
    shooter = s_player_type[:inds[0]] 
    stype    = s_player_type[inds[1]+1]
           
    if len(inds)==2:
        a1="NONE"
        a2="NONE"
    elif len(inds)==3:
        a1  = s_player_type[inds[2]+1:]
        a2="NONE"
    elif len(inds)==4:
        a1  = s_player_type[inds[2]+1:inds[3]]
        a2  = s_player_type[inds[3]+1:]
        
                   
    
    ###############################################################################
        #   OBTAIN APPROPRIATE DEFENSE DEPENDENT UPON SHOOTER
        
    defense_p,intim_p = getdefense.get_defense(shooter,stype,line_seq,Linhf,Linvf,puckposs)
#    if "LD" in s_player_type and 'RW' in intim_p and (line_seq['PENH']==1 or line_seq['PENV']==1):
#        x=1               
#    print(s_player_type)
#    print(intim_p)   
    
    ###############################################################################
        #   SET UP LOOPS TO OBTAIN SHOOTER AND ASSISTING STATS
    
    posn =[0,1,2,3,4]
    # GET SOG INFO, TAKES INTO ACCOUNT PLAYER SHOOTING, ASSISTS AND DEFENSIVE ATTS
    
    
    ###############################  HOME HAS POSSESSION #######################
    if puckposs["HOME"] == 1:
        #OFFENSE
        # SHOOTER
        for i in range(0,len(posn)): 
            if shooter in Linhf["HF"][posn[i]]:
                for j in range(0,len(h_stats)):
                    if stamina[Linhf["HF"][posn[i]]][Linhf["HF"][posn[i]]][0] == h_stats[j][0]:
                        shoot_r = list(h_stats[j][16:21])
                        break
                break
            elif  shooter in Linhd["HD"][posn[i]]:
                for j in range(0,len(h_stats)):
                    if stamina[Linhd["HD"][posn[i]]][Linhd["HD"][posn[i]]][0] == h_stats[j][0]:
                        shoot_r = list(h_stats[j][16:21])
                        break
                break
        
        # ASSISTS 1
       
        posn =[0,1,2,3,4,5] 
        if "NONE" not in a1:   
            for i in range(0,len(posn)): 
                if a1 in Linhf["HF"][posn[i]]:
                    for j in range(0,len(h_stats)):
                        if stamina[Linhf["HF"][posn[i]]][Linhf["HF"][posn[i]]][0] == h_stats[j][0]:
                            assist_1 = int(h_stats[j][21])
                            break
                    break
                elif a1 in Linhd["HD"][posn[i]]:
                    for j in range(0,len(h_stats)):
                        if stamina[Linhd["HD"][posn[i]]][Linhd["HD"][posn[i]]][0] == h_stats[j][0]:
                            assist_1 = int(h_stats[j][21])
                            break
                    break
        else:
            assist_1=0        
        # ASSIST 2
        if "NONE" not in a2:    
            for i in range(0,len(posn)): 
                if a2 in Linhf["HF"][posn[i]]:
                    for j in range(0,len(h_stats)):
                        if stamina[Linhf["HF"][posn[i]]][Linhf["HF"][posn[i]]][0] == h_stats[j][0]:
                            assist_2 = int(h_stats[j][21])
                            break
                    break
                elif a2 in Linhd["HD"][posn[i]]:
                    for j in range(0,len(h_stats)):
                        if stamina[Linhd["HD"][posn[i]]][Linhd["HD"][posn[i]]][0] == h_stats[j][0]:
                            assist_2 = int(h_stats[j][21])
                            break
                    break
        else:
            assist_2=0        
               
        ###############################################################################
            #   SET UP LOOPS TO OBTAIN DEFENSIVE STATS   
        
        
        posn =[0,1,2,3,4]
        dfq=[]
        for k in range(0,len(defense_p)):
            if defense_p[k] !=0:
                for i in range(0,len(posn)):
                    if defense_p[k] in Linvf["VF"][posn[i]]:
                        for j in range(0,len(v_stats)):
                            if stamina[Linvf["VF"][posn[i]]][Linvf["VF"][posn[i]]][0] == v_stats[j][0]:
                                dfq.append(int(v_stats[j][23]))
                                break
                        break
                    elif defense_p[k] in Linvd["VD"][posn[i]]:
                        for j in range(0,len(v_stats)):
                            if stamina[Linvd["VD"][posn[i]]][Linvd["VD"][posn[i]]][0] == v_stats[j][0]:
                                dfq.append(int(v_stats[j][23]))
                                break
                        break
                        
            else:
                dfq=[0]
        
        if intim_p[0] !=0:
            for k in range(0,len(intim_p)):
                for i in range(0,len(posn)):
                    if intim_p[k] in Linvf["VF"][posn[i]]:
                        for j in range(0,len(v_stats)):
                            if stamina[Linvf["VF"][posn[i]]][Linvf["VF"][posn[i]]][0] == v_stats[j][0]:
                                ifq=(int(v_stats[j][23]))
                                break
                        break
                    elif intim_p[k] in Linvd["VD"][posn[i]]:
                        for j in range(0,len(v_stats)):
                            if stamina[Linvd["VD"][posn[i]]][Linvd["VD"][posn[i]]][0] == v_stats[j][0]:
                                ifq=(int(v_stats[j][23]))
                                break
                        break
        else:
            ifq=0         
        
    
    ###############################  VISITOR HAS POSSESSION #######################    
    elif puckposs["VISITOR"] == 1:
        posn =[0,1,2,3,4]
        #OFFENSE
        # SHOOTER
        for i in range(0,len(posn)): 
            if shooter in Linvf["VF"][posn[i]]:
                for j in range(0,len(v_stats)):
                    if stamina[Linvf["VF"][posn[i]]][Linvf["VF"][posn[i]]][0] == v_stats[j][0]:
                        shoot_r = list(v_stats[j][16:21])
                        break
                break
            elif  shooter in Linvd["VD"][posn[i]]:
                for j in range(0,len(v_stats)):
                    if stamina[Linvd["VD"][posn[i]]][Linvd["VD"][posn[i]]][0] == v_stats[j][0]:
                        shoot_r = list(v_stats[j][16:21])
                        break
                break
        
        # ASSISTS 1
        
        posn =[0,1,2,3,4,5]
        
        if "NONE" not in a1:   
            for i in range(0,len(posn)): 
                if a1 in Linvf["VF"][posn[i]]:
                    for j in range(0,len(v_stats)):
                        if stamina[Linvf["VF"][posn[i]]][Linvf["VF"][posn[i]]][0] == v_stats[j][0]:
                            assist_1 = int(v_stats[j][21])
                            break
                    break
                elif a1 in Linvd["VD"][posn[i]]:
                    for j in range(0,len(v_stats)):
                        if stamina[Linvd["VD"][posn[i]]][Linvd["VD"][posn[i]]][0] == v_stats[j][0]:
                            assist_1 = int(v_stats[j][21])
                            break
                    break
        else:
            assist_1=0
            
        # ASSIST 2
        if "NONE" not in a2:    
            for i in range(0,len(posn)): 
                if a1 in Linvf["VF"][posn[i]]:
                    for j in range(0,len(v_stats)):
                        if stamina[Linvf["VF"][posn[i]]][Linvf["VF"][posn[i]]][0] == v_stats[j][0]:
                            assist_2 = int(v_stats[j][21])
                            break
                    break
                elif a1 in Linvd["VD"][posn[i]]:
                    for j in range(0,len(v_stats)):
                        if stamina[Linvd["VD"][posn[i]]][Linvd["VD"][posn[i]]][0] == v_stats[j][0]:
                            assist_2 = int(v_stats[j][21])
                            break
                    break
        else:
            assist_2=0            
        ###############################################################################
            #   SET UP LOOPS TO OBTAIN DEFENSIVE STATS   
        
        
        posn =[0,1,2,3,4]
        dfq=[]
        for k in range(0,len(defense_p)):
            if defense_p[k] !=0:
                for i in range(0,len(posn)):
                    if defense_p[k] in Linhf["HF"][posn[i]]:
                        for j in range(0,len(h_stats)):
                            if stamina[Linhf["HF"][posn[i]]][Linhf["HF"][posn[i]]][0] == h_stats[j][0]:
                                dfq.append(int(h_stats[j][23]))
                                break
                        break
                    elif defense_p[k] in Linhd["HD"][posn[i]]:
                        for j in range(0,len(h_stats)):
                            if stamina[Linhd["HD"][posn[i]]][Linhd["HD"][posn[i]]][0] == h_stats[j][0]:
                                dfq.append(int(h_stats[j][23]))
                                break
                        break
            else:
                dfq=[0]
        
        if intim_p[0] !=0:
            for k in range(0,len(intim_p)):
                for i in range(0,len(posn)):
                    if intim_p[k] in Linhf["HF"][posn[i]]:
                        for j in range(0,len(h_stats)):
                            if stamina[Linhf["HF"][posn[i]]][Linhf["HF"][posn[i]]][0] == h_stats[j][0]:
                                ifq=(int(h_stats[j][23]))
                                break
                        break
                    elif intim_p[k] in Linhd["HD"][posn[i]]:
                        for j in range(0,len(v_stats)):
                            if stamina[Linhd["HD"][posn[i]]][Linhd["HD"][posn[i]]][0] == h_stats[j][0]:
                                ifq=(int(h_stats[j][23]))
                                break
                        break
        else:
            ifq=0
    
    
    ###############################################################################         
    ###############################################################################
    ###############################################################################        
        
        # NOW DETERMINE SHOT QUALITY, dependent up on type and situation
    if "A" in stype and line_seq["PENH"]==0 and line_seq["PENV"]==0:
    
        shotQ = int(shoot_r[0]) + assist_1 + assist_2 - sum(dfq) - ifq 
   
    elif "A" in stype and (line_seq["PENH"] - line_seq["PENV"]==0):
    
        shotQ = int(shoot_r[0]) + assist_1 + assist_2 - sum(dfq) - ifq                
    
    elif "A" in stype and (line_seq["PENH"]-line_seq["PENV"]==1):
        
        if puckposs["HOME"]==1:
            shotQ = int(shoot_r[1]) + assist_1 + assist_2 - sum(dfq) - ifq
        elif puckposs["VISITOR"]==1:
            shotQ = int(shoot_r[0]) + assist_1 + assist_2 - 2*sum(dfq) - 2*ifq 
    
    elif "A" in stype and (line_seq["PENH"]-line_seq["PENV"]==-1):
        
        if puckposs["VISITOR"]==1:
            shotQ = int(shoot_r[1]) + assist_1 + assist_2 - sum(dfq) - ifq
        elif puckposs["HOME"]==1:
            shotQ = int(shoot_r[0]) + assist_1 + assist_2 - 2*sum(dfq) - 2*ifq 
    
    elif "A" in stype and (line_seq["PENH"]-line_seq["PENV"]>=2):
        
        if puckposs["HOME"]==1:
            shotQ = int(shoot_r[1]) + assist_1 + assist_2 - sum(dfq) - ifq
        elif puckposs["VISITOR"]==1:
            shotQ = int(shoot_r[0]) + assist_1 + assist_2 - 3*sum(dfq) - 3*ifq 
    
    elif "A" in stype and (line_seq["PENH"]-line_seq["PENV"]<=-2):
        
        if puckposs["VISITOR"]==1:
            shotQ = int(shoot_r[1]) + assist_1 + assist_2 - sum(dfq) - ifq
        elif puckposs["HOME"]==1:
            shotQ = int(shoot_r[0]) + assist_1 + assist_2 - 3*sum(dfq) - 3*ifq 
                       
    elif "B" in stype:
    
        shotQ = int(shoot_r[3]) + assist_1 + assist_2 - ifq 
    
    elif "C" in stype:
        
        shotQ = int(shoot_r[4]) + assist_1 + assist_2 - ifq 
                   
    if shotQ <=0:
        shotQ=1
                   
    return shotQ,stype,s_player_type
            
            
        
        
