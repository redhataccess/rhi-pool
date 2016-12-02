import logging
import unittest
from insights.configs import settings
from insights.ui.browser import browser
from insights.ui.login import Login
from insights.ui.overview import Overview
from insights.ui.inventory import Inventory

LOGGER = logging.getLogger(__name__)


class TestCase(unittest.TestCase):
    """Insights Test Case."""

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls).setUpClass()
        if not settings.configured:
            settings.configure()
        cls.insights_user = settings.rhn_login.rhn_username
        cls.insights_password = settings.rhn_login.rhn_password

    @classmethod
    def tearDownClass(cls):
        logging.info("In teardown class")

    def setUp(self):
        LOGGER.info("Started test : ")

    def tearDown(self):
        LOGGER.info("Finished test : ")


class UITestCase(TestCase):
    """Insights UI Test Case."""

    @classmethod
    def setUpClass(cls):
        super(UITestCase, cls).setUpClass()
        cls.driver_name = settings.webdriver
        cls.driver_binary = settings.webdriver_binary
        cls.server_name = settings.rhn_login.base_url

    @classmethod
    def tearDownClass(cls):
        super(UITestCase, cls).tearDownClass()

    def setUp(self):
        super(UITestCase, self).setUp()
        self.browser = browser()
        self.browser.maximize_window()
        self.browser.get(settings.rhn_login.base_url)
        self.login = Login(self.browser)
        self.overview = Overview(self.browser)
        self.inventory = Inventory(self.browser)


