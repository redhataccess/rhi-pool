from insights.ui.locators import insights_page_locators
from insights.ui.selenium_utility import SeleniumUtility


class Navigator(SeleniumUtility):
    def go_to_system_tab(self):
        self.find_element(insights_page_locators['system_tab']).click()
