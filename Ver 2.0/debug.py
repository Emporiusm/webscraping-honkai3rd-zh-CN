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
from_page   = 1
to_page     = 100
pages       = range(from_page,to_page+1)
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
    enumerate(souplist,start=from_page)
    return souplist

#%%
pp = pprint.PrettyPrinter()
souplist = loadweb(urls)

#%%
df = pd.DataFrame()

for soup in souplist:
    dic = {}
    dic.update(enumerate(soup.stripped_strings))
    name = dic.get(6)
    categories = [category.get_text() for category in soup.findAll('p',class_='item1')]
    major_name = [category.get_text() for category in soup.findAll('p',class_='item2')]
    string1 = str()
    major_detail = [string1 + category.get_text() for category in soup.findAll('p',class_='msg')]
    minor_name = [category.get_text() for category in soup.findAll('p',class_='item1_1')]
    string2 = str()
    minor_detail = [string2 + category.get_text() for category in soup.findAll('div',class_='item3')]
    major = pd.DataFrame([major_name,major_detail],index=['技能','描述'])
    minor = pd.DataFrame([minor_name[1:-1],minor_detail],index=['技能','描述'])
    concat = pd.concat([major,minor],axis=1).transpose()
    concat['女武神'] = name
    concat['Page'] = from_page
    df = df.append(concat).dropna()
df = df.set_index('女武神')

#%%
df

# %%
