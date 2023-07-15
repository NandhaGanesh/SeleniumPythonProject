from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    ProductCards = (By.XPATH, "//div[@class='card h-100']")
    product = (By.CSS_SELECTOR, "a[class*='btn-primary']")
#products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")


    def getProductCards(self):
        return self.driver.find_elements(*CheckOutPage.ProductCards)

    def selectProduct(self):
        self.driver.find_element(*CheckOutPage.product).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage