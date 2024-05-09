#!/usr/bin/env python3
import time
import progressbar
import requests
from bs4 import BeautifulSoup
from random import random

##### Edit below

START_ID = 65000000
END_ID = 68000000
SEARCH_STRING = 'dark magneton'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
DEBUG = False #Outputs every id

##### Edit above

url = 'https://www.psacard.com/cert/'
headers = {'User-Agent' : USER_AGENT}

for i in progressbar.progressbar(range(START_ID, END_ID), redirect_stdout=True):
    r = requests.get(url + str(i), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        player = soup.find("th", string="Player")
        td = str(player.parent.td.string).lower()
    except AttributeError:
        if DEBUG:
            print(f'ID NOT FOUND {i}')
        continue
    if SEARCH_STRING in td or DEBUG:
        pstring = f'ID: {url}{i} - {td}'
        print(pstring)
    time.sleep(random() / 10)
