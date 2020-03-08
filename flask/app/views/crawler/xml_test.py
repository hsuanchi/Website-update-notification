# Import 爬蟲相關
import re
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
import feedparser

# Import 資料處理相關

i = 1
url = 'https://qdm.zendesk.com/hc/zh-tw/sections/203750947-%E5%8A%9F%E8%83%BD%E7%95%B0%E5%8B%95'
# url = 'https://www.waca.net/support/account'
# url = 'https://product-updates.shoplineapp.com/zh'
# url = 'https://support.google.com/tagmanager/answer/4620708'
# url = 'https://www.ichdata.com/author/root'
# url = 'https://www.simoahava.com/index.xml'
# url = 'https://crawler.maxlist.xyz/rss.xml'
# url = 'http://webmasters.googleblog.com/atom.xml'

# =================feedparser===========================

# feed = feedparser.parse(url).entries

# title = feed
# print(title)

# txt = re.compile(r'<[^>]+>').sub('', feed[i].summary)[:300]
# words = re.compile(r'[^A-Z^a-z]+').split(txt)
# de = words.join''
# print(words)
# print(txt)

# =================BeautifulSoup===========================

r = requests.get(url=url)
soup = BeautifulSoup(r.text, features="html.parser")

title = '【QDM】' + soup.find_all(
    class_='article-list')[0].find_all('li')[i].text.strip()
print(title)
description = soup.find_all(
    class_='article-list')[0].find_all('li')[i].text.strip()
print(description)
link = 'https://qdm.zendesk.com/' + soup.find_all(
    class_='article-list')[0].find_all('li')[i].find('a').get('href')
print(link)

# ==================================================

# print(title_soup[0])
# print(link_soup)

# url = 'https://crawler.maxlist.xyz/rss.xml'
# url = 'https://crawler.maxlist.xyz'
# url = 'http://feedpress.me/mozblog.xml'

# r = requests.get(url=url)
# soup = BeautifulSoup(r.text, features="html.parser")

# for i in range(2):
#     print(i.title)
#     print(i.link)
#     print(i.description)

# title = re.compile(('<link rel="alternate" type="text/html" href=(.*)'))
# # link = re.compile('<link>(.*)</link>')

# find_title = re.findall(title, soup)
# find_link = re.findall(link, soup)

# literate = []
# literate[:] = range(1, 16)

# for i in literate:
#     print(find_title[i])
#     # print(find_link[i])
