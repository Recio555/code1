# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:20:16 2024

@author: usuario
"""

import os
def diskusage(path):
    '''Returnthenumberofbytesusedbyafile/folderandanydescendents.'''
    total=os.path.getsize(path) #account fordirectusage
    if os.path.isdir(path): #ifthis isadirectory,
        for filename in os.listdir(path): #thenforeachchild:
         childpath=os.path.join(path,filename) #composefullpathtochild
         total+=diskusage(childpath) #addchild’susagetototal
        
        print( '{0:<7}'.format(total),path) #descriptiveoutput(optional)
        return 
    
diskusage(C:/)
    
