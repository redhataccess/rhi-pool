from locators import insights_page_locators
from selenium_utility import SeleniumUtility
from navigator import Navigator


class UISearch(SeleniumUtility):
    def __init__(self, browser):
        super(UISearch, self).__init__(browser)
        self.nav = Navigator(self.browser)

    def register_system(self, hostname):
        # Click on system tab
        self.nav.go_to_system_tab()
        filter_field = self.find_element(insights_page_locators['filter'])
        filter_field.click()
        filter_field.send_keys(hostname)
        result = self.find_element(insights_page_locators['result']).text
        return result
