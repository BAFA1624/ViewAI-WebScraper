import time
from bs4 import BeautifulSoup

test_py_start = time.time()

from WebScraper import WebScraper


scraper = WebScraper()
response = scraper.getWebpageResponse("https://bbc.com")
print(BeautifulSoup(response.content, "xml"))


test_py_diff = time.time() - test_py_start

print("Total runtime was: {}".format(test_py_diff))

