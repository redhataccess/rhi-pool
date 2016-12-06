from selenium.webdriver.common.by import By
from .model import LocatorDict

menu_locators = LocatorDict({

    # Menu elements
    "menu.overview": (By.XPATH, ("//a[@ui-sref='app.overview']")),
    "menu.actions": (By.XPATH, ("//a[@ui-sref='app.actions']")),
    "menu.inventory": (By.XPATH, ("//a[@ui-sref='app.inventory']")),
    "menu.planner": (By.XPATH, ("//a[@ui-sref='app.maintenance']")),
    "menu.rules": (By.XPATH, ("//a[@ui-sref='app.rules']")),
    "menu.config": (By.XPATH, ("//a[@ui-sref='app.config']")),

    #
    "menu.filter": (By.XPATH, ("//span[@class='summary-name']"))
})