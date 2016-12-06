from insights.ui.base import Base, UIError, UINoSuchElementError
from insights.ui.locators import locators
from insights.ui.navigator import Navigator


class Inventory(Base):
    """
    Identifies content from Inventory of Insights UI
    """

    def navigate_to_entity(self):
        Navigator(self.browser).go_to_inventory()

    def search_inventory(self, name=None):
        self.find_element(locators['inventory.search.box']).send_keys(name)
        self.click(locators['inventory.search.icon'])

    def get_inventory_details(self):
        hostname = self.find_element(locators['inventory.system.hostname']).text
        sys_type = self.find_element(locators['inventory.system.type']).text
        return hostname, sys_type

    def wait_for_inventory_hostname(self, hostname):
        self.wait_until_text_present(locators['inventory.system.hostname'], hostname)
