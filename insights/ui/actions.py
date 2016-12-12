import time
from insights.ui.base import Base, UINoSuchElementError, UIError
from insights.ui.locators import action_locators
from insights.ui.navigator import Navigator

class Actions(Base):
    """
    Identifies contents from Actions page of Insights
    """
    def navigate_to_entity(self):
        Navigator(self.browser).go_to_actions()

    def actions_title(self):
        self.wait_until_element(action_locators['actions.title'], timeout=50)
        return self.find_element(action_locators['actions.title']).text

    def actions_chart_description(self):
        return self.find_element(action_locators['actions.pie.desc']).text

    def actions_pie_count(self):
        self.wait_until_text_present(action_locators['actions.pie.count'], '1010')
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

