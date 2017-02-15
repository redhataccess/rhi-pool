# coding=utf-8
import logging
from insights.test import UITestCase
from insights.ui.session import Session
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class InventoryTabTestCase(UITestCase):
    def test_positive_inventory_elements(self):
        """ This test verifies all the elements available on Inventory page """
        with Session(self.browser):
            Navigator(self.browser).go_to_inventory()
            # Checking systems filter
            self.inventory.search_inventory('test-k.novalocal')
            self.inventory.wait_for_inventory_hostname('test-k.novalocal')
            host, sys_type = self.inventory.get_inventory_details()
            self.assertEqual("test-k.novalocal", str(host).strip(' '))
            self.assertEqual("RHEL Server", str(sys_type).strip(' '))


            # Check all elements
            self.assertIsNotNone(self.inventory.inventory_search_icon())
            self.assertIsNotNone(self.inventory.get_inventory_details())

            # Checking single inventory
            self.inventory.inventory_click_system_name()
            system_name = self.inventory.inventory_text_system_name()
            system_name_on_detail = self.inventory.inventory_system_name_on_detail_page()
            self.assertEqual(system_name.lstrip(), system_name_on_detail)
            self.inventory.inventory_cross_button()

            # Checking group from inventory page 
            Navigator(self.browser).go_to_configuration()
            self.configuration.conf_group_tab()
            self.configuration.conf_group_search_box(search=123)
            self.assertEqual("Add Group", self.configuration.conf_add_group_text())
            self.configuration.conf_add_group_button()

            # Add Inventory in Group
            self.inventory.inventory_groups_search_box('test-k.novalocal')
            self.inventory.inventory_group_checkbox_click()
            self.inventory.inventory_group_add_systems_click()

            # Check on group dropdown on inventory page
            Navigator(self.browser).go_to_inventory()
            self.assertEqual('Groups', self.inventory.inventory_groups_label())
            self.inventory.inventory_groups_dropdown_click()
            self.assertEqual('All Groups', self.inventory.inventory_groups_dropdown_text())

            # Remove Group
            Navigator(self.browser).go_to_configuration()
            self.configuration.conf_group_tab()
            self.inventory.minimize_group_on_configuration()
            self.assertEqual("Delete Group", self.inventory.inventory_remove_group_text())
            self.inventory.inventory_remove_group()
            self.assertEqual("Yes",self.inventory.inventory_remove_group_popup_text())
            self.inventory.inventory_remove_group_popup()
