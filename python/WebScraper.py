from requests import get
from requests.models import Response
from requests.status_codes import codes as responseStatusLookup

from bs4 import BeautifulSoup, SoupStrainer

from ErrorHandles import logError, InvalidJSONError
from configuration_check import configuration_check

import time  # Only included for testing. Remove for package deployment?
import json

# Type hinting included for ease of reading and autocompletion while in dev
from typing import Union

'''
TODO:
--------
FEATURES:
    -Authentication for websites which require it.
IMPLEMENTATION:
    -Error Handles:
        -Bad web responses
            --> .getWebpageResponse(...)  -->  COMPLETE
        -Bad configs
            --> .loadConfig(...)  -->  COMPLETE
    -Error Logging:
        -( Bad web responses, FileNotFoundError, BadConfigError )  --> COMPLETE, all errors log.
        - Rudimentary structure of logError() built out, should be general enough for
          possible errors that I am currently aware of.  -->  COMPLETE, produces dict ready to
                                                              be passed to a lambda function as an
                                                              event.
    -Default handling
    -README.md with important naming conventions, formatting for config files, etc.  -->  COMPLETE
    -WebScraper.soupToText(...)  -->  Python interpreter can be super slow for iteration,
                                       write as wrapper for c function? Use cython? 
'''


class WebScraper:

    def __init__(self, url: Union[str, None] = None) -> None:
        self.url = url          # Holds url of webpage being scraped
        self.response = None    # Holds Response object created after receiving response from the url
        self.soup = None        # Holds BeautifulSoup object created using received response and the SoupStrainer created to parse it
        self.strainer = None    # Holds SoupStrainer object created to filter response according to configuration
        self.config = None      # Holds user specified configuration

    def getWebpageResponse(self, url: str, timeout: float = 2) -> Union[Response, None]:
        '''Returns either requests.models.Response or None'''

        # Make response request
        response = get(url)

        try:
            # This will raise an exception for any bad requests
            response.raise_for_status()
            self.response = response
            return response

        except:
            error_code = response.status_code

            logError("In .getWebpageResponse: Bad response received (%s) from %s." % (
                error_code, url))

            # The function that calls this should check the result for None response.
            # Assuming it was iterating through a list of urls to check, it should then
            # pass to the next one.

            return None

    def soupify(self, parser: str = "lxml", schema: dict = None, configuration_filename: Union[str, None] = None) -> Union[BeautifulSoup, None]:
        '''Returns bs4.BeautifulSoup if successful,
        returns None if unsuccessful or if no reponse has been received.'''

        strainer = None

        # If config file provided, create custom filter
        if configuration_filename is not None:
            strainer = self.createStrainer(self.loadConfig(schema, configuration_filename))

        # If a reponse has been received from webpage, run it through BeautifulSoup
        if self.response is not None:
            self.soup = BeautifulSoup(
                self.response.content, 
                parser, 
                parse_only=strainer
            )
            return self.soup
        else:
            # ERROR
            return None

    def createStrainer(self, config: Union[dict, None] = None) -> Union[SoupStrainer, None]:
        if config is not None:
            print("config:", config)
            strainer = SoupStrainer(
                name = config['tags'], 
                attrs = config['attrs']
            )
            print("strainer:", strainer)
            return strainer
        else:
            # Error out
            return None

    def loadConfig(self, schema: dict = None, filename: Union[str, None] = None) -> Union[dict, None]:

        config = {}

        # If filename is provided
        if filename[filename.rfind('.'):] != '.json':
            filename = f"{filename}{'.json'}"
        try:
            with open(filename, 'r') as file:
                try:
                    # If invalid JSON, raises ValueError
                    config = json.load(file)
                    # If invalid config (or schema), configuration_check handles respective errors.
                    if configuration_check(config, schema):
                        self.config = config
                        return self.config
                    else:
                        return None
                except ValueError:      # Exception for invalid JSON object within file.
                    InvalidJSONError(filename)
                    return None
        except FileNotFoundError:
            logError(
                f"FileNotFoundError: {filename} was not found whilst loading configuration")
            return None


    # Convert soup to text according to config file specifications
    def soupToText(self, schema: dict = None, configuration_filename: Union[str, None] = None) -> Union[str, None]:

        if self.soup is None:
            # Error
            return None

        if self.config is None and configuration_filename is None:
            return None
        elif self.config is None and configuration_filename is not None:
            self.config = self.loadConfig(schema, configuration_filename)
            if self.config is None:
                return None
       
        for key, value in zip(self.config['bad-attrs'].keys(), self.config['bad-attrs'].values()):
            self.soup.find({key: value}).decompose()

        return self.soup.text




