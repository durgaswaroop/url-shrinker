import unittest
from project import Router
from bs4 import BeautifulSoup as bs


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

        # There would be two input tags on the home page
        input_tags = soup.find_all('input')
        for tag in input_tags:
            # For url tag, value should be "http://"
            if tag['name'] == 'url':
                assert tag['value'] == 'http://'

            # For submit button the text should say "Shrink It!"
            if tag['name'] == 'submit':
                assert tag['value'] == 'Shrink It!'

        # We also have a paragraph tag which will be empty for the initial page load
        assert not soup.find('p').text

    def test_url_shrinking(self):
        website = "http://freblogg.com"
        raw_html = self.app.post('/', data={"url": website}).data
        soup = bs(raw_html, "html.parser")

        url_input = soup.find('input', {"name": "url"})

        # When we have submitted the url, the url value should be set to the entered url when it reloads
        assert url_input['value'] == website

        # Paragraph tag must now have text
        paragraph = soup.find('p')

        assert paragraph.text == "http://localhost:5000/3dc1318"

    def test_url_validation(self):
        valid_urls = [
            "http://google.com",
            "http://foo.com/blah_blah",
            "http://foo.com/blah_blah/",
            "http://foo.com/blah_blah_(wikipedia)",
            "http://foo.com/blah_blah_(wikipedia)_(again)",
            "http://www.example.com/wpstyle/?p=364",
            "https://www.example.com/foo/?bar=baz&inga=42&quux",
            "http://✪df.ws/123",
            "http://userid:password@example.com:8080",
            "http://userid:password@example.com:8080/",
            "http://userid@example.com",
            "http://userid@example.com/",
            "http://userid@example.com:8080",
            "http://userid@example.com:8080/",
        ]

        for url in valid_urls:
            assert Router.validate_url(url)

        invalid_urls = [
            "http://",
            "http://.",
            "http:// shouldfail.com",
            "http://..",
            "http://../",
            "http://?",
            "http://??",
            "http://??/",
            "http://#",
            "http://##",
            "http://##/",
            "http://foo.bar?q=Spaces should be encoded",
            "//",
            "//a",
            "///a",
            "///",
            "http:///a",
            "rdar://1234",
            "h://test",
            ":// should fail",
            "http://foo.bar/foo(bar)baz quux",
            "ftps://foo.bar/",
            "http://-error-.invalid/",
            "http://a.b--c.de/",
            "http://-a.b.co",
            "http://a.b-.co",
            "http://0.0.0.0",
            "http://10.1.1.0",
            "http://10.1.1.255",
            "http://224.1.1.1",
            "http://1.1.1.1.1",
            "http://123.123.123",
            "http://3628126748",
            "http://.www.foo.bar/",
            "http://www.foo.bar./",
            "http://.www.foo.bar./",
        ]

        for url in invalid_urls:
            assert not Router.validate_url(url)


if __name__ == '__main__':
    unittest.main()
