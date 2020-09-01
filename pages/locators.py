from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    ENTER = (By.CSS_SELECTOR, "#login_form")
    LOG_IN = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ON_THE_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    PRICE_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")