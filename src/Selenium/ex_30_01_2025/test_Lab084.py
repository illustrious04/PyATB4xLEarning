from selenium import webdriver
import pytest
import allure

@allure.title("Open the app.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    print(driver.session_id)

