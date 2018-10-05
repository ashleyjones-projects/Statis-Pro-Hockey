# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:47:39 2017

@author: w9641432
"""

def shoot_or_dump(diff_s,line_ticker,shotQ,stype,line_seq,puckposs):
    
    # IF THE DIFFERENCE BETWEEN DIFFS IS LARGER THEN ABS(100) THEN OPPORTUNITY TO CHANGE IF HAVE POSSESSION
    if (diff_s) >= 100 and "A" not in stype:
        if puckposs["HOME"] ==1:
            line_ticker["HD"]=6;line_ticker["HF"]=6
            shoot=0
        else:
            shoot=1
            
    elif (diff_s) <= -100 and "A" not in stype:
        if puckposs["VISITOR"] == 1:
            line_ticker["VD"]=6;line_ticker["VF"]=6
            shoot=0           
            
        else:
            shoot=1
    elif puckposs["HOME"]==1 and "A" not in stype:
        if line_ticker["HD"] > 4 or line_ticker["HF"] > 4:
            shoot= 0
        else:
            shoot=1
    elif puckposs["VISITOR"]==1 and "A" not in stype:
        if line_ticker["VD"] > 4 or line_ticker["VF"] > 4:
            shoot= 0
        else:
            shoot=1   
    else:
        shoot=1
    return shoot,line_ticker
            
    
    
    
    