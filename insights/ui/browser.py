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

# Dict of callables to format the output of selenium commands logging
param_formatters = {
    # normally this value is ['a', 'b', 'c'] but we want ['abc']
    'sendKeysToElement': lambda x: {
        'id': x['id'], 'value': ''.join(x['value'])
    }
}


class DriverLoggerMixin(object):
    """Custom Driver Mixin to allow logging of commands execution"""
    def execute(self, driver_command, params=None):
        # Execute and intercept the response
        response = super(DriverLoggerMixin, self).execute(driver_command,
                                                          params)

        # Skip messages for commands not in settings
        if driver_command not in settings.log_driver_commands:
            return response

        if params:
            # We don't need the sessionId in the log output
            params.pop('sessionId', None)
            value = response.get('value')
            id_msg = ''
            # append the 'id' of element in the front of message
            if isinstance(value, webdriver.remote.webelement.WebElement):
                id_msg = "id: %s" % value.id
            # Build the message like 'findElement: id: 1: {using: xpath}'
            msg = '%s: %s %s' % (
                driver_command,
                id_msg,
                param_formatters.get(driver_command, lambda x: x)(params)
            )
        else:
            msg = driver_command

        # output the log message
        LOGGER.debug(msg)

        return response


class Chrome(DriverLoggerMixin, webdriver.Chrome):
    """ Custom Chrome for custom logging """


def browser():
    """ Instantiate browser based on :param: in config file"""

    webdriver_name = settings.webdriver.lower()
    if settings.browser == 'selenium':
        if webdriver_name == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            prefs = {"download.default_directory": "./downloads"}
            chrome_options.add_experimental_option("prefs", prefs)
            return Chrome(executable_path=settings.rhn_login.chrome_driver_path,
                          chrome_options=chrome_options)
        elif webdriver_name == 'firefox':
            return webdriver.Firefox()
        else:
            raise NotSupportedBrowser
