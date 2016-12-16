import time
import logging
from insights.ui.base import Base, UINoSuchElementError, UIError
from insights.ui.locators import action_locators, locators
from insights.ui.navigator import Navigator

LOGGER = logging.getLogger('insights_portal')


class Actions(Base):
    """
    Identifies contents from Actions page of Insights
    """
    def navigate_to_entity(self):
        Navigator(self.browser).go_to_actions()

    def click_on_actions(self):
        self.click(action_locators['actions.menu'])
        time.sleep(3)
        self.wait_until_element_invisible(action_locators['actions.filter.invisible'],
                                          timeout=50)

    def actions_title(self):
        self.wait_until_element(action_locators['actions.title'], timeout=50)
        return self.find_element(action_locators['actions.title']).text

    def actions_chart_description(self):
        return self.find_element(action_locators['actions.pie.desc']).text

    def actions_pie_count(self):
        self.wait_until_element(action_locators['actions.pie.count'])
        return self.find_element(action_locators['actions.pie.count']).text

    def actions_desc_count(self):
        return self.find_element(action_locators['actions.desc.count']).text

    def click_on_actions_filter(self):
        self.click(action_locators['actions.filter'])
        self.click(action_locators['actions.filter.info'])

        #Added sleep because UI takes time to change the values in chart
        time.sleep(2)
        self.click(action_locators['actions.filter.warn'])
        time.sleep(2)
        self.click(action_locators['actions.filter.error'])
        time.sleep(2)
        self.click(action_locators['actions.filter.all'])
        time.sleep(2)

    def download_actions_csv(self):
        self.click(action_locators['actions.downloadcsv'])

    def actions_section_size(self):
        return len(self.find_elements(action_locators['actions.section']))

    def all_sections_name(self):
        sections = self.find_elements(action_locators['actions.section.names'])
        actions = []
        for section in sections:
            actions.append(section.text)
        return actions

    def go_to_section(self, name=None):
        """
        Require Section name to navigate to
        :param name:
        :return:
        """
        if name is not None:
            LOGGER.info("Checking section " + name)
            self.wait_until_element_invisible(action_locators['actions.filter.invisible'],
                                              timeout=50)
            sections = self.find_elements(action_locators['actions.section.names'])
            for section in sections:
                if name == section.text:
                    LOGGER.info("Clicking on " + section.text)
                    self.click(section)
                    break

    def get_section_title(self):
        self.wait_until_element(action_locators['actions.section.title'], timeout=50)
        return self.find_element(action_locators['actions.section.title']).text

    def click_first_row_on_sections(self):
        self.wait_until_element_invisible(action_locators['actions.filter.invisible'],
                                          timeout=50)
        time.sleep(3)  # Adding explicit sleep as it shows old table for a moment
        self.click(action_locators['actions.section.firstrow'])

    def click_first_impacted_system(self):
        self.wait_until_element(action_locators['actions.impacted.systemfirst'])
        self.click(action_locators['actions.impacted.systemfirst'])
        self.wait_until_element(action_locators['actions.system.modal.hostname'])
        return self.find_element(action_locators['actions.system.modal.hostname']).text

    def get_impacted_system_hostname(self):
        self.wait_until_element(action_locators['actions.system.hostname'], timeout=100)
        return self.find_element(action_locators['actions.system.hostname']).text

    def close_system_modal(self):
        self.click(action_locators['actions.system.close'])
        self.wait_until_element_invisible(action_locators['actions.system.close'],
                                          timeout=50)
        self.wait_until_element(action_locators['actions.menu'], timeout=100)

