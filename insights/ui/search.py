from datetime import datetime
from selenium.webdriver.common.keys import Keys
from insights.ui import locators
from selenium_utility import SeleniumUtility
from navigator import Navigator


class UISearch(SeleniumUtility):
    def __init__(self, browser):
        super(UISearch, self).__init__(browser)
        self.nav = Navigator(self.browser)

    def register_system(self, hostname):
        # Go to inventory tab
        self.nav.go_to_inventory_tab()
        # Enter hostname in search field
        search_field = self.find_element(locators.inventory_page_locators['search_box'])
        search_field.send_keys(hostname)
        # Click enter
        self.browser.implicitly_wait(10)
        search_field.send_keys(Keys.RETURN)
        search_field.send_keys(Keys.RETURN)
        search_field.send_keys(Keys.RETURN)
        self.browser.implicitly_wait(30)
        # Find hostname in list
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        result1 = self.browser.find_element_by_xpath(
            ".//*[@id='telemetry']//descendant::strong[@class='hostname' and contains(.,'" + hostname + "')]")
        result = result1.text
        return result

    def take_screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.browser.get_screenshot_as_file('screenshot-%s.png' % now)
