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

    # Elements under Actions summary on Overview
    "overview.actions.availability": (
        By.XPATH,
        ("//div[contains(@class, 'availability-color')]/div[@class='text']/div[@class='msg']")
    ),
    "overview.availability.num": (
        By.XPATH,
        ("//div[contains(@class, 'availability-color')]/div[@class='num']")
    ),
    "overview.actions.stability": (
        By.XPATH,
        ("//div[contains(@class, 'stability-color')]/div[@class='text']/div[@class='msg']")
    ),
    "overview.stability.num": (
        By.XPATH,
        ("//div[contains(@class, 'stability-color')]/div[@class='num']")
    ),
    "overview.actions.performance": (
        By.XPATH,
        ("//div[contains(@class, 'performance-color')]/div[@class='text']/div[@class='msg']")
    ),
    "overview.performance.num": (
        By.XPATH,
        ("//div[contains(@class, 'performance-color')]/div[@class='num']")
    ),
    "overview.actions.security": (
        By.XPATH,
        ("//div[contains(@class, 'security-color')]/div[@class='text']/div[@class='msg']")
    ),
    "overview.security.num": (
        By.XPATH,
        ("//div[contains(@class, 'security-color')]/div[@class='num']")
    ),
    "overview.viewactions": (By.LINK_TEXT, ("View actions")),

    # Elements under Newest systems on Overview
    "overview.newest.summary": (
        By.XPATH,
        ("//a[@ui-sref='app.inventory']/preceding-sibling::span")
    ),
    "overview.newest.firstsystem": (
        By.XPATH, ("//div[@class='content']/ul/li[1]")),
    "overview.newest.allsystems": (
        By.XPATH, ("//div[@class='content']/ul")
    ),
    "overview.viewinventory": (By.LINK_TEXT, ("View inventory")),

    # Elements under Plan summary
    "overview.plan.summary": (
        By.XPATH,
        ("//a[@ui-sref='app.maintenance']/preceding-sibling::span[2]")
    ),
    "overview.plan.createplan": (
        By.LINK_TEXT, ('CREATE A NEW PLAN')
    ),
    "overview.viewplanner": (By.LINK_TEXT, ("View planner")),

    # Elements on Inventory page
    "inventory.search.box": (
        By.CSS_SELECTOR, ("input[ng-model='model']")
    ),
    "inventory.search.icon": (
        By.XPATH, ("//span[@class='input-group-addon']")
    ),
    "inventory.system.hostname": (
        By.CSS_SELECTOR, ("strong[class='hostname']")
    ),
    "inventory.system.type": (
        By.CSS_SELECTOR, ("strong[ng-if='includeText']")
    ),
    "inventory.not.checking.in": (
        By.XPATH, ("//span[contains(text(),'Show only')]"))
    ,
    "inventory.system.count": (
        By.XPATH, ("//div[contains(@class, 'col-sm-4 bulk-actions-dropdown')]/h3")
    ),
    "inventory.expand.all": (
        By.XPATH, ("//*[@class='ng-animate-enabled inventory-actions']//*[text()='Expand All']")
    ),
    "inventory.hostname": (
        By.XPATH, ("//*[@class='btn-group sort-button-group insights-dropdown']//*[text()='Hostname']")
    ),
    "inventory.with_actions.tab": (
        By.ID, ('rha-multibutton-inventoryWithActions')
    ),
    "inventory.without_action.tab": (
        By.ID, ('rha-multibutton-inventoryWithoutActions')
    ),
    "inventory.toggle": (
        By.XPATH, "//label[@for='cmn-toggle-2']"
    ),
    "inventory.system.name": (
        By.XPATH, ("(//strong[contains(@ng-click, 'showActions()')])[1]")
    ),
    "inventory.system.name.text": (
        By.XPATH, ("(//strong[contains(@ng-click, 'showActions()')])[1]")
    ),
    "inventory.close.button": (
        By.XPATH, ("//div[contains(@class, 'fa fa-close pull-right')]")
    ),
    "inventory.system.count1": (
        By.XPATH, ("//div[@class='col-sm-4 text-center-sm']")
    ),
    "inventory.dropdown.button": (
        By.XPATH, ("//a[contains (text(), 'Hostname')][1]")
    ),
    "inventory.system.name.detail": (
        By.XPATH, ("//div[contains(@class, 'ellipsis-overflow')]")
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
})
