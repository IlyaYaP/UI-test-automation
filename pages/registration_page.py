import allure
import time
from .base_page import BasePage
from data.locators import RegistrationLocators
from data.registration_data import RegistrationData


class RegistrationPage(BasePage):

    def registration_new_user(self):
        """Функция регистрации нового пользователя"""
        with allure.step('Нажаимаем на кнопку регистрации\
                          нового пользователя в navbar.'):
            registration_button_novbar = self.find_element(
                            RegistrationLocators.registration_button_novbar)
            registration_button_novbar.click()

        with allure.step('Заполняем поля username и password.'):
            username_input_field = self.find_element(
                            RegistrationLocators.username)
            username_input_field.send_keys(RegistrationData.username)
            password_input_field = self.find_element(
                            RegistrationLocators.password)
            password_input_field.send_keys(RegistrationData.password)

        with allure.step('Нажимаем на кнопку регистрации\
                          нового пользователя в модальном окне регистрации.'):
            registration_button_modal = self.find_element(
                            RegistrationLocators.registration_button_modal)
            registration_button_modal.click()
            time.sleep(5)