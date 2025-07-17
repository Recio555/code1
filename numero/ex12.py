# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:11:15 2024

@author: usuario
"""

import	numpy	as	np
import	matplotlib.pyplot as plt

x1=-2
x2=2
y1=1
y2=-1
plt.axis([x1,x2,y1,y2])	
plt.axis('on')
#——————————————————grid	13
plt.grid(True,color='b') 
plt.title('Tick Mark Sample')

#————————————————tick	marks 
xmin=x1
xmax=x2
dx=10
ymin=y1
ymax=y2
dy=10
plt.xticks(np.arange(xmin, xmax, dx))
plt.yticks(np.arange(ymin, ymax, dy))

plt.xlabel('this is the x axis')
plt.ylabel('this is the y axis')


plt.show()
