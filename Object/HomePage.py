from selenium.webdriver.common.by import By


class PracticePath:

    def __init__(self, driver):
        self.driver= driver

    log_in = (By.XPATH, "//a[@class='sign_btn']")

    #login Process
    choose_portal = (By.XPATH, "//button[contains(.,'Student')]")
    std_email = (By.XPATH, "//input[@name='email']")
    std_pass = (By.XPATH, "//input[@name='password']")
    final_log_in = (By.XPATH, "//button[@type='submit']")

    #MainPart
    btn_search = (By.XPATH, "//input[@placeholder='Search']")
    slc_Math = (By.XPATH, "//div[@role='presentation']/div/ul/li[2]")
    slc_lesson1 = (By.XPATH, "//div[@class='Student-Active-Lesson-container']/div[1]/div/button")
    intro_Math = (By.XPATH, "//div[@class='overview-lesson-read-left-section']/div/div[1]")
    pract_Math_pb = (By.XPATH, "//div[@class='overview-lesson-read-left-section']/div/div[9]/div")
    dwn = (By.XPATH, "//div[@class='Overview-Lesson-inner-header']/div[2]/div[1]")
    btn_back = (By.XPATH, "//div[@class ='Overview-Lesson-inner-header'] / div[1]")
    slc_lesson2 = (By.XPATH, "//div[@class='Student-Active-Lesson-container']/div[2]/div/button")
    home = (By.XPATH, "//div[@class='MuiGrid-root css-1nu8j0e']/div/div/h2/a/div")


    def login(self):
        return self.driver.find_element(*PracticePath.log_in)

    def ChoosePortal(self):
        return self.driver.find_element(*PracticePath.choose_portal)

    def StudentEmail(self):
        return self.driver.find_element(*PracticePath.std_email)

    def StudentPass(self):
        return self.driver.find_element(*PracticePath.std_pass)

    def Final_login(self):
        return self.driver.find_element(*PracticePath.final_log_in)

    def SearchBtn(self):
        return self.driver.find_element(*PracticePath.btn_search)

    def Math_click(self):
        return self.driver.find_element(*PracticePath.slc_Math)

    def SelLesson1(self):
        return self.driver.find_element(*PracticePath.slc_lesson1)

    def IntroMath(self):
        return self.driver.find_element(*PracticePath.intro_Math)

    def Pract_Mathpb(self):
        return self.driver.find_element(*PracticePath.pract_Math_pb)

    def Dwnicon(self):
        return self.driver.find_element(*PracticePath.dwn)

    def Back_Btn(self):
        return self.driver.find_element(*PracticePath.btn_back)

    def SelLesson2(self):
        return self.driver.find_element(*PracticePath.slc_lesson2)

    def Home_page(self):
        return self.driver.find_element(*PracticePath.home)

