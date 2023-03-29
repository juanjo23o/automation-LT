import time
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest

class Test_HomePage(BaseTest):

    "By Locators"
    COMPLETE_HEADER = (By.XPATH, '//h2[@class="complete-header"]')

    def test_init(self):
        self.request = HomePage(self.driver)
        self.request.add_to_cart()
        item = self.request.get_item_name()
        self.request.go_to_cart_section()
        # Validate that the item is present and is the samen text
        assert self.request.present_element((By.XPATH, f'//div[@class="cart_item"]//div[text()="{item}"]'))
        self.request.do_checkout()
        self.request.fill_information(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.ZIP_CODE)
        self.request.do_continue()
        # Validate that the item is present and is the samen text
        assert self.request.present_element((By.XPATH, f'//div[@class="cart_item"]//div[text()="{item}"]'))
        self.request.do_finish()
        # Validate that we finish with the order
        assert self.request.present_element(self.COMPLETE_HEADER)
        time.sleep(3)