import logging
from insights.ui.base import Base
from insights.ui.locators import locators


LOGGER = logging.getLogger('insights_portal')

class Header(Base):
    """
       Identifies content of Header of Insights UI
    """
    def header_text(self):
        return self.find_element(locators['header.help.text']).text

    def header_getting_started(self):
        return self.find_element(locators['header.getting.started']).text

    def header_more_info(self):
        return self.find_element(locators['header.more.info']).text

    def header_security_text(self):
        return self.find_element(locators['header.security']).text

    def header_browser_support(self):
        return self.find_element(locators['header.browser.support']).text

    def header_insights_api(self):
        return self.find_element(locators['header.insights.api']).text

    def header_getting_started_click(self):
        LOGGER.info("Clicking on get started link")
        self.click(locators['header.getting.started'])

    def header_more_info_click(self):
        LOGGER.info("Clicking on more info link")
        self.click(locators['header.more.info'])

    def header_security_click(self):
        LOGGER.info("Clicking on security link")
        self.click(locators['header.security.click'])

    def header_browser_support_click(self):
        LOGGER.info("Clicking on browser support link")
        self.click(locators['header.browser.support'])

    def header_insights_api_documentation_click(self):
        LOGGER.info("Clicking on api documentation link")
        self.click(locators['header.insights.api'])

    def header_info_title(self):
        return self.find_element(locators['header.info.text']).text

    def header_security_title(self):
        return self.find_element(locators['header.security']).text

    def header_browser_support_title(self):
        return self.find_element(locators['header.browser.support.title']).text

    def header_api_documentation_title(self):
        return self.find_element(locators['header.insights.api.documentation']).text

    def header_switch_from_browser_tab(self):
        current_url = self.browser.current_url
        self.browser.get(current_url.rstrip('/help/browsers') + '/insights')
        self.browser.implicitly_wait(30)

    def header_switch_from_api_documentation(self):
        current_url = self.browser.current_url
        self.browser.get(current_url.rstrip('/r/insights/docs/') + '/insights')
        self.browser.implicitly_wait(30)

    def header_notification_icon(self):
        return self.find_element(locators['header.notification.button'])

    def header_notification_icon_click(self):
        LOGGER.info("Clicking on notification icon")
        return self.click(locators['header.notification.button'])

    def header_notification_view_all(self):
        LOGGER.info("Clicking on view all tab")
        return self.click(locators['header.notification.view.all'])

    def header_notification_announcements(self):
        return self.find_element(locators['header.notification.announcement']).text