import time
from telnetlib import EC

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("Browser_Invoke")
class Base:

    def Dropdown_up(self):
        self.driver.execute_script('window.scrollBy(250, 0)')

    def Dropdown_down(self):
        self.driver.execute_script('window.scrollBy(0,500)')

    def wait(self):
        time.sleep(10)

    def Explicit_wait(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='root']/div[2]/div/div")))


        except TimeoutException:
            print("The element was not found within the given time")
