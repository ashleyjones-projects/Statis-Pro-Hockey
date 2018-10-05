# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:15:48 2017

@author: w9641432
"""

from random import randint

def face_off(Linvf,Linhf,v_stats,h_stats,stamina):
    
    vf = stamina[Linvf["VF"][1]][Linvf["VF"][1]][0]
    hf = stamina[Linhf["HF"][1]][Linhf["HF"][1]][0]
    
    # Find visiting centre
    for i in range(0,len(v_stats)):
        
        if vf in v_stats[i][0]:
            
            fo_vf = int(v_stats[i][25])
            break
   # Find home centre
    for i in range(0,len(h_stats)):
        
        if hf in h_stats[i][0]:
            
            fo_hf = int(v_stats[i][25])
            break
    # Who wins F/O
    
    if fo_vf > fo_hf:
        
        diff = fo_vf - fo_hf
        rand = randint(1,100)
        if diff == 1:
            if rand < 55:
                puckposs = {"VISITOR": 1, "HOME": 0}
            else:
                puckposs = {"VISITOR": 0, "HOME": 1}
        elif diff == 2:
            if rand < 59:
                puckposs = {"VISITOR": 1, "HOME": 0}
            else:
                puckposs = {"VISITOR": 0, "HOME": 1}
        elif diff == 3:
            if rand < 63:
                puckposs = {"VISITOR": 1, "HOME": 0}
            else:
                puckposs = {"VISITOR": 0, "HOME": 1}        
        elif diff == 4:
            if rand < 67:
                puckposs = {"VISITOR": 1, "HOME": 0}
            else:
                puckposs = {"VISITOR": 0, "HOME": 1}
                
    elif fo_hf > fo_vf:
        
        diff = fo_hf - fo_vf
        rand = randint(1,100)
        if diff == 1:
            if rand < 55:
                puckposs = {"VISITOR": 0, "HOME": 1}
            else:
                puckposs = {"VISITOR": 1, "HOME": 0}
        elif diff == 2:
            if rand < 59:
                puckposs = {"VISITOR": 0, "HOME": 1}
            else:
                puckposs = {"VISITOR": 1, "HOME": 0}
        elif diff == 3:
            if rand < 63:
                puckposs = {"VISITOR": 0, "HOME": 1}
            else:
                puckposs = {"VISITOR": 1, "HOME": 0}        
        elif diff == 4:
            if rand < 67:
                puckposs = {"VISITOR": 0, "HOME": 1}
            else:
                puckposs = {"VISITOR": 1, "HOME": 0}
                
    else:
         rand = randint(1,100)
         if rand < 51:
             puckposs = {"VISITOR": 0, "HOME": 1}
         else:
             puckposs = {"VISITOR": 1, "HOME": 0}
             
    return puckposs        
             
         
            
            
            
        
    
    