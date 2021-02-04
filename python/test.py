from subprocess import call
import os
import time

from FormatText import format_text

from bs4 import BeautifulSoup
import numpy as np
from XMLScraper import XMLScraper, WebScraper

# https://www.bbc.co.uk/sitemaps/https-sitemap-uk-news-1.xml
# https://www.bbc.co.uk/news/business-55826646

#os.chmod('test.sh', 0o755)
#rc = call("./test.sh")

website = "https://www.bbc.co.uk/news/health-55757790"

start = time.time()
scraper = WebScraper()
scraper.getWebpageResponse(
    "https://www.bbc.co.uk/news/business-55916254",
    timeout=3
)
#soup = scraper.soupify()
soup = scraper.soupify(configuration_filename="test_config.json")
text = scraper.soupToText()
formatted_text = format_text(text)

diff = time.time() - start

for obj in formatted_text:
    print(obj)
    print("-")

print(diff)

with open("test_soup.txt", 'w') as file:
    file.writelines(text)

#    rc = call("./test.sh")
