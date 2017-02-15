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
        add_group = self.wait_until_element_to_be_clickable(locators['conf.add.group.button'])
        add_group.click()

    def conf_add_group_text(self):
        LOGGER.info("Adding Group")
        return self.find_element(locators['conf.add.group.text']).text

    def conf_delete_group_text(self):
        return self.find_element(locators['conf.delete.group']).text

    def conf_delete_group_button(self):
        conf_delete_group = self.wait_until_element(locators['conf.delete.group'], timeout=100)
        conf_delete_group.click()


    def conf_popup_yes_button(self):
        conf_popup_yes_button = self.wait_until_element(locators['conf.popup.yes.button'],timeout=100)
        conf_popup_yes_button.click()

    def conf_group_list_text(self):
        return self.find_element(locators['conf.group.grouplist.text']).text

    def conf_messaging_title(self):
        LOGGER.info("Checking Messaging section")
        self.click(locators['conf.messaging'])
        return self.find_element(locators['conf.messaging.title']).text

    def conf_messaging_checkbox(self):
        self.click(locators['conf.messaging.checkbox'])

    def conf_messaging_update_button(self):
        conf_messaging_update_button = self.wait_until_element(locators['conf.messaging.update.button'])
        conf_messaging_update_button.click()

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

    def conf_group_filter(self, system):
         self.click(locators['conf.group.filter'])
         self.field_update('conf.group.filter',system)

    def conf_group_available_system_text(self):
        self.wait_until_element(locators['conf.group.available'], timeout=50)
        return self.find_element(locators['conf.group.available']).text

    def conf_group_select_visible_text(self):
        return self.find_element(locators['conf.group.select.visible.text']).text

    def conf_group_select_all_checkbox(self):
        conf_group_select_all_checkbox = self.wait_until_element(locators['conf.group.select.all.checkbox'])
        conf_group_select_all_checkbox .click()
