import pytest
import time

from PageObjects.HomePage import HomePage
from TestData.CarInputData import CarInputData
from utilities.BaseClass import BaseClass

CAR_VALUATION_URL = "https://www.motorway.co.uk/"


class TestCarValuation(BaseClass):

    @pytest.mark.parametrize("registration_number", CarInputData().read_car_input_data())
    def test_car_valuation(self, registration_number):
        """Test car valuation using the Motorway website."""

        try:
            logger = self.get_logger()
            self.driver.get(CAR_VALUATION_URL)
            home_page = HomePage(self.driver)
           
            # Enter the registration number
            logger.info(f"Entering the Car registration number : {registration_number}")
            reg_input = home_page.enter_car_reg()
            reg_input.send_keys(registration_number)


            # Click the submit button and return the class object for ValuationPage
            valuation_page = home_page.submit_car_reg()
            #submit_button.click()


            # Extract the vehicle reg number
            logger.info(f"Extracting the Vehicle data for reg : {registration_number}")
            reg_data = valuation_page.get_registration_num().text
            print(reg_data)

            # Extract the make model
            make_model = valuation_page.get_make_model().text
            print(make_model)

            # Extract the vehical specifics text
            vehicle_specifics = valuation_page.get_vehicle_specifics()

            #Read the vehical specific data into list
            vehicle_details = list()
            for specifics in vehicle_specifics:
                vehicle_details.append(specifics.text.strip())


            #Get the output expected for the reg numb
            reg_num = registration_number.strip().lower().replace(" ","")
            expected_out = self.expected_data[reg_num]

            assert {'MAKE_MODEL':make_model,'YEAR':vehicle_details[0]} == expected_out,f"Valuation match failed for reg {reg_num}"


        except Exception as e:
            pytest.fail(f"Test failed to get details for Vehicle {registration_number}: {e}")

