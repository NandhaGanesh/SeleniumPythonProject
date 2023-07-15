from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):  #constructor to accept the driver args
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.CSS_SELECTOR, "input[name='name']")

    email = (By.NAME, "email")

    password = (By.ID, "exampleInputPassword1")

    checkBox = (By.ID, "exampleCheck1")

    #empStatusRadio = (By.XPATH, "//input[@id='inlineRadio2']")

    gender = (By.ID, "exampleFormControlSelect1")

    submitBtn = (By.XPATH, "//input[@type='submit']")
    alertText = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
    #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getMail(self):
        return self.driver.find_element(*HomePage.email)

    def getPass(self):
        return self.driver.find_element(*HomePage.password)

    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)



    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getAlertMsg(self):
        return self.driver.find_element(*HomePage.alertText)


