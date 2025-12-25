from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    WebDriverWait(driver, 10).until(
        lambda d: all(img.get_attribute("complete") == "true" for img in d.find_elements(By.TAG_NAME, "img"))
    )
    
    images = driver.find_elements(By.TAG_NAME, "img")
    print(images[2].get_attribute("src"))
finally:
    driver.quit()
