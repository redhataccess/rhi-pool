import logging
from insights.configs import settings
from selenium import webdriver

LOGGER = logging.getLogger(__name__)


class NotSupportedBrowser(Exception):
    """
      Raise this exception if browser passed is not supported
      Supported browser are : firefox, chrome
    """

class Firefox(webdriver.Firefox):
    """
    Custom Firefox for custom logging
    """


class Chrome(webdriver.Chrome):
    """ Custom Chrome for custom logging """


def browser():
    """ Instantiate browser based on :param: in config file"""

    webdriver_name = settings.webdriver.lower()
    if settings.browser == 'selenium':
        if webdriver_name == 'chrome':
            return webdriver.Chrome(settings.rhn_login.chrome_driver_path)
        elif webdriver_name == 'firefox':
            return webdriver.Firefox(firefox_binary=settings.webdriver_binary)
        else:
            raise NotSupportedBrowser
