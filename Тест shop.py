import time
import unittest
from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage

class TestShopping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def test_shopping_cart(self):
        
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        
        main_page = MainPage(self.driver)
        main_page.add_item_to_cart(0)
        main_page.add_item_to_cart(1)
        main_page.add_item_to_cart(2)

        
        main_page.go_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()

        
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_form("Misha", "Korol", "12345")

        
        time.sleep(2)
        total_price = checkout_page.get_total