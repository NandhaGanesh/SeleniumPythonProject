import time
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

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogging()

        homePage = HomePage(self.driver) #created obj for HomePage class

        #homePage.shopItems().click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        #checkoutPage = CheckOutPage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Items")


        products = checkoutPage.getProductCards()
        for prod in products:
            productName = prod.find_element(By.XPATH, "div/h4/a").text  # chaining
            if productName == "Blackberry":
                prod.find_element(By.XPATH, "div/button").click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage = checkoutPage.selectProduct()
        log.info("Entering Country Name as Ind")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")

        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        time.sleep(1)
        successMsg = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        assert "Success! Thank you!" in successMsg
        log.info("Getting Text as :"+successMsg)



