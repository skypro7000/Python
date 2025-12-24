from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


service = Service(executable_path="C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
finally:
    driver.quit()
