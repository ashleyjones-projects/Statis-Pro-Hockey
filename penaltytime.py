# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:41:01 2017

@author: w9641432
"""

def penalty_time(penbox,line,secs):
    
    # reduce penalty minutes by seconds on card
    # home
    if penbox["DURAT_H1"] != "NONE":
        penbox["DURAT_H1"] = penbox["DURAT_H1"] - secs
        if penbox["DURAT_H1"]<= 0:
            penbox["DURAT_H1"] = "NONE"
            penbox["PEN_H_NAME1"] = "NONE"
            penbox["PEN_TYPE_H1"] = "NONE"
            penbox["POS_H1"] = "NONE"
            if penbox["COINCIN_H1"]==0:
                     line["PENH"] -= 1
            penbox["COINCIN_H1"] = 0             
                
    if penbox["DURAT_H2"] != "NONE":
        penbox["DURAT_H2"] = penbox["DURAT_H2"] - secs
        if penbox["DURAT_H2"]<= 0:
            penbox["DURAT_H2"] = "NONE"
            penbox["PEN_H_NAME2"] = "NONE"
            penbox["PEN_TYPE_H2"] = "NONE"
            penbox["POS_H2"] = "NONE"
            if penbox["COINCIN_H2"]==0:
                     line["PENH"] -= 1
            penbox["COINCIN_H2"] = 0             
                
    if penbox["DURAT_H3"] != "NONE":
        penbox["DURAT_H3"] = penbox["DURAT_H3"] - secs
        if penbox["DURAT_H3"]<= 0:
            penbox["DURAT_H3"] = "NONE"
            penbox["PEN_H_NAME3"] = "NONE"
            penbox["PEN_TYPE_H3"] = "NONE"
            penbox["POS_H3"] = "NONE"
            if penbox["COINCIN_H3"]==0:
                     line["PENH"] -= 1
            penbox["COINCIN_H3"] = 0             
                
    if penbox["DURAT_H4"] != "NONE":
        penbox["DURAT_H4"] = penbox["DURAT_H4"] - secs
        if penbox["DURAT_H4"]<= 0:
            penbox["DURAT_H4"] = "NONE"
            penbox["PEN_H_NAME4"] = "NONE"
            penbox["PEN_TYPE_H4"] = "NONE"
            penbox["POS_H4"] = "NONE"
            if penbox["COINCIN_H4"]==0:
                     line["PENH"] -= 1
            penbox["COINCIN_H4"] = 0             
                
    if penbox["DURAT_H5"] != "NONE":
        penbox["DURAT_H5"] = penbox["DURAT_H5"] - secs
        if penbox["DURAT_H5"]<= 0:
            penbox["DURAT_H5"] = "NONE"
            penbox["PEN_H_NAME5"] = "NONE"
            penbox["PEN_TYPE_H5"] = "NONE"
            penbox["POS_H5"] = "NONE"
            if penbox["COINCIN_H5"]==0:
                     line["PENH"] -= 1
            penbox["COINCIN_H5"] = 0             
    # visitor          
    if penbox["DURAT_V1"] != "NONE":
        penbox["DURAT_V1"] = penbox["DURAT_V1"] - secs
        if penbox["DURAT_V1"]<= 0:
            penbox["DURAT_V1"] = "NONE"
            penbox["PEN_V_NAME1"] = "NONE"
            penbox["PEN_TYPE_V1"] = "NONE"
            penbox["POS_V1"] = "NONE"
            if penbox["COINCIN_V1"]==0:
                     line["PENV"] -= 1
            penbox["COINCIN_V1"] = 0             
                         
    if penbox["DURAT_V2"] != "NONE":
        penbox["DURAT_V2"] = penbox["DURAT_V2"] - secs
        if penbox["DURAT_V2"]<= 0:
            penbox["DURAT_V2"] = "NONE"
            penbox["PEN_V_NAME2"] = "NONE"
            penbox["PEN_TYPE_V2"] = "NONE"
            penbox["POS_V2"] = "NONE"
            if penbox["COINCIN_V2"]==0:
                     line["PENV"] -= 1
            penbox["COINCIN_V2"] = 0             
                               
    if penbox["DURAT_V3"] != "NONE":
        penbox["DURAT_V3"] = penbox["DURAT_V3"] - secs
        if penbox["DURAT_V3"]<= 0:
            penbox["DURAT_V3"] = "NONE"
            penbox["PEN_V_NAME3"] = "NONE"
            penbox["PEN_TYPE_V3"] = "NONE"
            penbox["POS_V3"] = "NONE"
            if penbox["COINCIN_V3"]==0:
                     line["PENV"] -= 1
            penbox["COINCIN_V3"] = 0              
                              
    if penbox["DURAT_V4"] != "NONE":
        penbox["DURAT_V4"] = penbox["DURAT_V4"] - secs
        if penbox["DURAT_V4"]<= 0:
            penbox["DURAT_V4"] = "NONE"
            penbox["PEN_V_NAME4"] = "NONE"
            penbox["PEN_TYPE_V4"] = "NONE"
            penbox["POS_V4"] = "NONE"
            if penbox["COINCIN_V4"]==0:
                     line["PENV"] -= 1
            penbox["COINCIN_V4"] = 0             
                               
    if penbox["DURAT_V5"] != "NONE":
        penbox["DURAT_V5"] = penbox["DURAT_V5"] - secs
        if penbox["DURAT_V5"]<= 0:
            penbox["DURAT_V5"] = "NONE"
            penbox["PEN_V_NAME5"] = "NONE"
            penbox["PEN_TYPE_V5"] = "NONE"
            penbox["POS_V5"] = "NONE"
            if penbox["COINCIN_V5"]==0:
                     line["PENV"] -= 1
            penbox["COINCIN_V5"] = 0             
                              
    
    # if value goes below or equal to zero, reset, player out box           
    
    return penbox,line
             
              