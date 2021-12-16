from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import random


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   marks=pytest.mark.xfail(reason="Product names on the page and on success message message don't match")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

@pytest.mark.xfail(reason="Success messages should appear after adding product to basket!")
def test_guest_cant_see_success_messages_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_messages()  # должен возвращать False

def test_guest_cant_see_success_messages(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_messages()  # должен возвращать True

@pytest.mark.xfail(reason="Success messages shouldn't disappear after adding product to basket!")
def test_messages_disappeared_after_adding_product_to_basket(browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_messages() # должен возвращать False

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.go_to_basket_page()            # переходим в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_text()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        register_page = LoginPage(browser, link)
        register_page.open()
        email = str(random.random()) + "@fakemail.com"  # генерация случайного email-адреса, чтобы избежать повторения в тестах
        password = "test_password"
        register_page.register_new_user(email, password)
        register_page.should_be_authorized_user()

    def test_user_cant_see_success_messages(self, browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_messages()  # должен возвращать True

    def test_user_can_add_product_to_basket(self, browser, link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
