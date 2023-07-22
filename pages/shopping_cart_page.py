import allure
import time
from .base_page import BasePage
from data.locators import ShoppingCartLocators
from data.data import ShoppingCartData
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains


class ShoppingCartPage(BasePage):
    
    def add_shopping_cart(self):
        '''Функция добавление продукта в корзину.'''
        with allure.step('Находим нужный нам продукт, прокручиваем страницу и открываем страницу с продуктом.')
        product_button = self.find_element(ShoppingCartLocators.add_product_button)
        ActionChains(self.browser).scroll_to_element(product_button).perform()
        product_button.click()








        # cart_button = self.find_element(ShoppingCartLocators.cart_button_novbar)
        # cart_button.click()
