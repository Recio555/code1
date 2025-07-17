# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:10:55 2024

@author: usuario
"""

import concurrent.futures as fu
import sys
import requests as req
import os

try:
    from bs4 import BeautifulSoup as Soup
except ImportError:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup as Soup
try:
    from tqdm import tqdm
except ImportError:
    os.system('pip install tqdm')
    from tqdm import tqdm


PREFIX = 'https://www.pdfdrive.com/'
DIR_LINK = 'https://www.pdfdrive.com/download.pdf?id={}&h={}&u=cache&ext=pdf'
BASE = 'Pdf Drive/'

SUGGEST = 'https://www.pdfdrive.com/search/complete?'

# seperated by -
SUGGESTED_FIRST_PAGE = 'https://www.pdfdrive.com/{}-books.html'
SUGGESTED_OTHER_PAGES = 'https://www.pdfdrive.com/search?q={}&pagecount=&pubyear=&searchin=&page={}'

# seperated by +
NOT_SUGGESTED_FIRST_PAGE = 'https://www.pdfdrive.com/search?q={}&pagecount=&pubyear=&searchin=&em=&more=true'
# seperated by %20
NOT_SUGGESTED_OTHER_PAGES = 'https://www.pdfdrive.com/search?q={}&pagecount=&pubyear=&searchin=&em=&more=true&page={}'


def suggest(search):

    parts = search.split()
    if len(parts) != 1:
        temp = ' '.join(parts[:-1]) + ' ' + parts[-1][:-2]
    else:
        temp = parts[0][:-1]

    params = {
        'query': temp,
    }

    r = req.get(SUGGEST, params=params)

    suggestions = r.json()['suggestions']
    if search in suggestions:
        return True, search
    else:
        while True:
            for index, each in enumerate(suggestions):
                print(index, '-', each)
            try:
                x = int(input("-1 - just my search\n-2 - search again \nSuggest ->"))
                if x == -1:
                    return False, search
                if x == -2:
                    return suggest(input("Search > "))

                if x < 0 or x >= len(suggestions):
                    print('Index Error')
                    continue
                return True, suggestions[x]
            except Exception as e:
                print(e)
                continue


            
            
def canGoForward(soup):
    try:
        pagination = soup.find('div', class_='Zebra_Pagination')
        if pagination is not None:
            next_page_list = pagination.find_all('li')
            if len(next_page_list) > 0:
                next_page = next_page_list[-1]
                if next_page.text == 'Next':
                    return next_page.a['href'] != 'javascript:void(0)'
    except Exception:
        return False
    return False           
            
            
            
            
            
            
            
            
            
            
            
            
            
            