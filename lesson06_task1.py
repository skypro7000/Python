from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/ajax")
    
    driver.find_element(By.ID, "ajaxButton").click()
    
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    print(message.text.strip())
finally:
    driver.quit()
