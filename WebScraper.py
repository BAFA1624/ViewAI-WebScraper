import requests
from bs4 import BeautifulSoup, SoupStrainer
import time  # Only included for testing. Remove for package deployment?
import json

# Custom request exceptions library, still to be properly implemented.
# Hopefully will find a way to use exceptions library provided by the requests module in requests.exceptions
from RequestExceptions import Error404

# Type hinting included for ease of reading and autocompletion while in dev
from typing import Union

'''
TODO:
    -Error Handles:
        -Bad web responses
            --> .getWebpageResponse(...)
        -Bad configs
            --> .loadConfig(...)
    -Error Logging:
        -Bad web responses
        -FileNotFoundError
        -BadConfigError
    -Default handling
    -README.md with important naming conventions, formatting for config files, etc.
'''

class WebScraper:

    def __init__(self, url: Union[str, None] = None) -> None:
        self.url = url
        self.response = None
        self.soup = None
        self.strainer = None
        self.config = None

    def getWebpageResponse(self, url: str, timeout: float = 2) -> Union[requests.models.Response, None]:
            
        '''Returns either requests.models.Response or None'''
        
        # Make response request
        response = requests.get(url)
        
        if response.status_code != 200:

            self.response = None

            if response.status_code == 404:
                raise Error404(url, timeout)
            
            return None

        else:

            self.response = response
            return response

    def soupify(self, parser: str = "lxml", config_file: Union[str, None] = None) -> Union[BeautifulSoup, None]:
        '''Returns bs4.BeautifulSoup if successful,
        returns None if unsuccessful or if no reponse has been received.'''
        
        # If config file provided, create custom filter
        strainer = self.createStrainer(self.loadConfig(config_file))
        
        # If a reponse has been received from webpage, run it through BeautifulSoup
        if self.response is not None:
            self.soup = BeautifulSoup(self.response.content, parser, parse_only=strainer)
            return self.soup
        else:
            # ERROR
            return None

    def createStrainer(self, config: Union[dict, None] = None) -> Union[SoupStrainer, None]:
        if config is not None:
            strainer = SoupStrainer(config['tags'], config['attrs'])
            return strainer
        else:
            # Error out
            return None


    def loadConfig(self, config_file: Union[str, None] = None) -> Union[dict, None]:
        
        #print("loading config")

        # If a config is neither stored or provided, error
        if config_file is None and self.config is None:
            #print("config_file & self.config == None")
            return None

        # If config is stored but not provided
        elif (config_file is None and self.config is not None):
            #print("config_file == None, self.config != None")
            return self.config

        # Load new config
        else:
            #print("else")
            # Check config file is .json
            fullstop_idx = config_file.rfind('.')
            if config_file[fullstop_idx:] != '.json':
                return None
            
            # Load [NAME]_config.json
            try:
                with open(config_file, 'r') as file:
                    self.config = json.load(file)
                return self.config

            # Error log and return old config
            except FileNotFoundError:
                return self.config


    # Convert soup to text according to config file specifications
    def soupToText(self, ):
        pass


