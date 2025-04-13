from selenium import webdriver
from selenium.webdriver.common.by import By

def test_auth_page():
    link = "https://testpages.eviltester.com/styled/auth/basic-auth-test.html"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)

    username_text = driver.find_element(By.XPATH, "//p[contains(text(), 'username:')]").text
    real_username = username_text.split(": ")[1]  

    password_text = driver.find_element(By.XPATH, "//p[contains(text(), 'password:')]").text
    real_password = password_text.split(": ")[1]  

    assert driver.find_element(By.XPATH, "//a[contains(text(), 'Basic Auth')]").is_displayed()

    webpage = "testpages.eviltester.com/styled/auth/basic-auth-results.html"
    url = f"https://{real_username}:{real_password}@{webpage}"
    driver.get(url)

    assert driver.find_element(By.XPATH, "//span[contains(text(), 'Authenticated')]").is_displayed()

    driver.quit()
