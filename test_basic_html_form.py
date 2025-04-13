from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def test_basic_html():
    link = "https://testpages.eviltester.com/styled/basic-html-form-test.html"

    browser = driver = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    username_input = "bob"
    password_input = "bobqweasdzxc"
    comments_input = "this is a comment box"
    file_upload = os.path.abspath("file_test.txt")
    file_name = "file_test.txt"
    checkbox_test_first = "cb1"
    radio_test = "rd2"
    multipleselect_test = "ms3"
    dropdown_test = "dd6"

    driver.find_element(By.NAME, "username").send_keys(username_input)
    driver.find_element(By.NAME, "password").send_keys(password_input)
    driver.find_element(By.NAME, "comments").clear()
    driver.find_element(By.NAME, "comments").send_keys(comments_input)
    driver.find_element(By.NAME, "filename").send_keys(file_upload)

    driver.find_element(By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[5]/td/input[1]").click()
    driver.find_element(By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[5]/td/input[3]").click()
    driver.find_element(By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[7]/td/select/option[3]").click()
    driver.find_element(By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[8]/td/select/option[6]").click()
    driver.find_element(By.XPATH, "//*[@id='HTMLFormElements']/table/tbody/tr[9]/td/input[2]").click()

    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{username_input}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{password_input}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{comments_input}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{file_name}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{checkbox_test_first}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{radio_test}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{multipleselect_test}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//li[contains(text(), '{dropdown_test}')]").is_displayed()

    browser.quit()
