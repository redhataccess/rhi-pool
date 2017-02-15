# -*- encoding: utf-8 -*-
"""Implements different locators for UI"""

from selenium.webdriver.common.by import By
from .model import LocatorDict

locators = LocatorDict({

    # Login
    "login.username": (By.ID, 'username'),
    "login.password": (By.ID, 'password'),
    "login.submit": (By.ID, '_eventId_submit'),

    # Overview
    "overview.title": (By.XPATH, ("//h1[contains(@class, 'page-title')]/span")
                       ),
    "overview.title.icon": (
        By.XPATH,
        ("//h1[contains(@class, 'page-title')]/i")
    ),
    "overview.latest": (
        By.XPATH,
        ("//h2[@class='title']/i[contains(@class, 'fa-fire')]/"
         "following-sibling::span")
    ),
    "overview.latest.icon": (
        By.XPATH,
        ("//h2[@class='title']/i[contains(@class, 'fa-fire')]")
    ),
    "overview.latest.news": (
        By.XPATH,
        ("//span[@class='handcrafted-content']/p")
    ),

    # Elements under Newest systems on Overview
    "overview.newest.summary": (
        By.XPATH,
        ("//a[@ui-sref='app.inventory']/preceding-sibling::span")
    ),
    "overview.viewinventory": (By.LINK_TEXT, ("View inventory")
                               ),

    # Elements under Plan summary
    "overview.plan.summary": (
        By.XPATH,
        ("//a[@ui-sref='app.maintenance']/preceding-sibling::span[2]")
    ),
    "overview.plan.createplan": (
        By.LINK_TEXT, ('CREATE A NEW PLAN')
    ),
    "overview.viewplanner": (By.LINK_TEXT, ("View planner")),
    "overview.viewactions": (By.LINK_TEXT, ('View actions')),

    # Elements on Inventory page
    "inventory.search.box": (
        By.CSS_SELECTOR, ("input[ng-model='model']")
    ),
    "inventory.search.icon": (
        By.XPATH, ("//span[@class='input-group-addon']")
    ),
    "inventory.system.hostname": (
        By.LINK_TEXT, ("test-k.novalocal")
    ),
    "inventory.system.type": (
        By.CSS_SELECTOR, ("strong[ng-if='includeText']")
    ),
    "inventory.hostname": (
        By.XPATH, ("//*[@class='btn-group sort-button-group insights-dropdown']//*[text()='Hostname']")
    ),
    "inventory.close.button": (
        By.XPATH, ("//div[contains(@class, 'fa fa-close pull-right')]")
    ),
    "inventory.system.count1": (
        By.XPATH, ("//div[@class='col-sm-4 text-center-sm']")
    ),

    "inventory.system.name.detail": (
        By.XPATH, ("//div[contains(@class, 'ellipsis-overflow')]")
    ),
    "inventory.groups.label": (
        By.XPATH, ("//span[contains(text(),'Groups')]")
    ),
    "inventory.group.dropdown": (
        By.XPATH, ("//button[contains(.,'All Groups')]")
    ),
    "inventory.group.dropdown.text": (
        By.XPATH, ("//select[@ng-model='group']/option[text()='123']")
    ),

    # Elements under Planner page 
    "planner.title": (
        By.XPATH, ("//h1[contains(@class, 'page-title')]/span")
    ),
    "planner.create.plan.text": (
        By.XPATH, ("//span[contains(text(),'Create')]")
    ),
    "planner.new.plan.text": (
        By.XPATH, ("//span[contains(text(),'New')]")
    ),
    "planner.search.box": (
        By.XPATH, ("//input[contains(@ng-model,'model')]")
    ),
    "planner.search.icon": (
        By.XPATH, ("//span[@class='input-group-addon']")
    ),
    "planner.past.button": (
        By.XPATH, ("//button[contains(.,'Past')]")
    ),
    "planner.not.scheduled.button": (
        By.XPATH, ("//button[contains(.,'Not')]")
    ),
    "planner.suggestion.button": (
        By.XPATH, ("//button[contains(.,'Suggestions')]")
    ),
    "planner.future.button": (
        By.XPATH, ("//button[contains(.,'Future')]")
    ),
    "planner.delete.button": (
        By.XPATH, ("//i[contains(@class, 'fa fa-trash-o action')]")
    ),
    "planner.create.plan.button": (
        By.XPATH, ("//*[@class='create-plan' and contains(@ng-click,'quickAdd()')]")
    ),
    "planner.all.button": (
        By.XPATH, ("//div[contains(@class, 'col-sm-4 col-md-7')]")
    ),
    "planner.yes.popup.button": (
        By.XPATH, ("//button[contains(.,'Yes')]")
    ),

    # Elements under Configuration page
    "conf.hidden.rule": (
        By.LINK_TEXT, ("Hidden Rules")
    ),
    "conf.groups": (
        By.LINK_TEXT, ("Groups")
    ),
    "conf.messaging": (
        By.LINK_TEXT, ("Messaging")
    ),
    "conf.setting": (
        By.LINK_TEXT, ("Settings")
    ),
    "conf.dev": (
        By.LINK_TEXT, ("Dev")
    ),

    # Elements under hidden_rule section
    "conf.hidden.rule.title": (
        By.XPATH, (" //h2[contains(@class, 'page-title')]/span")
    ),
    "conf.hidden.rule.info": (
        By.XPATH, ("//span[contains(text(),'account')] ")
    ),

    # Elements under group section
    "conf.create.group.title": (
        By.XPATH, ("//span[contains(text(),'Create')]")
    ),
    "conf.group.search.box": (
        By.XPATH, ("//input[@ng-model='newGroup.display_name']")
    ),
    "conf.add.group.button": (
        By.XPATH, ("//i[contains(@class, 'fa fa-plus')]")
    ),
    "conf.add.group.text": (
        By.XPATH, ("//span[contains(text(),'Add Group')]")
    ),
    "conf.delete.group": (
        By.XPATH, ("//span[contains(text(),'Delete Group')]")
    ),
    "conf.popup.yes.button": (
        By.XPATH, ("//button[contains(.,'Yes')]")
    ),
    "conf.group.grouplist.text": (
        By.XPATH, ("//h2[contains(@class, 'page-title')]/span")
    ),

    # Elements under messaging section
    "conf.messaging.title": (
        By.XPATH, ("//h2[contains(@class, 'page-title')]/span")
    ),
    "conf.messaging.checkbox": (
        By.XPATH, ("//input[@ng-model='campaign.enrolled']")
    ),

    # Elements under settings section
    "conf.settings.title": (
        By.XPATH, ("//h2[contains(@class, 'page-title')]/span ")
    ),
    "conf.settings.checkbox": (
        By.XPATH, ("//input[@ng-model='setting.value']")
    ),

    # Elements under Dev section
    "conf.dev.demo.mode": (
        By.XPATH, ("//*[@class='user']//*[text()='Demo Mode']")
    ),
    "conf.dev.api.prefix": (
        By.XPATH, ("//*[@class='user']//*[text()='API Prefix']")
    ),
    "conf.dev.api.version": (
        By.XPATH, ("//*[@class='tab-content']//*[text()='API Version']")
    ),
    "conf.dev.api.fake.user": (
        By.XPATH, ("//*[@class='tab-content']//*[text()='Fake user info']")
    ),
    "conf.dev.api.fake.entitlement": (
        By.XPATH, ("//*[@class='tab-content']//*[text()='Fake Entitlements']")
    ),

    # Elements under Rules section
    "rules.search.box": (
        By.XPATH, ("//input[contains(@class, 'search-box')]")
    ),
    # Elements on Header tab
    "header.help.text": (
        By.XPATH, ("//span[contains(text(),'Help')]")
    ),
    "header.getting.started": (
        By.LINK_TEXT, ("Getting Started")
    ),
    "header.more.info": (
        By.LINK_TEXT, ("More Info")
    ),
    "header.security": (
        By.LINK_TEXT, ("Security")
    ),
    "header.browser.support": (
        By.LINK_TEXT, ("Browser Support")
    ),
    "header.insights.api": (
        By.LINK_TEXT, ("Insights API Documentation")
    ),

    # Elements on info Page
    "header.info.text": (
        By.XPATH, ("//span[contains(.,'Introduction to Red Hat Insights')]")
    ),

    # Elements on Security Page
    "header.security.text": (
        By.XPATH, ("//*[@class='container info-page']//section/h1")
    ),
    "header.security.click": (
        By.XPATH, ("//a[@ui-sref='info.security']")
    ),

    # Elements on Browser Support Page
    "header.browser.support.title": (
        By.XPATH, ("//*[@class='container']//*[text()='Browser Support Policy']")
    ),

    # Elements on Insights api documentation page
    "header.insights.api.documentation": (
        By.XPATH, ("//*[@id='project']//*[text()='Red Hat Insights API Documentation']")
    ),
    "header.notification.button": (
        By.XPATH, ("//i[contains(@class, 'fa fa-globe')]")
    ),
    "conf.group.filter": (
        By.XPATH, ("//label[text()='Available Systems']/following-sibling::input")
    ),
    "conf.group.available": (
        By.XPATH, "//*[@class='col-md-6 group-list']//*[text()='Available Systems']"
    ),
    "conf.group.select.visible.text": (
        By.XPATH, "//span[contains(text(),'Select Visible')]"
    ),

    # Add system to group
    "groups.search.box":    (
        By.XPATH, ("//label[text()='Available Systems']/following-sibling::input")
    ),
    "group.checkbox": (
        By.XPATH, ("(//span[contains(text(),'Select Visible')])[1]")
    ),
    "group.add.system" : (
        By.XPATH, ("(//span[contains(text(),'Add Systems')])[1]")
    ),

    # Remove Group
    "group.mimimize.button" :(
        By.XPATH,"//div[contains(@class, 'fa fa-minus-square-o')]"
    ),

    "group.remove.group":(
        By.XPATH, "//span[contains(.,'Delete Group')]"
    ),
    "group.yes.popup.button": (
        By.XPATH, ("//button[contains(.,'Yes')]")
    ),
})
