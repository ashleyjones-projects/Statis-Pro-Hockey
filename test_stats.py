# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:38:05 2018

@author: w9641432
"""
shots=0
goals=0
types=0
types2=0
types3=0
types4=0
seks=0
seks1=0
seks2=0
seks3=0
#                       if puckposs['VISITOR']==0:
                           shots=shots+1
##                           if line_seq['LINVF']==1 or line_seq['LINVF']==1:
##                               types=types+1
##                           elif line_seq['LINVF']==2 or line_seq['LINVF']==2:
##                               types2=types2+1
##                           elif line_seq['LINVF']==3 or line_seq['LINVF']==3:
##                               types3=types3+1
##                           elif line_seq['LINVF']==4 or line_seq['LINVF']==4:
##                               types4=types4+1
#
#                           if Linhf['HF'][0]=='LWH1' :
#                                   types=types+1
#                           elif Linhf['HF'][0]=='LWH2':
#                                   types2=types2+1
#                           elif Linhf['HF'][0]=='LWH3' :
#                                   types3=types3+1
#                           elif Linhf['HF'][0]=='LWH4' :
#                                   types4=types4+1    
#                       
#                   if 'GOAL' in outcome:
#                       goals=goals+1  

if Linhf['HF'][0]=='LWH1' or Linhf['HF'][0]=='5LWH1' or Linhf['HF'][0]=='4LWH1':
               seks = seks+secs
           elif Linhf['HF'][0]=='LWH2' or Linhf['HF'][0]=='5LWH2' or Linhf['HF'][0]=='4LWH2':
               seks1 = seks1+secs 
           elif Linhf['HF'][0]=='LWH3' or Linhf['HF'][0]=='4KWH1' or Linhf['HF'][1]=='3KCH1':
               seks2 = seks2+secs
           elif Linhf['HF'][0]=='LWH4' or Linhf['HF'][0]=='4KWH2' or Linhf['HF'][1]=='3KCH2':
               seks3 = seks3+secs   