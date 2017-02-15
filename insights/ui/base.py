# -*- encoding: utf-8 -*-

import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from insights.ui.locators import locators, Locator

LOGGER = logging.getLogger('insights_portal')

class UIError(Exception):
    """Indicates that a UI action could not be done."""


class UINoSuchElementError(UIError):
    """Indicates that UI Element is not found."""


class UIPageSubmitionFailed(Exception):
    """Indicates that UI Page submition Failed."""


class Base(object):
    """ Base class for Insight UI"""
    logger = LOGGER

    button_timeout = 15
    result_timeout = 15

    def __init__(self, browser):
        """Sets up the browser object."""
        self.browser = browser

    def find_element(self, locator):
        """Wrapper around Selenium's WebDriver that allows you to search for an
        element in the web page.
        """
        try:
            _webelement = self.browser.find_element(*locator)
            if _webelement.is_displayed():
                return _webelement
            else:
                return None
        except NoSuchElementException as err:
            self.logger.debug(
                u'%s: Could not locate element %s: %s',
                type(err).__name__,
                locator[1],
                err
            )
        except TimeoutException as err:
            self.logger.debug(
                u'%s: Waiting for locator %s: %s',
                type(err).__name__,
                locator[1],
                err
            )
        except StaleElementReferenceException as err:
            self.logger.debug(
                u'%s: Element not attached to DOM %s: %s',
                type(err).__name__,
                locator[1],
                err
            )
            self.browser.find_element(*locator)
            if _webelement.is_displayed():
                return _webelement
            else:
                return None
        return None

    def find_elements(self, locator):
        """Wrapper around Selenium's WebDriver that allows you to search for an
        element in the web page.
        """

        try:
            _webelements = self.browser.find_elements(*locator)
            webelements = []

            for _webelement in _webelements:
                if _webelement.is_displayed():
                    webelements.append(_webelement)
            return webelements
        except NoSuchElementException as err:
            self.logger.debug(
                u'%s: Could not locate element %s: %s',
                type(err).__name__,
                locator[1],
                err
            )
        except TimeoutException as err:
            self.logger.debug(
                u'%s: Waiting for locator %s: %s',
                type(err).__name__,
                locator[1],
                err
            )
        except StaleElementReferenceException as err:
            self.logger.debug(
                u'%s: Element not attached to DOM %s: %s',
                type(err).__name__,
                locator[1],
                err
            )
            _webelements =  self.browser.find_elements(*locator)
            webelements = []

            for _webelement in _webelements:
                if _webelement.is_displayed():
                    webelements.append(_webelement)
            return webelements
        return None

    def _search_locator(self):
        """Specify element name locator which should be used in search
        procedure
        """
        raise NotImplementedError(
            'Subclasses must return locator of element to search')

    def wait_until_element(self, locator, timeout=12, poll_frequency=0.5):
        """Wrapper around Selenium's WebDriver that allows you to pause your
        test until an element in the web page is present and visible.
        """
        try:
            element = WebDriverWait(
                self.browser, timeout, poll_frequency
            ).until(
                expected_conditions.visibility_of_element_located(locator),
                message=u'element %s is not visible' % locator[1]
            )
            return element
        except TimeoutException as err:
            self.logger.debug(
                u"%s: Waiting for element '%s' to display. %s",
                type(err).__name__,
                locator[1],
                err
            )
            return None

    def wait_until_text_present(self, locator, text, timeout=12, poll_frequency=0.5):
        try:
            element = WebDriverWait(
                self.browser, timeout, poll_frequency
            ).until(
                expected_conditions.text_to_be_present_in_element(locator, text),
                message=u'text %s is not present in locator %s' % (text, locator[1])
            )
            return element
        except TimeoutException as err:
            self.logger.debug(
                u"%s: Waiting for text '%s' to be present under %s",
                type(err).__name__,
                locator[1],
                err
            )
            return None

    def wait_until_element_invisible(self, locator, timeout=12, poll_frequency=0.5):
        try:
            self.browser.implicitly_wait(3)
            element = WebDriverWait(
                self.browser, timeout, poll_frequency
            ).until(
                expected_conditions.invisibility_of_element_located(locator),
                message=u'Element is not clickable %s' %(locator[1])
            )
            return element
        except TimeoutException as err:
            self.logger.debug(
                u"%s: Waiting for element '%s' to be present under %s",
                type(err).__name__,
                locator[1],
                err
            )
            return None

    def wait_until_element_to_be_clickable(self, locator, timeout=12, poll_frequency=0.5):
        try:
            self.browser.implicitly_wait(3)
            element = WebDriverWait(
                self.browser, timeout, poll_frequency
            ).until(
                expected_conditions.element_to_be_clickable(locator),
                message=u'Element is not clickable %s' % (locator[1])
            )
            return element
        except TimeoutException as err:
                self.logger.debug(
                    u"%s: Waiting for element '%s' to be clickable under %s",
                    type(err).__name__,
                    locator[1],
                    err
                )
                return None

    def field_update(self, loc_string, newtext):
        """
        Function to replace the existing/default text from textbox
        """
        txt_field = self.find_element(locators[loc_string])
        txt_field.clear()
        txt_field.send_keys(newtext)

    def scroll_into_view(self, element):
        """ Scrolls current element into visible area of the browser window."""
        # Here aligntoTop=False option is set.
        self.browser.execute_script(
            'arguments[0].scrollIntoView(false);',
            element,
        )

    def scroll_to_top(self):
        """
        Scroll to top of the page
        :return:
        """
        self.browser.execute_script(
            'scroll(0, 0);'
        )

    def click(self, target, wait_for_ajax=True,
              waiter_timeout=12, scroll=True):
        if isinstance(target, (tuple, Locator)):
            element = self.wait_until_element(target, timeout=waiter_timeout)
        else:
            element = target
        if element is None:
            raise UINoSuchElementError(
                u'{0}: element {1} was not found while trying to click'
                    .format(type(self).__name__, str(target))
            )
        # Required since from selenium 2.48.0. which makes Selenium more
        # closely resemble a user when interacting with elements.
        # Scrolling element into view before attempting to click solves this.
        # Behaviour can be changed with new selenium versions, so it is
        # necessary to validate that functionality in case click method stopped
        # to work as intended
        if scroll:
            self.scroll_into_view(element)
        element.click()

    def refresh(self):
        self.browser.get(self.browser.current_url)

    def go_to_insights_url(self):
        current_url = self.browser.current_url
        self.browser.get(current_url.rstrip('/') + '/insights/overview')
        self.browser.implicitly_wait(30)
