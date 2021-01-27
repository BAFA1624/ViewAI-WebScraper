import requests
import bs4
import time

from RequestExceptions import Error404

class WebScraper:

    def getWebpageResponse(self, url: str, timeout: float = 2) -> requests.models.Response:
            
        start = time.time()
        response = requests.get(url)
        diff = time.time() - start

        if response.status_code != 200:
            
            if response.status_code == 404:
                raise Error404(url, diff)
        
        else:
            return response

