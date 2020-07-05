# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from urllib.request import urlopen
import sys
import pickle
# %%
class Valkyries:

    """
    Valkyrie class for Honkai 3rd

    <<list of available functions>>

    loadweb(urls)            - call function to synchronize with the web        - return  souplist:         list
    savesoup(souplist)       - call function to save the list from loadweb      - output  souplist.pkl      pkl
    loadsoup(souplist_pkl)   - call function to load local pickle file          - return  souplist:         list
    soup2stats(souplist)     - call function to parse the souplist              - return  df_vstat:         dataframe
    savestats(df_vstats)     - call function to save the dataframe              - output  Valkyrie.pkl      pkl
    loadstats(Valkyrie_pkl)  - call function to load local pickle file          - return  stats:            dataframe
    """

    stats = pd.read_pickle('Valkyrie.pkl')
    
    def __init__(self,name:str=None,rank:str=['B','A','S','SS','SSS']):
        self.name = name
        self.rank = rank

    def __repr__(self,name):
        return '''This is an instance of the Valkyrie class for statistics filter by {!r} in the 'name' column.'''.format(self.name)

    def refesh(self,url_part,pages):
        urls        = [url_part + str(page) for page in pages]
        htmls       = [urlopen(url).read() for url in urls]
        souplist    = [BeautifulSoup(html.decode('utf-8'),'html.parser') for html in htmls]
        return      souplist
        

    
#%%
    class Refresh(Valkyries):

        def __init__(self,url_parts,pages):
            super.__init___()

        def getstats(self,name=None,rank=None):
            if name == None:
                df = pd.DataFrame(rank in stats['rank'])
            elif rank == None:
                df = pd.DataFrame(name in stats['name'])
            else:
                df = pd.DataFrame(rank in stats['rank'] and name in stats['name'])


    def loadweb(self):
    urls        = [url_part + str(page) for page in pages]
    htmls       = [urlopen(url).read() for url in urls]
    souplist    = [BeautifulSoup(html.decode('utf-8'),'html.parser') for html in htmls]
    return souplist

    
#%%
pages       = range(100)
url_part    = 'https://3rdguide.com/web/valk/detail?id='
souplist    = []
df_vstats   = pd.DataFrame()
df          = pd.DataFrame()

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
info()


# %%
def loadweb(urls):
    urls        = [url_part + str(page) for page in pages]
    htmls       = [urlopen(url).read() for url in urls]
    souplist    = [BeautifulSoup(html.decode('utf-8'),'html.parser') for html in htmls]
    return souplist


# %%
def loadsoup(souplist_pkl):
    print('Now loading...')
    souplist = pickle.load(souplist_pkl)
    return souplist


# %%
def savesoup(souplist):
    sys.setrecursionlimit(100000)
    print('Now saving...')
    with open ('souplist.pkl','wb') as chowder:
        pickle.dump(souplist,chowder)
        print('Saving completed!')
    sys.setrecursionlimit(1000)


# %%
def soup2stats(souplist):
    df = pd.DataFrame()
    for soup in souplist:
        dic = {}
        dic.update(enumerate(soup.stripped_strings))
        print(dic)
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
    df_vstats = df
    return df_vstats.reset_index(drop=True,inplace=True)


# %%
def savestats(df):
    print('Now saving...')
    df.to_pickle('Valkyrie.pkl')
    print('Saving Completed!')


# %%
def loadstats(Valkyrie_pkl):
    print('Now Loading')
    df = pd.read_pickle(Valkyrie_pkl)
    print('Loading completed!')
    return df_vstats


# %%
def refreshall():
    souplist = loadweb(urls)
    savesoup(souplist)
    dfstats = soup2stats(souplist)
    savestats(dfstats)
    dfstats.to_excel('Valkyrie_stats.xlsx')


