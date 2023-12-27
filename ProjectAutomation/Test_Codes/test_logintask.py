from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from Test_Data import data
from Test_Locators import locators

class Test_Kavitha:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
    

    def test_login_TC_Login_01(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        sleep(5)
        assert self.driver.title == 'OrangeHRM'
        


    
    def test_login1_TC_Login_02(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().invalidpassword)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        sleep(5)
        ivalidmsg=self.driver.find_element(by=By.XPATH, value=locators.Locators().variable).text
        sleep(5)
        assert ivalidmsg == data.Data().result

    def test_loginaddemployee_TC_PIM_01(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().addemployee).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().firstname).send_keys(data.Data().addname1)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().lastname).send_keys(data.Data().addname2)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Checkboxes).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().username).send_keys(data.Data().addusername)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().password).send_keys(data.Data().addpassword)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().confirmpassword).send_keys(data.Data().addconfirmpass)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().savelist).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().personalnickname).send_keys(data.Data().addpname)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().personaldl).send_keys(data.Data().adddlnum)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().personalssn).send_keys(data.Data().addpssn)
        sleep(5)
        male_radio=self.driver.find_element(by=By.XPATH, value=locators.Locators().maleradiobutton)
        if male_radio.is_selected():
            pass
        else:
            male_radio.click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().smoker).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().savepersonalemployee).click()
        sleep(5)


    def test_loginedit_TC_PIM_02(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().editemployeelist).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().nickname).send_keys(data.Data().name)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().ssnnumber).send_keys(data.Data().number)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().saveemployeelist).click()
        sleep(5)


       

    def test_logindelete_TC_PIM_03(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().pim).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().deleteemployee).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().yesdeleted).click()
        sleep(2)
        sucessdelete=self.driver.find_element(by=By.XPATH, value=locators.Locators().successfullydelete).text
        sleep(2)
        assert sucessdelete==data.Data().deletemsg

    