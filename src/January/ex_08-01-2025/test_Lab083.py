import pytest
import allure
from selenium import webdriver


def test_method1():
    print("This is Pytest case")
    # assert True == False

@pytest.mark.regression
def test_method2():
    print("This is Method 2")
    assert 1+1 == 2


@pytest.mark.smoke
def test_method3():
    print("This is Method 3")
    assert  1-1 == 2

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")
@pytest.mark.negative
def test_create_booking_negative_4():
    print("test2")
    assert 15 + 5 == 20