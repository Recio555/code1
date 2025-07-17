# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:08:35 2024

@author: usuario
"""

def echo(): 
    """Returns everything you type until you press Ctrl-C""" 
    while True: 
        try: 
            print(input('Type Something: ')) 
        except KeyboardInterrupt: 
            print()  # Make sure the prompt appears on a new line. 
            break 
echo()