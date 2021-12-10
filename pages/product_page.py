from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"

    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_success_messages()
        self.should_be_equal_product_names()
        self.should_be_equal_product_prices()

    def should_be_success_messages(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), "Success message with product name is not presented"
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE), "Success message with product price is not presented"

    def should_be_equal_product_names(self):
        page_product_name = self.browser.find_element(*ProductPageLocators.PAGE_PRODUCT_NAME).text
        success_message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert page_product_name == success_message_product_name, "Product names on the page and on the success message don't match"

    def should_be_equal_product_prices(self):
        page_product_price = self.browser.find_element(*ProductPageLocators.PAGE_PRODUCT_PRICE).text
        success_message_product_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE).text
        assert page_product_price == success_message_product_price, "Product prices on the page and on the success message don't match"
