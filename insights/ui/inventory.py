import logging
import time
from insights.ui.base import Base
from insights.ui.locators import locators
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class Inventory(Base):
    """
    Identifies content from Inventory of Insights UI
    """

    def navigate_to_entity(self):
        Navigator(self.browser).go_to_inventory()

    def search_inventory(self, name=None):
        LOGGER.info("Search Inventory")
        self.find_element(locators['inventory.search.box']).send_keys(name)
        self.click(locators['inventory.search.icon'])

    def get_inventory_details(self):
        LOGGER.info(" get inventory details")
        hostname_text = self.wait_until_element(locators['inventory.system.hostname'])
        hostname = hostname_text.text
        sys_type_text = self.wait_until_element(locators['inventory.system.type'])
        sys_type = sys_type_text.text
        return hostname, sys_type

    def wait_for_inventory_hostname(self, hostname):
        self.wait_until_text_present(locators['inventory.system.hostname'], hostname)

    def search_box(self):
        return self.find_element(locators['inventory.search.box.placeholder'])

    def inventory_search_icon(self):
        LOGGER.info("Check all elements")
        return self.find_element(locators['inventory.search.icon'])

    def inventory_click_system_name(self):
        self.click(locators['inventory.system.hostname'])

    def inventory_text_system_name(self):
        return self.find_element(locators['inventory.system.hostname']).text

    def inventory_system_name_on_detail_page(self):
        self.wait_until_element(locators['inventory.system.name.detail'], timeout=100)
        return self.find_element(locators['inventory.system.name.detail']).text

    def inventory_cross_button(self):
        cross_button = self.wait_until_element(locators['inventory.close.button'])
        cross_button.click()

    # Checking group section from inventory page
    def inventory_groups_label(self):
        return self.find_element(locators['inventory.groups.label']).text

    def inventory_groups_dropdown_click(self):
        dropdown = self.wait_until_element(locators['inventory.group.dropdown'])
        dropdown.click()

    def inventory_groups_dropdown_text(self):
        return self.find_element(locators['inventory.group.dropdown']).text

    def inventory_groups_search_box(self, name1=None):
        search_box = self.wait_until_element(locators['groups.search.box'], timeout=100)
        search_box.send_keys(name1)

    def inventory_group_checkbox_click(self):
        LOGGER.info("Adding inventory in group")
        time.sleep(2)
        add_inventory = self.wait_until_element(locators['group.checkbox'], timeout=100)
        add_inventory.click()

    def inventory_group_add_systems_click(self):
        add_system = self.wait_until_element(locators['group.add.system'], timeout=100)
        add_system.click()

    def minimize_group_on_configuration(self):
        mimimize_button = self.wait_until_element(locators['group.mimimize.button'])
        mimimize_button.click()

    def inventory_remove_group_text(self):
        remove_group = self.wait_until_element_to_be_clickable(locators['group.remove.group'], timeout=100)
        return remove_group.text

    def inventory_remove_group(self):
        LOGGER.info("Deleting Group")
        remove_group = self.wait_until_element(locators['group.remove.group'], timeout=100)
        remove_group.click()

    def inventory_remove_group_popup_text(self):
        remove_group_popup = self.wait_until_element_to_be_clickable(locators['group.yes.popup.button'], timeout=100)
        return remove_group_popup.text

    def inventory_remove_group_popup(self):
        remove_group_popup = self.wait_until_element_to_be_clickable(locators['group.yes.popup.button'], timeout=100)
        time.sleep(2)
        remove_group_popup.click()
