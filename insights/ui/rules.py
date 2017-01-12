import logging
import time
from insights.ui.base import Base
from insights.ui.locators import rules_locators
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')

class Rules(Base):
    """
    Identifies contents from Rules page of Insights
    """

    def navigate_to_entity(self):
        Navigator(self.browser).go_to_rules()

    def go_to_filter(self, name=None):
        """
        This will select rules filter
        """
        time.sleep(5) #Added explicit wait as rules cards takes time to load
        if name is not None:
            LOGGER.info("Checking filter: " + name)
            if name is 'Availability':
                self.click(rules_locators['rules.filter.availability'])
            elif name is 'Performance':
                self.click(rules_locators['rules.filter.performance'])
            elif name is 'Stability':
                self.click(rules_locators['rules.filter.stability'])
            elif name is 'Security':
                self.click(rules_locators['rules.filter.security'])
            elif name is 'All':
                self.click(rules_locators['rules.filter.all'])

    def get_active_filter_text(self):
        return self.find_element(rules_locators['rules.active.filter']).text

    def get_rule_card_title(self):
        time.sleep(5) #Added explicit wait as rule cards takes time to load
        rules_title = self.find_elements(rules_locators['rules.cards'])
        title = []
        for rule_title in rules_title:
            title.append(rule_title.text)
        LOGGER.info(title)
        return title

    def search_rule(self, search_text='HTTPoxy'):
        self.click(rules_locators['rules.search.box'])
        self.field_update("rules.search.box", search_text)
        self.click(rules_locators['rules.search.icon'])
        time.sleep(5) #Wait for search rules

    def get_rules_count(self):
        rule_blocks = self.find_elements(rules_locators['rules.content.blocks'])
        return len(rule_blocks)



