import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def login_setup(request):
    service_obj = Service("C:\chrome_driver\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(2)
    request.cls.driver = driver
    driver.get("https://proschool.ai/")
    driver.maximize_window()




