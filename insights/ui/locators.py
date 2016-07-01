import collections
from selenium.webdriver.common.by import By


class LocatorDict(collections.Mapping):
    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __init__(self, *args, **kwargs):
        self.store = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self.store[key]


login_page_locators = LocatorDict({
    "username_field": (By.ID, 'username'),
    "password_field": (By.ID, 'password'),
    "submit_btn": (By.ID, '_eventId_submit')
})


inventory_page_locators = LocatorDict({
    "inventory_tab": (By.XPATH, '//a[contains(@href,"/insights/inventory")]'),
    "search_box": (By.XPATH, '//input[contains(@ng-keypress,"event")]'),

})
