import logging
import time
from insights.ui.base import Base
from insights.ui.locators import locators

LOGGER = logging.getLogger('insights_portal')


class Configuration(Base):
    def conf_click_on_configuration_tabs(self):
        time.sleep(2)
        self.click(locators['conf.groups'])
        time.sleep(2)
        self.click(locators['conf.messaging'])
        time.sleep(2)
        self.click(locators['conf.setting'])
        time.sleep(2)
        self.click(locators['conf.dev'])
        time.sleep(2)
        self.click(locators['conf.hidden.rule'])

    def conf_hidden_rule_text(self):
        LOGGER.info("Checking Hidden rule section")
        return self.find_element(locators['conf.hidden.rule.title']).text

    def conf_hidden_rule_info(self):
        return self.find_element(locators['conf.hidden.rule.info']).text

    def conf_group_tab(self):
        LOGGER.info("Checking Groups section")
        self.click(locators['conf.groups'])
        return self.find_element(locators['conf.create.group.title']).text

    def conf_group_search_box(self, search):
        self.click(locators['conf.group.search.box'])
        self.field_update('conf.group.search.box', search)

    def conf_add_group_button(self):
        self.click(locators['conf.add.group.button'])

    def conf_add_group_text(self):
        return self.find_element(locators['conf.add.group.text']).text

    def conf_delete_group_text(self):
        return self.find_element(locators['conf.delete.group']).text

    def conf_delete_group_button(self):
        time.sleep(2)
        self.click(locators['conf.delete.group'])

    def conf_popup_yes_button(self):
        time.sleep(2)
        self.click(locators['conf.popup.yes.button'])

    def conf_group_list_text(self):
        return self.find_element(locators['conf.group.grouplist.text']).text

    def conf_messaging_title(self):
        LOGGER.info("Checking Messaging section")
        self.click(locators['conf.messaging'])
        return self.find_element(locators['conf.messaging.title']).text

    def conf_messaging_checkbox(self):
        self.click(locators['conf.messaging.checkbox'])

    def conf_messaging_update_button(self):
        time.sleep(2)
        self.click(locators['conf.messaging.update.button'])

    def conf_settings_title(self):
        LOGGER.info("Checking settings section")
        self.click(locators['conf.setting'])
        return self.find_element(locators['conf.settings.title']).text

    def conf_settings_checkbox(self):
        return self.find_element(locators['conf.settings.checkbox']).text

    def conf_dev_title(self):
        LOGGER.info("Checking Dev section")
        self.click(locators['conf.dev'])
        return self.find_element(locators['conf.dev.demo.mode']).text

    def conf_dev_api_prefix(self):
        return self.find_element(locators['conf.dev.api.prefix']).text

    def conf_dev_api_version(self):
        return self.find_element(locators['conf.dev.api.version']).text

    def conf_dev_fake_user_info(self):
        return self.find_element(locators['conf.dev.api.fake.user']).text

    def conf_dev_fake_entitlements(self):
        return self.find_element(locators['conf.dev.api.fake.entitlement']).text
