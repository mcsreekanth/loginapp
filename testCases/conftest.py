from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    return driver


#def pytest_adoption(parser):
#    parser.addoption("--browser")


#@pytest.fixture()
#def browser(request):
#    return request.config.getoption("--browser")



# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'ATHMA'
    config._metadata['Module Name'] = 'Inventory'
    config._metadata['Tester'] = 'Sreekanth'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)