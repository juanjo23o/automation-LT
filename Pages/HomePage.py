from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage

class HomePage(LoginPage):

    "By Locators"
    ITEM_NAME = (By.XPATH, '(//div[@class="inventory_item_name"])[1]')
    ADD_TO_CART_BUTTON = (By.XPATH, '(//div[@class="inventory_item"]//button)[1]')
    SHOPPING_CART_BUTTON = (By.ID, 'shopping_cart_container')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')

    def get_item_name(self):
        return self.get_element_text(self.ITEM_NAME)

    def add_to_cart(self):
        self.do_click(self.ADD_TO_CART_BUTTON)

    def go_to_cart_section(self):
        self.do_click(self.SHOPPING_CART_BUTTON)
    
    def do_checkout(self):
        self.do_click(self.CHECKOUT_BUTTON)
    
    def do_continue(self):
        self.do_click(self.CONTINUE_BUTTON)

    def do_finish(self):
        self.do_click(self.FINISH_BUTTON)

    def fill_information(self, f_name, s_name, zip):
        self.send_keys(self.FIRST_NAME, f_name)
        self.send_keys(self.LAST_NAME, s_name)
        self.send_keys(self.ZIP_CODE, zip)
    

