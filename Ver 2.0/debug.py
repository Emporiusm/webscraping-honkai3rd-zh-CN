# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# -*- coding: UTF-8 -*-
# %%
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request
from urllib.request import urlopen
import sys
import pickle
import openpyxl
import os
import time
import numpy as np
import pprint



# %%
pages       = range(1,2)
url_part    = 'https://3rdguide.com/web/valk/detail?id='
urls        = [url_part + str(page) for page in pages]
souplist    = []
df_vstats   = pd.DataFrame()
df          = pd.DataFrame()
path        = os.path.abspath(os.getcwd())

#%%
def loadweb(urls):
    htmls       = [urlopen(url).read() for url in urls]
    souplist    = []
    for html in htmls:
        soup = BeautifulSoup(html.decode('utf-8'),'html.parser')
        souplist.append(soup)
        time.sleep(np.random.randint(2,5))
    return souplist
    
#%%
soup = loadweb(urls)

#%%
category = soup[0].findAll('p',class_='item1')
cats = []
for cat in category:
    text = cat.get_text()
    cats.append(text)
lst = []
for string in soup[0].stripped_strings:
    lst.append(string)

#%%
index = []
print(cats)
for cat in cats:
    position = lst.index(cat)
    index.append(position)

# %%
print(index)
#%%
dic = {}
for r in range(0,5):
    dic.update(
        {
            lst[index[r]]:
            lst[
                index[r]+1:
                int(index[r+1])-1
            ]
        }
    )
