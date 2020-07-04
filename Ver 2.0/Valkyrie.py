# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# -*- coding: UTF-8 -*-
#import the necessary libraries
# %%
from bs4 import BeautifulSoup
import re
import pandas as pd
import urllib.request
from urllib.request import urlopen
# %%
pages = range(100)
urls        = ['https://3rdguide.com/web/valk/detail?id=' + str(page) for page in pages]
htmls       = [urlopen(url).read() for url in urls]
souplist    = [BeautifulSoup(html.decode('utf-8'),'html.parser') for html in htmls]