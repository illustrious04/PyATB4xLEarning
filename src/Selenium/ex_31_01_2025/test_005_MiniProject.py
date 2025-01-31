"""
Open URL: https://demo.us.espocrm.com/

verify the title and current url

assert and create Allure HTML report also.
"""
from selenium import webdriver
import allure
import pytest
import time

@allure.title("Open demo espocrm verify title and current url")
@pytest.mark.positive
def test_espocrmLogin():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(8)
    assert driver.current_url == "https://demo.us.espocrm.com/"
    assert driver.title == "EspoCRM Demo"
