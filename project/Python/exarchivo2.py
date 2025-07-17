# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:52:18 2024

@author: usuario
"""
tex = """ 
    greetings i am salvador recio i have more than 10 years as a mathematics teacher
i graduated from the bachelor's degree in education mention mathematics in 2005 
and in 2011 from the master's degree in pure mathematics in addition to being 
a teacher i am interested in working in any field where mathematics is applied as
programming and data analysis, my formation is centered in mathematics for that 
reason I need a training to relate to the specific field of application of
mathematics, which allows me to work in any field where mathematics is involved or
where the domain of mathematics plays a key role. 

with open("archivo.txt", "a") as f:
    tex 
    f.write(tex)
    f.close()
            
"""
import os            
print(os.path.exists('Hola')  )        
with open("archivo.txt", "w") as f:
    tex 
    f.write(tex)
    f.close()
    
with open("archivo.txt") as f:
    tex = f.read()
    print(tex)
    f.close()
    
with open("archivo.txt") as f:
    tex = f.read(10)
    cursor = f.tell()
    print(cursor)
    f.seek(14)
    cursor2 = f.tell()
    print(cursor2)
    f.close()
    
    




























    