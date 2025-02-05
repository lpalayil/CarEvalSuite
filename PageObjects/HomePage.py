from selenium.webdriver.common.by import By

from PageObjects.ValuationPage import ValuationPage


class HomePage:
    """
    Class to hold the elements of Home Page
    """
    #loctors
    registration_num_field = (By.CSS_SELECTOR, "#vrm-input")
    submit = (By.XPATH, "//button[@data-cy='valueButton']")

    def __init__(self,driver):
        self.driver = driver

    def enter_car_reg(self):
        """
        Gets the field to return car reg number
        :return: element for car reg number field
        """
        return self.driver.find_element(*HomePage.registration_num_field) #desearilize the tuple values

    def submit_car_reg(self):
        """
        Gets the button element to submit the form
        :return: Button element to submit form
        """
        self.driver.find_element(*HomePage.submit).click()
        valuation_page = ValuationPage(self.driver)
        return valuation_page