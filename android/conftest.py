import pytest
from appium import webdriver

APPIUM_SERVER_PATH = 'http://localhost:4723/wd/hub'
current_device = {
    "platformName": "Android",
    "deviceName": "773b46e"
}


@pytest.fixture(scope="class")
def mobile_driver():
    driver = webdriver.Remote(APPIUM_SERVER_PATH, current_device)
    yield driver
    driver.quit()
