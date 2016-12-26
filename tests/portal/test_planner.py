import logging
from insights.test import UITestCase
from insights.ui.session import Session
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class PlannerTabTestCase(UITestCase):
    planner_sections = ['PAST', 'NOT SCHEDULED', 'SUGGESTIONS', 'FUTURE']

    def test_positive_planner_elements(self):
        """ This test verifies all the elements available on planner page """
        with Session(self.browser):
            Navigator(self.browser).go_to_planner()
            # Check all elements
            self.assertEqual('Planner', self.planner.planner_title())
            self.assertEqual(' Create a plan', self.planner.planner_create_plan_text())
            self.assertEqual('New suggested plan', self.planner.planner_new_plan_text())
            self.assertIsNotNone(self.planner.planner_search_box())
            self.assertIsNotNone(self.planner.planner_search_icon())
            LOGGER.info(self.planner.planner_all_sections_name())

            # Click on buttons
            self.planner.click_on_planner_filter()

            # Create new plan and delete it
            self.planner.planner_create_plan_button()
            self.planner.planner_delete_plan_button()
            self.planner.planner_popup_yes_button()
