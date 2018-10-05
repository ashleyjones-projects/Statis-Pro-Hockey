# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:43:49 2017

@author: w9641432
"""

#def get_stamina(stamina):
    
 # Home team
import makerosters
from math import floor
[rosth, rostv] = makerosters.make_rosters() 
                                                               # Visitor 5v5
secs=6
stamina={}
for k, v in rosth.items():
    
    pos = k
    player = v
    
    if "G" not in pos:
  
        for i in range(0,len(v_stats)):
            
            if player in v_stats[i][0]:
                
                vfs = (int(v_stats[i][26]))
                break
        
        if '1' in pos:
            secs1=secs
        elif '2' in pos:    
            secs1=0.9*secs
        elif '3' in pos:    
            secs1=0.8*secs
        elif '4' in pos:    
            if period["PERIOD"]==3 and tid<300:
                secs1=0*secs
            else:
                secs1=0.35*secs
        
        stamina[k] = {k:(player,vfs,vfs-secs1,floor(((vfs-secs1)/vfs)*100))}        
                
    
                                                     
#return stamina                          
                                


    
    
    
    
    
    
    
    