# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:00:13 2024

@author: usuario
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
#html = urlopen('https://www.planetadelibros.com/seleccion-editorial/libros-recomendados/132')
bs = BeautifulSoup(html.read(), 'html.parser')
#print(bs)

#nameList = bs.findAll('h1')
nameList = bs.find_all(['h1','h2','h3','h4','h5','h6'])
for name in nameList:
    print(name.get_text())