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
import time
import numpy as np


# %%
pages       = range(100)
url_part    = 'https://3rdguide.com/web/valk/detail?id='
urls        = [url_part + str(page) for page in pages]
souplist    = []
df_vstats   = pd.DataFrame()
df          = pd.DataFrame()
path        = os.path.abspath(os.getcwd())

#%%
class Valkyrie:
    ''' Webscraping 3rdguide.com creating an object per Valkyrie page '''

    url_prefix = 'https://3rdguide.com/web/valk/detail?id='

    def __init__(self,page,soup=None):
        self.page   = 'https://3rdguide.com/web/valk/detail?id=' + str(page)
        html        = urlopen(self.page).read()
        soup   = BeautifulSoup(html.decode('utf-8'),'html.parser')

    def getskills(self):
        df = pd.DataFrame()
        sk        = [sk.get_text()      for sk      in self.soup.findAll('p',    class_='item1')     ]
        skname    = [skname.get_text()  for skname  in self.soup.findAll('p',    class_='item2')     ]
        skdesc    = [skdesc.get_text()  for skdesc  in self.soup.findAll('p',    class_='msg')       ]
        sk1name   = [sk1name.get_text() for sk1name in self.soup.findAll('p',    class_='item1_1')   ]
        sk1desc   = [sk1desc.get_text() for sk1desc in self.soup.findAll('p',    class_='item1_2')   ]
        sk1stat   = [sk1stat.get_text() for sk1stat in self.soup.findAll('div',  class_='item3')     ]
        sk2name   = [sk2name.get_text() for sk2name in self.soup.findAll('p',    class_='item1_1')   ]
        sk2desc   = [sk2desc.get_text() for sk2desc in self.soup.findAll('p',    class_='item1_2')   ]
        sk2stat   = [sk2stat.get_text() for sk2stat in self.soup.findAll('div',  class_='item3')     ]
        sk3name   = [sk3name.get_text() for sk3name in self.soup.findAll('p',    class_='item1_1')   ]
        sk3desc   = [sk3desc.get_text() for sk3desc in self.soup.findAll('p',    class_='item1_2')   ]
        sk3stat   = [sk3stat.get_text() for sk3stat in self.soup.findAll('div',  class_='item3')     ]
        skill = pd.DataFrame(
            [
                sk,
                skname,
                skdesc,
                sk1name,
                sk1desc,
                sk1stat,
                sk2name,
                sk2desc,
                sk2stat,
                sk3name,
                sk3desc,
                sk3stat
            ],
        ).transpose().set_index(0)
        return skill
        self.skills = skills


# %%
def loadweb(urls):
    htmls       = [urlopen(url).read() for url in urls]
    souplist    = []
    for html in htmls:
        soup = BeautifulSoup(html.decode('utf-8'),'html.parser')
        souplist.append(soup)
        time.sleep(np.random.randint(2,5))
    return souplist


# %%
def savesoup(souplist):
    sys.setrecursionlimit(100000)
    print('Now saving...souplist as pickle file')
    with open ('souplist_skills.pkl','wb') as chowder:
        pickle.dump(souplist,chowder)
        print('Saving completed!')
    sys.setrecursionlimit(1000)


# %%
def loadsoup(souplist_pkl):
    print('Now loading souplist from pickle file...')
    with open('souplist_skills.pkl','rb') as chowder:
        souplist = pickle.load(chowder)
    return souplist
    return print('Loading completed!')


# %%
def soup2skills(souplist):
    df_vskills = pd.DataFrame()
    for soup in souplist:
        sk        = [sk.get_text()      for sk      in soup.findAll('p',    class_='item1')     ]
        skname    = [skname.get_text()  for skname  in soup.findAll('p',    class_='item2')     ]
        skdesc    = [skdesc.get_text()  for skdesc  in soup.findAll('p',    class_='msg')       ]
        sk1name   = [sk1name.get_text() for sk1name in soup.findAll('p',    class_='item1_1')   ]
        sk1desc   = [sk1desc.get_text() for sk1desc in soup.findAll('p',    class_='item1_2')   ]
        sk1stat   = [sk1stat.get_text() for sk1stat in soup.findAll('div',  class_='item3')     ]
        sk2name   = [sk2name.get_text() for sk2name in soup.findAll('p',    class_='item1_1')   ]
        sk2desc   = [sk2desc.get_text() for sk2desc in soup.findAll('p',    class_='item1_2')   ]
        sk2stat   = [sk2stat.get_text() for sk2stat in soup.findAll('div',  class_='item3')     ]
        sk3name   = [sk3name.get_text() for sk3name in soup.findAll('p',    class_='item1_1')   ]
        sk3desc   = [sk3desc.get_text() for sk3desc in soup.findAll('p',    class_='item1_2')   ]
        sk3stat   = [sk3stat.get_text() for sk3stat in soup.findAll('div',  class_='item3')     ]
        df_vskills = df_vskills.append(
            [
                sk,
                skname,
                skdesc,
                sk1name,
                sk1desc,
                sk1stat,
                sk2name,
                sk2desc,
                sk2stat,
                sk3name,
                sk3desc,
                sk3stat
            ]
        )
    return df_vskills


# %%
def savestats(df):
    print('Now saving dataframe to pickle file...')
    df.to_pickle('valkyries_skills.pkl')
    print('Dataframe saving Completed!')


# %%
def loadstats(Valkyrie_pkl):
    print('Now Loading pickle file to dataframe')
    df_vskills = pd.read_pickle("valkyries_skills.pkl")
    print('Dataframe loading completed!')
    return df_vskills


# %%
def refreshall(urls):
    print('Refreshing Web Content...')
    souplist = loadweb(urls)
    df_vskills = soup2skills(souplist)
    return df_vskills.to_excel('valkyrie_skills.xlsx')
    return savesoup(souplist)
    return savestats(df_vstats)
    return print('Task Completed!')

#%%
vsk = refreshall(urls)
vsk

# %%
