from selenium.webdriver.common.by import By
from data.data import RegistrationData


class RegistrationLocators():
    registration_button_novbar = (By.CSS_SELECTOR, '#signin2')
    username = (By.CSS_SELECTOR, '#sign-username')
    password = (By.CSS_SELECTOR, '#sign-password')
    registration_button_modal = (By.XPATH, '//button[text()="Sign up"]')


class LoginLocators():
    login_button_novbar = (By.CSS_SELECTOR, '#login2')
    username = (By.CSS_SELECTOR, '#loginusername')
    password = (By.CSS_SELECTOR, '#loginpassword')
    login_button_modal = (By.XPATH, '//button[text()="Log in"]')


class ContactMessageLocators():
    contact_button = (By.XPATH, '//a[text()="Contact"]')
    recipient_email = (By.CSS_SELECTOR, '#recipient-email')
    recipient_name = (By.CSS_SELECTOR, '#recipient-name')
    recipient_message = (By.CSS_SELECTOR, '#message-text')
    send_meesage_button = (By.XPATH, '//button[text()="Send message"]')
