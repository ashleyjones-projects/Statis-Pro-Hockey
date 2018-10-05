# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:36:40 2017

@author: w9641432
"""

def put_player_in_box(Pen_analysis,Penbox):
    
    if Pen_analysis["PEN_H_NAME"] != "NONE":
        
        if Penbox["PEN_H_NAME1"] == "NONE":
            Penbox["PEN_H_NAME1"] = Pen_analysis["PEN_H_NAME"];Penbox["POS_H1"] = Pen_analysis["POS_H"];Penbox["DURAT_H1"] = Pen_analysis["DURAT_H"]*60;Penbox["PEN_TYPE_H1"] = Pen_analysis["PEN_TYPE_H"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_H1"]=1
        elif Penbox["PEN_H_NAME2"] == "NONE":
            Penbox["PEN_H_NAME2"] = Pen_analysis["PEN_H_NAME"];Penbox["POS_H2"] = Pen_analysis["POS_H"];Penbox["DURAT_H2"] = Pen_analysis["DURAT_H"]*60;Penbox["PEN_TYPE_H2"] = Pen_analysis["PEN_TYPE_H"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_H2"]=1
        elif Penbox["PEN_H_NAME3"] == "NONE":
            Penbox["PEN_H_NAME3"] = Pen_analysis["PEN_H_NAME"];Penbox["POS_H3"] = Pen_analysis["POS_H"];Penbox["DURAT_H3"] = Pen_analysis["DURAT_H"]*60;Penbox["PEN_TYPE_H3"] = Pen_analysis["PEN_TYPE_H"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_H3"]=1
        elif Penbox["PEN_H_NAME4"] == "NONE":
            Penbox["PEN_H_NAME4"] = Pen_analysis["PEN_H_NAME"];Penbox["POS_H4"] = Pen_analysis["POS_H"];Penbox["DURAT_H4"] = Pen_analysis["DURAT_H"]*60;Penbox["PEN_TYPE_H4"] = Pen_analysis["PEN_TYPE_H"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_H4"]=1
        elif Penbox["PEN_H_NAME5"] == "NONE":
            Penbox["PEN_H_NAME5"] = Pen_analysis["PEN_H_NAME"];Penbox["POS_H5"] = Pen_analysis["POS_H"];Penbox["DURAT_H5"] = Pen_analysis["DURAT_H"]*60;Penbox["PEN_TYPE_H5"] = Pen_analysis["PEN_TYPE_H"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_H5"]=1
    
    if Pen_analysis["PEN_V_NAME"] != "NONE":
        
        if Penbox["PEN_V_NAME1"] == "NONE":
            Penbox["PEN_V_NAME1"] = Pen_analysis["PEN_V_NAME"];Penbox["POS_V1"] = Pen_analysis["POS_V"];Penbox["DURAT_V1"] = Pen_analysis["DURAT_V"]*60;Penbox["PEN_TYPE_V1"] = Pen_analysis["PEN_TYPE_V"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_V1"]=1
        elif Penbox["PEN_V_NAME2"] == "NONE":
            Penbox["PEN_V_NAME2"] = Pen_analysis["PEN_V_NAME"];Penbox["POS_V2"] = Pen_analysis["POS_V"];Penbox["DURAT_V2"] = Pen_analysis["DURAT_V"]*60;Penbox["PEN_TYPE_V2"] = Pen_analysis["PEN_TYPE_V"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_V2"]=1
        elif Penbox["PEN_V_NAME3"] == "NONE":
            Penbox["PEN_V_NAME3"] = Pen_analysis["PEN_V_NAME"];Penbox["POS_V3"] = Pen_analysis["POS_V"];Penbox["DURAT_V3"] = Pen_analysis["DURAT_V"]*60;Penbox["PEN_TYPE_V3"] = Pen_analysis["PEN_TYPE_V"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_V3"]=1
        elif Penbox["PEN_V_NAME4"] == "NONE":
            Penbox["PEN_V_NAME4"] = Pen_analysis["PEN_V_NAME"];Penbox["POS_V4"] = Pen_analysis["POS_V"];Penbox["DURAT_V4"] = Pen_analysis["DURAT_V"]*60;Penbox["PEN_TYPE_V4"] = Pen_analysis["PEN_TYPE_V"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_V4"]=1
        elif Penbox["PEN_V_NAME5"] == "NONE":
            Penbox["PEN_V_NAME5"] = Pen_analysis["PEN_V_NAME"];Penbox["POS_V5"] = Pen_analysis["POS_V"];Penbox["DURAT_V5"] = Pen_analysis["DURAT_V"]*60;Penbox["PEN_TYPE_V5"] = Pen_analysis["PEN_TYPE_V"]
            if Pen_analysis["DURAT_H"] == Pen_analysis["DURAT_V"]:
                Penbox["COINCIN_V5"]=1
    return Penbox
    