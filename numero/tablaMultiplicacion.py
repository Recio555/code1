# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:15:51 2024

@author: usuario
"""

def multi_table(a): 
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(float(a)) 