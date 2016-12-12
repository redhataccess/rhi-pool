import logging
from insights.configs import settings
from selenium import webdriver

LOGGER = logging.getLogger(__name__)


class NotSupportedBrowser(Exception):
    """
      Raise this exception if browser passed is not supported
      Supported browser are : firefox, chrome
    """

#class Firefox(webdriver.Firefox):
#    """
#    Custom Firefox for custom logging
#    """


class Chrome(webdriver.Chrome):
    """ Custom Chrome for custom logging """


def browser():
    """ Instantiate browser based on :param: in config file"""

    webdriver_name = settings.webdriver.lower()
    if settings.browser == 'selenium':
        if webdriver_name == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            prefs = {"download.default_directory": "./downloads"}
            chrome_options.add_experimental_option("prefs", prefs)
            return webdriver.Chrome(settings.rhn_login.chrome_driver_path,
                                    chrome_options=chrome_options)
        elif webdriver_name == 'firefox':
            return webdriver.Firefox()
        else:
            raise NotSupportedBrowser
