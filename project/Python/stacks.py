# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:42:56 2024

@author: usuario
"""

classArrayStack: 
    '''LIFOStackimplementationusingaPythonlistasunderlyingstorage.''' 
    
    def init (self): 
        """Createanemptystack.""" 
        self. data=[ ] #nonpubliclist instance
 
 8 def len (self):
 9 ”””Returnthenumberofelements inthestack.”””
 10 returnlen(self. data)
 11
 12 def isempty(self):
 13 ”””ReturnTrueifthestackisempty.”””
 14 returnlen(self. data)==0
 15
 16 defpush(self,e):
 17 ”””Addelementetothetopofthestack.”””
 18 self. data.append(e) #newitemstoredatendof list
 19
 20 deftop(self):
 21 ”””Return(butdonotremove)theelementatthetopof thestack.
 22
 23 RaiseEmptyexceptionifthestackisempty.
 24 ”””
 25 ifself.isempty():
 26 raiseEmpty( Stackisempty )
 27 returnself. data[−1] #thelast iteminthelist
 28
 29 defpop(self):
 30 ”””Removeandreturntheelement fromthetopof thestack(i.e.,LIFO).
 31
 32 RaiseEmptyexceptionifthestackisempty.
 33 ”””
 34 ifself.isempty():
 35 raiseEmpty( Stackisempty )
 36 returnself. data.pop()