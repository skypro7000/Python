import pytest
from selenium import webdriver
from time import sleep

from calculator_page import CalculatorPage

class TestCalculator:
    @pytest.fixture(scope="module")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield
        self.driver.quit()

    def test_calculator(self, setup):
        calculator = CalculatorPage(self.driver)

        calculator.set_delay(45)

        calculator.press_button_7()
        calculator.press_button_plus()
        calculator.press_button_8()
        calculator.press_button_equals()

        sleep(45)
        result = calculator.get_result()
        assert result == "15", f"Expected result to be '15', but got '{result}'"
