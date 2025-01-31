from selenium import webdriver
import allure
import pytest


def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

def test_katalon_edge():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

"""
To run the parallel test cases.
1) We need to install the python xdist 
2) run the file => pytest -n auto -s "file path"
Example: pytest -n auto -s src/Selenium/ex_30_01_2025/test_003_MultiBrowser.py

"""

