import time
from bs4 import BeautifulSoup
import numpy as np

from XMLScraper import XMLScraper, WebScraper

start = time.time()

scraper = XMLScraper()
scraper.getWebpageResponse("https://www.bbc.co.uk/sitemaps/https-sitemap-uk-news-1.xml")
soup = scraper.soupify()

diff = time.time() - start


print(soup.prettify())




