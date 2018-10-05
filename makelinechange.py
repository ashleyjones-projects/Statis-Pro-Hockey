# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:18:08 2017

@author: w9641432
"""


def make_line_change(line_seq,period,penbox,Linhf,Linhd,Linvf,Linvd):
    
    import makerosters
    
    [rosth, rostv] = makerosters.make_rosters(penbox,line_seq,Linhf,Linhd,Linvf,Linvd)
    # ES LINES LOAD UP
    
    if line_seq["PENH"] == 0 and line_seq["PENV"] == 0:
            
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("LWH1","CH1","RWH1"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("LWH2","CH2","RWH2"),"NUM": 2}
        elif line_seq["LINHF"] == 3:
            Linhf = {"HF":("LWH3","CH3","RWH3"),"NUM": 3}
        elif line_seq["LINHF"] == 4:
            Linhf = {"HF":("LWH4","CH4","RWH4"),"NUM": 4}    
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("LDH1","RDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("LDH2","RDH2"),"NUM": 2}
        elif line_seq["LINHD"] == 3:
            Linhd = {"HD":("LDH3","RDH3"),"NUM": 3}    
                
   
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("LWV1","CV1","RWV1"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("LWV2","CV2","RWV2"),"NUM": 2}
        elif line_seq["LINVF"] == 3:
            Linvf = {"VF":("LWV3","CV3","RWV3"),"NUM": 3}
        elif line_seq["LINVF"] == 4:
            Linvf = {"VF":("LWV4","CV4","RWV4"),"NUM": 4}    
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("LDV1","RDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("LDV2","RDV2"),"NUM": 2}
        elif line_seq["LINVD"] == 3:
            Linvd = {"VD":("LDV3","RDV3"),"NUM": 3}      
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}
            
    elif line_seq["PENH"] == 1 and line_seq["PENV"] == 0:  # PP visitor 5v4
        
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("4KLWH1","4KCH1","NONE"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("4KLWH2","4KCH2","NONE"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("4KLDH1","4KRDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("4KLDH2","4KRDH2"),"NUM": 2}
   
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("5LWV1","5CV1","5RWV1"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("5LWV2","5CV2","5RWV2"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("5LDV1","5RDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("5LDV2","5RDV2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}
                      
    elif line_seq["PENH"] == 0 and line_seq["PENV"] == 1:  # PP home 5v4
    
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("4KLWV1","4KCV1","NONE"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("4KLWV2","4KCV2","NONE"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("4KLDV1","4KRDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("4KLDV2","4KRDV2"),"NUM": 2}
   
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("5LWH1","5CH1","5RWH1"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("5LWH2","5CH2","5RWH2"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("5LDH1","5RDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("5LDH2","5RDH2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}
    
    elif (line_seq["PENH"] == 0 and line_seq["PENV"] == 2) or (line_seq["PENH"]==1 and line_seq["PENV"]==3) or (line_seq["PENH"]==2 and line_seq["PENV"]==4) or (line_seq["PENH"]==3 and line_seq["PENV"]==5):  # PP home 5v3
    
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("NONE","3KCV1","NONE"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("NONE","3KCV2","NONE"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("3KLDV1","3KRDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("3KLDV2","3KRDV2"),"NUM": 2}
   
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("5LWH1","5CH1","5RWH1"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("5LWH2","5CH2","5RWH2"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("5LDH1","5RDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("5LDH2","5RDH2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}        
    
    elif (line_seq["PENH"] == 2 and line_seq["PENV"] == 0) or (line_seq["PENH"] == 3 and line_seq["PENV"]==1) or (line_seq["PENH"]==4 and line_seq["PENV"]==2) or (line_seq["PENH"]==5 and line_seq["PENV"]==3):  # PP visitor 5v3
        
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("NONE","3KCH1","NONE"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("NONE","3KCH2","NONE"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("3KLDH1","3KRDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("3KLDH2","3KRDH2"),"NUM": 2}
   
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("5LWV1","5CV1","5RWV1"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("5LWV2","5CV2","5RWV2"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("5LDV1","5RDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("5LDV2","5RDV2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}
    
            
    elif (line_seq["PENH"] == 1 and line_seq["PENV"] == 1) or (line_seq["PENH"] == 2 and line_seq["PENV"] == 2) or (line_seq["PENH"] == 3 and line_seq["PENV"] == 3) or (line_seq["PENH"] == 4 and line_seq["PENV"] == 4) or (line_seq["PENH"] == 5 and line_seq["PENV"] == 5):  # 4v4 or case where would be 3v3 (in reg time) or 2v2 etc
    
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("4LWV1","4CV1","NONE"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("4LWV2","4CV2","NONE"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("4LDV1","4RDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("4LDV2","4RDV2"),"NUM": 2}
   
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("4LWH1","4CH1","NONE"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("4LWH2","4CH2","NONE"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("4LDH1","4RDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("4LDH2","4RDH2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1} 
            
    elif line_seq["PENH"] == 1 and line_seq["PENV"] == 2:  # PP home 4V3
    
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("NONE","3KCV1","NONE"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("NONE","3KCV2","NONE"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("3KLDV1","3KRDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("3KLDV2","3KRDV2"),"NUM": 2}
   
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("4LWH1","4CH1","NONE"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("4LWH2","4CH2","NONE"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("4LDH1","4RDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("4LDH2","4RDH2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}        
    
    elif line_seq["PENH"] == 2 and line_seq["PENV"] == 1:  # PP visitor 4V3
        
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("NONE","3KCH1","NONE"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("NONE","3KCH2","NONE"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("3KLDH1","3KRDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("3KLDH2","3KRDH2"),"NUM": 2}
   
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("4LWV1","4CV1","NONE"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("4LWV2","4CV2","NONE"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("4LDV1","4RDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("4LDV2","4RDV2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1} 
            
    elif (line_seq["PENH"]==0 and line_seq["PENV"]==3) or (line_seq["PENH"]==1 and line_seq["PENV"]==4) or (line_seq["PENH"]==2 and line_seq["PENV"]==5): # HOME PP 5V3
    
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("NONE","3KCV1","NONE"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("NONE","3KCV2","NONE"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("3KLDV1","3KRDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("3KLDV2","3KRDV2"),"NUM": 2}
   
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("5LWH1","5CH1","5RWH1"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("5LWH2","5CH2","5RWH2"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("5LDH1","5RDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("5LDH2","5RDH2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}        
    
    elif (line_seq["PENH"]==3 and line_seq["PENV"]==0) or (line_seq["PENH"]==4 and line_seq["PENV"]==1) or (line_seq["PENH"]==5 and line_seq["PENV"]==2): # VISITOR PP 5V3
        
        if line_seq["LINHF"] == 1:
            Linhf = {"HF":("NONE","3KCH1","NONE"),"NUM": 1}
        elif line_seq["LINHF"] == 2:
            Linhf = {"HF":("NONE","3KCH2","NONE"),"NUM": 2}
        
        if line_seq["LINHD"] == 1:
            Linhd = {"HD":("3KLDH1","3KRDH1"),"NUM": 1}
        elif line_seq["LINHD"] == 2:
            Linhd = {"HD":("3KLDH2","3KRDH2"),"NUM": 2}
   
        if line_seq["LINVF"] == 1:
            Linvf = {"VF":("5LWV1","5CV1","5RWV1"),"NUM": 1}
        elif line_seq["LINVF"] == 2:
            Linvf = {"VF":("5LWV2","5CV2","5RWV2"),"NUM": 2}
        
        if line_seq["LINVD"] == 1:
            Linvd = {"VD":("5LDV1","5RDV1"),"NUM": 1}
        elif line_seq["LINVD"] == 2:
            Linvd = {"VD":("5LDV2","5RDV2"),"NUM": 2}
                
        if line_seq["GH"] > 0:
            # Change needed
            Linhg = {"HG":"GH1","NUM": 1}
            
        if line_seq["GV"] > 0:
            # Change needed
            Linvg = {"VG":"GV1","NUM": 1}        
        
                
            
    return Linhf, Linhd, Linvf, Linvd, Linhg, Linvg            
