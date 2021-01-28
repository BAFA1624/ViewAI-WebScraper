from WebScraper import WebScraper

from bs4 import BeautifulSoup, SoupStrainer
from typing import Union

# Test default config for .xml web documents
default_cfg = {
    'tags': ['loc','lastmod'],
    'ids': {}
}

# Specific crawler for .xml webdocuments with different default for .soupify(...) method
class XMLScraper(WebScraper):

    def soupify(self, parser: str = 'lxml', config: Union[str, None] = None) -> Union[BeautifulSoup, None]:
        
        # If no response has been received, return None. TODO: maybe this should error log?
        if self.response is None:
            return None

        # If config.json is provided create custom strainer, else default to default_cfg
        strainer = None
        if config is not None:
            self.strainer = self.strainerFromFile(config)
            strainer = self.strainer
        else:
            self.strainer = self.strainerFromDict(default_cfg)
            strainer = self.strainer

        
        self.soup = BeautifulSoup(self.response.content, parser, parse_only=strainer)
        return self.soup

