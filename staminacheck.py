# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:38:24 2017

@author: w9641432
"""

def stamina_check(stamina,h_stats,v_stats,Linhf,Linhd,Linvf,Linvd,secs,period,tid,penbox,line_seq):
    
    
    from math import floor
    import makerosters
    
    [rosth, rostv] = makerosters.make_rosters(penbox,line_seq,Linhf,Linhd,Linvf,Linvd)
    Linehf = Linhf["HF"]
    Linehd = Linhd["HD"]
      
    pos = ['GH1','GH2','5LWH1','5CH1','5RWH1','5LWH2',
     '5CH2','5RWH2','5LDH1','5RDH1','5LDH2','5RDH2','4KLWH1','4KCH1','4KLWH2','4KCH2',
     '4KLDH1','4KRDH1','4KLDH2','4KRDH2','4LWH1','4CH1','4LWH2','4CH2','4LDH1','4RDH1',
     '4LDH2','4RDH2','3KLDH1','3KCH1','3KRDH1','3KLDH2','3KCH2','3KRDH2','3LWH1','3CH1',
     '3LDH1','3LWH2','3CH2','3LDH2','3LWH3','3CH3','3LDH3']
    reg_pos=['LWH1','CH1','RWH1','LWH2','CH2','RWH2','LWH3','CH3','RWH3','LWH4','CH4','RWH4',
     'LDH1','RDH1','LDH2','RDH2','LDH3','RDH3']
    
    for i in range(0,len(reg_pos)):
        
        name=rosth[reg_pos[i]]
        for k in range(0,len(h_stats)):
                
                if name in h_stats[k][0]:
                    
                    vfs = (int(h_stats[k][26]))
                    break
        
        pos_list = [reg_pos[i]]
        ind=0
        for j in range(0,len(pos)):
            
            if name in rosth[pos[j]]:
                pos_list.append(pos[j])
        
        for j in range(0,len(pos_list)):
            if pos_list[j] in Linehf or pos_list[j] in Linehd:
                ind = 1
        
        if ind > 0:
            for m in range(0,len(pos_list)):
                numerator = round(stamina[pos_list[m]][pos_list[m]][2]-secs,2)
                pct = floor(((numerator)/vfs)*100)
                if pct< 0:
                    pct=0
                    numerator=0
                stamina[pos_list[m]] = {pos_list[m]:(name,vfs,numerator,pct)} 
        else:
             if '1' in pos_list[0]:
                secs1 = secs
             elif '2' in pos_list[0]:    
                secs1=0.6*secs
             elif '3' in pos_list[0]:    
                secs1=0.4*secs
             elif '4' in pos_list[0]:    
                 if period["PERIOD"]==3 and tid<300:
                     secs1=0*secs
                 else:
                     secs1=0.25*secs
             for m in range(0,len(pos_list)):        
                 numerator = round(stamina[pos_list[m]][pos_list[m]][2]+secs1,2)
                 pct = floor(((numerator)/vfs)*100)
                 if pct> 100:
                    pct=100
                    numerator = vfs
                    
                 stamina[pos_list[m]] = {pos_list[m]:(name,vfs,numerator,pct)}         
                
    
    Linevf = Linvf["VF"]
    Linevd = Linvd["VD"]
      
    pos = ['GV1','GV2','5LWV1','5CV1','5RWV1','5LWV2',
     '5CV2','5RWV2','5LDV1','5RDV1','5LDV2','5RDV2','4KLWV1','4KCV1','4KLWV2','4KCV2',
     '4KLDV1','4KRDV1','4KLDV2','4KRDV2','4LWV1','4CV1','4LWV2','4CV2','4LDV1','4RDV1',
     '4LDV2','4RDV2','3KLDV1','3KCV1','3KRDV1','3KLDV2','3KCV2','3KRDV2','3LWV1','3CV1',
     '3LDV1','3LWV2','3CV2','3LDV2','3LWV3','3CV3','3LDV3']
    reg_pos=['LWV1','CV1','RWV1','LWV2','CV2','RWV2','LWV3','CV3','RWV3','LWV4','CV4','RWV4',
     'LDV1','RDV1','LDV2','RDV2','LDV3','RDV3']
    
    for i in range(0,len(reg_pos)):
        
        name=rostv[reg_pos[i]]
        for k in range(0,len(v_stats)):
                
                if name in v_stats[k][0]:
                    
                    vfs = (int(v_stats[k][26]))
                    break
        
    
        pos_list = [reg_pos[i]]
        ind=0
        for j in range(0,len(pos)):
            
            if name in rostv[pos[j]]:
                pos_list.append(pos[j])
        
        for j in range(0,len(pos_list)):
            if pos_list[j] in Linevf or pos_list[j] in Linevd:
                ind = 1
        
        if ind > 0:
            for m in range(0,len(pos_list)):
                numerator = round(stamina[pos_list[m]][pos_list[m]][2]-secs,2)
                pct = floor(((numerator)/vfs)*100)
                if pct< 0:
                    pct=0
                    numerator=0
                stamina[pos_list[m]] = {pos_list[m]:(name,vfs,numerator,pct)} 
        else:
             if '1' in pos_list[0]:
                secs1 = secs
             elif '2' in pos_list[0]:    
                secs1=0.9*secs
             elif '3' in pos_list[0]:    
                secs1=0.8*secs
             elif '4' in pos_list[0]:    
                 if period["PERIOD"]==3 and tid<300:
                     secs1=0*secs
                 else:
                     secs1=0.35*secs
             for m in range(0,len(pos_list)):        
                 numerator = round(stamina[pos_list[m]][pos_list[m]][2]+secs1,2)
                 pct = floor(((numerator)/vfs)*100)
                 if pct> 100:
                    pct=100
                    numerator = vfs
                    
                 stamina[pos_list[m]] = {pos_list[m]:(name,vfs,numerator,pct)}         
                    
 
    # CHECK DIFFERENCE IN STAMINA TO DETERMINE IF THERE IS A MISMATCH
    # VISITOR
     
    if "4L" in  Linvf["VF"][0] or "4C" in  Linvf["VF"][0] or "4R" in  Linvf["VF"][0] or "4K" in Linvf["VF"][0] or "3L" in Linvf["VF"][0] or "3C" in Linvf["VF"][0] or "3R" in Linvf["VF"][0]:      
        vfs_avg = (stamina[Linvf["VF"][0]][Linvf["VF"][0]][3] + stamina[Linvf["VF"][1]][Linvf["VF"][1]][3] + 0)/2
    else:
        vfs_avg = (stamina[Linvf["VF"][0]][Linvf["VF"][0]][3] + stamina[Linvf["VF"][1]][Linvf["VF"][1]][3] + stamina[Linvf["VF"][2]][Linvf["VF"][2]][3])/3
    
    if "3L" in Linvd["VD"][0]:
        vds_avg = (stamina[Linvd["VD"][0]][Linvd["VD"][0]][3] + 0)/1
    else:
        vds_avg = (stamina[Linvd["VD"][0]][Linvd["VD"][0]][3] + stamina[Linvd["VD"][1]][Linvd["VD"][1]][3])/2 
          
    
    
# HOME
    if "4L" in  Linhf["HF"][0] or "4C" in  Linhf["HF"][0] or "4R" in  Linhf["HF"][0] or "4K" in Linhf["HF"][0] or "3L" in Linhf["HF"][0] or "3C" in Linhf["HF"][0] or "3R" in Linhf["HF"][0]:      
        hfs_avg = (stamina[Linhf["HF"][0]][Linhf["HF"][0]][3] + stamina[Linhf["HF"][1]][Linhf["HF"][1]][3] + 0)/2
    else:
        hfs_avg = (stamina[Linhf["HF"][0]][Linhf["HF"][0]][3] + stamina[Linhf["HF"][1]][Linhf["HF"][1]][3] + stamina[Linhf["HF"][2]][Linhf["HF"][2]][3])/3

   
    if "3L" in Linhd["HD"][0]:
        hds_avg = (stamina[Linhd["HD"][0]][Linhd["HD"][0]][3] + 0)/1 
    else:
        hds_avg = (stamina[Linhd["HD"][0]][Linhd["HD"][0]][3] + stamina[Linhd["HD"][1]][Linhd["HD"][1]][3])/2  
    
                 
                       
            
    diff_s = (vfs_avg+vds_avg) - (hfs_avg+hds_avg)
        
    return stamina,diff_s          
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#                   
#               
#               
#               
#               
#               