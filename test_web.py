import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_samsung_tablet():
    url = "https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=20"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Tablets')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='product-list']/div/div/div[1]/a").click()

    assert driver.find_element(By.XPATH, "//*[contains(text(),'720p HD video recording')]").is_displayed()

    driver.quit()
