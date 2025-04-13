from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_form():
    link = "https://testpages.eviltester.com/styled/html5-form-test.html"

    browser = driver = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    date_picker = "10-03-2025"
    date_time_picker = "100320251230"
    email = "bob2@gmail.com"
    month_field  = "December"
    month_year  = "2025"
    number_field = "405"
    date_picker_2 = "2025-03-10"
    month_field_test = "2025-12"

    
    driver.find_element(By.ID, "date-picker").send_keys(date_picker) 
    driver.find_element(By.ID, "date-time-picker").send_keys(date_time_picker)
    driver.find_element(By.ID, "email-field").clear()
    driver.find_element(By.ID, "email-field").send_keys(email) 
    driver.find_element(By.ID, "month-field").send_keys(month_field)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.perform()
    driver.find_element(By.ID, "month-field").send_keys(month_year)
    driver.find_element(By.ID, "number-field").clear()
    driver.find_element(By.ID, "number-field").send_keys(number_field) 
    driver.find_element(By.NAME, "submitbutton").click() 

 
    assert driver.find_element(By.XPATH, f"//li[contains(text(),'{date_picker_2}')]").is_displayed() 
    assert driver.find_element(By.XPATH, f"//li[contains(text(),'{email}')]").is_displayed() 
    assert driver.find_element(By.XPATH, f"//li[contains(text(),'{number_field}')]").is_displayed() 
    assert driver.find_element(By.XPATH, f"//li[contains(text(),'{month_field_test}')]").is_displayed() 

    browser.quit()
