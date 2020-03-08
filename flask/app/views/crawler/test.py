# Import 爬蟲相關
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Import 資料處理相關
import pandas as pd
from datetime import datetime

# Import Date Transformate
from DateFormate import DateFormatHelper


class Craw:
    def __init__(self):
        self.dict_crawl = {
            'website': [],
            'name': [],
            'date': [],
            'description': [],
            'updatetime': [],
            'link': []
        }

        # 爬蟲
        self.headers = {
            'User-Agent': UserAgent().random
        }

        self.NOW = datetime.now()
        self.date_transformate = DateFormatHelper()

    def fetch_data(self, website_url):
        url = website_url
        r = requests.get(url=url, headers=self.headers)
        soup = BeautifulSoup(r.text, features="html.parser")
        try:
            for i in range(2):
                self.dict_crawl['website'].append('test'
                                                  )
                self.dict_crawl['name'].append(
                    soup.find_all(class_='announcement__post')[i].find(class_='announcement__post-title').text)
                self.dict_crawl['date'].append(
                    self.NOW)
                self.dict_crawl['link'].append(
                    'https://support.google.com'+soup.find_all(class_='announcement__post-body-read-more-link')[i].get('href'))
                self.dict_crawl['description'].append(
                    soup.find_all(class_='announcement__post')[i].find(class_='announcement__post-body').text[:150])
                self.dict_crawl['updatetime'].append(self.NOW)
            df = pd.DataFrame({'name': 'test',
                               'url': [url],
                               'status': ['ok'],
                               'updatetime': [self.NOW]
                               })

            # df.to_sql(name='statusLog', con=db.engine,
            #           if_exists='append', index=False, index_label='id')
        except:
            df = pd.DataFrame({'name': 'test',
                               'url': [url],
                               'status': ['error'],
                               'updatetime': [self.NOW]
                               })
            # df.to_sql(namedxists='append', index=False, index_label='id')

        return self.dict_crawl


if __name__ == "__main__":
    url_google_ads = 'https://support.google.com/google-ads/announcements/9048695'
    url_metchants = "https://support.google.com/merchants/announcements/6192467"
    url_op = "https://support.google.com/optimize/announcements/9176329"

    # 'https://support.google.com'+soup.find_all(class_='announcement__post')[i].find_all('a')[1].get('href')

    crawler = Craw()

    print(crawler.fetch_data(url_op))
    # crawler.fetch_data(url_metchants)
