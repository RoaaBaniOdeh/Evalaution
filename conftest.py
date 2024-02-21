import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get('http://172.22.1.141:8089/')
    yield driver

    driver.quit()


