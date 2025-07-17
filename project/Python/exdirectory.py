# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 13:37:46 2024

@author: usuario
"""
import sys
d = sys.argv[1]
 # name of subdirectory
import os, shutil
if os.path.isdir(d):
    shutil.rmtree(d) # yes, remove old directory
    os.mkdir(d)
    # make new directory d
    os.chdir(d)
    # move to new directory d