import time

from insights.ui.base import Base, UIError, UINoSuchElementError, LOGGER
from insights.ui.locators import locators
from insights.ui.navigator import Navigator


class Planner(Base):
    """
    Identifies content from Planner of Insights UI
    """

    def navigate_to_entity(self):
        Navigator(self.browser).go_to_planner()

    def planner_title(self):
        return self.find_element(locators['planner.title']).text

    def planner_create_plan_text(self):
        return self.find_element(locators['planner.create.plan.text']).text

    def planner_new_plan_text(self):
        return self.find_element(locators['planner.new.plan.text']).text

    def planner_create_plan_button(self):
        self.wait_until_element(locators['planner.create.plan.button'], timeout=50)
        self.click(locators['planner.create.plan.button'])

    def planner_delete_plan_button(self):
        self.wait_until_element(locators['planner.delete.button'], timeout=50)
        time.sleep(5)
        self.click(locators['planner.delete.button'])

    def planner_popup_yes_button(self):
        self.wait_until_element(locators['planner.yes.popup.button'], timeout=50)
        self.click(locators['planner.yes.popup.button'])

    def planner_add_new_plan_text(self):
       return self.find_element(locators['planner.new.plan.text']).text

    def planner_search_box(self):
        return self.find_element(locators['planner.search.box'])

    def planner_search_icon(self):
        return self.find_element(locators['planner.search.icon'])

