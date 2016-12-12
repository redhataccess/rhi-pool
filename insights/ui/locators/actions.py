# -*- encoding: utf-8 -*-
"""Implements different locators for UI"""

from selenium.webdriver.common.by import By
from .model import LocatorDict

action_locators = LocatorDict({
    "actions.title": (
        By.XPATH, ("//h1[contains(@class, 'page-title')]/span")
    ),
    "actions.pie.desc": (
        By.XPATH, ("//div[contains(@class, 'col-sm-offset-1')]/p[1]/span")
    ),
    "actions.desc.count": (
        By.XPATH, ("//div[contains(@class, 'col-sm-offset-1')]/p[2]/strong")
    ),
    "actions.pie.count": (
        By.XPATH, ("//div[@class='content']/span[@class='num']")
    ),
    "actions.filter": (
        By.LINK_TEXT, ("FILTER")
    ),
    "actions.filter.all": (
        By.ID, ("rha-multibutton-severityFiltersAll")
    ),
    "actions.filter.info": (
        By.ID, ("rha-multibutton-severityFiltersINFO")
    ),
    "actions.filter.warn": (
        By.ID, ("rha-multibutton-severityFiltersWARN")
    ),
    "actions.filter.error": (
        By.ID, ("rha-multibutton-severityFiltersERROR")
    ),
    "actions.downloadcsv": (
        By.XPATH, ("//div[@class='action']")
    ),
    "actions.section":(
        By.XPATH, ("//div[@class='tbody-scrollable']/table/tbody/tr")
    ),
    "actions.section.names":(
        By.XPATH, ("//div[@class='tbody-scrollable']/table/tbody/tr/td[1]")
    )
})
