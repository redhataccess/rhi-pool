import logging
from insights.test import UITestCase
from insights.ui.session import Session
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class ConfigurationTabTestCase(UITestCase):
    def test_positive_configuration_elements(self):
        """ This test verifies all the elements available on configuration page """

        with Session(self.browser):
            Navigator(self.browser).go_to_configuration()
            self.configuration.conf_click_on_configuration_tabs()
            # Checking Hidden rule section
            self.assertEqual("Hidden Rules", self.configuration.conf_hidden_rule_text())
            self.assertEqual("These are account wide. You must be an Org Admin to make these changes.",
                             self.configuration.conf_hidden_rule_info())
            # Checking Groups section
            self.configuration.conf_group_tab()
            self.configuration.conf_group_search_box(search=123)
            self.assertEqual("Add Group", self.configuration.conf_add_group_text())
            self.configuration.conf_add_group_button()
            self.assertEqual("Groups List", self.configuration.conf_group_list_text())
            self.assertEqual("Delete Group", self.configuration.conf_delete_group_text())
            self.configuration.conf_delete_group_button()
            self.configuration.conf_popup_yes_button()

            # Checking Messaging section
            self.assertEqual("Messaging Preferences", self.configuration.conf_messaging_title())
            self.configuration.conf_messaging_checkbox()

            # Checking Settings section
            self.configuration.conf_settings_title()
            self.configuration.conf_settings_checkbox()

            # Checking Dev section
            self.configuration.conf_dev_title()
            self.assertEqual("API Prefix", self.configuration.conf_dev_api_prefix())
            self.assertEqual("API Version", self.configuration.conf_dev_api_version())
            self.assertEqual("Fake user info", self.configuration.conf_dev_fake_user_info())
            self.assertEqual("Fake Entitlements", self.configuration.conf_dev_fake_entitlements())
