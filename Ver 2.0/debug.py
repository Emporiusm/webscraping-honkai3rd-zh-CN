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
categories = [category.get_text() for category in soup[0].findAll('p',class_='item1')]

#%%
skname1 = [category.get_text() for category in soup[0].findAll('p',class_='item2')]
print(skname1)

#%%
skdesc1 = [category.get_text() for category in soup[0].findAll('p',class_='msg')]
pp.pprint(skdesc1)

#%%
skname1_1 = [category.get_text() for category in soup[0].findAll('div',class_='item3')]
pp.pprint(skname1_1)
print(len(skname1_1))

#%%

for string in soup[0].stripped_strings:
    lst.append(string)

#%%
skills = [skill.get_text() for skill in soup[0].findAll('p',class_='item2')]
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

#%%


# %%
duc

# %%
dic

# %%
