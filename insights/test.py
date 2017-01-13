import logging
import unittest
from datetime import datetime
import os
import sys
from insights.configs import settings
from insights.ui.browser import browser
from insights.ui.configuration import Configuration
from insights.ui.header import Header
from insights.ui.login import Login
from insights.ui.overview import Overview
from insights.ui.inventory import Inventory
from insights.ui.actions import Actions
from insights.ui.planner import Planner
from insights.ui.rules import Rules
from insights.configs.base import get_project_root

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
        self.addCleanup(self.browser.quit)
        self.browser.maximize_window()
        self.browser.get(settings.rhn_login.base_url)
        self.addCleanup(self.take_screenshot)

        #Library methods
        self.login = Login(self.browser)
        self.overview = Overview(self.browser)
        self.inventory = Inventory(self.browser)
        self.actions = Actions(self.browser)
        self.planner = Planner(self.browser)
        self.configuration = Configuration(self.browser)
        self.rules = Rules(self.browser)
        self.header = Header(self.browser)




    def take_screenshot(self):
        """Take screen shot from the current browser window.
        The screenshot named ``screenshot-YYYY-mm-dd_HH_MM_SS.png`` will be
        placed on the path specified by
        ``settings.screenshots_path/YYYY-mm-dd/ClassName-method_name-``.
        All directories will be created if they don't exist. Make sure that the
        user running insights have the right permissions to create files and
        directories matching the complete.
        """
        if sys.exc_info()[0]:
            # Take screenshot if any exception is raised and the test method is
            # not in the skipped tests.
            now = datetime.now()
            if not settings.screenshots_path:
                #Screenshots will be saved at project root path
                path = os.path.join(
                    get_project_root(),
                    'screenshots',
                    now.strftime('%Y-%m-%d'),
                )
            else:
                #Screenshots will be saved at specified location in pool.conf
                path = os.path.join(
                    settings.screenshots_path,
                    now.strftime('%Y-%m-%d'),
                )
            if not os.path.exists(path):
                os.makedirs(path)
            filename = '{0}-{1}-screenshot-{2}.png'.format(
                type(self).__name__,
                self._testMethodName,
                now.strftime('%Y-%m-%d_%H_%M_%S')
            )
            path = os.path.join(path, filename)
            LOGGER.debug('Saving screenshot %s', path)
            self.browser.save_screenshot(path)
