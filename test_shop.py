import pytest
from selenium import webdriver
from pages import LoginPage, MainPage, CartPage, CheckoutPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_checkout_process(driver):
    
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    main_page = MainPage(driver)
    main_page.add_product_to_cart(0)
    main_page.add_product_to_cart(1)
    main_page.add_product_to_cart(2)
    
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Misha", "Korol", "70707")

    total_cost = checkout_page.get_total_cost()
    assert total_cost == "Total: $58.29"
