import pandas as pd


class Database:
    def __init__(self):
        pass

    def get_data(self, db, crawler_link):
        sql_cmd = "SELECT * FROM websiteStructureList where status = 'Y'"
        website_db = pd.read_sql(sql_cmd, db.engine)

        if crawler_link == 'All':
            website_db = website_db.reset_index()
            print(website_db)
            return website_db
        else:
            website_db = website_db[website_db['website_url'] == crawler_link]
            website_db = website_db.reset_index()
            print(website_db)
            return website_db
