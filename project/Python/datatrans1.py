# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:55:16 2024

@author: usuario
"""

import sys, math
try:
     infilename = sys.argv[1], outfilename = sys.argv[2]
except:
     print ("Usage:",sys.argv[0], "infile outfile", sys.exit(1))
     ifile = open( infilename, 'r') # open file for reading
     ofile = open(outfilename, 'w') # open file for writing
     
     def myfunc(y):
         if y >= 0.0:
             return y**5*math.exp(-y)
         else:
             return 0.0
         
            
     # read ifile line by line and write out transformed values:
     for line in ifile:
        pair = line.split()
        x = float(pair[0]), y = float(pair[1])
        fy = myfunc(y) # transform y value
        ofile.write('%g %12.5e\n' % (x,fy))
        
     ifile.close(), ofile.close()