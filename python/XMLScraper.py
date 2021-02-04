from WebScraper import WebScraper

from bs4 import BeautifulSoup, SoupStrainer
from typing import Union

'''
TODO:
    See WebScraper TODO list, similar issues.
'''

# Test default config for .xml web documents
default_config = {
    'tags': ['loc', 'lastmod', 'news:publication_date'],
    'attrs': {}
}
default_strainer = SoupStrainer(
    default_config['tags'], default_config['attrs'])


# Specific crawler for .xml webdocuments with different default for .soupify(...) method
class XMLScraper(WebScraper):

    def soupify(self, parser: str = 'lxml', config_file: Union[str, None] = None) -> Union[BeautifulSoup, None]:

        # If config.json is provided create custom strainer, else default to default_config
        strainer = self.createStrainer(self.loadConfig(config_file))

        # If no response has been received, return None. TODO: maybe this should error log?
        if self.response is None:
            return None
        else:
            self.soup = BeautifulSoup(
                self.response.content, parser, parse_only=strainer)
            return self.soup

    def createStrainer(self, config: Union[dict, None] = None) -> Union[SoupStrainer, None]:
        if config is not None:
            return SoupStrainer(config['tags'], config['attrs'])
        else:
            #print("XML default_strainer")
            return default_strainer
