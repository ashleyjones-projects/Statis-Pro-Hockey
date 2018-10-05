# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:47:33 2017

@author: w9641432
"""

def stamina_init(h_stats,v_stats,penbox,line_seq,Linhf,Linhd,Linvf,Linvd):
    
    import makerosters
    from math import floor
    
    [rosth, rostv] = makerosters.make_rosters(penbox,line_seq,Linhf,Linhd,Linvf,Linvd) 
                                                                   # Visitor 5v5
    
    staminah={}
    staminav={}
    for k, v in rosth.items():
        
        pos = k
        player = v
        
        if "G" not in pos:
      
            for i in range(0,len(h_stats)):
                
                if player in h_stats[i][0]:
                    
                    vfs = (int(h_stats[i][26]))
                    break
                      
            numerator = vfs
            pct = floor(((numerator)/vfs)*100)
            
                            
            staminah[k] = {k:(player,vfs,numerator,pct)}
        else:
            staminah[k] = {k:(player,100,100,100)}
            
    for k, v in rostv.items():
        
        pos = k
        player = v
        
        if "G" not in pos:
      
            for i in range(0,len(v_stats)):
                
                if player in v_stats[i][0]:
                    
                    vfs = (int(v_stats[i][26]))
                    break
           
            numerator = vfs
            pct = floor(((numerator)/vfs)*100)
           
            staminav[k] = {k:(player,vfs,numerator,pct)}
        else:
            staminav[k] = {k:(player,100,100,100)}     
            
    stamina = dict(staminah,**staminav)   
    return stamina
         