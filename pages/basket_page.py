from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PROCEED_TO_CHECKOUT_BUTTON), \
        "There are products in basket ('Proceed to checkout' button is presented), but should not be"

    def should_be_empty_basket_text(self):
        empty_basket_text = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_TEXT).text
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_TEXT)  \
        and empty_basket_text == "Your basket is empty. Continue shopping", \
        "'Your basket is empty. Continue shopping' text is not presented"
