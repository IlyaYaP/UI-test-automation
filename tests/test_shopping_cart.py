import allure
import pytest
import time
from data.data import ShoppingCartData
from selenium.webdriver.common.by import By
from pages.shopping_cart_page import ShoppingCartPage
from data.locators import ShoppingCartLocators


@pytest.mark.shopping_cart_tests(scope='class', autouse=True)
@allure.feature('Тесты добавления продукта в корзину.')
class TestShoppingCart():

    main_page_url = 'https://www.demoblaze.com/'

    @pytest.mark.add_shopping_cart_test()
    @allure.story('Тест добавления продукта в корзину.')
    def test_shopping_cart(self, browser):
        page = ShoppingCartPage(browser, self.main_page_url)
        page.open_page()
        page.add_shopping_cart()
        page.should_be_product_in_cart(*ShoppingCartLocators.product_title)
