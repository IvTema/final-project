from selenium.webdriver.common.by import By


class LoginPageLocators():
    ENTER = (By.CSS_SELECTOR, "#login_form")
    LOG_IN = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ON_THE_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    PRICE_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".header .btn-group .btn.btn-default:nth-child(1)")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, "#.basket-items")
    NO_ITEM_TEXT = (By.XPATH, "//*[contains(text(),'Ваша корзина пуста')]")