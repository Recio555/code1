# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:11:13 2024

@author: usuario
"""

class SingletonObject(object):
    class __SingletonObject():
        def __init__(self): 
            self.val = None 
        def __str__(self): 
            return "{0!r} {1}".format(self, self.val)
        instance = None
        def __new__(cls): 
            if not SingletonObject.instance: 
                SingletonObject.instance = SingletonObject.__SingletonObject() 
                return SingletonObject.instance
        def __getattr__(self, name):
            return getattr(self.instance, name)
        def __setattr__(self, name):
            return setattr(self.instance, name)
obj1 = SingletonObject()
obj1.val = "Object value 1"
print("print obj1: ", obj1)