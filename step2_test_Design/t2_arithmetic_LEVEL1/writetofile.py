#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 08:01:06 2018

Name: fUNCTION -writetofile(str,Matrix,str)

@author: kishore, 217BM1284, MEI LAB, NITR
Project: Biosignal Processing (EEG and Cognition)
"""

import os.path

def writetofile(testname,Matrix):
    VolunteerNAME=Matrix[2][1]
    save_path = '/home/k/workbench/cognitionExp/step2_test_Design/Results/'
    #save_path = 'C:\Results'
    filename=testname+"_"+VolunteerNAME
    filepath=os.path.join(save_path,filename+".txt")
    file = open(filepath,"w")
    file.write(str(Matrix))
    file.close()
