class SeleniumUtility(object):
    def __init__(self, browser):
        super(SeleniumUtility, self).__init__()
        self.browser = browser
        self.timeout = 30

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def teardown(self):
        self.browser.quit()
