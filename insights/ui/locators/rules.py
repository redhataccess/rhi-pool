# -*- encoding: utf-8 -*-
"""Rules data model for UI locators"""

from selenium.webdriver.common.by import By
from .model import LocatorDict

rules_locators = LocatorDict({
    "rules.filter.all": (
        By.ID, ("rha-multibutton-categoryFiltersall")
    ),
    "rules.filter.availability": (
        By.ID, ("rha-multibutton-categoryFiltersavailability")
    ),
    "rules.filter.stability": (
        By.ID, ("rha-multibutton-categoryFiltersstability")
    ),
    "rules.filter.performance": (
        By.ID, ("rha-multibutton-categoryFiltersperformance")
    ),
    "rules.filter.security": (
        By.ID, ("rha-multibutton-categoryFilterssecurity")
    ),
    "rules.cards": (
        By.XPATH, ("//span[@class='title pointer']/span")
    ),
    "rules.active.filter": (
        By.XPATH, ("//a[contains(@class,'active')]")
    ),
    "rules.search.box": (
        By.XPATH, ("//input[contains(@class, 'search-box')]")
    ),
    "rules.search.icon": (
        By.XPATH, ("//div[contains(@class, 'fa-search')]")
    ),
    "rules.content.blocks": (
        By.XPATH, ("//div[contains(@class, 'content-block-outline')]")
    )
})