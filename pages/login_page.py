import allure
import time
from .base_page import BasePage
from data.locators import RegistrationLocators, LoginLocators
from data.registration_data import RegistrationData
from allure_commons.types import AttachmentType


class LoginPage(BasePage):
    def login_new_user(self):
        with allure.step('Нажаимаем на кнопку входа в учетную запись\
                          нового пользователя в navbar.'):
            login_button_novbar = self.find_element(LoginLocators.login_button_novbar)
            login_button_novbar.click()
        with allure.step('Заполняем поля username и password.'):
            user_input_field = self.find_element(LoginLocators.username)
            user_input_field.send_keys(RegistrationData.username)
            password_input_field = self.find_element(LoginLocators.password)
            password_input_field.send_keya(RegistrationData.password)
        with allure.step('Нажимаем на кнопку входа в учетную запись\
                          нового пользователя в модальном окне регистрации.'):
            login_button_modal = self.find_element(LoginLocators.login_button_modal)
            login_button_modal.click()
