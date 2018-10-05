# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:36:08 2017

@author: w9641432
"""

def get_defense(shooter,stype,line_seq,Linhf,Linvf,puckposs):
    
#LW defended by C and RD
#C defended by the C, LD, and RD
#RW defended by C and LD
#LD defended by RW
#RD defended by LW

#LW intimidated by RD
#C intimidated by C
#RW intimidated LD
#LD intimidated by RW
#RD intimidated by LW


    def defense_5(shooter):              
        if "LW" in  shooter:
            defense_p = ["C","RD"]
        elif "C" in shooter:
            defense_p = ["C","LD","RD"]
        elif "RW" in shooter:
            defense_p = ["C","LD"]
        elif "LD" in shooter:
            defense_p = ["RW"]
        elif "RD" in shooter:
            defense_p = ["LW"]
        return defense_p
    
    def intim_5(shooter):    
        if "LW" in  shooter:
            intim_p = ["RD"]
        elif "C" in shooter:
            intim_p = ["C"]
        elif "RW" in shooter:
            intim_p = ["LD"]
        elif "LD" in shooter:
            intim_p = ["RW"]
        elif "RD" in shooter:
            intim_p = ["LW"]
        return intim_p    

    def defense_4(shooter):        
        if "LW" in  shooter:
            defense_p = ["RD"]
        elif "C" in shooter:
            defense_p = ["C"]
        elif "RW" in shooter:
            defense_p = ["LD"]
        elif "LD" in shooter:
            defense_p = ["LW"]
        elif "RD" in shooter:
            defense_p = ["C"]
        return defense_p

    def intim_4(shooter):        
        if "LW" in  shooter:
            intim_p = ["RD"]
        elif "C" in shooter:
            intim_p = ["C"]
        elif "RW" in shooter:
            intim_p = ["LD"]
        elif "LD" in shooter:
            intim_p = ["LW"]
        elif "RD" in shooter:
            intim_p = ["C"]
        return intim_p    

    def defense_3(shooter):        
        if "LW" in  shooter:
            defense_p = ["RD"]
        elif "C" in shooter:
            defense_p = ["C"]
        elif "RW" in shooter:
            defense_p = ["LD"]
        elif "LD" in shooter:
            defense_p =[0]
        elif "RD" in shooter:
            defense_p =[0]
        return defense_p
    
    def intim_3(shooter):        
        if "LW" in  shooter:
            intim_p = ["RD"]
        elif "C" in shooter:
            intim_p = ["C"]
        elif "RW" in shooter:
            intim_p = ["LD"]
        elif "LD" in shooter:
            intim_p = [0]
        elif "RD" in shooter:
            intim_p = [0]
        return intim_p     

    def defense_null(shooter):
        if "LW" in  shooter:
            defense_p =[0]
        elif "C" in shooter:
            defense_p =[0]
        elif "RW" in shooter:
            defense_p =[0]
        elif "LD" in shooter:
            defense_p =[0]
        elif "RD" in shooter:
            defense_p =[0]
        return defense_p    

    def intim_null(shooter):        
        if "LW" in  shooter:
            intim_p =[0]
        elif "C" in shooter:
            intim_p =[0]
        elif "RW" in shooter:
            intim_p =[0]
        elif "LD" in shooter:
            intim_p =[0]
        elif "RD" in shooter:
            intim_p =[0]
        return intim_p 
    
    def defense_ext_5(shooter):
        if "LW" in  shooter:
            defense_p = ["RD"]
        elif "C" in shooter:
            defense_p = ["C"]
        elif "RW" in shooter:
            defense_p = ["LD"]
        elif "LD" in shooter:
            defense_p = ["LW"]
        elif "RD" in shooter:
            defense_p = ["RW"]
        elif "EX" in shooter:
            defense_p =[0]
        return defense_p

    def defense_ext_4(shooter):
        if "LW" in  shooter:
            defense_p = ["RD"]
        elif "C" in shooter:
            defense_p = ["C"]
        elif "RW" in shooter:
            defense_p = ["LD"]
        elif "LD" in shooter:
            defense_p = ["LW"]
        elif "RD" in shooter:
            defense_p = ["C"]
        elif "EX" in shooter:
            defense_p =[0]
        return defense_p    

    def defense_ext_3(shooter):        
        if "LW" in  shooter:
            defense_p = ["RD"]
        elif "C" in shooter:
            defense_p = ["C"]
        elif "RW" in shooter:
            defense_p = ["LD"]
        elif "LD" in shooter:
            defense_p =[0]
        elif "RD" in shooter:
            defense_p =[0]
        elif "EX" in shooter:
            defense_p =[0]
        return defense_p    

    def intim_ext_null(shooter):        
        if "LW" in  shooter:
            intim_p =[0]
        elif "C" in shooter:
            intim_p =[0]
        elif "RW" in shooter:
            intim_p =[0]
        elif "LD" in shooter:
            intim_p =[0]
        elif "RD" in shooter:
            intim_p =[0]
        elif "EX" in shooter:
            intim_p =[0]
        return intim_p    
            
    def defense_ext_null(shooter):             
        if "LW" in  shooter:
            defense_p =[0]
        elif "C" in shooter:
            defense_p =[0]
        elif "RW" in shooter:
            defense_p =[0]
        elif "LD" in shooter:
            defense_p =[0]
        elif "RD" in shooter:
            defense_p =[0]
        elif "EX" in shooter:
            defense_p =[0]
        return defense_p  
    
# NOW PROVIDE ALL SITUATIONS AND CHOOSE WHICH DEFINITION IS NEEDED TO GET DEFENSIVE AND INTIM RATINGS    
    # EVENSTRENGTHS
    if '5L' not in Linhf['HF'][0] and '5L' not in Linvf['VF'][0] and '4L' not in Linhf['HF'][0] and '3C' not in Linhf['HF'][1] and '4L' not in Linvf['VF'][0] and '3C' not in Linvf['VF'][1]:
        if 'A' in stype:
            defense_p = defense_5(shooter)
            intim_p   = intim_5(shooter)
        elif 'B' in stype:
            defense_p = defense_null(shooter)
            intim_p   = intim_5(shooter)
        elif 'C' in stype:
            defense_p = defense_null(shooter)
            intim_p   = intim_5(shooter)
    elif '4L' in Linhf['HF'][0] and '4L' in Linvf['VF'][0]:
        if 'A' in stype:
            defense_p = defense_4(shooter)
            intim_p   = intim_4(shooter)
        elif 'B' in stype:
            defense_p = defense_null(shooter)
            intim_p   = intim_4(shooter)
        elif 'C' in stype:
            defense_p = defense_null(shooter)
            intim_p   = intim_4(shooter)
    elif '3C' in Linhf['HF'][1] and '3C' in Linvf['VF'][1]:
        if 'A' in stype:
            defense_p = defense_3(shooter)
            intim_p   = intim_null(shooter)
        elif 'B' in stype:
            defense_p = defense_3(shooter)
            intim_p   = intim_null(shooter)
        elif 'C' in stype:
            defense_p = defense_null(shooter)
            intim_p   = intim_null(shooter)
    #PPLS 5v4
    elif '4K' in Linhf['HF'][0] and '5L' in Linvf['VF'][0]:
        if puckposs['VISITOR']==1:
            if 'A' in stype:
                defense_p = defense_4(shooter)
                intim_p   = intim_null(shooter)
            elif 'B' in stype:
                defense_p = defense_4(shooter)
                intim_p   = intim_null(shooter)
            elif 'C' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
        elif puckposs['HOME']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_5(shooter)
    elif '5L' in Linhf['HF'][0] and '4K' in Linvf['VF'][0]:
        if puckposs['VISITOR']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_5(shooter)
        elif puckposs['HOME']==1:
            if 'A' in stype:
                defense_p = defense_4(shooter)
                intim_p   = intim_null(shooter)
            elif 'B' in stype:
                defense_p = defense_4(shooter)
                intim_p   = intim_null(shooter)
            elif 'C' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
    #PPLS 5v3
    elif '3K' in Linhf['HF'][1] and '5L' in Linvf['VF'][0]:
        if puckposs['VISITOR']==1:
            if 'A' in stype:
                defense_p = defense_3(shooter)
                intim_p   = intim_null(shooter)
            elif 'B' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
            elif 'C' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
        elif puckposs['HOME']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_5(shooter)
    elif '5L' in Linhf['HF'][0] and '3K' in Linvf['VF'][1]:
        if puckposs['VISITOR']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_5(shooter)
        elif puckposs['HOME']==1:
            if 'A' in stype:
                defense_p = defense_3(shooter)
                intim_p   = intim_null(shooter)
            elif 'B' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
            elif 'C' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
    #PPLS 4v3
    elif '3K' in Linhf['HF'][1] and '4L' in Linvf['VF'][0]:
        if puckposs['VISITOR']==1:
            if 'A' in stype:
                defense_p = defense_3(shooter)
                intim_p   = intim_null(shooter)
            elif 'B' in stype:
                defense_p = defense_3(shooter)
                intim_p   = intim_null(shooter)
            elif 'C' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
        elif puckposs['HOME']==1:
            defense_p = defense_4(shooter)
            intim_p   = intim_4(shooter)
    elif '4L' in Linhf['HF'][0] and '3K' in Linvf['VF'][1]:
        if puckposs['VISITOR']==1:
            defense_p = defense_4(shooter)
            intim_p   = intim_4(shooter)
        elif puckposs['HOME']==1:
            if 'A' in stype:
                defense_p = defense_3(shooter)
                intim_p   = intim_null(shooter)
            elif 'B' in stype:
                defense_p = defense_3(shooter)
                intim_p   = intim_null(shooter)
            elif 'C' in stype:
                defense_p = defense_null(shooter)
                intim_p   = intim_null(shooter)
    #EXT 6V5
    elif line_seq['EAV']==1 and line_seq['GV']==0 and '4L' not in Linhf['HF'][0] and '3C' not in Linhf['HF'][1] and '4K' not in Linhf['HF'][0] and '3K' not in Linhf['HF'][1]:            
        if puckposs['VISITOR']==1:
            if 'A' in stype:
                defense_p = defense_ext_5(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'B' in stype:
                defense_p = defense_ext_5(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'C' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
        elif puckposs['HOME']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_null(shooter)
    elif line_seq['EAH']==1 and line_seq['GH']==0 and '4L' not in Linvf['VF'][0] and '3C' not in Linvf['VF'][1] and '4K' not in Linhf['HF'][0] and '3K' not in Linhf['HF'][1]:            
        if puckposs['HOME']==1:
            if 'A' in stype:
                defense_p = defense_ext_5(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'B' in stype:
                defense_p = defense_ext_5(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'C' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
        elif puckposs['VISITOR']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_null(shooter)
    # EXT 6V4
    elif line_seq['EAV']==1 and line_seq['GV']==0 and '4K' in Linhf['HF'][0]:            
        if puckposs['VISITOR']==1:
            if 'A' in stype:
                defense_p = defense_ext_4(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'B' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'C' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
        elif puckposs['HOME']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_null(shooter)
    elif line_seq['EAH']==1 and line_seq['GH']==0 and '4K' in Linvf['VF'][0]:            
        if puckposs['HOME']==1:
            if 'A' in stype:
                defense_p = defense_ext_4(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'B' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'C' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
        elif puckposs['VISITOR']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_null(shooter) 
    # EXT 6V3
    elif line_seq['EAV']==1 and line_seq['GV']==0 and '3K' in Linhf['HF'][1]:            
        if puckposs['VISITOR']==1:
            if 'A' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'B' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'C' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
        elif puckposs['HOME']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_null(shooter)
    elif line_seq['EAH']==1 and line_seq['GH']==0 and '3K' in Linvf['VF'][1]:            
        if puckposs['HOME']==1:
            if 'A' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'B' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
            elif 'C' in stype:
                defense_p = defense_ext_null(shooter)
                intim_p   = intim_ext_null(shooter)
        elif puckposs['VISITOR']==1:
            defense_p = defense_5(shooter)
            intim_p   = intim_null(shooter)             
     
    return defense_p,intim_p