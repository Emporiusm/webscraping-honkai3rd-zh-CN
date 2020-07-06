# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
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


# %%
pages       = range(100)
url_part    = 'https://3rdguide.com/web/valk/detail?id='
urls        = [url_part + str(page) for page in pages]
souplist    = []
df_vstats   = pd.DataFrame()
df          = pd.DataFrame()
path        = os.path.abspath(os.getcwd())


# %%
def info():
    bowls   = len(souplist)
    vstats  = round(len(df_vstats)/5)
    print(f"""
    Currently there are {bowls} bowls of soup in the souplist and the {vstats} sets of stats in the Dataframe buffer.

    <<list of available functions>>

    loadweb(urls)            - call function to synchronize with the web        - return  souplist:       list
    savesoup(souplist)       - call function to save the list from loadweb      - output  souplist.pkl    pkl
    loadsoup(souplist_pkl)   - call function to load local pickle file          - return  souplist:       list
    soup2stats(souplist)     - call function to parse the souplist              - return  df_vstat:       dataframe
    savestats(df_vstats)     - call function to save the dataframe              - output  Valkyrie.pkl    pkl
    loadstats(Valkyrie_pkl)  - call function to load local pickle file          - return  df_vstats:      dataframe""")


# %%
def loadweb(urls):
    history = {}
    htmls       = [urlopen(url).read() for url in urls]
    souplist    = [BeautifulSoup(html.decode('utf-8'),'html.parser') for html in htmls]
    return souplist


# %%
for soup in souplist:
    for string in soup.stripped_strings:
        print(repr(string))


# %%
def history():
    htmls       = [urlopen(url).read() for url in urls]


# %%
def savesoup(souplist):
    sys.setrecursionlimit(100000)
    print('Now saving...souplist as pickle file')
    with open ('Vstats.pkl','wb') as chowder:
        pickle.dump(souplist,chowder)
        print('Saving completed!')
    sys.setrecursionlimit(1000)


# %%
def loadsoup(souplist_pkl):
    print('Now loading souplist from pickle file...')
    with open('Vstats.pkl','rb') as chowder:
        souplist = pickle.load(chowder)
    return souplist
    return print('Loading completed!')


# %%
def soup2stats(souplist):
    df = pd.DataFrame()
    for soup in souplist:
        dic = {}
        dic.update(enumerate(soup.stripped_strings))
        name = dic.get(8)
        if name.startswith('正在'):
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
    return df


# %%
def savestats(df):
    print('Now saving dataframe to pickle file...')
    df.to_pickle('Valkyrie.pkl')
    print('Dataframe saving Completed!')


# %%
def loadstats(Valkyrie_pkl):
    print('Now Loading pickle file to dataframe')
    df = pd.read_pickle(Valkyrie_pkl)
    print('Dataframe loading completed!')
    return df_vstats


# %%
def refreshall(urls):
    print('Refreshing Web Content...')
    souplist = loadweb(urls)
    df_vstats = soup2stats(souplist)
    return df_vstats.to_excel('Valkyrie_stats.xlsx')
    return savesoup(souplist)
    return savestats(df_vstats)
    return print('Task Completed!')


