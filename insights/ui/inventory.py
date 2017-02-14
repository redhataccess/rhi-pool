import time
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
        time.sleep(5)
        hostname = self.find_element(locators['inventory.system.hostname']).text
        sys_type = self.find_element(locators['inventory.system.type']).text
        return hostname, sys_type

    def wait_for_inventory_hostname(self, hostname):
        self.wait_until_text_present(locators['inventory.system.hostname'], hostname)

    def search_box(self):
        return self.find_element(locators['inventory.search.box.placeholder'])

    def inventory_search_icon(self):
        return self.find_element(locators['inventory.search.icon'])

    def inventory_click_system_name(self):
        self.click(locators['inventory.system.hostname'])

    def inventory_text_system_name(self):
        return self.find_element(locators['inventory.system.hostname']).text

    def inventory_system_name_on_detail_page(self):
        time.sleep(2)
        return self.find_element(locators['inventory.system.name.detail']).text

    def inventory_cross_button(self):
        time.sleep(2)
        self.click(locators['inventory.close.button'])

    def inventory_groups_label(self):
        return self.find_element(locators['inventory.groups.label']).text

    def inventory_groups_dropdown_click(self):
        time.sleep(2)
        self.click(locators['inventory.group.dropdown'])

    def inventory_groups_dropdown_text(self):
        return self.find_element(locators['inventory.group.dropdown']).text

