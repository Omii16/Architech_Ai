import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("login_setup")
class Base:
    pass