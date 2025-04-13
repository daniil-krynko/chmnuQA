import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_upload_page():

    link= "https://testpages.eviltester.com/styled/file-upload-test.html"

    browser=driver=webdriver.Chrome () 
    browser.implicitly_wait(10) 
    browser.get(link)

    file_upload = os.path.abspath("file_test.txt")
    file_name= "file_test.txt"

    driver.find_element(By.NAME, "filename").send_keys(file_upload)
    driver.find_element(By.XPATH, "//*[@id='itsafile']").click()
    driver.find_element(By.NAME, "upload").click()

    assert driver.find_element(By.XPATH, f"//p[contains(text(), '{file_name}')]").is_displayed()

    browser.quit()