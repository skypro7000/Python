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