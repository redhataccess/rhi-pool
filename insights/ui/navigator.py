from insights.ui import locators
from insights.ui.selenium_utility import SeleniumUtility


class Navigator(SeleniumUtility):
    def go_to_inventory_tab(self):
        self.find_element(locators.inventory_page_locators['inventory_tab']).click()
