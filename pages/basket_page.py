from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "At least 1 item in basket, but should not be"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEM_TEXT), \
            "No YOUR BASKET EMPTY text, but should be"
