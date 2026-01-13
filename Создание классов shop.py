from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = (By.CSS_SELECTOR, ".btn_inventory")
        self.cart_button = (By.ID, "shopping_cart_container")

    def add_item_to_cart(self, index):
        self.driver.find_elements(*self.add_to_cart_buttons)[index].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        return self.driver.find_element(*self.total_label).text