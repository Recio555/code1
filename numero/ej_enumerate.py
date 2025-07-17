# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 13:16:57 2025

@author: usuario
"""

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)
print("\n")


# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)
print("\n")


# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)


print("\n")
print(*enumerate(names,2))