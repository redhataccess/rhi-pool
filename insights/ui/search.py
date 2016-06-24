import locators
from navigator import Navigator
from datetime import datetime
from selenium_utility import SeleniumUtility


class UISearch(SeleniumUtility):
    def __init__(self, browser):
        super(UISearch, self).__init__(browser)
        self.nav = Navigator(self.browser)

    def register_system(self, hostname):
        # Click on system tab
        self.nav.go_to_system_tab()
        filter_field = self.find_element(locators.insights_page_locators['filter'])
        filter_field.click()
        filter_field.send_keys(hostname)
        result = self.find_element(locators.insights_page_locators['result']).text
        return result

    def take_screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.browser.get_screenshot_as_file('screenshot-%s.png' % now)
