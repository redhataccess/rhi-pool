
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
            LOGGER.info(self.overview.overview_latest_news())
            self.assertIsNotNone(self.overview.overview_latest_news())

            #Assert all elements under Actions
            self.assertEqual('Availability',
                             self.overview.overview_action_availability())
            self.assertIsNotNone(self.overview.overview_action_avl_count())
            self.assertEqual('Stability',
                             self.overview.overview_action_stability())
            self.assertIsNotNone(self.overview.overview_action_stable_count())
            self.assertEqual('Performance',
                             self.overview.overview_action_performance())
            self.assertIsNotNone(self.overview.overview_action_perf_count())
            self.assertEqual('Security',
                             self.overview.overview_action_security())
            self.assertIsNotNone(self.overview.overview_action_security_count())

            #Assert all elements under Newest Summary
            self.assertEqual("NEWEST SYSTEMS",
                             self.overview.overview_newest_summary())
            self.assertIsNotNone(self.overview.overview_newset_first_system())

            #Assert all elements under Plan Summary
            self.assertEqual("PLAN",
                             str(self.overview.overview_plan_summary()).rstrip(' '))
            self.assertTrue(self.overview.is_create_plan_displayed())



