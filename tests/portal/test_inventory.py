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
            self.assertIsNotNone(self.inventory.inventory_toggle())
            self.assertEqual('Show only not checking in',
                             self.inventory.inventory_not_checking_in_text())
            self.assertEqual('EXPAND ALL', self.inventory.inventory_expand_all_text())
            self.assertEqual('Hostname', self.inventory.inventory_hostname_dropdown_text())
            self.assertEqual(' WITH ACTIONS', self.inventory.inventory_action_tab_text())
            self.assertEqual(' WITHOUT ACTIONS', self.inventory.inventory_without_action_tab_text())
            self.assertIsNotNone(self.inventory.inventory_system_avl_count())

            # Checking single inventory
            self.inventory.inventory_click_system_name()
            system_name = self.inventory.inventory_text_system_name()
            system_name_on_detail = self.inventory.inventory_system_name_on_detail_page()
            self.assertEqual(system_name.lstrip(), system_name_on_detail)
            self.inventory.inventory_cross_button()
