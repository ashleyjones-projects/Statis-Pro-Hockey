# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:59:10 2017

@author: w9641432
"""

def manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker):
    limitf=40
    limitd=50
    # CALCULATE AVERAGE LIINE STAMINA FOR EACH LINE
    
    # VISITOR
    if Linvf["NUM"] == 1:
        vfs_avg = (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 
    elif Linvf["NUM"] == 2:
        vfs_avg = (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 
    elif Linvf["NUM"] == 3:
        vfs_avg = (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3
    elif Linvf["NUM"] == 4:
        vfs_avg = (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3
    
    if Linvd["NUM"] == 1:
        vds_avg = (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 
    elif Linvd["NUM"] == 2:
        vds_avg = (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 
    elif Linvd["NUM"] == 3:
        vds_avg = (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2
    
    # HOME
    if Linhf["NUM"] == 1:
        hfs_avg = (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 
    elif Linhf["NUM"] == 2:
        hfs_avg = (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 
    elif Linhf["NUM"] == 3:
        hfs_avg = (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3
    elif Linhf["NUM"] == 4:
        hfs_avg = (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3
    
    if Linhd["NUM"] == 1:
        hds_avg = (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 
    elif Linhd["NUM"] == 2:
        hds_avg = (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 
    elif Linhd["NUM"] == 3:
        hds_avg = (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2
    
    # IF AVERAGE LINE STAMINA LESS THAN 40%, LOOK TO CHANGE. HOWEVER CHANGES ARE DEPENDENT UPON GAME FLOW AND 
    # STOPPAGES. 
    # 
    # IN GAME FLOW, CAN ONLY MAKE A CHANGE IF YOU HAVE THE PUCK ON EITHER A SHOT ATTEMPT B OR C (DUMP IN)
    # RESULTING IN A CHANGE OF POSESSION, PASSSPACE, WHERE POSESSION TEAM DMAN WAITS BEHIND NET FOR THE CHANGE.
    # THAT ONE REMAING PLAYER WILL CHANGE AS LONG AS NEXT RESULTING FAC IS NOT A GW OR TK. THE CHANGE WILL
    # TAKE 5 EXTRA SECONDS TO HIS TOTAL. STAMINA RATINGS WILL CONTINUE AS NORMAL TO ALL LINES 
    #
    # STOPPAGE IN PLAY, BOTH TEAMS CAN MAKE A CHANGE AS LONG AS THE VISTING TEAM MUST PUT THEIR LINE OUT FIRST
    # THEN THE HOME TEAM CAN MATCH THE LINE. EXCEPTION TO THIS IS ICING, WHERE ICING TEAM MUST KEEP THE
    # SAME LINE ON.
    
    # A NEW LINE CANT COME BACK ON UNTIL THEY HAVE REACHED ATLEAST 80% OF STAMINA. THIS WILL ENSURE PROPER AI AND
    # CORRECT ALLOCATION OF SHIFTS PER LINE 
    
    # THE CODE WILL OFFER A MANUAL SELECTION FOR ONE OR BOTH TEAMS, OR USE AI TO DO THE JOB. THIS IS THE HARDEST
    # PART TO CODE!
    
    if mode["HOME"] ==0 and mode["VISITOR"] == 0: # PURE AI
       
       if "ICING" in s_player_type:
            
            if "ICING_0" in s_player_type: # HOME TEAM ICE PUCK
                line_ticker["VF"]=0;line_ticker["VD"]=0;
                if (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                       line_seq["LINVF"] = 1
                elif (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                       line_seq["LINVF"] = 2
                elif (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                       line_seq["LINVF"] = 3
                               
                if (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 > 80:
                       line_seq["LINVD"] = 1
                elif (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 > 80:
                       line_seq["LINVD"] = 2
                elif (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2 > 80:
                       line_seq["LINVD"] = 3               
                               
            elif "ICING_1" in s_player_type: # VISTING TEAM ICE PUCK
                line_ticker["HF"]=0;line_ticker["HD"]=0;
                if (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                       line_seq["LINHF"] = 1
                elif (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                       line_seq["LINHF"] = 2
                elif (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                       line_seq["LINHF"] = 3 
                
                if (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 > 80:
                       line_seq["LINHD"] = 1
                elif (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 > 80:
                       line_seq["LINHD"] = 2
                elif (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2 > 80:
                       line_seq["LINHD"] = 3 
                               
       elif line_ticker["HF"]>4 or line_ticker["VF"]>4 or line_ticker["HD"]>4 or line_ticker["VD"]>4:
           if puckposs["HOME"]==1:
               if line_ticker["HF"]>4:
                   line_ticker["HF"]=0
                   # HOME FORWARDS           
                   if Linhf["NUM"] == 1:
                       if (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                           line_seq["LINHF"] = 2
                       elif (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                           line_seq["LINHF"] = 3
                       elif (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                           line_seq["LINHF"] = 4
                   elif Linhf["NUM"] == 2:
                       if (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                           line_seq["LINHF"] = 3
                       elif (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                           line_seq["LINHF"] = 4
                       elif (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                           line_seq["LINHF"] = 1                
                   elif Linhf["NUM"] == 3:
                       if (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                           line_seq["LINHF"] = 4
                       elif (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                           line_seq["LINHF"] = 1
                       elif (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                           line_seq["LINHF"] = 2
                   elif Linhf["NUM"] == 4:
                       if (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                           line_seq["LINHF"] = 1
                       elif (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                           line_seq["LINHF"] = 2
                       elif (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                           line_seq["LINHF"] = 3
               
               if line_ticker["HD"] > 4:
                   line_ticker["HD"] = 0
                   puckposs={"HOME":0,"VISITOR":1} # ASSUMED HERE THAT DMEN CHANGE, ITS A DUMP AND CHANGE EVENTHOUGH FORWARS STILL ON
                   # visinitng DMEN                
           
                   # HOME DMEN                
                   if Linhd["NUM"] == 1:
                       if (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 > 80:
                           line_seq["LINHD"] = 2
                       elif (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2 > 80:
                           line_seq["LINHD"] = 3
                   elif Linhd["NUM"] == 2:
                       if (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2 > 80:
                           line_seq["LINHD"] = 3
                       elif (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 > 80:
                           line_seq["LINHD"] = 1
                   elif Linhd["NUM"] == 3:
                       if (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 > 80:
                           line_seq["LINHD"] = 1
                       elif (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 > 80:
                           line_seq["LINHD"] = 2
           elif puckposs["VISITOR"]==1: 
               if line_ticker["VF"]>4:
                   line_ticker["VF"]=0
                   # visting FORWARDS           
                   if Linvf["NUM"] == 1:
                       if (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                           line_seq["LINVF"] = 2
                       elif (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                           line_seq["LINVF"] = 3
                       elif (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                           line_seq["LINVF"] = 4
                   elif Linvf["NUM"] == 2:
                       if (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                           line_seq["LINVF"] = 3
                       elif (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                           line_seq["LINVF"] = 4
                       elif (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                           line_seq["LINVF"] = 1                
                   elif Linvf["NUM"] == 3:
                       if (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                           line_seq["LINVF"] = 4
                       elif (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                           line_seq["LINVF"] = 1
                       elif (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                           line_seq["LINVF"] = 2
                   elif Linvf["NUM"] == 4:
                       if (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                           line_seq["LINVF"] = 1
                       elif (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                           line_seq["LINVF"] = 2
                       elif (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                           line_seq["LINVF"] = 3
               
               if line_ticker["VD"] > 4:
                   line_ticker["VD"] = 0
                   puckposs ={"HOME":1,"VISITOR":0} # ASSUMED HERE THAT DMEN CHANGE, ITS A DUMP AND CHANGE EVENTHOUGH FORWARS STILL ON
                   # visinitng DMEN                
           
                   # visinitng DMEN                
                   if Linvd["NUM"] == 1:
                       if (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 > 80:
                           line_seq["LINVD"] = 2
                       elif (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2 > 80:
                           line_seq["LINVD"] = 3
                   elif Linvd["NUM"] == 2:
                       if (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2 > 80:
                           line_seq["LINVD"] = 3
                       elif (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 > 80:
                           line_seq["LINVD"] = 1
                   elif Linvd["NUM"] == 3:
                       if (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 > 80:
                           line_seq["LINVD"] = 1
                       elif (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 > 80:
                           line_seq["LINVD"] = 2        
                   
       elif "PUCKDEFLECTEDOUT" in s_player_type or "OFFSIDE" in s_player_type or "FROZENPUCK" in s_player_type or result["GOAL"]==1:
           
           if vfs_avg < limitf: # LOOK TO CHANGE
               # VISTING FORWARDS
               line_ticker["VF"]=0
               if Linvf["NUM"] == 1:
                   if (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                       line_seq["LINVF"] = 2
                   elif (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                       line_seq["LINVF"] = 3
                   elif (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                       line_seq["LINVF"] = 4
               elif Linvf["NUM"] == 2:
                   if (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                       line_seq["LINVF"] = 3
                   elif (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                       line_seq["LINVF"] = 4
                   elif (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                       line_seq["LINVF"] = 1                
               elif Linvf["NUM"] == 3:
                   if (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                       line_seq["LINVF"] = 4
                   elif (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                       line_seq["LINVF"] = 1
                   elif (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                       line_seq["LINVF"] = 2
               elif Linvf["NUM"] == 4:
                   if (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                       line_seq["LINVF"] = 1
                   elif (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                       line_seq["LINVF"] = 2
                   elif (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                       line_seq["LINVF"] = 3
           
           if vds_avg < limitd: # LOOK TO CHANGE
               line_ticker["VD"]=0;
               # VISTING DMEN                
               if Linvd["NUM"] == 1:
                   if (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 > 80:
                       line_seq["LINVD"] = 2
                   elif (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2 > 80:
                       line_seq["LINVD"] = 3
               elif Linvd["NUM"] == 2:
                   if (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2 > 80:
                       line_seq["LINVD"] = 3
                   elif (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 > 80:
                       line_seq["LINVD"] = 1
               elif Linvd["NUM"] == 3:
                   if (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 > 80:
                       line_seq["LINVD"] = 1
                   elif (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 > 80:
                       line_seq["LINVD"] = 2
           if hfs_avg < limitf: # LOOK TO CHANGE
               line_ticker["HF"]=0       
               # HOME FORWARDS
               if Linhf["NUM"] == 1:
                   if (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                       line_seq["LINHF"] = 2
                   elif (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                       line_seq["LINHF"] = 3
                   elif (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                       line_seq["LINHF"] = 4
               elif Linhf["NUM"] == 2:
                   if (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                       line_seq["LINHF"] = 3
                   elif (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                       line_seq["LINHF"] = 4
                   elif (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                       line_seq["LINHF"] = 1                
               elif Linhf["NUM"] == 3:
                   if (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                       line_seq["LINHF"] = 4
                   elif (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                       line_seq["LINHF"] = 1
                   elif (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                       line_seq["LINHF"] = 2
               elif Linhf["NUM"] == 4:
                   if (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                       line_seq["LINHF"] = 1
                   elif (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                       line_seq["LINHF"] = 2
                   elif (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                       line_seq["LINHF"] = 3
           if hds_avg < limitd: # LOOK TO CHANGE
               line_ticker["HD"]=0;
               # HOME DMEN                
               if Linvd["NUM"] == 1:
                   if (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 > 80:
                       line_seq["LINHD"] = 2
                   elif (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2 > 80:
                       line_seq["LINHD"] = 3
               elif Linvd["NUM"] == 2:
                   if (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2 > 80:
                       line_seq["LINHD"] = 3
                   elif (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 > 80:
                       line_seq["LINHD"] = 1
               elif Linvd["NUM"] == 3:
                   if (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 > 80:
                       line_seq["LINHD"] = 1
                   elif (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 > 80:
                       line_seq["LINHD"] = 2  
                               
               # MAKE SURE THERE IS NOT A MISTMATCH FAVOURING VISTING TEAM, IF HOME TEAM CANT MATCH, PICK NEXT BEST LINE                
           if Linvf["NUM"] < Linhf["NUM"]:
                if Linhf["NUM"]-1 > 80:
                    Linhf["NUM"] = Linvf["NUM"]
                    line_ticker["HF"]=0
                if Linhd["NUM"]-1 > 80:
                    Linhd["NUM"] = Linvd["NUM"]
                    line_ticker["HD"]=0
   
       #elif "PASSSPACE" in s_player_type or "SOG-C" in s_player_type :
       else:   
           if puckposs["VISITOR"]==1:
               if vfs_avg < (limitf+limitd)/2: # LOOK TO CHANGE 
                   puckposs = {"HOME":1,"VISITOR":0} # DUMP PUCK TO CHANGE, POSSESSION CHANGES, WHOLE LINE CHANGE
                   line_ticker["VF"]=0;line_ticker["VD"]=0;
                   # VISITOR FORWARDS           
                   if Linvf["NUM"] == 1:
                       if (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                           line_seq["LINVF"] = 2
                       elif (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                           line_seq["LINVF"] = 3
                       elif (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                           line_seq["LINVF"] = 4
                   elif Linvf["NUM"] == 2:
                       if (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                           line_seq["LINVF"] = 3
                       elif (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                           line_seq["LINVF"] = 4
                       elif (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                           line_seq["LINVF"] = 1                
                   elif Linvf["NUM"] == 3:
                       if (stamina["LWV4"]["LWV4"][3] + stamina["CV4"]["CV4"][3] + stamina["RWV4"]["RWV4"][3])/3 > 99:
                           line_seq["LINVF"] = 4
                       elif (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                           line_seq["LINVF"] = 1
                       elif (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                           line_seq["LINVF"] = 2
                   elif Linvf["NUM"] == 4:
                       if (stamina["LWV1"]["LWV1"][3] + stamina["CV1"]["CV1"][3] + stamina["RWV1"]["RWV1"][3])/3 > 80:
                           line_seq["LINVF"] = 1
                       elif (stamina["LWV2"]["LWV2"][3] + stamina["CV2"]["CV2"][3] + stamina["RWV2"]["RWV2"][3])/3 > 80:
                           line_seq["LINVF"] = 2
                       elif (stamina["LWV3"]["LWV3"][3] + stamina["CV3"]["CV3"][3] + stamina["RWV3"]["RWV3"][3])/3 > 80:
                           line_seq["LINVF"] = 3
               
                    # VISTING DMEN                
                   if Linvd["NUM"] == 1:
                       if (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 > 80:
                           line_seq["LINVD"] = 2
                       elif (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2 > 80:
                           line_seq["LINVD"] = 3
                   elif Linvd["NUM"] == 2:
                       if (stamina["LDV3"]["LDV3"][3] + stamina["RDV3"]["RDV3"][3])/2 > 80:
                           line_seq["LINVD"] = 3
                       elif (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 > 80:
                           line_seq["LINVD"] = 1
                   elif Linvd["NUM"] == 3:
                       if (stamina["LDV1"]["LDV1"][3] + stamina["RDV1"]["RDV1"][3])/2 > 80:
                           line_seq["LINVD"] = 1
                       elif (stamina["LDV2"]["LDV2"][3] + stamina["RDV2"]["RDV2"][3])/2 > 80:
                           line_seq["LINVD"] = 2
                                   
           elif puckposs["VISITOR"]==0:
               if hfs_avg < (limitf+limitd)/2: # LOOK TO CHANGE 
                   puckposs = {"HOME":0,"VISITOR":1} # DUMP PUCK TO CHANGE, POSSESSION CHANGES, WHOLE LINE CHANGE
                   line_ticker["HF"]=0;line_ticker["HD"]=0;
                   # HOME FORWARDS           
                   if Linhf["NUM"] == 1:
                       if (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                           line_seq["LINHF"] = 2
                       elif (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                           line_seq["LINHF"] = 3
                       elif (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                           line_seq["LINHF"] = 4
                   elif Linhf["NUM"] == 2:
                       if (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                           line_seq["LINHF"] = 3
                       elif (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                           line_seq["LINHF"] = 4
                       elif (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                           line_seq["LINHF"] = 1                
                   elif Linhf["NUM"] == 3:
                       if (stamina["LWH4"]["LWH4"][3] + stamina["CH4"]["CH4"][3] + stamina["RWH4"]["RWH4"][3])/3 > 99:
                           line_seq["LINHF"] = 4
                       elif (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                           line_seq["LINHF"] = 1
                       elif (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                           line_seq["LINHF"] = 2
                   elif Linhf["NUM"] == 4:
                       if (stamina["LWH1"]["LWH1"][3] + stamina["CH1"]["CH1"][3] + stamina["RWH1"]["RWH1"][3])/3 > 80:
                           line_seq["LINHF"] = 1
                       elif (stamina["LWH2"]["LWH2"][3] + stamina["CH2"]["CH2"][3] + stamina["RWH2"]["RWH2"][3])/3 > 80:
                           line_seq["LINHF"] = 2
                       elif (stamina["LWH3"]["LWH3"][3] + stamina["CH3"]["CH3"][3] + stamina["RWH3"]["RWH3"][3])/3 > 80:
                           line_seq["LINHF"] = 3
               
                    # HOME DMEN                
                   if Linhd["NUM"] == 1:
                       if (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 > 80:
                           line_seq["LINHD"] = 2
                       elif (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2 > 80:
                           line_seq["LINHD"] = 3
                   elif Linhd["NUM"] == 2:
                       if (stamina["LDH3"]["LDH3"][3] + stamina["RDH3"]["RDH3"][3])/2 > 80:
                           line_seq["LINHD"] = 3
                       elif (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 > 80:
                           line_seq["LINHD"] = 1
                   elif Linhd["NUM"] == 3:
                       if (stamina["LDH1"]["LDH1"][3] + stamina["RDH1"]["RDH1"][3])/2 > 80:
                           line_seq["LINHD"] = 1
                       elif (stamina["LDH2"]["LDH2"][3] + stamina["RDH2"]["RDH2"][3])/2 > 80:
                           line_seq["LINHD"] = 2  
   
    
         
    #elif  mode["HOME"] ==1 and mode["VISITOR"] == 0: # MANAGE HOME TEAM
    #
    #elif  mode["HOME"] ==0 and mode["VISITOR"] == 1: # MANAGE AWAY TEAM 
    #
    #elif  mode["HOME"] ==1 and mode["VISITOR"] == 1: # MANAGAE BOTH TEAMS
    
    return line_seq,puckposs,line_ticker
                   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                  