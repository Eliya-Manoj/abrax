from Wappalyzer import Wappalyzer, WebPage
class Wappalyz():
    def __init__(self,url):
        self.url = url

    def start(self):
        url = self.url
        webpage = WebPage.new_from_url(url)
        #results = Wappalyzer.analyze_with_categories(webpage)
        response = Wappalyzer.analyze_with_categories(webpage)
        print(response)