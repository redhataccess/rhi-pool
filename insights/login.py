import configparser
import selenium_utility
from locators import *


class LoginUI(selenium_utility.Base):

  config = configparser.ConfigParser()
  config.read("pool.conf")
  base_url = config.get('rhn_login', 'base_url')
  username = config.get('rhn_login', 'rhn_username')
  password = config.get('rhn_login', 'rhn_password')

  def login_to_portal(self, username, password):
    username_field = self.find_element(*LoginPageLocators.username_field)
    username_field.send_keys(username)
    password_field = self.find_element(*LoginPageLocators.password_field)
    password_field.send_keys(password)
    submit_btn = self.find_element(*LoginPageLocators.submit_Btn)
    submit_btn.click()
