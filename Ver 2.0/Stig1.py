# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# -*- coding: UTF-8 -*-
#import the necessary libraries
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request
from urllib.request import urlopen


# %%
def webpage(pages):
    ls = []
    for page in range(pages):
        url = 'https://3rdguide.com/web/stig/detail?id=' + str(page)
        html = urlopen(url).read()
        html = html.decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')
        if type(soup) != None:
            ls.append(soup)
            print(setname + ' stored!')
    return ls


# %%
def get_setname(x):
    tag = 'p'
    clas = "mark-item-16 center"
    html = x.find(tag,class_=clas)
    setname = html.get_text()
    return setname


# %%
def get_stig(x):
    tag = 'div'
    clas = 'stig-table'
    stiglist = []
    df = pd.DataFrame()
    sr = pd.DataFrame()
    hp = None
    atk = None
    dfs = None
    crt = None
    e = 1
    for element in x.find_all(tag,class_=clas):
        text = element.get_text().split("\n\n\n")
        stigname = text[1]
        stigstat = list(text[2].split("\n"))
        hp = stigstat[0]
        atk = stigstat[1]
        dfs = stigstat[2]
        crt = stigstat[3]
        dic = {
            e:[stigname,hp,atk,dfs,crt]
        }
        df = df.append(pd.DataFrame.from_dict(dic,orient='index',columns=['部位','生命','攻擊','防禦','會心']))
        e = e + 1
    df = df.reset_index(drop=True)
    return df


# %%
def set_setname(x):
    df = pd.Series(dtype=str)
    instances = len(get_stig(x))
    result = []
    for i in range(instances):
        result.append(get_setname(x))
    return result


# %%
def get_desc(x):
    tag = 'p'
    clas = 'mark-item-19'
    result = []
    sr = pd.Series(dtype=str)
    for element in x.find_all(tag,class_=clas):
        text = element.get_text()
        text = text.strip()
        sr = sr.append(pd.Series(text,dtype=str))
    sr = sr[1:]
    return sr


# %%
def frame(x):
    dic_desc = {
        '套裝':set_setname(x),
        '能力':get_desc(x)
    }
    df = pd.DataFrame.from_dict(dic_desc,dtype=str).reset_index(drop=True)
    df = df.join(get_stig(x),how='left')
    df = df.filter(items=['套裝','部位','生命','攻擊','防禦','會心','能力'])
    return df


# %%
def setability(x):
    if type(x) == None:
        result = None
        return result
    else:
        settwo = x.find('p',class_='mark-item-20').get_text()
        setthree = x.find('p',class_='mark-item-20 mb60').get_text()
        if len(setthree) == None and len(settwo) == None:
            result = None
            return result
        elif len(setthree) == None and len(settwo) != None:
            result = pd.DataFrame(
                data=[get_setname(x)[0],'兩件套','','','','',settwo],
                columns=['套裝','部位','生命','攻擊','防禦','會心','能力']
                )
            return result
        elif len(setthree) != None and len(settwo) != None:
            result = pd.DataFrame(
                data=[[get_setname(x)[0],'兩件套','','','','',settwo.strip()],[get_setname(x)[0],'三件套','','','','',setthree.strip()]],
                columns=['套裝','部位','生命','攻擊','防禦','會心','能力']
            )
            return result


# %%
def compiling(x):
    if type(setability(x)) == str:
        df = frame(x)
        return df
    elif type(setability(x)) != str:
        df = pd.concat([frame(x),setability(x)],axis=0)
        return df


# %%
def get_info(pages):
    souplist = []
    r = range(len(pages))
    for page in r:
        hotsoup = webpage(page) 
        souplist.append(hotsoup)
    return souplist


# %%
pages = webpage(10)
frame = compiling(pages)
info = get_indo(frame)


# %%



