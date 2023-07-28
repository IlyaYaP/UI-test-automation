import allure
import time
from .base_page import BasePage
from data.locators import PlacingAnOrderLocators
from data.data import ShoppingCartData
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class PlacingOrderPage(BasePage):


    def place_an_order(self):
        phones_button_categories = self.find_element(PlacingAnOrderLocators.phones_categories_button)
        phones_button_categories.click()