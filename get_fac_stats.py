# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:06:21 2017

@author: w9641432
"""

path = 'C:/Users/w9641432/Documents/Work/Python_learning/StatisproHockey/fac_card_files/fac_plays.txt'

f= open(path,'r')

line = [line for line in f if line.strip()]

f.close()
plays=[]
randn=[]
rebound=[]
faceoff=[]
sixthm=[]
somenum=[]
for i in range(0,len(line)):
    
    commas=[pos for pos, char in enumerate(line[i]) if char == '"']
    
    plays.append(line[i][commas[0]+1:commas[1]])
    
    randn.append(line[i][commas[2]+1:commas[3]]) 
    
    rebound.append(line[i][commas[4]+1:commas[5]])
    
    faceoff.append(line[i][commas[6]+1:commas[7]]) 
    
    sixthm.append(line[i][commas[8]+1:commas[9]])
    
    somenum.append(line[i][commas[10]+1:commas[11]]) 
    
randn = sorted(randn) 
stat=[]
for i in range(0,len(sixthm)):
    
   if 'SOG-C' in plays[i]:
    
        stat.append(i)
      
