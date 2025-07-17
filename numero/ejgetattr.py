# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:26:05 2024

@author: usuario
"""


class Contact:
    def __init__(self, lName, fName): # explicit constructor for class
        self.lastName = lName
        self.firstName = fName
worker1 = Contact('Smith', 'James')

print(worker1.lastName, worker1.firstName) # object.public_property
print(getattr(worker1, 'lastName'))
newLast=input('Enter new last name: ')

setattr(worker1,'lastName',newLast) # set attribute with new value
print(worker1.lastName, worker1.firstName)
print(getattr(worker1, 'lastName'))  # get existing attribute
newLast=input('Enter new last name: ')
setattr(worker1, 'firstName', newLast)
print(worker1.lastName, worker1.firstName)