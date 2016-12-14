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

    def search_box(self):
        return self.find_element(locators['inventory.search.box.placeholder'])

    def inventory_not_checking_in_text(self):
        return self.find_element(locators['inventory.not.checking.in']).text

    def inventory_system_avl_count(self):
        return self.find_element(locators['inventory.system.count1']).text

    def inventory_expand_all_text(self):
        return self.find_element(locators['inventory.expand.all']).text

    def inventory_hostname_dropdown_text(self):
        return self.find_element(locators['inventory.hostname']).text

    def inventory_action_tab_text(self):
        return self.find_element(locators['inventory.with_actions.tab']).text

    def inventory_without_action_tab_text(self):
        return self.find_element(locators['inventory.without_action.tab']).text

    def inventory_toggle(self):
        return self.find_element(locators['inventory.toggle'])

    def inventory_search_icon(self):
        return self.find_element(locators['inventory.search.icon'])

    def inventory_dropdown_button(self):
        self.find_element(locators['inventory.dropdown.button']).click()

    def inventory_click_system_name(self):
        self.find_element(locators['inventory.system.hostname']).click()

    def inventory_text_system_name(self):
        return self.find_element(locators['inventory.system.hostname']).text

    def inventory_system_name_on_detail_page(self):
        return self.find_element(locators['inventory.system.name.detail']).text

    def inventory_get_hostname(self):
        return self.find_element(locators['inventory.system.name']).text

    def inventory_cross_button(self):
        self.find_element(locators['inventory.close.button']).click()

