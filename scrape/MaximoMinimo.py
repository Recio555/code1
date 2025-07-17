# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:47:28 2024

@author: usuario
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
#html = urlopen('https://www.planetadelibros.com/seleccion-editorial/libros-recomendados/132')
bs = BeautifulSoup(html.read(), 'html.parser')
#print(bs)

#nameList = bs.findAll('h1')
nameList = bs.find_all(string ='the prince')
print(len(nameList))
for name in nameList:
    print(name.get_text())