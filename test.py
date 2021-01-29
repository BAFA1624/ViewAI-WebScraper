from subprocess import call
import os
import time

from bs4 import BeautifulSoup
import numpy as np
from XMLScraper import XMLScraper, WebScraper

# https://www.bbc.co.uk/sitemaps/https-sitemap-uk-news-1.xml
# https://www.bbc.co.uk/news/business-55826646

#os.chmod('test.sh', 0o755)
#rc = call("./test.sh")

website = "https://www.bbc.co.uk/news/business-55826646"


start = time.time()
scraper = WebScraper()
scraper.getWebpageResponse(
    "https://www.bbc.co.uk/news/business-55826646", timeout=3)
soup = scraper.soupify(filename="test_config.json")
#soup = scraper.soupify()
diff = time.time() - start

print(diff)

#    rc = call("./test.sh")
