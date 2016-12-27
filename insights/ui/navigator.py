from insights.ui.locators import locators, menu_locators, common_locators
from insights.ui.base import Base


class Navigator(Base):

    def go_to_actions(self):
        self.go_to_insights_url()
        self.wait_until_element(menu_locators['menu.actions'], timeout=100)
        self.click(menu_locators['menu.actions'])

    def go_to_logout(self):
        self.wait_until_element(common_locators['username'])
        self.click(common_locators['username'])
        self.wait_until_element(common_locators['logout'])
        self.click(common_locators['logout'])

    def go_to_overview(self):
        self.click(menu_locators['menu.overview'])
        self.wait_until_element(locators['overview.latest'])

    def go_to_inventory(self):
        self.click(menu_locators['menu.inventory'])

    def go_to_planner(self):
        self.click(menu_locators['menu.planner'])

    def go_to_rules(self):
        self.click(menu_locators['menu.rules'])

    def go_to_configuration(self):
        self.click(menu_locators['menu.config'])
