from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service(executable_path="C:/path/to/geckodriver.exe")
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(message.text.strip())
finally:
    driver.quit()
