# Import Model
import pandas as pd
from ..crawler import Database, Spider


class Crawler:

    def __init__(self):
        # url DB 管理
        self.database = Database.Database()
        # url 爬取
        self.spider = Spider.Craw()

    def crawl(self, db, crawler_link):
        website_soup = self.database.get_data(db, crawler_link)
        dict_crawl = self.spider.fetch_data(db, website_soup)
        df = pd.DataFrame(dict_crawl)
        df.to_sql(name='crawlerData', con=db.engine,
                  if_exists='append', index=False)


if __name__ == "__main__":
    obj_Crawler = Crawler_main()
    obj_Crawler.crawl('All')


'''
# 爬取網站清單 announcements：
# Google Ads
https: // support.google.com/google-ads/announcements/9048695

# Merchant Center
https: // support.google.com/merchants/announcements/6192467

# Data Studio
https: // support.google.com/datastudio/answer/6311467?hl = en & ref_topic = 6267740

# 參考框架
https://www.itread01.com/content/1548981552.html

'''
