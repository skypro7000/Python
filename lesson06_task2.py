from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/textinput")
    
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    
    driver.find_element(By.ID, "updatingButton").click()
    
    button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    print(driver.find_element(By.ID, "updatingButton").text.strip())
finally:
    driver.quit()
