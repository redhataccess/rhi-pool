import logging
from insights.test import UITestCase
from insights.ui.session import Session
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class HeaderTabTestCase(UITestCase):

    def test_positive_header_elements(self):
        """ This test verifies all the elements available on Header tab """

        with Session(self.browser):
            Navigator(self.browser).go_to_help_tab()
            # # Elements present on dropdown
            self.assertEqual("Help", self.header.header_text())
            self.assertEqual("Getting Started", self.header.header_getting_started())
            self.assertEqual("More Info", self.header.header_more_info())
            self.assertEqual("Security", self.header.header_security_text())
            self.assertEqual("Browser Support", self.header.header_browser_support())
            self.assertEqual("Insights API Documentation", self.header.header_insights_api())

            # # Click on More info tab
            self.header.header_more_info_click()
            self.assertEqual("Introduction to Red Hat Insights",self.header.header_info_title())
            Navigator(self.browser).go_to_insights_url()

            # # Click on Security tab
            Navigator(self.browser).go_to_help_tab()
            self.header.header_security_click()
            self.assertEqual("Security", self.header.header_security_title())
            Navigator(self.browser).go_to_insights_url()

            # Click on browser support
            Navigator(self.browser).go_to_help_tab()
            self.header.header_browser_support_click()
            self.assertEqual("Browser Support Policy",self.header.header_browser_support_title())
            self.header.header_switch_from_browser_tab()

            # Click on api documentation
            Navigator(self.browser).go_to_help_tab()
            self.header.header_insights_api_documentation_click()
            self.assertEqual("Red Hat Insights API Documentation", self.header.header_api_documentation_title())
            self.header.header_switch_from_api_documentation()

            # Elements present on notification icon
            self.assertIsNotNone(self.header.header_notification_icon())
            Navigator(self.browser).go_to_overview()


