import requests
from bs4 import BeautifulSoup, SoupStrainer
import time  # Only included for testing. Remove for package deployment?

# Custom request exceptions library, still to be properly implemented.
# Hopefully will find a way to use exceptions library provided by the requests module in requests.exceptions
from RequestExceptions import Error404

# Type hinting included for ease of reading
from typing import Union

class WebScraper:

    def __init__(self, url: Union[str, None] = None) -> None:
        self.url = url
        self.response = None
        self.soup = None
        self.strainer = None

    def getWebpageResponse(self, url: str, timeout: float = 2) -> Union[requests.models.Response, None]:
            
        '''Returns either requests.models.Response or None'''
        
        response = requests.get(url)
        self.response = response

        if response.status_code != 200:
            
            if response.status_code == 404:
                raise Error404(url, timeout)
            
            return None
        
        else:
            return response

    def soupify(self, parser: str = "lxml", config: Union[str, None] = None) -> Union[BeautifulSoup, None]:
        '''Returns bs4.BeautifulSoup if successful,
        returns None if unsuccessful or if no reponse has been received.'''
        
        strainer = None
        if config is not None:
            self.strainer = self.createStrainer(config)
        
        if self.response is not None:
            self.soup = BeautifulSoup(self.response.content, parser, parse_only=strainer)
            return self.soup
        else:
            return None

    def createStrainer(self, cfg_file: str) -> SoupStrainer:
        
        fullstop_idx = cfg_file.rfind('.')
        if cfg_file[fullstop_idx:] not in ['.json', '.csv',]:
            return None
        
        with open(cfg_file, 'r') as file:
            if cfg_file[fullstop_idx:] == '.json':
                print(file.readlines())
            elif cfg_file[fullstop_idx:] == '.csv':
                print(file.readlines())
        
        return SoupStrainer()




