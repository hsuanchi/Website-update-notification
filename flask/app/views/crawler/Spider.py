# Import 爬蟲相關
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import feedparser


# Import 資料處理相關
import pandas as pd
from datetime import datetime
import re

# Import Date Transformate
# from .DateFormate import DateFormatHelper


class Craw:
    def __init__(self):
        self.dict_crawl = {
            'wid': [],
            'crawler_name': [],
            'crawler_description': [],
            'crawler_link': [],
            'insert_time': [],
        }

        # 爬蟲
        self.headers = {
            'User-Agent': UserAgent().random
        }

        self.NOW = datetime.now()
        # self.date_transformate = DateFormatHelper()

    def fetch_data(self, db, website_db):
        for row in range(website_db.shape[0]):
            url = website_db['website_url'][row]
            r = requests.get(url=url, headers=self.headers)
            soup = BeautifulSoup(r.text, features="html.parser")
            feed = feedparser.parse(url).entries
            try:
                for i in range(2):
                    css_name = eval(website_db['css_name'][row])
                    css_description = eval(website_db['css_description'][row])
                    css_link = eval(website_db['css_link'][row])

                    self.dict_crawl['wid'].append(website_db['wid'][row])
                    self.dict_crawl['crawler_name'].append(css_name)
                    self.dict_crawl['crawler_description'].append(
                        css_description)
                    self.dict_crawl['crawler_link'].append(css_link)
                    self.dict_crawl['insert_time'].append(self.NOW)
                df = pd.DataFrame({'wid': [website_db['wid'][row]],
                                   'crawler_status': ['ok'],
                                   'insert_time': [self.NOW],
                                   })
                df.to_sql(name='statusLog', con=db.engine,
                          if_exists='append', index=False)
            except Exception as e:
                print(
                    '[This is Exception ------------------------------------------------------------------------------------]', e)
                dff = pd.DataFrame({'wid': [website_db['wid'][row]],
                                    'crawler_status': ['error'],
                                    'insert_time': [self.NOW],
                                    })
                dff.to_sql(name='statusLog', con=db.engine,
                           if_exists='append', index=False)

        return self.dict_crawl
