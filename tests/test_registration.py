import allure
import pytest
import time

from pages.registration_page import RegistrationPage


class TestRegistrationForm():
    @pytest.mark.registration_test(scope='function', autouse=True)
    def test_registration_form(self, browser):
        page = RegistrationPage(browser, 'https://www.demoblaze.com/')
        page.open_page()
        page.registration_new_user()
        page.is_alert_message_present('Sign up successful.')
