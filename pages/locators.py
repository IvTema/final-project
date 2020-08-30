from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    ENTER = (By.CSS_SELECTOR, "#login_form")
    LOG_IN = (By.CSS_SELECTOR, "#register_form")