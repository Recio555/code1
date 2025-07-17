# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:44:30 2024

@author: usuario
"""

import ctypes #provides low-levelarrays

class DynamicArray:
    '''AdynamicarrayclassakintoasimplifiedPythonlist.'''
    def init (self):
        '''Createanemptyarray.'''
        Addobjecttoendof
        self. n=0 #countactualelements
        self. capacity=1 #defaultarraycapacity
        self.A=self.makearray(self. capacity) #low-levelarray
 
    def len (self): 
        """Returnnumberofelementsstoredinthearray.""" 
        return self. n 
        
    def getitem (self,k): 
        """Returnelementat indexk.""" 
        if not 0<=k<self. n: 
            raise IndexError( invalidindex ) 
            return self.A[k] #retrievefromarray 
            def append(self,obj): 
                """Addobjecttoendof thearray.""" 
                if self. n==self. capacity: #notenoughroom 
                    self. resize(self.capacity) #sodoublecapacity 
                    self.A[self. n]=obj 
                    self. n+=1
 
    def resize(self,c): #nonpublicutitit 
        """Resizeinternalarraytocapacityc.""" 
        B=self.makearray(c) #new(bigger)array 
        for k in range(self.n): 
            #foreachexistingvalue
            B[k]=self.A[k] 
            self.A=B #usethebiggerarray 
            self. capacity=c
 
    def makearray(self,c): #nonpublicutitity 
        """Returnnewarraywithcapacityc.""" 
        return(ctypes.pyobject)()