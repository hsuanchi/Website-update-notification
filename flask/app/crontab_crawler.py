from sqlalchemy import create_engine
from config.config import config
from views.crawler import Main


# MySql datebase
db_conn = create_engine(config['development'].SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    obj_Crawler = Main.Crawler()
    obj_Crawler.crawl(
        db_conn, 'All')
