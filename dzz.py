#!/usr/bin/python3.5
# coding: utf8

import urllib3
import re
from bs4 import BeautifulSoup

def dzz(getmenu,charpter):
    url = 'http://www.23wx.com/html/42/42377/'
    http = urllib3.PoolManager()
    req = http.request('Get',url)
    soup = BeautifulSoup(req.data,'lxml')
    cont = soup.find_all('a',href=re.compile(r'^[0-9]'))
    menu = []
    for c in cont:
        if '第' in c.text and '章' in c.text:
            x = [c.text, url + c['href']]
            menu.append(x)
    if (getmenu == 'y'):
        print(menu)
        print('\n')

    urlcontents = menu[int(charpter)][1]
    print(menu[int(charpter)])
    http2 = urllib3.PoolManager()
    req2 = http2.request('GET', urlcontents)
    soup2 = BeautifulSoup(req2.data, "lxml")
    contents = soup2.find_all('dd', id='contents')
    for cs in contents:
        print(cs.text)

getmenu = input('Get menus(Type y to get menus and type n to pass)? y/n:')
charpter = input('input charpter:')
dzz(getmenu,charpter)