# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:45:29 2017

@author: w9641432
"""

from random import randint
import numpy as np
import facmaker
import makelinechange
import time
import faceoff
import staminacheck
import managelines
import managelines_54V
import managelines_54H
import managelines_53V
import managelines_53H
import managelines_43V
import managelines_43H
import managelines_4V4
import checkpenalty
import puthplayerinbox
import staminainit
import penaltytime
import shotpotential
import shootordump
import shotQammend
import shotresult



class Keepscore:

    def __init__(self,period,time,scoreboard,possession,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats):    
        
        self.Period     = period
        self.Time       = time
        self.Scoreboard = scoreboard
        self.Possession = possession
        self.Line       = line_seq
        self.Stamina    = stamina
        self.V_stats    = v_stats
        self.H_stats    = h_stats
        self.Linvf      = Linvf
        self.Linhf      = Linhf
        self.Linvd      = Linvd
        self.Linhd      = Linhd
        self.Linvg      = Linvg
        self.Linhg      = Linhg
        self.Secs       = secs
        self.Tid        = tid
        self.Penbox     = penbox
        self.Vt_stats   = vt_stats
        self.Ht_stats   = ht_stats

    def score_board(self):
        
        if self.Possession["VISITOR"]==1:
            self.Scoreboard["VISITOR"] += 1
        elif self.Possession["HOME"]==1:
            self.Scoreboard["HOME"] += 1                   
        
    def poss_change(self):
        
        if self.Possession["VISITOR"]==1:
            self.Possession["VISITOR"]=0
            self.Possession["HOME"]=1
        else:
            self.Possession["VISITOR"]=1
            self.Possession["HOME"]=0
        
    def new_period(self):
        
        self.Period["PERIOD"] += 1
                   
    def line_change(self):

        [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = makelinechange.make_line_change(self.Line,self.Period, self.Penbox, self.Linhf, self.Linhd, self.Linvf, self.Linvd)
        return Linhf, Linhd, Linvf, Linvd, Linhg, Linvg  

    def check_stamina(self):

        [stamina,diff_s] = staminacheck.stamina_check(self.Stamina,self.H_stats,self.V_stats,self.Linhf, self.Linhd, self.Linvf, self.Linvd, self.Secs, self.Period, self.Tid, self.Penbox, self.Line)            
        return stamina,diff_s
    
    def penalty_box(self):
        
        [Pen_analysis,line_seq]=checkpenalty.check_penalty(self.V_stats,self.Vt_stats,self.H_stats,self.Ht_stats,self.Linvf,self.Linvd,self.Linhf,self.Linhd,self.Linvg,self.Linhg,self.Line,self.Stamina)
        if Pen_analysis["PEN_H_NAME"]!="NONE" or Pen_analysis["PEN_V_NAME"]!="NONE":
            penbox = puthplayerinbox.put_player_in_box(Pen_analysis,self.Penbox)
            penalty=1
            return penbox, line_seq,penalty
        else:
            penalty=0
            return self.Penbox, self.Line, penalty 

    def pen_time(self):
        
        [penbox,line_seq] = penaltytime.penalty_time(self.Penbox,self.Line,self.Secs)
        return penbox, line_seq
      
        

###############################################################################
###############################################################################

#Load players' stats home
inpath='C:/Users/w9641432/Documents/Work/Python_learning/StatisproHockey/teams/'

ph_code=[]
h_stats = []
f = open(inpath+'test_team.csv','r')
for line in f:
    
    cells = line.split(",")
    ph_code.append((cells[0]))
    h_stats.append((cells[0],cells[1],cells[2],cells[3],cells[4],cells[5],cells[6],cells[7],cells[8],cells[9],
                    cells[10],cells[11],cells[12],cells[13],cells[14],cells[15],cells[16],cells[17],cells[18],
                    cells[19],cells[20],cells[21],cells[22],cells[23],cells[24],cells[25],cells[26],cells[27],cells[28],
                    cells[29],cells[30],cells[31],cells[32],cells[33],cells[34],cells[35],cells[36],cells[37],cells[38],
                    cells[39],cells[40],cells[41],cells[42],cells[43],cells[44],cells[45],cells[46],cells[47],cells[48],
                    cells[49],cells[50],cells[51],cells[52],cells[53],cells[54]))     
f.close()

#Load players' stats vistior
pv_code=[]
v_stats = []
f = open(inpath+'test_team.csv','r')
for line in f:
    
    cells = line.split(",")
    pv_code.append((cells[0]))
    v_stats.append((cells[0],cells[1],cells[2],cells[3],cells[4],cells[5],cells[6],cells[7],cells[8],cells[9],
                    cells[10],cells[11],cells[12],cells[13],cells[14],cells[15],cells[16],cells[17],cells[18],
                    cells[19],cells[20],cells[21],cells[22],cells[23],cells[24],cells[25],cells[26],cells[27],cells[28],
                    cells[29],cells[30],cells[31],cells[32],cells[33],cells[34],cells[35],cells[36],cells[37],cells[38],
                    cells[39],cells[40],cells[41],cells[42],cells[43],cells[44],cells[45],cells[46],cells[47],cells[48],
                    cells[49],cells[50],cells[51],cells[52],cells[53],cells[54]))
f.close()    

        
# HOME TEAM COLLECTIVE STATS- TEAM CARD
ht_stats=[]
f=open(inpath+'team.csv','r')
for line in f:
    
    cells = line.split(",")
    ht_stats.append((cells[0],cells[1],cells[2],cells[3],cells[4],cells[5],cells[6],cells[7],cells[8]))

# VISITING TEAM COLLECTIVE STATS- TEAM CARD
vt_stats=[]
f=open(inpath+'team.csv','r')
for line in f:
    
    cells = line.split(",")
    vt_stats.append((cells[0],cells[1],cells[2],cells[3],cells[4],cells[5],cells[6],cells[7],cells[8]))    

scoreboard = {"VISITOR": 0, "HOME": 0, "V_SHOTS": 0, "H_SHOTS": 0}
period = {"PERIOD": 0}
card_range=160
mode = {"HOME":0,"VISITOR":0}
result = {"GOAL":0}
penbox = {"PEN_V_NAME1":'NONE',"POS_V1":'NONE',"PEN_TYPE_V1":'NONE',"DURAT_V1":'NONE',"COINCIN_V1":0,"PEN_H_NAME1":'NONE',"POS_H1":'NONE',"PEN_TYPE_H1":'NONE',"DURAT_H1":'NONE',"COINCIN_H1":0,
          "PEN_V_NAME2":'NONE',"POS_V2":'NONE',"PEN_TYPE_V2":'NONE',"DURAT_V2":'NONE',"COINCIN_V2":0,"PEN_H_NAME2":'NONE',"POS_H2":'NONE',"PEN_TYPE_H2":'NONE',"DURAT_H2":'NONE',"COINCIN_H2":0,
          "PEN_V_NAME3":'NONE',"POS_V3":'NONE',"PEN_TYPE_V3":'NONE',"DURAT_V3":'NONE',"COINCIN_V3":0,"PEN_H_NAME3":'NONE',"POS_H3":'NONE',"PEN_TYPE_H3":'NONE',"DURAT_H3":'NONE',"COINCIN_H3":0,
          "PEN_V_NAME4":'NONE',"POS_V4":'NONE',"PEN_TYPE_V4":'NONE',"DURAT_V4":'NONE',"COINCIN_V4":0,"PEN_H_NAME4":'NONE',"POS_H4":'NONE',"PEN_TYPE_H4":'NONE',"DURAT_H4":'NONE',"COINCIN_H4":0,
          "PEN_V_NAME5":'NONE',"POS_V5":'NONE',"PEN_TYPE_V5":'NONE',"DURAT_V5":'NONE',"COINCIN_V5":0,"PEN_H_NAME5":'NONE',"POS_H5":'NONE',"PEN_TYPE_H5":'NONE',"DURAT_H5":'NONE',"COINCIN_H5":0}

del cells,line       
###############################################################################
###############################################################################
line_seq = {"LINVF": 1, "LINHF": 1, "LINVD": 1, "LINHD": 1, "GV": 1, "GH": 1, "EAV": 0, "EAH": 0, "PENV": 0, "PENH": 0}
Linvf=[]; Linhf=[]; Linvd=[]; Linhd=[]; Linvg=[]; Linhg=[]
z=0 
for j in range(0,300):
       
    stamina = staminainit.stamina_init(h_stats,v_stats,penbox,line_seq,Linhf,Linhd,Linvf,Linvd)    
    puckposs = {"VISITOR": 0, "HOME": 0}
    secs=0
    r  = [np.random.randint(low=6,high=14,size=card_range)]
    tid = 1200
    play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
    play.new_period()
    [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change()
    diff_s=0
    # Opening Face Off
    
    puckposs = faceoff.face_off(Linvf,Linhf,v_stats,h_stats,stamina)
    play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
    needfo=0
    line_ticker = {"HF":0,"VF":0,"HD":0,"VD":0}    
    
    for i in range(0,card_range):
        
        [fac_random,s_player_type] = facmaker.facmaker(Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,puckposs,line_seq)
        line_ticker["HF"] += 1; line_ticker["VF"] +=1;line_ticker["HD"] += 1; line_ticker["VD"] +=1
        #print(Linhf["NUM"])
        #print(line_seq)
        secs =  r[0][i]
        tid = tid -secs
                        
        if tid > 0:
#           print(time.strftime("%M:%S",time.gmtime(tid)) + "   card=" + str(i+1))      # North American clock
           #print(time.strftime("%M:%S",time.gmtime(r[0][i])) + "   card=" + str(i+1)) # International clock
           if needfo ==1:
               needfo=0
               puckposs = faceoff.face_off(Linvf,Linhf,v_stats,h_stats,stamina)
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
           
           #if 'SAC' in s_player_type:
               
           if 'HIT' in s_player_type:
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               rand = randint(1,100)
               
               hit_weight = [75,25]
               
               if rand > hit_weight[1]:
                   play.poss_change()
           
           if 'GV' in s_player_type:
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               play.poss_change()      
           
           if 'TK' in s_player_type:
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               play.poss_change()
               
           if  'ICING' in s_player_type:
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [line_seq,puckposs,line_ticker] = managelines.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker) 
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change()
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               needfo=1
           if  'OFFSIDE' in s_player_type:
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [line_seq,puckposs,line_ticker] = managelines.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker) 
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change()
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               needfo=1
           if  'PUCKDEFLECTEDOUT' in s_player_type:
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [line_seq,puckposs,line_ticker] = managelines.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker) 
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change()
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               needfo=1
           if  'FROZENPUCK' in s_player_type:
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [line_seq,puckposs,line_ticker] = managelines.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker) 
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change()
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               needfo=1
           if  'PASSSPACE' in s_player_type:
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [line_seq,puckposs,line_ticker] = managelines.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker) 
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
#               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change()
#               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               xxxxx=1
           if  'PENALTY?' in s_player_type:
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               if penbox["PEN_H_NAME5"]=="NONE" and penbox["PEN_V_NAME5"]=="NONE": # prevent penalty box getting too crowded! 5 max
                   [penbox,line_seq,penalty] = play.penalty_box()
               else:
                   penalty=0
               if penalty ==1:
                   line_seq["LINHF"]=1;line_seq["LINHD"]=1;line_seq["LINVF"]=1;line_seq["LINVD"]=1;
                   play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
                   [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               puckposs={"HOME":1,"VISITOR":1} # CASE HERE WHERE THERE WILL BE STOPPAGE IN PLAY REGARDLESS OF PENALTY OR NOT. WILL BE A NEUATRAL FO, SO OPPORTUNITY TO CHANGE LINES
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               # IF PENALTY STOPPAGE IN PLAY, CHANGE LINES, THEN FACEOFF, THE CONTINUE
               needfo=1
               
           if "SOG" in s_player_type:
               
               [shotQ,stype,s_player_type] = shotpotential.shot_potential(h_stats,v_stats,scoreboard,s_player_type,puckposs,Linhf,Linhd,Linhg,Linvf,Linvd,Linvg,stamina,line_seq)
               [shoot,line_ticker] = shootordump.shoot_or_dump(diff_s,line_ticker,shotQ,stype,line_seq,puckposs)
               if shoot == 1:
                   
                   shotQ = shotQammend.shotQ_ammend(shotQ,diff_s,puckposs) # AMMEND DUE TO STAMINA
                   [outcome,puckposs] = shotresult.shot_result(shotQ,puckposs,line_seq,h_stats,v_stats,stamina,Linvf,Linvd,Linhf,Linhd)
                   if 'SAVEF' in outcome:
                       needfo=1
                   elif 'SAVER' in outcome:
                       rebound = randint(0,1)
                       if rebound==0:
                           puckposs["HOME"]=1;puckposs["VISITOR"]=0
                       elif rebound==1:
                           puckposs["HOME"]=0;puckposs["VISITOR"]=1
                   elif 'GOAL' in outcome:
                       needfo=1
                       play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
                       play.score_board()
                       play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
                       # IF PPL NEED TO RESET MAN IN BOX IF MINOR PENALTY
                       if abs(line_seq['PENH']-line_seq['PENV'])>0:
                           
                           NEED TO ACT HERE: IF GOAL ON PENALTY, REMOVE PLAYER FROM BOX ON MINOR
                           
                                   
                           
                       
                       

                
               #################################################################################
            #CREATE LINE MANAGEMENT FOR EACH LINE SEQUENCE, IE 5V5,5V4,5v3,4V4,4V3,3V3
            #CHECK STAMINA AFTER EACH FAC CARD
           if line_seq["PENH"]==0 and line_seq["PENV"]==0: # 5V5
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker) 
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               if penbox["COINCIN_H1"]==1 or penbox["COINCIN_H2"]==1 or penbox["COINCIN_H3"]==1 or penbox["COINCIN_H4"]==1 or penbox["COINCIN_H5"]==1 or penbox["COINCIN_V1"]==1 or penbox["COINCIN_V2"]==1 or penbox["COINCIN_V3"]==1 or penbox["COINCIN_V4"]==1 or penbox["COINCIN_V1"]==5:
                   [penbox,line_seq] = play.pen_time()
                   play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
    
           elif line_seq["PENH"]==1 and line_seq["PENV"]==0: # VISITOR PP 5V4
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_54V.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)

           elif line_seq["PENH"]==0 and line_seq["PENV"]==1: # HOME PP 5V4
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_54H.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
           
           elif line_seq["PENH"]==2 and line_seq["PENV"]==0: # VISITOR PP 5V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_53V.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)

           elif line_seq["PENH"]==0 and line_seq["PENV"]==2: # HOME PP 5V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_53H.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)

           elif line_seq["PENH"]==1 and line_seq["PENV"]==1: # 4V4
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_4V4.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
           
           elif line_seq["PENH"]==2 and line_seq["PENV"]==1: # VISTING PP 4V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_43V.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
 
           elif line_seq["PENH"]==1 and line_seq["PENV"]==2: # HOME PP 4V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_43H.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
           
           elif (line_seq["PENH"]==2 and line_seq["PENV"]==2) or (line_seq["PENH"]==3 and line_seq["PENV"]==3) or (line_seq["PENH"]==4 and line_seq["PENV"]==4) or (line_seq["PENH"]==5 and line_seq["PENV"]==5): # 4V4
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_4V4.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)

           elif line_seq["PENH"]==3 and line_seq["PENV"]==1 or line_seq["PENH"]==4 and line_seq["PENV"]==2 or line_seq["PENH"]==5 and line_seq["PENV"]==3: # VISITOR PP 5V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_53V.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)

           elif line_seq["PENH"]==1 and line_seq["PENV"]==3 or line_seq["PENH"]==2 and line_seq["PENV"]==4 or line_seq["PENH"]==3 and line_seq["PENV"]==5: # HOME PP 5V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_53H.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
           
           elif line_seq["PENH"]==0 and line_seq["PENV"]==3 or line_seq["PENH"]==1 and line_seq["PENV"]==4 or line_seq["PENH"]==2 and line_seq["PENV"]==5: # HOME PP 5V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_53H.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)

           elif line_seq["PENH"]==3 and line_seq["PENV"]==0 or line_seq["PENH"]==4 and line_seq["PENV"]==1 or line_seq["PENH"]==5 and line_seq["PENV"]==2 or line_seq["PENH"]==4 and line_seq["PENV"]==0 or line_seq["PENH"]==5 and line_seq["PENV"]==1: # VISITOR PP 5V3
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [stamina,diff_s]=play.check_stamina()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)
               [line_seq,puckposs,line_ticker] = managelines_53V.manage_lines(Linvf,Linvd,Linhf,Linhd,stamina,line_seq,result,mode,s_player_type,puckposs,line_ticker,penbox) 
               [Linhf, Linhd, Linvf, Linvd, Linhg, Linvg] = play.line_change() # GET INITIAL PP AND PK LINES OUT. NOW NEED TO ADJUST FOR POSSIBLE PENALIZED PLAYER AND STAMINA
               [penbox,line_seq] = play.pen_time()
               play = Keepscore(period,time,scoreboard,puckposs,line_seq,stamina,v_stats,h_stats,Linhf,Linhd,Linvf,Linvd,Linvg,Linhg,secs,tid,penbox,vt_stats,ht_stats)

           else:
            x=1
#           f=open("log.txt",'a')
#           f.write(str(tid) + "\n" + str(line_seq) + "  " + s_player_type + "\n" + str(penbox) + "\n\n"  )
#           f.close()
        else:
            print("END OF PERIOD: " + str(period["PERIOD"]))
            break
        
        

print(shots,(shots-goals)/shots, goals, types,types2,types3,types4,seks/60,seks1/60,seks2/60,seks3/60)               