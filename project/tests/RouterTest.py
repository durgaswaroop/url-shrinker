import unittest
from project import Router


class RouterTest(unittest.TestCase):

    def setUp(self):
        self.app = Router.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        raw_html = self.app.get('/').data
        soup = bs(raw_html, "html.parser")
        # print(soup)

        assert soup.find('title').text == "Swaroop's URL Shrinker"
        assert soup.find('h1').text == "Swaroop's URL Shrinker"

if __name__ == '__main__':
    unittest.main()
