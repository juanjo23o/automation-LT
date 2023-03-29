from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    "By Locators"
    USER = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.send_keys(self.USER, TestData.USER)
        self.send_keys(self.PASSWORD, TestData.PASSWORD)
        self.do_click(self.LOGIN_BUTTON)