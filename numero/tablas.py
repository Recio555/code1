# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:36:16 2024

@author: usuario
"""

def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
if __name__ == '__main__':
    while True:
        a = input('Enter a number: ')
        multi_table(float(a))
        
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break