# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:01:46 2018

@author: w9641432
"""

def shot_result(shotQ,puckposs,line_seq,h_stats,v_stats,stamina,Linvf,Linvd,Linhf,Linhd):
    from random import randint 
    import numpy as np
    
    shootpct=50 # HARD CODED PCT NUMBER OF SHOTS GET TO NET
    gpct=0.010 # HARD CODED GOAL PCT ON SHOTS
    bs_pct=20   #HARD CODED BLOCKSHOT PCT
    goalie_bonus = 0.025 # HARD CODED GOALIE BONUS NUMBER, TO BE DETERMINED AS GAME GOES
    shotontarget = randint(1,100)
    if  shotontarget <= shootpct:#shotQ:   # SHOT IS ON TARGET
        
        # OBTAIN GOLAIE RANGE
        
        if puckposs['VISITOR']==1:
            for j in range(0,len(h_stats)):
                if stamina["GH1"]["GH1"][0] == h_stats[j][0]:
                    zone = ((h_stats[j][19]))           # FOR NEUTRAL VALUES CHOOSE 17
                    break
        elif puckposs['HOME']==1:
            for j in range(0,len(h_stats)):
                if stamina["GV1"]["GV1"][0] == h_stats[j][0]:   
                    zone = ((h_stats[j][21]))           # FOR NEUTRAL VALUES CHOOSE 17
                    break
        
        savepct = 0.91# int(zone[0:2])
        control = 2*randint(0,20)
        a_savepct = goalie_bonus + savepct - shotQ/1000 - gpct
        
        saveornot = randint(1,1000)/1000
        
        if saveornot < a_savepct - control:
            result = 'SAVEF'
        elif saveornot >= a_savepct - control and saveornot <=a_savepct:
            result = 'SAVER'
        elif saveornot > a_savepct:
            result = 'GOAL'
            
        
    elif shotontarget > shootpct and shotontarget <= shootpct + bs_pct: # SHOT IS BLOCKED, LOOK FOR REBOUND # 20 IS DEFAULTED HERE!
    
        
        bsr=[]
        
        if puckposs['HOME']==1:
            posn =[0,1,2]
            for i in range(0,len(posn)):
                for j in range(0,len(v_stats)):
                    if 'NONE' in stamina[Linvf["VF"][posn[i]]][Linvf["VF"][posn[i]]][0]:
                        bsr.append(0)
                        break
                    elif stamina[Linvf["VF"][posn[i]]][Linvf["VF"][posn[i]]][0] == v_stats[j][0]:
                        bsr.append(int(v_stats[j][49]))
                        break
            
            posn =[0,1]            
            for i in range(0,len(posn)):   
                for j in range(0,len(v_stats)):
                    if 'NONE' in stamina[Linvd["VD"][posn[i]]][Linvd["VD"][posn[i]]][0]:
                        bsr.append(0)
                        break
                    elif stamina[Linvd["VD"][posn[i]]][Linvd["VD"][posn[i]]][0] == v_stats[j][0]:
                        bsr.append(int(v_stats[j][49]))
                        break
                        
               
        
        elif puckposs['VISITOR']==1:
            posn =[0,1,2]
            for i in range(0,len(posn)):
                for j in range(0,len(h_stats)):
                    if 'NONE' in stamina[Linhf["HF"][posn[i]]][Linhf["HF"][posn[i]]][0]:
                        bsr.append(0)
                        break
                    elif stamina[Linhf["HF"][posn[i]]][Linhf["HF"][posn[i]]][0] == h_stats[j][0]:
                        bsr.append(int(h_stats[j][49]))
                        break
                    
                        
            posn =[0,1]            
            for i in range(0,len(posn)):    
                for j in range(0,len(h_stats)):
                    if 'NONE' in stamina[Linhd["HD"][posn[i]]][Linhd["HD"][posn[i]]][0]:
                        bsr.append(0)
                        break
                    elif stamina[Linhd["HD"][posn[i]]][Linhd["HD"][posn[i]]][0] == h_stats[j][0]:
                        bsr.append(int(h_stats[j][49]))
                        break
                    
                        
    
        # CALCULATE WHO MAKES BLOCK GIVEN WEIGHTS, MAX WEIGHT IS 40%
        bsr = np.cumsum((bsr/np.sum(bsr))*100)
              
        rand_bs = randint(1,100)
        if rand_bs <= bsr[0]:
            player = 'LW'
        elif rand_bs > bsr[0] and rand_bs <= bsr[1]:
            player = 'CE'
        elif bsr[2]==bsr[1]: 
            player = 'LD' 
        elif rand_bs > bsr[1] and rand_bs <= bsr[2]:
            player = 'RW'
        elif rand_bs > bsr[2] and rand_bs <= bsr[3]:
            player = 'LD'
        elif bsr[4] == bsr[3]:
            player = 'LD'
        elif rand_bs > bsr[3] and rand_bs <= bsr[4]:
            player = 'RD'
        
        player='LD'
        result = 'SBLOCK-' + player
        if randint(1,100)<=50:
            puckposs['HOME']=1
            puckposs['VISITOR']=0        
        else:
            puckposs['VISITOR']=1
            puckposs['HOME']=0 
                    
    elif shotontarget > shootpct + bs_pct: # SHOT IS MISSED, LOOK FOR REBOUND # 20 IS DEFAULTED HERE!
    
        result = 'SMISS'
        if randint(1,100)<=50:
            puckposs['HOME']=1
            puckposs['VISITOR']=0        
        else:
            puckposs['VISITOR']=1
            puckposs['HOME']=0 
                
        
    return result,puckposs            
                    
    
        

       
            
            
                        