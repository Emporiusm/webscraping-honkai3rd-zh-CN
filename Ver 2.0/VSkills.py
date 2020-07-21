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
import xlsxwriter as xlwt
souplist    = []
path        = os.path.abspath(os.getcwd())
stats       = pd.DataFrame()
skills      = pd.DataFrame()


#%%
def parsepages(from_page,to_page):
    pages       = range(from_page,to_page+1)
    url_part    = 'https://3rdguide.com/web/valk/detail?id='
    urls        = [url_part + str(page) for page in pages]
    progress    = from_page
    souplist.clear()
    
    for url in urls:
        html    = urlopen(url).read()
        soup    = BeautifulSoup(html.decode('utf-8'),'html.parser')
        dic     = {}
        dic.update(enumerate(soup.stripped_strings))
        name    = dic.get(6)
        if name == None:
            pass
        else:
            souplist.append(soup)
            print('Valkyrie ' + name + ' completed: ' + str(progress) + ' of ' + str(to_page) + ' pages loading...')
            time.sleep(np.random.randint(1,3))
            progress = progress + 1
        return souplist

#%%
def get_skills(souplist):
    if type(souplist) != list:
        raise TypeError
        print('Type of variable souplist must be List')
    else:
        for soup in souplist:
            dic = {}
            dic.update(enumerate(soup.stripped_strings))
            if dic.get(6) == None:
                pass
            else:
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
                concat['Page'] = page
                concat['描述'] = concat['描述'].astype(str).str.strip()
                page = page + 1
                df = df.append(concat)
            df = df.set_index(df['女武神'],drop=True)
            df = df.dropna()
            df.to_excel('valkyrie_skills.xlsx')
            df.to_pickle('valkyrie_skills.pkl')
            skills = df
            return df

#%%
def get_stats(souplist):
    df = pd.DataFrame()
    for soup in souplist:
        dic = {}
        dic.update(enumerate(soup.stripped_strings))
        name = dic.get(8)
        if name.startswith('正在'):
            pass
        elif name == None:
            pass
        elif name in df.iloc[:0].values:
            pass
        else:
            header      = ['name','rank','hp','sp','atk','dfs','crt']
            b           = [name,'B']    + [dic.get(x) for x in range(14,19)]
            a           = [name,'A']    + [dic.get(x) for x in range(19,24)]
            s           = [name,'S']    + [dic.get(x) for x in range(24,29)]
            ss          = [name,'SS']   + [dic.get(x) for x in range(29,34)]
            sss         = [name,'SSS']  + [dic.get(x) for x in range(34,39)]
            df          = df.append(pd.DataFrame(data=[b,a,s,ss,sss],columns=header))
        df = df.reset_index(drop=True)
    df.to_excel('valkyrie_stats.xlsx')
    df.to_pickle('valkyrie_stats.pkl')
    stats = df
    return df

#%%
def export():
    xlwt.w