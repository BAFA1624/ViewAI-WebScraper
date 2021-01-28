import time

start = time.time()

from bs4 import BeautifulSoup
import numpy as np
from XMLScraper import XMLScraper, WebScraper



#https://www.bbc.co.uk/sitemaps/https-sitemap-uk-news-1.xml
#https://www.bbc.co.uk/news/business-55826646

scraper = XMLScraper()
scraper.getWebpageResponse("https://www.bbc.co.uk/sitemaps/https-sitemap-uk-news-1.xml")
soup = scraper.soupify(config_file="test_cfg.json")

diff = time.time() - start

print(diff)
print(soup.get_text('\n'))
print(type(soup))



