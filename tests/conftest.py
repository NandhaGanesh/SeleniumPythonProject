import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# Explicit wait class importing
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

'''
def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )
'''

@pytest.fixture(scope="class")
def setup(request):
    #browserName = request.config.getoption("browserName")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(5)


        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

        request.cls.driver = driver
        yield
    # driver.close()
