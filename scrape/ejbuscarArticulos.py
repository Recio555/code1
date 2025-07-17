# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:54:30 2024

@author: usuario
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now().timestamp())
#random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))



links = getLinks('/wiki/Kevin_Bacon')
print(len(links))
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)