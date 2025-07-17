# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 10:09:14 2025

@author: usuario
"""
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

indexed_names = []
for i in range(len(names)):

    index_name = (i, names[i])

    indexed_names.append(index_name)


print(indexed_names)