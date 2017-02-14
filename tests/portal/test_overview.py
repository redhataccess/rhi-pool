import logging
from insights.test import UITestCase
from insights.ui.session import Session
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class OverviewTabTestCase(UITestCase):
    def test_positive_overview_elements(self):
        with Session(self.browser):
            Navigator(self.browser).go_to_overview()
            self.assertEqual('Overview',
                             self.overview.overview_title())
            self.assertEqual('LATEST', self.overview.overview_latest())
            LOGGER.info(self.overview.overview_latest_news())
            self.assertIsNotNone(self.overview.overview_latest_news())
            self.assertEqual('NEWEST SYSTEMS', self.overview.overview_newest_summary())
            # Assert all elements under Plan Summary
            self.assertEqual('PLAN',
                             str(self.overview.overview_plan_summary()).rstrip(' '))
            self.assertTrue(self.overview.is_create_plan_displayed())

    def test_positive_navigation_from_overview(self):
        with Session(self.browser):
            # Check view actions
            Navigator(self.browser).go_to_overview()
            self.overview.go_to_overview_view_actions()

            # Check view Inventory
            Navigator(self.browser).go_to_overview()
            self.assertEqual('Overview',
                             self.overview.overview_title())
            self.overview.go_to_overview_view_inventory()

            # Check view Planner
            Navigator(self.browser).go_to_overview()
            self.overview.go_to_overview_view_planner()
            Navigator(self.browser).go_to_overview()
            self.overview.go_to_overview_planner()
