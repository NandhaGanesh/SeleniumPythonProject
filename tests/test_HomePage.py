import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class TestHomePage(BaseClass):
    def test_FormSubmit(self, getData):
        log = self.getLogging()
        homepage= HomePage(self.driver)

        print(driver.title)
        print(driver.current_url)

        # CSSselector => tagname[attribute='value']  #id,  .classname
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Nandha Ganesh")
        homepage.getName().send_keys(getData["name"])
        log.info("Name is :"+ getData["name"] )

        #driver.find_element(By.NAME, "email").send_keys("nandha@gmail.com")  # here NAME is an attribute in html page
        homepage.getMail().send_keys(getData["email"])
        log.info("eMail id is  :" + getData["email"])

        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345678")
        homepage.getPass().send_keys("12345678")

        #driver.find_element(By.ID, "exampleCheck1").click()
        homepage.clickCheckBox().click()



        #driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        #WebDriverWait(driver,10).until(EC.element_to_be_clickable(homepage.selectRadio())).click()
        #homepage.selectRadio().click()

        # Static (Fixed) Drop_Down
        #drop = Select(homepage.getGender())
        #drop.select_by_visible_text("Male")
        self.selectByText(homepage.getGender(),getData["gender"])
        #time.sleep(2)
        #drop.select_by_index(0)

        # Xpath syntax => //tagname[@attribute='value']

        #driver.find_element(By.XPATH, "//input[@type='submit']").click()
        homepage.submitForm().click()

        #msg = driver.find_element(By.CLASS_NAME, "alert-success").text
        message = homepage.getAlertMsg().text


        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepageData)
    def getData(self,request):
        return request.param

