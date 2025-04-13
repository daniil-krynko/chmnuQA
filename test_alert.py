from selenium import webdriver
from selenium.webdriver.common.by import By

def test_simple_alert():
    link = "https://testpages.eviltester.com/styled/alerts/alert-test.html"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(link)

    driver.find_element(By.ID, "alertexamples").click()  # Натискаємо кнопку для виклику alert

    alert = driver.switch_to.alert
    alert.accept()  # Закриваємо alert, натиснувши "OK"

    result_text = driver.find_element(By.ID, "alertexplanation").text
    assert "triggered and handled the alert dialog" in result_text

    driver.quit()
