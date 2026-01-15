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


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_primary")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_index):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        buttons[product_index].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_cost = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_cost(self):
        return self.driver.find_element(*self.total_cost).text
