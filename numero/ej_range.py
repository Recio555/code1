# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 10:04:49 2025

@author: usuario
"""

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))
print(nums)

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,13,2)]
print(nums_list2)