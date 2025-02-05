import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("invoke_browser")
class BaseClass:
    def get_logger(self):
        """
        Function to invoke a python logger
        :return: logger instance
        """
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyXpathpresence(self,locator):
        """
        Function to explicitly wait for a XPATH locator to be visible
        :param locator:
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,f"{locator}")))

    def verifyCSSpresence(self,locator):
        """
        Function to explicitly wait for a CSS locator to be visible
        :param locator:
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f"{locator}")))

