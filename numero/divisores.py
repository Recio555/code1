# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:06:36 2024

@author: usuario
"""
def factors(b): 
    for i in range(1, b+1):
        if b % i == 0:
            print(i)
if __name__ == '__main__':
    b = input('Your Number Please: ')
    b = float(b) 
    if b > 0 and b.is_integer(): 
        factors(int(b))
    else:
        print('Please enter a positive integer')
