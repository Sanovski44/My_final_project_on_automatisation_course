from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def is_basket_empty(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty." in text , "Basket is not empty"

    def should_be_basket_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Item in basket"
