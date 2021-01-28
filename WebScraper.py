import requests
from bs4 import BeautifulSoup, SoupStrainer
import time  # Only included for testing. Remove for package deployment?
import json

# Custom request exceptions library, still to be properly implemented.
# Hopefully will find a way to use exceptions library provided by the requests module in requests.exceptions
from RequestExceptions import Error404

# Type hinting included for ease of reading and autocompletion while in dev
from typing import Union

# In future will turn this into 
class WebScraper:

    def __init__(self, url: Union[str, None] = None) -> None:
        self.url = url
        self.response = None
        self.soup = None
        self.strainer = None

    def getWebpageResponse(self, url: str, timeout: float = 2) -> Union[requests.models.Response, None]:
            
        '''Returns either requests.models.Response or None'''
        
        # Make response request
        response = requests.get(url)
        self.response = response

        # Error handling to be written for responses other than 200 (successful response)
        if response.status_code != 200:
            
            if response.status_code == 404:
                raise Error404(url, timeout)
            
            return None
        
        else:
            return response

    def soupify(self, parser: str = "lxml", config: Union[str, None] = None) -> Union[BeautifulSoup, None]:
        '''Returns bs4.BeautifulSoup if successful,
        returns None if unsuccessful or if no reponse has been received.'''
        
        # If config file provided, create custom filter
        strainer = None
        if config is not None:
            self.strainer = self.strainerFromFile(config)
            strainer = self.strainer
        
        # If a reponse has been received from webpage, run it through BeautifulSoup
        if self.response is not None:
            self.soup = BeautifulSoup(self.response.content, parser, parse_only=strainer)
            return self.soup
        else:
            return None

    # Customization to be provided by .json file in deployment pckg
    def strainerFromFile(self, cfg_file: str) -> SoupStrainer:
        
        # Check config file is .json
        fullstop_idx = cfg_file.rfind('.')
        if cfg_file[fullstop_idx:] != '.json':
            return None

        # Load config.json as dict
        cfg = {}
        with open(cfg_file, 'r') as file:
            cfg = json.load(file)
        
        # TODO: Check that configuration is legal, error out if config is invalid

        return self.strainerFromDict(cfg)

    def strainerFromDict(self, cfg: dict) -> SoupStrainer:
        return SoupStrainer(cfg['tags'], cfg['ids'])


