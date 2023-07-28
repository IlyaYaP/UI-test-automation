import allure
import time
from .base_page import BasePage
from data.locators import ShoppingCartLocators
from data.data import ShoppingCartData
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ShoppingCartPage(BasePage):

    def add_shopping_cart(self):
        '''Функция добавление продукта в корзину.'''
        with allure.step('Находим нужный нам продукт, прокручиваем страницу и открываем страницу с продуктом.'):
            product_button = self.find_element(ShoppingCartLocators.add_product_button)
            ActionChains(self.browser).scroll_to_element(product_button).perform()
            product_button.click()
        with allure.step('Добавляем продукт в корзину, \
                         нажимая на соответствующую кнопку.'):
            add_cart_button = self.find_element(
                              ShoppingCartLocators.add_product_shopping_cart)
            add_cart_button.click()
            self.is_alert_message_present(ShoppingCartData.add_cart_message)
        with allure.step('Переходим на страницу корзины, нажимая на кнопку в navbar'):
            cart_button_novbar = self.find_element(ShoppingCartLocators.cart_button_novbar)
            cart_button_novbar.click()

    def should_be_product_in_cart(self, *locator):
        '''Проверка наличия имя пользователя, после успешной регистрации'''
        with allure.step('Проверяем, наличие продукта в корзине.'):
            assert self.is_element_present(*locator), 'Product is not presented'











        # cart_button = self.find_element(ShoppingCartLocators.cart_button_novbar)
        # cart_button.click()
