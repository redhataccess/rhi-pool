from locators import login_page_locators
from selenium_utility import SeleniumUtility
from insights.config import Settings


class LoginUI(SeleniumUtility, Settings):
    def __init__(self, browser):
        super(LoginUI, self).__init__(browser)
        self.base_url = self.get('rhn_login', 'base_url')
        self.username = self.get('rhn_login', 'rhn_username')
        self.password = self.get('rhn_login', 'rhn_password')

    def login_to_portal(self):
        username_field = self.find_element(login_page_locators['username_field'])
        username_field.send_keys(self.username)
        password_field = self.find_element(login_page_locators['password_field'])
        password_field.send_keys(self.password)
        submit_btn = self.find_element(login_page_locators['submit_btn'])
        submit_btn.click()
        self.go_to_insights_url()

    def go_to_insights_url(self):
        current_url = self.browser.current_url
        self.browser.get(current_url + 'insights/actions')
        self.browser.implicitly_wait(30)
