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

#first create an empty dataframe
df = pd.DataFrame()

#create a variable that ranges from 1 to 200, representing the numerical id of the page, to be used later in the for loop
counter = range(1,200)

#another counter for the completion announcer
c = 1

#classic for loop since the url of each stigmata page is differentiated using a serial code starting from 1
for u in counter:
    url = 'https://3rdguide.com/web/stig/detail?id=' + str(u)
    html = urlopen(url).read()
    html = html.decode('utf-8')
    soup = BeautifulSoup(html,'html.parser')

    #this will grab the name of the stigmata set
    name = soup.find('p',class_="mark-item-16 center").get_text()

    #This will grab the name of the stigmata piece by body part, and fill it with None if there is no set ability
    stig = soup.find_all('div',class_="stig-table")
    stiglist = []
    if stig == None:
        stiglist = None
    else:
        for s in stig:
            data = s.get_text()
            pattern = re.compile('[0-9]')
            target = pattern.split(data)[0]
            target1 = str.strip(target)
            stiglist.append(target1)

    #this will grab the stats of each of the stigmata piece, and fill it with None if there is no set ability
    stig1 = soup.find_all('div',class_="stig-table-1")
    stiglist1 = []
    if stig1 == None:
        stiglist1 = None
    else:
        for s in stig1:
            data = s.get_text()
            target = data.splitlines()
            stiglist1.append(target)

    #this will grab the description of the ability of the stigmata piece, and fill it with None if there is no set ability
    stigdesc = soup.find_all('p',class_="mark-item-19 mb30")
    desclist = []
    if stigdesc == None:
        desclist = None
    else:
        for s in stigdesc:
            s = s.get_text()
            s = s.strip()
            desclist.append(s)

    #this will grab the description of the 2 piece set ability, and fill it with None if there is no set ability
    stigset2 = soup.find('p',class_="mark-item-20")
    if stigset2 == None:
        stigset2 = None
    else:
        stigset2 = stigset2.get_text().strip()

    #this will grab the description of the 3 piece set ability, and fill it with None if there is no set ability
    stigset3 = soup.find('p',class_="mark-item-20 mb60")
    if stigset3 == None:
        stigset3 = None
    else:
        stigset3 = stigset3.get_text().strip()

    #this will first evaluate the piece count of the set, and pass a different set of assignment to avoid out of bound
    if len(stiglist) == 0:
        top = ''
        mid = ''
        btm = ''
        set2 = ''
        set3 = ''

    if len(stiglist) == 3:
        top = (name,stiglist[0],stiglist1[0][1],stiglist1[0][2],stiglist1[0][3],stiglist1[0][4],desclist[0])
        mid = (name,stiglist[1],stiglist1[1][1],stiglist1[1][2],stiglist1[1][3],stiglist1[1][4],desclist[1])
        btm = (name,stiglist[2],stiglist1[2][1],stiglist1[2][2],stiglist1[2][3],stiglist1[2][4],desclist[2])
        set2 = (name,'兩件套','','','','',stigset2)
        set3 = (name,'三件套','','','','',stigset3)

    elif len(stiglist) == 2:
        top = (name,stiglist[0],stiglist1[0][1],stiglist1[0][2],stiglist1[0][3],stiglist1[0][4],desclist[0])
        mid = (name,stiglist[1],stiglist1[1][1],stiglist1[1][2],stiglist1[1][3],stiglist1[1][4],desclist[1])
        btm = ''
        set2 = (name,'兩件套','','','','',stigset2)
        set3 = ''

    elif len(stiglist) == 1:
        top = (name,stiglist[0],stiglist1[0][1],stiglist1[0][2],stiglist1[0][3],stiglist1[0][4],desclist[0])
        mid = ''
        btm = ''
        set2 = ''
        set3 = ''

    #Compiling of the variables into a DataFrame
    df = df.append([top,mid,btm,set2,set3])

    #Completion announcer for one stigmata set
    print(str(c) + ' - ' + name + ' completed!')

    #counter + 1
    c = c + 1

#creating a column header mapper for later use of renaming the column headers
columns={
    '0':'聖痕套裝',
    '1':'聖痕單件',
    '2':'血量',
    '3':'攻擊',
    '4':'防禦',
    '5':'會心',
    '6':'描述'
}

#trim whitespaces
df[6] = df[6].str.strip()

#renaming the columns
df = df.rename(columns=columns)

#export the excel file
df.to_csv('stigmata.csv')
exit()


