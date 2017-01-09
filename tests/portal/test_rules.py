import logging
from insights.test import UITestCase
from insights.ui.navigator import Navigator
from insights.ui.session import Session
import time

LOGGER = logging.getLogger('insights_portal')


class RulestabTestCase(UITestCase):

    rules_filters = ['Performance', 'Availability', 'Security', 'Stability']

    def test_positive_rules_filter(self):
        """
        This test asserts all rule filters available i.e. Availability,
        Scalability, Performance and Security functionality.
        """
        with Session(self.browser):
            Navigator(self.browser).go_to_rules()
            for rule_filter in self.rules_filters:
                self.rules.go_to_filter(rule_filter)
                LOGGER.info("Get %s rules card" % rule_filter)
                all_rules_title = self.rules.get_rule_card_title()
                LOGGER.info("Assering rule filter " + rule_filter)
                self.assertTrue(
                    all(rule_filter + " >" in string for string in all_rules_title),
                    msg="Filter %s is not applied correctly" % rule_filter
                )

    def test_search_rule(self):
        """
        This test verifies search text ion Rule tab.
        """
        with Session(self.browser):
            Navigator(self.browser).go_to_rules()
            #Search rule HTTPoxy
            self.rules.search_rule(search_text="HTTPoxy")

            #Assert only 2 rules are displayed
            LOGGER.info("Total rules displayed after filter ")
            LOGGER.info(self.rules.get_rules_count())
            self.assertEqual(2, self.rules.get_rules_count())


