from insights.ui.base import Base, UIError, UINoSuchElementError
from insights.ui.locators import locators, menu_locators
from insights.ui.navigator import Navigator


class Overview(Base):
    """
    Identifies Overview contents from Insights UI
    """

    def navigate_to_entity(self):
        Navigator(self.browser).go_to_overview()

    def _search_locator(self):
        return menu_locators['menu.filter']

    def overview_title(self):
        return self.find_element(locators['overview.title']).text

    def overview_latest(self):
        return self.find_element(locators['overview.latest']).text

    def overview_latest_news(self):
        return self.find_element(locators['overview.latest.news']).text

    def go_to_overview_view_actions(self):
        self.click(locators['overview.viewactions'])

    def overview_newest_summary(self):
        return self.find_element(locators['overview.newest.summary']).text

    def go_to_overview_view_inventory(self):
        self.click(locators['overview.viewinventory'])

    def overview_plan_summary(self):
        return self.find_element((locators['overview.plan.summary'])).text

    def overview_create_plan(self):
        return self.find_element(locators['overview.plan.createplan'])

    def is_create_plan_displayed(self):
        return self.overview_create_plan().is_displayed()

    def go_to_overview_planner(self):
        self.click(locators['overview.plan.createplan'])

    def go_to_overview_view_planner(self):
        self.click(locators['overview.viewplanner'])


