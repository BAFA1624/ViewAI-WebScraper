import time
from bs4 import BeautifulSoup
import numpy as np

from WebScraper import WebScraper

start = time.time()

scraper = WebScraper()
scraper.getWebpageResponse("https://bbc.com")
soup = scraper.soupify()

diff = time.time() - start

print(diff)



