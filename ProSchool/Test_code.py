import time

from Utility.BaseClass import Base

from Object.HomePage import PracticePath


class TestCodes(Base):

    def test_practice(self):
        obj = PracticePath(self.driver)
        obj.login().click()
        obj.ChoosePortal().click()
        obj.StudentEmail().send_keys("omiarch16@gmail.com")
        obj.StudentPass().send_keys("Proschool@16")
        obj.Final_login().click()
        time.sleep(10)
        obj.SearchBtn().click()
        obj.Math_click().click()
        obj.SelLesson1().click()
        obj.IntroMath().click()
        obj.Pract_Mathpb().click()
        obj.Dwnicon().click()
        obj.Vdo_Btn().click()
        obj.Back_Btn().click()
        obj.SelLesson2().click()