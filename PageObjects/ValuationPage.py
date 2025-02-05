from selenium.webdriver.common.by import By

class ValuationPage:
    """
    Class to hold the elements of the Car Validation form
    """
    #locators
    registration_num = (By.CSS_SELECTOR, ".VRM-module__regular-RiIR")
    make_model = (By.CSS_SELECTOR,".HeroVehicle__title-FAmG")
    vehicle_specifics = (By.CSS_SELECTOR,"ul[data-cy='vehicleSpecifics']")
    tag_names = (By.TAG_NAME,'li')

    def __init__(self,driver):
        self.driver = driver

    def get_registration_num(self):
        """
        Function to read registration number text element
        :return: element for the registration number
        """
        return self.driver.find_element(*ValuationPage.registration_num)

    def get_make_model(self):
        """
        Function to get the make model
        :return: Element for the make model
        """
        return self.driver.find_element(*ValuationPage.make_model)

    def get_vehicle_specifics(self):
        """
        Function to get the vehicle specifics element
        :return: List() of vehicle specific elements
        """
        vehicle_sp_element = self.driver.find_element(*ValuationPage.vehicle_specifics)
        return vehicle_sp_element.find_elements(*ValuationPage.tag_names)



