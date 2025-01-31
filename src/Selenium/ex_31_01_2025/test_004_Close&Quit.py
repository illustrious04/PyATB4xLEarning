"""
Difference Between Close and Quit:
driver.close() Command:
    1) driver.close() will only close the current window or tab.
    2) It leaves the webdriver session open
    3) session id != null (Invalid)
    4) It will not close other tabs.
    5) Typically used at the end of the single test case.

driver.quit() Command:
    1) It will close all the window or tab and ends the webdriver session..
    2) session id != null (Invalid)
    3) It will  close all the tabs and windows.
    4) 80% of the time we use this one.
    5) Typically used at the end of the test suite or test case.
"""

from selenium import webdriver
import allure
import pytest
import time

@allure.title("Check Close command")
@pytest.mark.positive
def test01_check_close():
    driver = webdriver.Chrome()
    driver.get("www.google.com")
    time.sleep(8)
    driver.close()

@allure.title("Check Quit command")
@pytest.mark.positive
def test02_check_quit():
    driver = webdriver.Chrome()
    driver.get("www.facebook.com")
    time.sleep(8)
    driver.quit()

