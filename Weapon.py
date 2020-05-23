# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# -*- coding: UTF-8 -*-

#import the necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from urllib.request import urlopen

#first create an empty dataframe
df = pd.DataFrame()

#create a variable that ranges from 1 to 300, representing the numerical id of the page derived from the url
counter = range(1,300)

#another counter for the completion announcer at the end of each loop
c = 1

for u in counter:
    url = 'https://3rdguide.com/web/arm/detail?id=' + str(u)
    html = urlopen(url).read()
    html = html.decode('utf-8')
    soup = BeautifulSoup(html,'html.parser')
    name = soup.find('p',class_='item-1').get_text()
    atk = soup.find('div',class_='gongji').get_text()
    crt = soup.find('div',class_='huixin').get_text()
    ability = soup.find_all('p',class_='mark-item-20')
    if len(ability) == 2:
        spec = [name,atk,crt,ability[0].get_text(),ability[1].get_text()]
        sp = pd.DataFrame(spec).transpose()
        df = df.append(sp)
        df.to_excel('weapon.xlsx')
    if len(ability) == 1:
        spec = [name,atk,crt,ability[0].get_text()]
        sp = pd.DataFrame(spec).transpose()
        df = df.append(sp)
    print(str(c) + ' - ' + name + ' completed!')
    c = c + 1

#create the mapper dict for the renaming of columns
columns={
    '0':'武器名稱',
    '1':'攻擊',
    '2':'會心',
    '3':'技能一',
    '4':'技能二'
}

#trim whitespaces
df[3] = df[3].str.strip()
df[4] = df[4].str.strip()

#renaming the columns
df = df.rename(columns=columns)

#export the excel file
df.to_csv('weapon.csv')
exit()


