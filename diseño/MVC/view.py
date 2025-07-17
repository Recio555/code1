# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:13:50 2024

@author: usuario
"""

class GreetingView(object): 
    def __init__(self):
        pass
    def generate_greeting(self, name,time_of_day, known):
        if name == "lion":
            print("RRRrrrrroar!")
            return
        if known:
            print("Good {} welcome back {}!".format(time_of_day, name))
            #print("Welcome back {}!".format(name))
        else:
            print("Good {} {}, it is good to meet you".format(time_of_day, name))
            #print("Hi {}, it is good to meet you".format(name))