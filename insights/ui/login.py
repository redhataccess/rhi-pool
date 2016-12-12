# -*- encoding: utf-8 -*-
from insights.ui.base import Base, UINoSuchElementError
from insights.ui.locators import locators, common_locators
from insights.ui.navigator import Navigator
import time


class Login(Base):
    """Implements login, logout functions for Foreman UI"""

    def login(self, username, password, organization=None, location=None):
        """Logins user from UI"""
        if self.wait_until_element(locators['login.username']):
            self.field_update('login.username', username)
            self.field_update('login.password', password)
            self.click(locators['login.submit'])
            self.wait_until_element(common_locators['username'], timeout=50)

            #Go to Insights home page
            self.go_to_insights_url()

            #Adding explicit wait as so many redirection happens after login
            time.sleep(5)

    def logout(self):
        """ Log out from Insights UI"""
        self.browser.execute_script('scroll(0, 0);')
        # Adding explicit wait as web page is taking too long to respond
        time.sleep(5)
        Navigator(self.browser).go_to_logout()