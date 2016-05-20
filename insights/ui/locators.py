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

insights_page_locators = LocatorDict({

    "system_tab": (By.XPATH, '//aside[@class="dashboard-navigation profile-image-visible"]//li[2]/a'),
    "filter": (By.XPATH, '//input[@class= "form-control nomar-left input-sm ng-pristine ng-untouched ng-valid"]'),
    "result": (By.XPATH, '//*[@id="rha-systems-summary-table"]/tbody/tr[1]/td[2]')
})
