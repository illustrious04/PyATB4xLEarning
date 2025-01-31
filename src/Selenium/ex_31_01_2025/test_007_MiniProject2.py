from dotenv import load_dotenv
import os
from  selenium.webdriver.chrome.options import Options
from selenium import webdriver
import allure
import pytest

@allure.title("App.vwo login")
@allure.description("Varify login with invalid credentials")
def test01_mini_project2():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
