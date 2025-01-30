from allure_pytest.utils import allure_title
from selenium import webdriver
import allure
import pytest


@allure_title("Print Current URL and Page Source")
def test_01():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)

@allure_title("Failed Test case Forcefully")
def test_02():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "We dont Care About Your Health" in driver.page_source:
        print("Text Found!, Test case found")
    else:
        #print("Text Not Found, Test case fail")
        pytest.fail("Text Not Found!, Test case fail")
