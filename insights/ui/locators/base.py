# -*- encoding: utf-8 -*-
"""Implements different locators for UI"""

from selenium.webdriver.common.by import By
from .model import LocatorDict

locators = LocatorDict({

    # Login
    "login.username": (By.ID, 'username'),
    "login.password": (By.ID, 'password'),
    "login.submit": (By.ID, '_eventId_submit'),

    #Overview
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
      ("//span[@class='handcrafted-content']")
    ),

    #Elements under Actions summary on Overview
    "overview.actions.availability": (
        By.XPATH,
        ("//div[contains(@class, 'availability-color')]/div[@class='text']")
    ),
    "overview.availability.num": (
        By.XPATH,
        ("//div[contains(@class, 'availability-color')]/div[@class='num']")
    ),
    "overview.actions.stability": (
        By.XPATH,
        ("//div[contains(@class, 'stability-color')]/div[@class='text']")
    ),
    "overview.stability.num": (
        By.XPATH,
        ("//div[contains(@class, 'stability-color')]/div[@class='num']")
    ),
    "overview.actions.performance": (
        By.XPATH,
        ("//div[contains(@class, 'performance-color')]/div[@class='text']")
    ),
    "overview.performance.num": (
        By.XPATH,
        ("//div[contains(@class, 'performance-color')]/div[@class='num']")
    ),
    "overview.actions.security": (
        By.XPATH,
        ("//div[contains(@class, 'security-color')]/div[@class='text']")
    ),
    "overview.security.num": (
        By.XPATH,
        ("//div[contains(@class, 'security-color')]/div[@class='num']")
    ),
    "overview.viewactions": (By.LINK_TEXT, ("View actions")),

    #Elements under Newest systems on Overview
    "overview.newest.summary": (
        By.XPATH,
        ("//a[@ui-sref='app.inventory']/preceding-sibling::span")
    ),
    "overview.newest.firstsystem": (
        By.XPATH, ("//div[@class='content']/ul/li[1]")),
    "overview.newest.allsystems": (
        By.XPATH, ("//div[@class='content']/ul")
    ),
    "overview.plan.summary": (
        By.XPATH,
        ("//a[@ui-sref='app.maintenance']/preceding-sibling::span[2]")
    ),
    "overview.plan.createplan": (
        By.LINK_TEXT, ('CREATE A NEW PLAN')
    ),

    #Elements on Inventory page
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
    )
})
