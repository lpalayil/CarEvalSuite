import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from TestData.OutputValidation import OutputValidation


def pytest_addoption(parser):
    """
    Function to pass the browser name from cmdline
    :param parser: cmdline parser
    :return: None
    """
    parser.addoption(
        "--browser_name",action="store",default="chrome",help="Browser to run the test on. Default=chrome"
    )

@pytest.fixture(scope="class")
def invoke_browser(request):
    #Get browser name from cmd line options
    browser_name = request.config.getoption("browser_name")
    if browser_name  == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    else:
        # Using default Chrome browser
        # Configure Chrome WebDriver
        chrome_options = Options()
        driver = webdriver.Chrome()
    driver.maximize_window()

    #Implicit wait for 10s
    driver.implicitly_wait(10)

    #Read Output data to verify from
    request.cls.expected_data = OutputValidation().read_csv_to_dict()
    request.cls.driver = driver
    yield
    driver.quit()