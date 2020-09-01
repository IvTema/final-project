from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_in_basket(self):
        element_btn_add = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        element_btn_add.click()
        self.solve_quiz_and_get_code()
        self.should_see_product_added_message()
        self.price_in_message_same_as_in_basket()

    def should_see_product_added_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_THE_PAGE).text, (
            'Name of the product in message != name on the page')

    def price_in_message_same_as_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_ON_PAGE).text, (
            'Price in message != price on the page')
