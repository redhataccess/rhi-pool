import os
import time
from insights.test import UITestCase
from insights.ui.session import Session
from insights.ui.navigator import Navigator
from insights.configs.base import get_project_root


class ActionstabTestCase(UITestCase):
    actions_sections = ['Performance', 'Availability', 'Security', 'Stability']

    def test_positive_actions_elements(self):
        """
        This test verifies all the elements available on Actions page
        """

        filename = 'all_actions.csv'
        with Session(self.browser):
            Navigator(self.browser).go_to_actions()
            self.assertEqual('Actions', self.actions.actions_title())
            self.assertEqual(
                "Use this chart to drill down and discover problems within your organization.",
                self.actions.actions_chart_description())
            self.assertIsNotNone(self.actions.actions_pie_count())
            self.assertIsNotNone(self.actions.actions_desc_count())
            self.actions.click_on_actions_filter()

            #Download CSV for all Actions
            self.actions.download_actions_csv()
            time.sleep(5) #Wait for file to download

            #Read CSV file downloaded
            downloads_path = os.path.join(get_project_root(),  'downloads')
            filename = max([f for f in os.listdir(downloads_path)])
            self.assertIsNotNone(filename)

            #Assert CSV file count and web chart count
            self.assertEqual(self.actions.actions_pie_count(),
                             str(len(open(os.path.join(
                                 downloads_path, filename)).readlines()) - 1))

            #Assert all sections
            self.assertEqual(4, self.actions.actions_section_size())
            self.assertItemsEqual(self.actions_sections,
                                  self.actions.all_sections_name())

    def test_positive_navigate_to_sections(self):
        """
        This test navigates to all sections available on Actions page
        """

        with Session(self.browser):
            Navigator(self.browser).go_to_actions()
            for section_name in self.actions_sections:
                self.actions.go_to_section(section_name)
                self.assertEqual(section_name, self.actions.get_section_title())
                self.actions.click_on_actions()

    def test_positive_impacted_systems_info(self):
        """
        This test verifies impacted system modal
        Navigates from Action page till impacted system modal
        """
        with Session(self.browser):
            Navigator(self.browser).go_to_actions()
            for section_name in self.actions_sections:
                self.actions.go_to_section(section_name)
                self.actions.click_first_row_on_sections()
                system_host = self.actions.get_impacted_system_hostname()
                system_modal_host = self.actions.click_first_impacted_system()
                self.assertEqual(system_host, system_modal_host, msg="Hostname is not matching")
                self.actions.close_system_modal()
                self.actions.click_on_actions()

