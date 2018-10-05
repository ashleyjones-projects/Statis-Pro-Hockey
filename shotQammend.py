# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:43:28 2018

@author: w9641432
"""

def shotQ_ammend(shotQ,diff_s,puckposs):
    
    # USED TO DETERMINE IF THERE IS A GAIN/LOSS IN SHOT QUALITY TO TEAM WITH PUCK
    # BASED ON STAMINA. DIFF_S IS DTERMINED BY SUBTRATCTING 
    
    #   VISITOR_SYAMINA - HOME_STAMINA
    # IF STAMINA IS >100 IN EITHER CASE, THERE IS A ADVANTAGE TO THAT TEAM REGARDLESS
    # OF PUCK POSESSION
    # FOR EVERY 10 ABOVE 100 THAT TEAM IS AWARDED AN EXTRA SHOTQ NUMBER
    
    if diff_s >= 100:
        
        ammended = round((abs(diff_s)-100)/10)
        
        if puckposs['VISITOR']==1:
            shotQ=shotQ + ammended
        elif puckposs['HOME']==1:
            shotQ=shotQ - ammended
            
    elif diff_s <= -100:
        
        ammended = round((abs(diff_s)-100)/10)
        
        if puckposs['VISITOR']==1:
            shotQ=shotQ - ammended
        elif puckposs['HOME']==1:
            shotQ=shotQ + ammended
            
    return shotQ        
        
        

         
            
            
        