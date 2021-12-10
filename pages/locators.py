from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")  # или ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    PAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    SUCCESS_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
