import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select



'''
    logger.debug("Debug is executed")
    logger.info("info about log")
    logger.warning("warning msg")
    logger.error("error message is displayed")
    logger.critical("critical error")
'''


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogging(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('LogFile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)  # will execute from  level of order we assign below
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectByText(self, locator, text):
        drop = Select(locator)
        drop.select_by_visible_text(text)
