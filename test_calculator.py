import unittest
from selenium import webdriver

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator_page = CalculatorPage(self.driver)

    def test_calculator_functionality(self):
        self.calculator_page.set_delay(45)
        
        self.calculator_page.click_button_7()
        self.calculator_page.click_button_plus()
        self.calculator_page.click_button_8()
        self.calculator_page.click_button_equals()
        
        time.sleep(45)
        
        result = self.calculator_page.get_result()
        self.assertEqual(result, "15")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()