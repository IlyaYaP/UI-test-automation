from selenium.webdriver.common.by import By


class RegistrationLocators():
    registration_button_novbar = (By.CSS_SELECTOR, '#signin2')
    username = (By.CSS_SELECTOR, '#sign-username')
    password = (By.CSS_SELECTOR, '#sign-password')
    registration_button_modal = (By.XPATH, '//button[text()="Sign up"]')