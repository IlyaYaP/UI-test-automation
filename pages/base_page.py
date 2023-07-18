import os

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    
    def is_alert_message_present(self, allert_message):
        '''Функция проверки появления алерта с соответствующим сообщением'''
        try:
            WebDriverWait(self.browser, timeout=1).until(EC.alert_is_present(), 'Timed out waiting.')
            print(self.browser.switch_to.alert.text)
            assert self.browser.switch_to.alert.text == allert_message, 'The message in the alert box does not match the expected'
        except TimeoutException:
            return False
        return True

