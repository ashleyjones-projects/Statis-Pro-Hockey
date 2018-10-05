# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:59:10 2017

@author: w9641432
"""

def manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox):
    limitf=40
    limitd=50
    
    # GET PP AND PK LINES TOGETHER.
    
    
    
    # CALCULATE AVERAGE LIINE STAMINA FOR EACH LINE
    
    # VISITOR PP
    if Linvf["NUM"] == 1:
        hfs_avg = (stamina["5LWH1"]["5LWH1"][3] + stamina["5CH1"]["5CH1"][3] + stamina["5RWH1"]["5RWH1"][3])/3           
    elif Linvf["NUM"] == 2:
        hfs_avg = (stamina["5LWH2"]["5LWH2"][3] + stamina["5CH2"]["5CH2"][3] + stamina["5RWH2"]["5RWH2"][3])/3   
    
    if Linvd["NUM"] == 1:
        hds_avg = (stamina["5LDH1"]["5LDH1"][3] + stamina["5RDH1"]["5RDH1"][3])/2  
    elif Linvd["NUM"] == 2:
        hds_avg = (stamina["5LDH2"]["5LDH2"][3] + stamina["5RDH2"]["5RDH2"][3])/2  
   
    # HOME PK
    if Linhf["NUM"] == 1:
        vfs_avg = (stamina["4KLWV1"]["4KLWV1"][3] + stamina["4KCV1"]["4KCV1"][3])/2 
    elif Linhf["NUM"] == 2:
        vfs_avg = (stamina["4KLWV2"]["4KLWV2"][3] + stamina["4KCV2"]["4KCV2"][3])/2

    if Linhd["NUM"] == 1:
        vds_avg = (stamina["4KLDV1"]["4KLDV1"][3] + stamina["4KRDV1"]["4KRDV1"][3])/2 
    elif Linhd["NUM"] == 2:
        vds_avg = (stamina["4KLDV2"]["4KLDV2"][3] + stamina["4KRDV2"]["4KRDV2"][3])/2
    
    
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
       
       if "ICING_0" in s_player_type or "ICING_1" in s_player_type:
     
                line_ticker["VF"]=0;line_ticker["VD"]=0;
                if (stamina["4KLWV1"]["4KLWV1"][3] + stamina["4KCV1"]["4KCV1"][3])/2 > 60:
                       line_seq["LINVF"] = 1
                else:
                       line_seq["LINVF"] = 2
                
                
                if (stamina["4KLDV1"]["4KLDV1"][3] + stamina["4KRDV1"]["4KRDV1"][3])/2 > 60:
                       line_seq["LINVD"] = 1
                else:
                       line_seq["LINVD"] = 2
               
                               
       elif line_ticker["HF"]>4 or line_ticker["VF"]>4 or line_ticker["HD"]>4 or line_ticker["VD"]>4:
           if puckposs["HOME"]==1:
               if line_ticker["HF"]>4:
                   line_ticker["HF"]=0
                   # HOME FORWARDS           
                   if Linhf["NUM"] == 1:
                       
                           line_seq["LINHF"] = 2
                       
                   elif Linhf["NUM"] == 2:
                       
                           line_seq["LINHF"] = 1
                       
               
               if line_ticker["HD"] > 4:
                   line_ticker["HD"] = 0
                   if Linhd["NUM"] == 1:
                      
                           line_seq["LINHD"] = 2
                       
                   elif Linhd["NUM"] == 2:
                       
                           line_seq["LINHD"] = 1
                  
           elif puckposs["VISITOR"]==1: 
               if line_ticker["VF"]>4:
                   line_ticker["VF"]=0
                   # visting FORWARDS           
                   if Linvf["NUM"] == 1:
                       
                           line_seq["LINVF"] = 2
                      
                   elif Linvf["NUM"] == 2:
                      
                           line_seq["LINVF"] = 1
                        
                              
               if line_ticker["VD"] >4:
                   line_ticker["VD"]=0
                   puckposs={"HOME":1,"VISITOR":0} # ASSUMED HERE THAT DMEN CHANGE, ITS A DUMP AND CHANGE EVENTHOUGH FORWARS STILL ON
                   # visinitng DMEN                
                   if Linvd["NUM"] == 1:
                       
                           line_seq["LINVD"] = 2
                      
                   elif Linvd["NUM"] == 2:
                      
                           line_seq["LINVD"] = 1                        
                   
       elif "PUCKDEFLECTEDOUT" in s_player_type or "OFFSIDE" in s_player_type or "FROZENPUCK" in s_player_type or result["GOAL"]==1:
           
           if vfs_avg < limitf: # LOOK TO CHANGE
               # VISTING FORWARDS
               line_ticker["VF"]=0
               if Linvf["NUM"] == 1:
                   
                       line_seq["LINVF"] = 2
                              
               elif Linvf["NUM"] == 2:
                   
                       line_seq["LINVF"] = 1
                   
           
           if vds_avg < limitd: # LOOK TO CHANGE
               line_ticker["VD"]=0;
               # VISTING DMEN                
               if Linvd["NUM"] == 1:
                   
                       line_seq["LINVD"] = 2
                  
               elif Linvd["NUM"] == 2:
                  
                       line_seq["LINVD"] = 1
              
           if hfs_avg < limitf: # LOOK TO CHANGE
               line_ticker["HF"]=0       
               # HOME FORWARDS
               if Linhf["NUM"] == 1:
                   
                       line_seq["LINHF"] = 2
                  
               elif Linhf["NUM"] == 2:
                  
                       line_seq["LINHF"] = 1
              
           if hds_avg < limitd: # LOOK TO CHANGE
               line_ticker["HD"]=0;
               # HOME DMEN                
               if Linvd["NUM"] == 1:
                   
                       line_seq["LINHD"] = 2
                   
               elif Linvd["NUM"] == 2:
                  
                       line_seq["LINHD"] = 1
                               
               # MAKE SURE THERE IS NOT A MISTMATCH FAVOURING VISTING TEAM, IF HOME TEAM CANT MATCH, PICK NEXT BEST LINE                
           if Linvf["NUM"] < Linhf["NUM"]:
                if Linhf["NUM"]-1 > 60:
                    Linhf["NUM"] = Linvf["NUM"]
                    line_ticker["HF"]=0
                if Linhd["NUM"]-1 > 60:
                    Linhd["NUM"] = Linvd["NUM"]
                    line_ticker["HD"]=0
   
       elif "PASSSPACE" in s_player_type or "SOG-C" in s_player_type :
          
           if puckposs["VISITOR"]==1:
               if vfs_avg < (limitf+limitd)/2: # LOOK TO CHANGE 
                   puckposs = {"HOME":1,"VISITOR":0} # DUMP PUCK TO CHANGE, POSSESSION CHANGES, WHOLE LINE CHANGE
                   line_ticker["VF"]=0;line_ticker["VD"]=0;
                   # VISITOR FORWARDS           
                   if Linvf["NUM"] == 1:
                       
                           line_seq["LINVF"] = 2
                       
                   elif Linvf["NUM"] == 2:
                       
                           line_seq["LINVF"] = 1                
               
                    # VISTING DMEN                
                   if Linvd["NUM"] == 1:
                       
                           line_seq["LINVD"] = 2
                     
                   elif Linvd["NUM"] == 2:
                      
                           line_seq["LINVD"] = 1
                                                     
           elif puckposs["VISITOR"]==0:
               if hfs_avg < (limitf+limitd)/2: # LOOK TO CHANGE 
                   puckposs = {"HOME":0,"VISITOR":1} # DUMP PUCK TO CHANGE, POSSESSION CHANGES, WHOLE LINE CHANGE
                   line_ticker["HF"]=0;line_ticker["HD"]=0;
                   # HOME FORWARDS           
                   if Linhf["NUM"] == 1:
                      
                           line_seq["LINHF"] = 2
                      
                   elif Linhf["NUM"] == 2:
                      
                           line_seq["LINHF"] = 1                
               
                    # HOME DMEN                
                   if Linhd["NUM"] == 1:
                       
                           line_seq["LINHD"] = 2
                     
                   elif Linhd["NUM"] == 2:
                      
                           line_seq["LINHD"] = 1
         
    #elif  mode["HOME"] ==1 and mode["VISITOR"] == 0: # MANAGE HOME TEAM
    #
    #elif  mode["HOME"] ==0 and mode["VISITOR"] == 1: # MANAGE AWAY TEAM 
    #
    #elif  mode["HOME"] ==1 and mode["VISITOR"] == 1: # MANAGAE BOTH TEAMS
    
    return line_seq,puckposs,line_ticker
                   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                  