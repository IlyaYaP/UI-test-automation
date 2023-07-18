import os

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_page(self):
        '''Функция открытия страницы'''
        with allure.step('Открываем главную страницу'):
            self.browser.get(self.url)

    def find_element(self, locator):
        '''Функция поиска элемента'''
        return self.browser.find_element(*locator)

    def is_element_present(self, how, what):
        '''Функция проверки наличия элемента на странице'''
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
