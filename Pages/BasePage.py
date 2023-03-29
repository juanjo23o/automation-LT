from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(by_locator)).click()
        except:pass

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator)).click()
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator)).send_keys(text)
        except:pass
    
    def get_element_text(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator)).text
            return element
        except:pass

    def present_element(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator))
            return bool(element)
        except:pass