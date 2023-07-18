import allure
import time
from .base_page import BasePage
from data.locators import RegistrationLocators


class RegistrationPage(BasePage):

    def registration_new_user(self):
        with allure.step('Нажать кнопку регистрации нового пользователя в navbar.'):
            registration_button = self.find_element(RegistrationLocators.registration_button_novbar)
            time.sleep(5)
            registration_button.click()
            time.sleep(3) 