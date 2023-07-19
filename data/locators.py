from selenium.webdriver.common.by import By
from data.registration_data import RegistrationData


class RegistrationLocators():
    registration_button_novbar = (By.CSS_SELECTOR, '#signin2')
    username = (By.CSS_SELECTOR, '#sign-username')
    password = (By.CSS_SELECTOR, '#sign-password')
    registration_button_modal = (By.XPATH, '//button[text()="Sign up"]')


class LoginLocators():
    login_button_novbar = (By.CSS_SELECTOR, '#login2')
    username = (By.CSS_SELECTOR, '#loginusername')
    password = (By.CSS_SELECTOR, 'loginpassword')
    login_button_modal = (By.XPATH, 'button[text()="Log in"]')
    username_on_novbar = (By.XPATH, f'//button[text()="Welcome {RegistrationData.username}"]')