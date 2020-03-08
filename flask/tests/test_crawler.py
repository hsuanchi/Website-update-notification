import unittest
import os
import os.path
import sys
import json

from app import create_app, db


class TestCrawlerClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('[setUpClass]')
        cls.app = create_app("development")
        cls.app = cls.app.test_client()

        db.create_all()
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        print('[tearDownClass]')
        db.session.remove()
        db.drop_all()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_db_connect(self):
        print('[this is first function]')
        response = self.app.get('/category/1')
        # print(response.data)
        self.assertEquals(200, response.status_code)

    def test_db(self):
        print('[this is second function]')

        with self.app.session_transaction() as sess:
            sess["role"] = 'Y'
            assert flask.session['role'] == 'Y'

            response = self.app.post(
                '/crawler/add',
                data=json.dumps({
                    'website':
                    "Google Webmaster",
                    'name':
                    "feed[i].title",
                    'description':
                    "re.compile(r'<[^>]+>').sub('', feed[i].summary)[:300]",
                    'link':
                    "feed[i].link",
                    'url':
                    "http://webmasters.googleblog.com/atom.xml"
                }),
                content_type='application/json')

            self.assertEquals(200, response.status_code)


if __name__ == "__main__":

    unittest.main()