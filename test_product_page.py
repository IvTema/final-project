from pages.product_page import ProductPage
import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                    marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.add_test
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()


@pytest.mark.message
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
class TestMessageAfterAdd():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_basket()
        page.success_message_should_disappear()


@pytest.mark.login
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"])
class TestLoginLink_OnProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_into_the_basket()
    basket_page.should_not_be_items()
    basket_page.should_be_empty_text()


@pytest.mark.user
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"])
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", str(time.time()) + "passWord")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_basket()
