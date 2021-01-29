import time



from bs4 import BeautifulSoup
import numpy as np
from XMLScraper import XMLScraper, WebScraper



#https://www.bbc.co.uk/sitemaps/https-sitemap-uk-news-1.xml
#https://www.bbc.co.uk/news/business-55826646

times = []
for i in range(100):
    start = time.time()
    scraper = XMLScraper()
    scraper.getWebpageResponse("https://www.bbc.co.uk/sitemaps/https-sitemap-uk-news-1.xml")
    #soup = scraper.soupify(config_file="test_config.json")
    soup = scraper.soupify()
    diff = time.time() - start
    times.append(diff)
    if diff < 1:
        time.sleep(1.75 - diff)
    print("Completed iteration %s." % str(i+1))


print(np.mean(times), np.std(times, ddof=1), "N = 100")




