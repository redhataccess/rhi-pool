from insights.ui.locators import locators, menu_locators, common_locators
from insights.ui.base import Base


class Navigator(Base):

    def go_to_actions(self):
        self.go_to_insights_url()
        self.wait_until_element(menu_locators['menu.actions'], timeout=100)
        self.find_element(menu_locators['menu.actions']).click()

    def go_to_logout(self):
        self.wait_until_element(common_locators['username'])
        self.find_element(common_locators['username']).click()
        self.wait_until_element(common_locators['logout'])
        self.find_element(common_locators['logout']).click()

    def go_to_overview(self):
        self.find_element(menu_locators['menu.overview']).click()
        self.wait_until_element(locators['overview.latest'])

    def go_to_inventory(self):
        self.find_element(menu_locators['menu.inventory']).click()

    def go_to_planner(self):
        self.find_element(menu_locators['menu.planner']).click()

    def go_to_rules(self):
        self.find_element(menu_locators['menu.rules']).click()

    def go_to_configuration(self):
        self.find_element(menu_locators[['menu.config']])
