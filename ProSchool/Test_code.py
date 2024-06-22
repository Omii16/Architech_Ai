import time

from Utility.BaseClass import Base

from Object.HomePage import PracticePath


class TestCodes(Base):

    def test_login_process(self):
        obj = PracticePath(self.driver)
        obj.login().click()
        obj.ChoosePortal().click()
        obj.StudentEmail().send_keys("omiarch16@gmail.com")
        obj.StudentPass().send_keys("Proschool@16")
        obj.Final_login().click()
        self.wait()

    def test_Math_lesson1(self):
        obj = PracticePath(self.driver)
        obj.SearchBtn().click()
        obj.Math_click().click()
        obj.SelLesson1().click()
        self.Dropdown_up()
        obj.Dwnicon().click()
        self.wait()
        obj.Back_Btn().click()

    def test_Math_lesson2(self):
        obj = PracticePath(self.driver)
        obj.SearchBtn().click()
        obj.Math_click().click()
        obj.SelLesson2().click()
        self.Dropdown_up()
        obj.Dwnicon().click()
        self.wait()
        obj.Home_page().click()
        self.driver.quit()