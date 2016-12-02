from selenium.webdriver.common.by import By
from .model import LocatorDict

common_locators = LocatorDict({
    'username': (By.ID, ('accountUserName')),
    'logout': (By.ID, ('accountLogout')),
    'login': (By.ID, ('accountLogin'))
})