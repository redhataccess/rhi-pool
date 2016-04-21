from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    # Login Page
    page_title = (By.XPATH, '//*[@ class= "col-md-12"]/h1')
    username_field = (By.ID, 'username')
    password_field = (By.ID, 'password')
    submit_Btn = (By.ID, '_eventId_submit')
